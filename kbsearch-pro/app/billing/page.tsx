"use client";
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

const PLANS = [
  { id: "free", name: "Free", price: 0, features: ["1 user", "Basic features"] },
  { id: "starter", name: "Starter", price: 19, features: ["3 users", "Full features", "Email support"] },
  { id: "pro", name: "Pro", price: 49, features: ["10 users", "Integrations", "Priority support"] },
  { id: "team", name: "Team", price: 99, features: ["25 users", "SSO", "SLA"] },
];

export default function BillingPage() {
  const [currentPlan, setCurrentPlan] = useState("free");

  async function upgrade(planId: string) {
    const res = await fetch("/api/billing/checkout", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ plan: planId }),
    });
    const data = await res.json();
    if (data.url) window.location.href = data.url;
  }

  return (
    <main className="container py-10">
      <h1 className="text-3xl font-semibold">Kbsearch Pro — Billing</h1>
      <p className="mt-2 text-muted-foreground">Choose the plan that fits your team.</p>

      <section className="mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        {PLANS.map((plan) => (
          <Card key={plan.id} className={currentPlan === plan.id ? "border-primary" : ""}>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle>{plan.name}</CardTitle>
                {currentPlan === plan.id && <Badge>Current</Badge>}
              </div>
              <p className="text-3xl font-bold">${plan.price}<span className="text-sm font-normal">/mo</span></p>
            </CardHeader>
            <CardContent>
              <ul className="mb-4 space-y-2 text-sm">
                {plan.features.map((f) => <li key={f}>✓ {f}</li>)}
              </ul>
              <Button
                className="w-full"
                variant={currentPlan === plan.id ? "outline" : "default"}
                disabled={currentPlan === plan.id}
                onClick={() => upgrade(plan.id)}
              >
                {currentPlan === plan.id ? "Current Plan" : "Upgrade"}
              </Button>
            </CardContent>
          </Card>
        ))}
      </section>
    </main>
  );
}
