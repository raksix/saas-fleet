import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { z } from "zod";
import { prisma } from "@/lib/db";
import { authOptions } from "@/lib/auth";

const Create = z.object({ name: z.string().min(1).max(200) });

export async function GET() {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({ items: [] });
  const items = await prisma.contentbriefgenerator.findMany({
    where: { orgId }, orderBy: { createdAt: "desc" }, take: 50,
  });
  return NextResponse.json({ items });
}

export async function POST(req: Request) {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({ error: "No org" }, { status: 400 });
  const json = await req.json().catch(() => null);
  const parsed = Create.safeParse(json);
  if (!parsed.success) return NextResponse.json({ error: "Invalid input" }, { status: 400 });
  const item = await prisma.contentbriefgenerator.create({
    data: { orgId, name: parsed.data.name },
  });
  await prisma.auditLog.create({
    data: {
      orgId, userId: (session.user as any).id,
      action: "contentbriefgenerator.create", targetType: "contentbriefgenerator", targetId: item.id,
    },
  });
  return NextResponse.json({ item }, { status: 201 });
}
