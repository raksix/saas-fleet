# SaaS Fleet — 1000 App Concepts

A monorepo containing 1000 SaaS app concepts, each with a full-stack Next.js 14 + Prisma + NextAuth scaffold.

## Structure

```
.
├── INDEX.md                  # List of all 1000 apps by category
├── _generate.py              # Original spec generator (100 apps)
├── _generate_fs.py           # Full-stack scaffold generator
├── _generate_900.py          # 900 additional apps generator
└── <app-slug>/               # One folder per SaaS app
    ├── README.md             # App overview
    ├── SPEC.md               # Product specification
    ├── ARCHITECTURE.md       # System architecture
    ├── API.md                # API surface
    ├── DB_SCHEMA.md          # Data model
    ├── package.json          # Node deps
    ├── tsconfig.json
    ├── next.config.mjs
    ├── tailwind.config.ts
    ├── postcss.config.js
    ├── components.json
    ├── middleware.ts
    ├── .env.example
    ├── .gitignore
    ├── prisma/
    │   └── schema.prisma     # Database schema
    ├── app/
    │   ├── layout.tsx
    │   ├── globals.css
    │   ├── page.tsx          # Landing page
    │   ├── (auth)/
    │   │   ├── login/page.tsx
    │   │   └── signup/page.tsx
    │   ├── dashboard/page.tsx
    │   └── api/
    │       ├── auth/
    │       │   ├── signup/route.ts
    │       │   └── [...nextauth]/route.ts
    │       └── <resource>/
    │           ├── route.ts          # GET + POST
    │           └── [id]/route.ts     # GET + DELETE
    ├── lib/
    │   ├── db.ts             # Prisma client
    │   ├── auth.ts           # NextAuth config
    │   └── utils.ts
    └── components/
        └── ui/
            ├── button.tsx
            └── card.tsx
```

## Categories (1000 apps)

- Productivity (10)
- Marketing (10)
- Sales / CRM (10)
- HR / Recruiting (10)
- Finance / Accounting (10)
- Education (10)
- Healthcare (5)
- Real Estate (5)
- E-commerce (10)
- Developer Tools (10)
- Analytics (5)
- Communication (5)
- AI Tools (100)
- Content Creation (100)
- Customer Support (100)
- Project Management (100)
- Data & BI (100)
- Security (100)
- Integration Tools (100)
- Voice/Audio (100)
- Video/Media (100)

## Tech Stack (per app)

- **Frontend:** Next.js 14 (App Router), TypeScript, Tailwind, shadcn/ui
- **Backend:** Next.js API routes (Fastify-ready)
- **Database:** PostgreSQL via Prisma ORM
- **Auth:** NextAuth (credentials + Google/GitHub OAuth)
- **Billing:** Stripe (env-configured)
- **Email:** Resend (env-configured)

## Quick Start (any app)

```bash
cd <app-slug>
npm install
cp .env.example .env
# Edit DATABASE_URL and NEXTAUTH_SECRET (openssl rand -base64 32)
npm run db:push
npm run dev
```

## Generation Scripts

To regenerate everything from scratch:

```bash
python _generate.py        # 100 spec concepts
python _generate_fs.py     # full-stack scaffolds for those 100
python _generate_900.py    # 900 additional apps with full-stack
```

## Notes

- All code is auto-generated and serves as a starting point.
- Each app follows the same scaffold structure for consistency.
- Customize per-app copy, features, and integrations as needed.

---

Generated with Claude Code.
