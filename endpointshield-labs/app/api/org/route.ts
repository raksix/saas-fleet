import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { prisma } from "@/lib/db";
import { authOptions } from "@/lib/auth";

export async function GET() {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({ org: null });
  const org = await prisma.org.findUnique({ where: { id: orgId } });
  return NextResponse.json({ org });
}

export async function PATCH(req: Request) {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({ error: "No org" }, { status: 400 });
  const { name } = await req.json();
  await prisma.org.update({ where: { id: orgId }, data: { name } });
  await prisma.auditLog.create({
    data: { orgId, userId: (session.user as any).id, action: "org.update", metadata: { name } },
  });
  return NextResponse.json({ ok: true });
}
