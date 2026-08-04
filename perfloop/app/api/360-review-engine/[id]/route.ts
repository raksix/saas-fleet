import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { prisma } from "@/lib/db";
import { authOptions } from "@/lib/auth";

export async function GET(_: Request, { params }: { params: { id: string } }) {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const item = await prisma.360reviewengine.findUnique({ where: { id: params.id } });
  if (!item) return NextResponse.json({ error: "Not found" }, { status: 404 });
  return NextResponse.json({ item });
}

export async function DELETE(_: Request, { params }: { params: { id: string } }) {
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  await prisma.360reviewengine.delete({ where: { id: params.id } });
  await prisma.auditLog.create({
    data: {
      orgId: (session.user as any).orgId,
      userId: (session.user as any).id,
      action: "360reviewengine.delete", targetType: "360reviewengine", targetId: params.id,
    },
  });
  return NextResponse.json({ ok: true });
}
