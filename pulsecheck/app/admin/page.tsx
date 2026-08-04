import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export default function AdminPage() {
  return (
    <main className="container py-10">
      <h1 className="text-3xl font-semibold">Admin Panel</h1>
      <p className="mt-2 text-muted-foreground">Internal tools and platform health.</p>

      <section className="mt-8 grid gap-4 md:grid-cols-3">
        <Card>
          <CardHeader><CardTitle>System Status</CardTitle></CardHeader>
          <CardContent>
            <Badge variant="success">All Systems Operational</Badge>
            <ul className="mt-4 space-y-2 text-sm">
              <li>API: <span className="text-green-500">✓ 99.99%</span></li>
              <li>DB: <span className="text-green-500">✓ Healthy</span></li>
              <li>Queue: <span className="text-green-500">✓ Processing</span></li>
            </ul>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Active Workspaces</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">847</p></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Revenue Today</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">$2,341</p></CardContent>
        </Card>
      </section>

      <Card className="mt-8">
        <CardHeader><CardTitle>Recent Activity</CardTitle></CardHeader>
        <CardContent>
          <ul className="space-y-2 text-sm">
            <li>🆕 New workspace: TechFlow Inc</li>
            <li>💳 Upgrade: Sarah Chen → Pro</li>
            <li>🚨 Alert: API latency spike (resolved)</li>
            <li>🔄 Webhook retry: 3 successful</li>
          </ul>
        </CardContent>
      </Card>
    </main>
  );
}
