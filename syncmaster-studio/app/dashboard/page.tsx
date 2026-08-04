"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

type Item = { id: string; name: string; status: string; createdAt: string };

export default function Dashboard() {
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/conflict-resolution")
      .then((r) => r.json())
      .then((d) => { setItems(d.items ?? []); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  return (
    <main className="container py-10">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-semibold">SyncMaster Studio</h1>
        <Button asChild><Link href="/api/auth/signout">Sign out</Link></Button>
      </header>

      <section className="mt-8">
        <Card>
          <CardHeader>
            <CardTitle>Conflict resolution</CardTitle>
          </CardHeader>
          <CardContent>
            {loading ? (
              <p className="text-sm text-muted-foreground">Loading...</p>
            ) : items.length === 0 ? (
              <p className="text-sm text-muted-foreground">No items yet. Connect your data source to get started.</p>
            ) : (
              <ul className="space-y-2">
                {items.map((it) => (
                  <li key={it.id} className="flex items-center justify-between rounded border p-3 text-sm">
                    <span>{it.name}</span>
                    <span className="text-muted-foreground">{it.status}</span>
                  </li>
                ))}
              </ul>
            )}
          </CardContent>
        </Card>
      </section>
    </main>
  );
}
