# Scriptly Pro

> Screenplay formatting

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
