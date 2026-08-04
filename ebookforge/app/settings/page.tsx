"use client";
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function SettingsPage() {
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    fetch("/api/org").then(r => r.json()).then((d) => setName(d.org?.name ?? ""));
  }, []);

  async function save(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    await fetch("/api/org", {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    setLoading(false);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  }

  return (
    <main className="container py-10">
      <h1 className="text-3xl font-semibold">Ebookforge — Settings</h1>
      <Card className="mt-8 max-w-2xl">
        <CardHeader>
          <CardTitle>Organization</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={save} className="space-y-4">
            <div>
              <label className="text-sm font-medium">Organization name</label>
              <Input value={name} onChange={(e) => setName(e.target.value)} />
            </div>
            <Button type="submit" disabled={loading}>
              {loading ? "Saving..." : saved ? "Saved ✓" : "Save"}
            </Button>
          </form>
        </CardContent>
      </Card>

      <Card className="mt-6 max-w-2xl">
        <CardHeader>
          <CardTitle>Danger Zone</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">Permanently delete this workspace and all data.</p>
          <Button variant="destructive" className="mt-3">Delete Workspace</Button>
        </CardContent>
      </Card>
    </main>
  );
}
