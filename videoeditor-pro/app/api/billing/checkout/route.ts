import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { stripe } from "@/lib/stripe";
import { prisma } from "@/lib/db";
import { authOptions } from "@/lib/auth";

const PRICE_IDS: Record<string, string> = {
  starter: process.env.STRIPE_PRICE_STARTER!,
  pro: process.env.STRIPE_PRICE_PRO!,
  team: process.env.STRIPE_PRICE_TEAM!,
};

export async function POST(req: Request) {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({ error: "No org" }, { status: 400 });

  const { plan } = await req.json();
  const priceId = PRICE_IDS[plan];
  if (!priceId) return NextResponse.json({ error: "Invalid plan" }, { status: 400 });

  const org = await prisma.org.findUnique({ where: { id: orgId } });
  let customerId = org?.stripeId;
  if (!customerId) {
    const customer = await stripe.customers.create({ metadata: { orgId } });
    customerId = customer.id;
    await prisma.org.update({ where: { id: orgId }, data: { stripeId: customerId } });
  }

  const checkout = await stripe.checkout.sessions.create({
    customer: customerId,
    mode: "subscription",
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/billing?success=1`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/billing?canceled=1`,
    metadata: { orgId, plan },
  });
  return NextResponse.json({ url: checkout.url });
}
