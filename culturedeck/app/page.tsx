import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export default function Home() {
  return (
    <main className="container py-16">
      <section className="mx-auto max-w-3xl text-center">
        <h1 className="text-5xl font-bold tracking-tight">CultureDeck</h1>
        <p className="mt-6 text-xl text-muted-foreground">Culture and values management</p>
        <p className="mt-4 text-base text-muted-foreground">Define values, attach them to review criteria, and run culture surveys with consistent scoring.</p>
        <div className="mt-8 flex justify-center gap-4">
          <Button asChild><Link href="/signup">Get Started</Link></Button>
          <Button asChild variant="outline"><Link href="/login">Sign In</Link></Button>
        </div>
      </section>

      <section className="mt-16 grid gap-6 md:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>Value definitions</CardTitle>
            <CardDescription>Core capability that sets CultureDeck apart.</CardDescription>
          </CardHeader>
          <CardContent>Production-ready with full audit logging and analytics events.</CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Multi-tenant</CardTitle>
            <CardDescription>Organization-scoped data with row-level security.</CardDescription>
          </CardHeader>
          <CardContent>Workspaces, members, and roles out of the box.</CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Developer-first</CardTitle>
            <CardDescription>Public API + SDKs + webhooks.</CardDescription>
          </CardHeader>
          <CardContent>Integrate CultureDeck into your stack in minutes.</CardContent>
        </Card>
      </section>
    </main>
  );
}
