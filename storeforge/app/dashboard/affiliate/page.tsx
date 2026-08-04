import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

export default function AffiliatePage() {
  const stats = {
    referrals: 47,
    conversions: 12,
    conversionRate: 25.5,
    pendingPayout: 340,
    lifetimeEarnings: 2840,
    referralLink: "https://app.example.com/?ref=USER_ID",
  };
  return (
    <main className="container py-10">
      <h1 className="text-3xl font-semibold">Affiliate Program</h1>
      <p className="mt-2 text-muted-foreground">Earn 30% recurring on every referral.</p>

      <section className="mt-8 grid gap-4 md:grid-cols-4">
        <Card>
          <CardHeader><CardTitle>Referrals</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">{stats.referrals}</p></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Conversions</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">{stats.conversions}</p></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Conversion Rate</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">{stats.conversionRate}%</p></CardContent>
        </Card>
        <Card>
          <CardHeader><CardTitle>Lifetime Earnings</CardTitle></CardHeader>
          <CardContent><p className="text-3xl font-bold">${stats.lifetimeEarnings}</p></CardContent>
        </Card>
      </section>

      <Card className="mt-8">
        <CardHeader>
          <CardTitle>Your Referral Link</CardTitle>
        </CardHeader>
        <CardContent>
          <code className="block rounded bg-muted p-3 text-sm">{stats.referralLink}</code>
          <Button className="mt-4">Copy Link</Button>
        </CardContent>
      </Card>

      <Card className="mt-6">
        <CardHeader>
          <CardTitle>Pending Payout</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-2xl font-bold">${stats.pendingPayout}</p>
          <p className="text-sm text-muted-foreground">Paid out on the 1st of each month via Stripe.</p>
          <Button className="mt-4">Payout History</Button>
        </CardContent>
      </Card>
    </main>
  );
}
