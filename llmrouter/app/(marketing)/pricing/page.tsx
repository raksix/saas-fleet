import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

const PLANS = [
  {
    id: "free", name: "Free", price: 0, yearly: 0,
    description: "Try it out — perfect for individuals.",
    features: [
      "1 user", "100 API calls/mo", "Community support",
      "Basic features", "Single workspace",
    ],
    cta: "Get Started Free",
  },
  {
    id: "starter", name: "Starter", price: 19, yearly: 190,
    description: "For small teams getting serious.",
    features: [
      "5 users", "10,000 API calls/mo", "Email support",
      "All basic features", "3 workspaces",
      "Basic analytics",
    ],
    cta: "Start Free Trial",
    highlighted: false,
  },
  {
    id: "pro", name: "Pro", price: 49, yearly: 490,
    description: "Most popular for growing teams.",
    features: [
      "25 users", "100,000 API calls/mo", "Priority support",
      "Advanced features", "Unlimited workspaces",
      "Full analytics", "Custom integrations",
      "Webhooks + API access",
    ],
    cta: "Start Free Trial",
    highlighted: true,
    badge: "Most Popular",
  },
  {
    id: "team", name: "Team", price: 99, yearly: 990,
    description: "For larger teams with advanced needs.",
    features: [
      "100 users", "1,000,000 API calls/mo", "Dedicated support",
      "SSO/SAML", "Audit logs",
      "Advanced security", "Custom domains",
      "SLA + uptime guarantees",
    ],
    cta: "Contact Sales",
  },
  {
    id: "enterprise", name: "Enterprise", price: null, yearly: null,
    description: "Custom solutions for big orgs.",
    features: [
      "Unlimited everything", "Dedicated CSM",
      "On-prem option", "Custom contracts",
      "99.99% SLA", "White-glove onboarding",
      "Custom development",
    ],
    cta: "Contact Sales",
  },
];

const FAQ = [
  { q: "Can I switch plans anytime?", a: "Yes, upgrade or downgrade at any time. Pro-rated billing handled automatically." },
  { q: "What happens when I exceed limits?", a: "We notify you at 80% and 100%. Overages billed at $0.001/call or you can upgrade." },
  { q: "Do you offer a free trial?", a: "Yes — 14 days, no credit card required. Try all Pro features risk-free." },
  { q: "Is there a discount for non-profits?", a: "Yes, 50% off Team plan for registered non-profits. Apply via support." },
  { q: "What payment methods do you accept?", a: "All major credit cards, ACH for Team+, and wire transfer for Enterprise." },
];

const COMPARISON_FEATURES = [
  { name: "Users", free: "1", starter: "5", pro: "25", team: "100", enterprise: "Unlimited" },
  { name: "API calls/mo", free: "100", starter: "10K", pro: "100K", team: "1M", enterprise: "Custom" },
  { name: "Workspaces", free: "1", starter: "3", pro: "Unlimited", team: "Unlimited", enterprise: "Unlimited" },
  { name: "Analytics", free: "Basic", starter: "Basic", pro: "Advanced", team: "Advanced", enterprise: "Custom" },
  { name: "Webhooks", free: "—", starter: "—", pro: "✓", team: "✓", enterprise: "✓" },
  { name: "SSO/SAML", free: "—", starter: "—", pro: "—", team: "✓", enterprise: "✓" },
  { name: "Audit logs", free: "—", starter: "—", pro: "—", team: "✓", enterprise: "✓" },
  { name: "Custom domains", free: "—", starter: "—", pro: "—", team: "✓", enterprise: "✓" },
  { name: "SLA", free: "—", starter: "—", pro: "99.9%", team: "99.9%", enterprise: "99.99%" },
  { name: "Support", free: "Community", starter: "Email", pro: "Priority", team: "Dedicated", enterprise: "White-glove" },
];

const TESTIMONIALS = [
  { name: "Sarah Chen", role: "CTO, TechFlow", quote: "Replaced 3 tools with this. Saved us $40K/year and our team is 2x faster." },
  { name: "Mike Johnson", role: "Founder, LaunchPad", quote: "Onboarded in 10 minutes. We hit ROI in the first week." },
  { name: "Priya Patel", role: "VP Eng, ScaleOps", quote: "The API is rock solid. We process 10M events/day without breaking a sweat." },
];

export default function PricingPage() {
  return (
    <main className="container py-16">
      <header className="mx-auto max-w-3xl text-center">
        <h1 className="text-5xl font-bold">Simple, transparent pricing</h1>
        <p className="mt-4 text-xl text-muted-foreground">Start free. Scale as you grow. Cancel anytime.</p>
        <div className="mt-6 inline-flex items-center gap-2 text-sm">
          <span>Monthly</span>
          <span className="text-muted-foreground">|</span>
          <span className="font-semibold">Save 17% with yearly</span>
        </div>
      </header>

      <section className="mt-16 grid gap-6 md:grid-cols-3 lg:grid-cols-5">
        {PLANS.map((plan) => (
          <Card key={plan.id} className={plan.highlighted ? "border-primary shadow-lg" : ""}>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle>{plan.name}</CardTitle>
                {plan.badge && <Badge>{plan.badge}</Badge>}
              </div>
              <CardDescription>{plan.description}</CardDescription>
              <div className="mt-4">
                {plan.price === null ? (
                  <p className="text-3xl font-bold">Custom</p>
                ) : (
                  <>
                    <p className="text-4xl font-bold">${plan.price}<span className="text-sm font-normal">/mo</span></p>
                    {plan.yearly && plan.yearly > 0 && (
                      <p className="text-xs text-muted-foreground">${plan.yearly}/yr</p>
                    )}
                  </>
                )}
              </div>
            </CardHeader>
            <CardContent>
              <ul className="mb-6 space-y-2 text-sm">
                {plan.features.map((f) => <li key={f}>✓ {f}</li>)}
              </ul>
              <Button asChild className="w-full" variant={plan.highlighted ? "default" : "outline"}>
                <Link href={`/signup?plan=${plan.id}`}>{plan.cta}</Link>
              </Button>
            </CardContent>
          </Card>
        ))}
      </section>

      <section className="mt-24">
        <h2 className="text-center text-3xl font-bold">What customers say</h2>
        <div className="mt-8 grid gap-6 md:grid-cols-3">
          {TESTIMONIALS.map((t) => (
            <Card key={t.name}>
              <CardContent className="pt-6">
                <p className="text-sm">"{t.quote}"</p>
                <div className="mt-4">
                  <p className="font-semibold">{t.name}</p>
                  <p className="text-sm text-muted-foreground">{t.role}</p>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section className="mt-24">
        <h2 className="text-center text-3xl font-bold">Compare plans</h2>
        <div className="mt-8 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b">
                <th className="px-4 py-3 text-left">Feature</th>
                {PLANS.map((p) => <th key={p.id} className="px-4 py-3 text-center">{p.name}</th>)}
              </tr>
            </thead>
            <tbody>
              {COMPARISON_FEATURES.map((f) => (
                <tr key={f.name} className="border-b">
                  <td className="px-4 py-3 font-medium">{f.name}</td>
                  <td className="px-4 py-3 text-center">{f.free}</td>
                  <td className="px-4 py-3 text-center">{f.starter}</td>
                  <td className="px-4 py-3 text-center">{f.pro}</td>
                  <td className="px-4 py-3 text-center">{f.team}</td>
                  <td className="px-4 py-3 text-center">{f.enterprise}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="mt-24 max-w-3xl mx-auto">
        <h2 className="text-center text-3xl font-bold">Frequently asked</h2>
        <div className="mt-8 space-y-4">
          {FAQ.map((item) => (
            <Card key={item.q}>
              <CardHeader>
                <CardTitle className="text-lg">{item.q}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">{item.a}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <section className="mt-24 rounded-lg bg-primary p-12 text-center text-primary-foreground">
        <h2 className="text-3xl font-bold">Ready to get started?</h2>
        <p className="mt-2 text-lg opacity-90">14-day free trial. No credit card required.</p>
        <Button asChild size="lg" variant="secondary" className="mt-6">
          <Link href="/signup">Start Free Trial</Link>
        </Button>
      </section>
    </main>
  );
}
