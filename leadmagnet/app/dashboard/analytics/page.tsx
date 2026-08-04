import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function AnalyticsPage() {
  const metrics = [
    { label: "MRR", value: "$48,290", change: "+12.3%", trend: "up" },
    { label: "Active Users", value: "3,847", change: "+8.7%", trend: "up" },
    { label: "Churn Rate", value: "2.1%", change: "-0.4%", trend: "down" },
    { label: "LTV", value: "$1,240", change: "+5.2%", trend: "up" },
  ];
  return (
    <main className="container py-10">
      <h1 className="text-3xl font-semibold">Analytics</h1>
      <p className="mt-2 text-muted-foreground">Real-time business metrics.</p>

      <section className="mt-8 grid gap-4 md:grid-cols-4">
        {metrics.map((m) => (
          <Card key={m.label}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">{m.label}</CardTitle>
              <span className={m.trend === "up" ? "text-green-500 text-xs" : "text-red-500 text-xs"}>
                {m.change}
              </span>
            </CardHeader>
            <CardContent>
              <p className="text-2xl font-bold">{m.value}</p>
            </CardContent>
          </Card>
        ))}
      </section>

      <section className="mt-8 grid gap-6 lg:grid-cols-2">
        <Card>
          <CardHeader><CardTitle>Revenue (30d)</CardTitle></CardHeader>
          <CardContent>
            <div className="h-64 flex items-end gap-1">
              {Array.from({ length: 30 }).map((_, i) => {
                const h = Math.sin(i * 0.4) * 30 + 50 + Math.random() * 20;
                return <div key={i} className="flex-1 bg-primary rounded-t" style={{ height: `${h}%` }} />;
              })}
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>User Signups (30d)</CardTitle></CardHeader>
          <CardContent>
            <div className="h-64 flex items-end gap-1">
              {Array.from({ length: 30 }).map((_, i) => {
                const h = Math.cos(i * 0.3) * 25 + 50 + Math.random() * 20;
                return <div key={i} className="flex-1 bg-green-500 rounded-t" style={{ height: `${h}%` }} />;
              })}
            </div>
          </CardContent>
        </Card>
      </section>

      <Card className="mt-8">
        <CardHeader><CardTitle>Cohort Retention</CardTitle></CardHeader>
        <CardContent>
          <div className="grid grid-cols-7 gap-1 text-xs">
            {Array.from({ length: 35 }).map((_, i) => {
              const v = Math.max(20, 100 - i * 2.5);
              const bg = v > 80 ? "bg-green-500" : v > 60 ? "bg-yellow-500" : "bg-red-500";
              return <div key={i} className={`${bg} aspect-square rounded`} title={`${Math.round(v)}%`} />;
            })}
          </div>
        </CardContent>
      </Card>
    </main>
  );
}
