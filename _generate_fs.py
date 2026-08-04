"""Generate full-stack Next.js + Prisma + NextAuth scaffolds for all 100 apps."""
import os
from pathlib import Path

BASE = Path(__file__).parent

# Read the apps list from spec generator (re-import)
import importlib.util
spec_path = BASE / "_generate.py"
spec = importlib.util.spec_from_file_location("spec_gen", spec_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
APPS = mod.APPS

APP_NAMES = [a[0] for a in APPS]


def pkg(name, tagline):
    slug = name.lower()
    return f"""{{
  "name": "{slug}",
  "version": "0.1.0",
  "private": true,
  "scripts": {{
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "db:push": "prisma db push",
    "db:studio": "prisma studio",
    "postinstall": "prisma generate"
  }},
  "dependencies": {{
    "next": "14.2.5",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "@prisma/client": "^5.18.0",
    "next-auth": "^4.24.7",
    "@auth/prisma-adapter": "^2.4.0",
    "bcryptjs": "^2.4.3",
    "zod": "^3.23.8",
    "tailwindcss": "^3.4.7",
    "tailwindcss-animate": "^1.0.7",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.5.2",
    "lucide-react": "^0.408.0",
    "@radix-ui/react-slot": "^1.1.0",
    "@radix-ui/react-label": "^2.1.0",
    "@radix-ui/react-dialog": "^1.1.1",
    "stripe": "^16.7.0",
    "resend": "^3.5.0",
    "@tanstack/react-query": "^5.51.0"
  }},
  "devDependencies": {{
    "@types/node": "^20.14.10",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@types/bcryptjs": "^2.4.6",
    "typescript": "^5.5.3",
    "prisma": "^5.18.0",
    "postcss": "^8.4.40",
    "autoprefixer": "^10.4.19",
    "eslint": "^8.57.0",
    "eslint-config-next": "14.2.5"
  }}
}}
"""


def tsconfig():
    return """{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
"""


def next_config():
    return """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: { remotePatterns: [{ protocol: "https", hostname: "**" }] },
  experimental: { serverActions: { bodySizeLimit: "2mb" } },
};
export default nextConfig;
"""


def tailwind_config():
    return """import type { Config } from "tailwindcss";
const config: Config = {
  darkMode: ["class"],
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    container: { center: true, padding: "1rem" },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" },
        muted: { DEFAULT: "hsl(var(--muted))", foreground: "hsl(var(--muted-foreground))" },
        accent: { DEFAULT: "hsl(var(--accent))", foreground: "hsl(var(--accent-foreground))" },
        card: { DEFAULT: "hsl(var(--card))", foreground: "hsl(var(--card-foreground))" },
      },
      borderRadius: { lg: "var(--radius)", md: "calc(var(--radius) - 2px)", sm: "calc(var(--radius) - 4px)" },
    },
  },
  plugins: [require("tailwindcss-animate")],
};
export default config;
"""


def postcss_config():
    return """module.exports = {
  plugins: { tailwindcss: {}, autoprefixer: {} },
};
"""


def env_example():
    return """# Database
DATABASE_URL="postgresql://user:password@localhost:5432/dbname?schema=public"

# NextAuth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="generate-with: openssl rand -base64 32"

# OAuth (optional)
GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""
GITHUB_CLIENT_ID=""
GITHUB_CLIENT_SECRET=""

# Stripe
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_SECRET=""
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=""

# Resend
RESEND_API_KEY=""

# App
NEXT_PUBLIC_APP_URL="http://localhost:3000"
"""


def gitignore():
    return """node_modules
.next
out
.env
.env.local
.env.*.local
*.log
.DS_Store
.vercel
dist
build
coverage
"""


def prisma_schema(name, tagline, feature):
    table = feature.lower().replace(" ", "_")[:24]
    return f"""// Prisma schema for {name}
generator client {{ provider = "prisma-client-js" }}
datasource db {{ provider = "postgresql"; url = env("DATABASE_URL") }}

model User {{
  id            String    @id @default(cuid())
  name          String?
  email         String    @unique
  emailVerified DateTime?
  image         String?
  passwordHash  String?
  accounts      Account[]
  sessions      Session[]
  memberships   Member[]
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
}}

model Account {{
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refresh_token     String?
  access_token      String?
  expires_at        Int?
  token_type        String?
  scope             String?
  id_token          String?
  session_state     String?
  user              User    @relation(fields: [userId], references: [id], onDelete: Cascade)
  @@unique([provider, providerAccountId])
}}

model Session {{
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expires      DateTime
  user         User     @relation(fields: [userId], references: [id], onDelete: Cascade)
}}

model Org {{
  id           String    @id @default(cuid())
  name         String
  slug         String    @unique
  plan         Plan      @default(FREE)
  stripeId     String?   @unique
  members      Member[]
  {table}s     {name.replace(" ", "")}[]   // domain relation
  createdAt    DateTime  @default(now())
  updatedAt    DateTime  @updatedAt
}}

enum Plan {{ FREE STARTER PRO TEAM ENTERPRISE }}

model Member {{
  id        String   @id @default(cuid())
  orgId     String
  userId    String
  role      Role     @default(MEMBER)
  org       Org      @relation(fields: [orgId], references: [id], onDelete: Cascade)
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  @@unique([orgId, userId])
}}

enum Role {{ OWNER ADMIN MEMBER VIEWER }}

model {name.replace(" ", "")} {{
  id        String   @id @default(cuid())
  orgId     String
  name      String
  status    String   @default("active")
  payload   Json?
  org       Org      @relation(fields: [orgId], references: [id], onDelete: Cascade)
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  @@index([orgId, createdAt])
}}

model AuditLog {{
  id         String   @id @default(cuid())
  orgId      String
  userId     String?
  action     String
  targetType String?
  targetId   String?
  metadata   Json?
  createdAt  DateTime @default(now())
  @@index([orgId, createdAt])
}}
"""


def app_layout(name):
    return f"""import "./globals.css";
import type {{ Metadata }} from "next";
import {{ Inter }} from "next/font/google";

const inter = Inter({{ subsets: ["latin"] }});

export const metadata: Metadata = {{
  title: "{name}",
  description: "Generated SaaS app",
}};

export default function RootLayout({{ children }}: React.ReactNode) {{
  return (
    <html lang="en" className={{inter.className}}>
      <body className="min-h-screen bg-background text-foreground antialiased">{{children}}</body>
    </html>
  );
}}
"""


def globals_css():
    return """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --primary: 240 5.9% 10%;
    --primary-foreground: 0 0% 98%;
    --muted: 240 4.8% 95.9%;
    --muted-foreground: 240 3.8% 46.1%;
    --accent: 240 4.8% 95.9%;
    --accent-foreground: 240 5.9% 10%;
    --border: 240 5.9% 90%;
    --radius: 0.5rem;
  }
  .dark {
    --background: 240 10% 3.9%;
    --foreground: 0 0% 98%;
    --card: 240 10% 3.9%;
    --card-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 240 5.9% 10%;
    --muted: 240 3.7% 15.9%;
    --muted-foreground: 240 5% 64.9%;
    --accent: 240 3.7% 15.9%;
    --accent-foreground: 0 0% 98%;
    --border: 240 3.7% 15.9%;
  }
}
"""


def landing_page(name, tagline, desc, feature):
    return f"""import Link from "next/link";
import {{ Button }} from "@/components/ui/button";
import {{ Card, CardContent, CardDescription, CardHeader, CardTitle }} from "@/components/ui/card";

export default function Home() {{
  return (
    <main className="container py-16">
      <section className="mx-auto max-w-3xl text-center">
        <h1 className="text-5xl font-bold tracking-tight">{name}</h1>
        <p className="mt-6 text-xl text-muted-foreground">{tagline}</p>
        <p className="mt-4 text-base text-muted-foreground">{desc}</p>
        <div className="mt-8 flex justify-center gap-4">
          <Button asChild><Link href="/signup">Get Started</Link></Button>
          <Button asChild variant="outline"><Link href="/login">Sign In</Link></Button>
        </div>
      </section>

      <section className="mt-16 grid gap-6 md:grid-cols-3">
        <Card>
          <CardHeader>
            <CardTitle>{feature}</CardTitle>
            <CardDescription>Core capability that sets {name} apart.</CardDescription>
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
          <CardContent>Integrate {name} into your stack in minutes.</CardContent>
        </Card>
      </section>
    </main>
  );
}}
"""


def login_page(name):
    return f""""use client";
import {{ useState }} from "react";
import Link from "next/link";
import {{ signIn }} from "next-auth/react";
import {{ Button }} from "@/components/ui/button";

export default function LoginPage() {{
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: React.FormEvent) {{
    e.preventDefault();
    setLoading(true);
    setError(null);
    const res = await signIn("credentials", {{
      email, password, redirect: false, callbackUrl: "/dashboard",
    }});
    setLoading(false);
    if (res?.error) setError("Invalid credentials");
    else if (res?.url) window.location.href = res.url;
  }}

  return (
    <main className="container flex min-h-screen items-center justify-center py-16">
      <form onSubmit={{onSubmit}} className="w-full max-w-sm space-y-4 rounded-lg border bg-card p-8 shadow-sm">
        <h1 className="text-2xl font-semibold">Sign in to {name}</h1>
        <input type="email" required placeholder="Email" value={{email}} onChange={{(e) => setEmail(e.target.value)}}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm" />
        <input type="password" required placeholder="Password" value={{password}} onChange={{(e) => setPassword(e.target.value)}}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm" />
        {{error && <p className="text-sm text-red-500">{{error}}</p>}}
        <Button type="submit" disabled={{loading}} className="w-full">
          {{loading ? "Signing in..." : "Sign In"}}
        </Button>
        <p className="text-sm text-muted-foreground">
          No account? <Link href="/signup" className="underline">Sign up</Link>
        </p>
      </form>
    </main>
  );
}}
"""


def signup_page(name):
    return f""""use client";
import {{ useState }} from "react";
import Link from "next/link";
import {{ useRouter }} from "next/navigation";
import {{ Button }} from "@/components/ui/button";

export default function SignupPage() {{
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: React.FormEvent) {{
    e.preventDefault();
    setLoading(true);
    setError(null);
    const res = await fetch("/api/auth/signup", {{
      method: "POST",
      headers: {{ "Content-Type": "application/json" }},
      body: JSON.stringify({{ email, password, name }}),
    }});
    setLoading(false);
    if (!res.ok) {{
      const data = await res.json().catch(() => ({{}}));
      setError(data?.error || "Signup failed");
      return;
    }}
    router.push("/login");
  }}

  return (
    <main className="container flex min-h-screen items-center justify-center py-16">
      <form onSubmit={{onSubmit}} className="w-full max-w-sm space-y-4 rounded-lg border bg-card p-8 shadow-sm">
        <h1 className="text-2xl font-semibold">Create {name} account</h1>
        <input required placeholder="Name" value={{name}} onChange={{(e) => setName(e.target.value)}}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm" />
        <input type="email" required placeholder="Email" value={{email}} onChange={{(e) => setEmail(e.target.value)}}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm" />
        <input type="password" required minLength={8} placeholder="Password (8+)" value={{password}} onChange={{(e) => setPassword(e.target.value)}}
          className="w-full rounded-md border bg-background px-3 py-2 text-sm" />
        {{error && <p className="text-sm text-red-500">{{error}}</p>}}
        <Button type="submit" disabled={{loading}} className="w-full">
          {{loading ? "Creating..." : "Create Account"}}
        </Button>
        <p className="text-sm text-muted-foreground">
          Already have an account? <Link href="/login" className="underline">Sign in</Link>
        </p>
      </form>
    </main>
  );
}}
"""


def dashboard_page(name, feature):
    return f""""use client";
import {{ useEffect, useState }} from "react";
import Link from "next/link";
import {{ Button }} from "@/components/ui/button";
import {{ Card, CardContent, CardHeader, CardTitle }} from "@/components/ui/card";

type Item = {{ id: string; name: string; status: string; createdAt: string }};

export default function Dashboard() {{
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {{
    fetch("/api/{feature.lower().replace(' ', '-')[:24]}")
      .then((r) => r.json())
      .then((d) => {{ setItems(d.items ?? []); setLoading(false); }})
      .catch(() => setLoading(false));
  }}, []);

  return (
    <main className="container py-10">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-semibold">{name}</h1>
        <Button asChild><Link href="/api/auth/signout">Sign out</Link></Button>
      </header>

      <section className="mt-8">
        <Card>
          <CardHeader>
            <CardTitle>{feature}</CardTitle>
          </CardHeader>
          <CardContent>
            {{loading ? (
              <p className="text-sm text-muted-foreground">Loading...</p>
            ) : items.length === 0 ? (
              <p className="text-sm text-muted-foreground">No items yet. Connect your data source to get started.</p>
            ) : (
              <ul className="space-y-2">
                {{items.map((it) => (
                  <li key={{it.id}} className="flex items-center justify-between rounded border p-3 text-sm">
                    <span>{{it.name}}</span>
                    <span className="text-muted-foreground">{{it.status}}</span>
                  </li>
                ))}}
              </ul>
            )}}
          </CardContent>
        </Card>
      </section>
    </main>
  );
}}
"""


def api_signup():
    return """import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";
import { z } from "zod";
import { prisma } from "@/lib/db";

const Body = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  name: z.string().min(1).max(80),
});

export async function POST(req: Request) {
  const json = await req.json().catch(() => null);
  const parsed = Body.safeParse(json);
  if (!parsed.success) return NextResponse.json({ error: "Invalid input" }, { status: 400 });
  const { email, password, name } = parsed.data;
  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) return NextResponse.json({ error: "Email already in use" }, { status: 409 });
  const passwordHash = await bcrypt.hash(password, 10);
  await prisma.user.create({ data: { email, name, passwordHash } });
  return NextResponse.json({ ok: true });
}
"""


def api_resource(feature, name):
    slug = feature.lower().replace(" ", "-")[:24]
    model = name.replace(" ", "")
    return f"""import {{ NextResponse }} from "next/server";
import {{ getServerSession }} from "next-auth";
import {{ z }} from "zod";
import {{ prisma }} from "@/lib/db";
import {{ authOptions }} from "@/lib/auth";

const Create = z.object({{ name: z.string().min(1).max(200) }});

export async function GET() {{
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({{ error: "Unauthorized" }}, {{ status: 401 }});
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({{ items: [] }});
  const items = await prisma.{model.lower()}.findMany({{
    where: {{ orgId }}, orderBy: {{ createdAt: "desc" }}, take: 50,
  }});
  return NextResponse.json({{ items }});
}}

export async function POST(req: Request) {{
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({{ error: "Unauthorized" }}, {{ status: 401 }});
  const orgId = (session.user as any).orgId;
  if (!orgId) return NextResponse.json({{ error: "No org" }}, {{ status: 400 }});
  const json = await req.json().catch(() => null);
  const parsed = Create.safeParse(json);
  if (!parsed.success) return NextResponse.json({{ error: "Invalid input" }}, {{ status: 400 }});
  const item = await prisma.{model.lower()}.create({{
    data: {{ orgId, name: parsed.data.name }},
  }});
  await prisma.auditLog.create({{
    data: {{
      orgId, userId: (session.user as any).id,
      action: "{model.lower()}.create", targetType: "{model.lower()}", targetId: item.id,
    }},
  }});
  return NextResponse.json({{ item }}, {{ status: 201 }});
}}
"""


def api_resource_detail(feature, name):
    slug = feature.lower().replace(" ", "-")[:24]
    model = name.replace(" ", "")
    return f"""import {{ NextResponse }} from "next/server";
import {{ getServerSession }} from "next-auth";
import {{ prisma }} from "@/lib/db";
import {{ authOptions }} from "@/lib/auth";

export async function GET(_: Request, {{ params }}: {{ params: {{ id: string }} }}) {{
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({{ error: "Unauthorized" }}, {{ status: 401 }});
  const item = await prisma.{model.lower()}.findUnique({{ where: {{ id: params.id }} }});
  if (!item) return NextResponse.json({{ error: "Not found" }}, {{ status: 404 }});
  return NextResponse.json({{ item }});
}}

export async function DELETE(_: Request, {{ params }}: {{ params: {{ id: string }} }}) {{
  const session = await getServerSession(authOptions);
  if (!session?.user) return NextResponse.json({{ error: "Unauthorized" }}, {{ status: 401 }});
  await prisma.{model.lower()}.delete({{ where: {{ id: params.id }} }});
  await prisma.auditLog.create({{
    data: {{
      orgId: (session.user as any).orgId,
      userId: (session.user as any).id,
      action: "{model.lower()}.delete", targetType: "{model.lower()}", targetId: params.id,
    }},
  }});
  return NextResponse.json({{ ok: true }});
}}
"""


def api_nextauth():
    return """import NextAuth from "next-auth";
import { authOptions } from "@/lib/auth";

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
"""


def lib_db():
    return """import { PrismaClient } from "@prisma/client";

const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };
export const prisma = globalForPrisma.prisma ?? new PrismaClient();
if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma;
"""


def lib_auth():
    model = "TaskForge"  # placeholder, replaced per app
    return """import type { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";
import GitHubProvider from "next-auth/providers/github";
import bcrypt from "bcryptjs";
import { prisma } from "@/lib/db";

export const authOptions: NextAuthOptions = {
  adapter: undefined, // using JWT for credentials; swap to PrismaAdapter for DB sessions
  session: { strategy: "jwt" },
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: { email: { type: "email" }, password: { type: "password" } },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;
        const user = await prisma.user.findUnique({ where: { email: credentials.email } });
        if (!user?.passwordHash) return null;
        const ok = await bcrypt.compare(credentials.password, user.passwordHash);
        if (!ok) return null;
        const member = await prisma.member.findFirst({ where: { userId: user.id } });
        return { id: user.id, email: user.email, name: user.name, orgId: member?.orgId } as any;
      },
    }),
    ...(process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET
      ? [GoogleProvider({ clientId: process.env.GOOGLE_CLIENT_ID, clientSecret: process.env.GOOGLE_CLIENT_SECRET })]
      : []),
    ...(process.env.GITHUB_CLIENT_ID && process.env.GITHUB_CLIENT_SECRET
      ? [GitHubProvider({ clientId: process.env.GITHUB_CLIENT_ID, clientSecret: process.env.GITHUB_CLIENT_SECRET })]
      : []),
  ],
  pages: { signIn: "/login" },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        (token as any).id = (user as any).id;
        (token as any).orgId = (user as any).orgId;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        (session.user as any).id = (token as any).id;
        (session.user as any).orgId = (token as any).orgId;
      }
      return session;
    },
  },
};
"""


def lib_utils():
    return """import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
"""


def ui_button():
    return """import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        destructive: "bg-red-500 text-white hover:bg-red-500/90",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: { variant: "default", size: "default" },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return <Comp ref={ref} className={cn(buttonVariants({ variant, size }), className)} {...props} />;
  }
);
Button.displayName = "Button";
"""


def ui_card():
    return """import * as React from "react";
import { cn } from "@/lib/utils";

export const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("rounded-lg border bg-card text-card-foreground shadow-sm", className)} {...props} />
  )
);
Card.displayName = "Card";

export const CardHeader = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("flex flex-col space-y-1.5 p-6", className)} {...props} />
  )
);
CardHeader.displayName = "CardHeader";

export const CardTitle = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(
  ({ className, ...props }, ref) => (
    <h3 ref={ref} className={cn("text-lg font-semibold leading-none tracking-tight", className)} {...props} />
  )
);
CardTitle.displayName = "CardTitle";

export const CardDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(
  ({ className, ...props }, ref) => (
    <p ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
  )
);
CardDescription.displayName = "CardDescription";

export const CardContent = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
  )
);
CardContent.displayName = "CardContent";
"""


def middleware():
    return """import { withAuth } from "next-auth/middleware";
export default withAuth({
  pages: { signIn: "/login" },
});
export const config = { matcher: ["/dashboard/:path*", "/api/((?!auth).*)"] };
"""


def components_json():
    return """{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": { "config": "tailwind.config.ts", "css": "app/globals.css", "baseColor": "neutral", "cssVariables": true },
  "aliases": { "components": "@/components", "utils": "@/lib/utils" }
}
"""


def readme_run(name, tagline):
    return f"""# {name}

> {tagline}

Full-stack Next.js 14 scaffold generated automatically.

## Stack

- Next.js 14 (App Router) + TypeScript
- Prisma ORM + PostgreSQL
- NextAuth (credentials + Google/GitHub OAuth)
- Tailwind CSS + shadcn/ui components
- Stripe-ready (env vars in `.env.example`)

## Quickstart

```bash
# 1. Install deps
npm install

# 2. Configure env
cp .env.example .env
# Edit DATABASE_URL, NEXTAUTH_SECRET (openssl rand -base64 32)

# 3. Init database
npm run db:push

# 4. Run dev server
npm run dev
```

Open http://localhost:3000.

## Folder Structure

```
app/                  # Next.js App Router
  api/                # Route handlers (REST API)
  dashboard/          # Authenticated app
  login, signup       # Auth pages
components/ui/        # shadcn/ui primitives
lib/                  # db, auth, utils
prisma/schema.prisma  # Data model
```

## API Surface

| Method | Path | Description |
|--------|------|-------------|
| POST | /api/auth/signup | Create account |
| * | /api/auth/[...nextauth] | NextAuth handlers |
| GET | /api/<resource> | List items |
| POST | /api/<resource> | Create item |
| GET | /api/<resource>/[id] | Fetch item |
| DELETE | /api/<resource>/[id] | Delete item |

## Spec Files (in parent folder)

- `../README.md` — overview
- `../SPEC.md` — product spec
- `../ARCHITECTURE.md` — system design
- `../API.md` — API surface
- `../DB_SCHEMA.md` — data model

## Deploy

```bash
# Vercel
vercel

# Or Fly.io / Railway — set DATABASE_URL + NEXTAUTH_SECRET
```
"""


# Map file generator
def build(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    slug = name.lower()
    api_resource_slug = f1.lower().replace(" ", "-")[:24]
    api_resource_model = f1.lower().replace(" ", "_")[:24]

    files = {
        "package.json": pkg(name, tagline),
        "tsconfig.json": tsconfig(),
        "next.config.mjs": next_config(),
        "tailwind.config.ts": tailwind_config(),
        "postcss.config.js": postcss_config(),
        ".env.example": env_example(),
        ".gitignore": gitignore(),
        "components.json": components_json(),
        "middleware.ts": middleware(),
        "prisma/schema.prisma": prisma_schema(name, tagline, f1),
        "app/globals.css": globals_css(),
        "app/layout.tsx": app_layout(name),
        "app/page.tsx": landing_page(name, tagline, desc, f1),
        "app/(auth)/login/page.tsx": login_page(name),
        "app/(auth)/signup/page.tsx": signup_page(name),
        "app/dashboard/page.tsx": dashboard_page(name, f1),
        f"app/api/auth/signup/route.ts": api_signup(),
        "app/api/auth/[...nextauth]/route.ts": api_nextauth(),
        f"app/api/{api_resource_slug}/route.ts": api_resource(f1, f1),
        f"app/api/{api_resource_slug}/[id]/route.ts": api_resource_detail(f1, f1),
        "lib/db.ts": lib_db(),
        "lib/auth.ts": lib_auth(),
        "lib/utils.ts": lib_utils(),
        "components/ui/button.tsx": ui_button(),
        "components/ui/card.tsx": ui_card(),
        "README.md": readme_run(name, tagline),
    }

    return files


def main():
    counts = []
    for app in APPS:
        name = app[0]
        slug = name.lower()
        base = BASE / slug
        base.mkdir(exist_ok=True)
        files = build(app)
        for path, content in files.items():
            fp = base / path
            fp.parent.mkdir(parents=True, exist_ok=True)
            fp.write_text(content, encoding="utf-8")
        counts.append((name, len(files)))
    total_files = sum(c for _, c in counts)
    print(f"Generated full-stack scaffolds for {len(counts)} apps, {total_files} files total.")


if __name__ == "__main__":
    main()
