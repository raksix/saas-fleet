import { NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";
import { prisma } from "@/lib/db";
import type Stripe from "stripe";

export async function POST(req: Request) {
  const sig = req.headers.get("stripe-signature");
  if (!sig) return NextResponse.json({ error: "No signature" }, { status: 400 });
  const body = await req.text();

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch (err) {
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
  }

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object as Stripe.Checkout.Session;
      const orgId = session.metadata?.orgId;
      const plan = session.metadata?.plan;
      if (orgId && plan) {
        await prisma.org.update({
          where: { id: orgId },
          data: { plan: plan.toUpperCase() as any },
        });
      }
      break;
    }
    case "invoice.paid": {
      const invoice = event.data.object as Stripe.Invoice;
      await prisma.auditLog.create({
        data: {
          orgId: "system",
          action: "invoice.paid",
          metadata: { invoiceId: invoice.id, amount: invoice.amount_paid },
        },
      });
      break;
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object as Stripe.Subscription;
      await prisma.org.updateMany({
        where: { stripeId: sub.customer as string },
        data: { plan: "FREE" },
      });
      break;
    }
  }
  return NextResponse.json({ received: true });
}
