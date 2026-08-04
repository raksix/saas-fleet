# SkillMap — Database Schema

PostgreSQL 16. All tables include `id uuid pk`, `created_at`, `updated_at`, `deleted_at`.

## Identity

### `users`
- `email text unique`
- `name text`
- `avatar_url text`
- `email_verified_at timestamptz`

### `orgs`
- `name text`
- `slug text unique`
- `plan text` — free|starter|pro|team|enterprise
- `stripe_customer_id text`

### `org_members`
- `org_id fk orgs`
- `user_id fk users`
- `role text` — owner|admin|member|viewer
- unique `(org_id, user_id)`

## Domain — Skill graph

### `skill_graphs`
- `org_id fk orgs`
- `name text`
- `status text`
- `payload jsonb`
- `created_by fk users`

### `skill_graph_events`
- `parent_id fk`
- `actor_id fk users`
- `event jsonb`
- `occurred_at timestamptz`

## Domain — Internal gig board

### `internal_gig_board_configs`
- `org_id fk orgs`
- `config jsonb`

## Domain — Manager visibility (AI)

### `ai_tasks`
- `org_id fk orgs`
- `kind text`
- `input jsonb`
- `output jsonb`
- `status text` — queued|running|done|failed
- `cost_cents int`
- `model text`
- `approved_by fk users`

### `ai_task_reviews`
- `task_id fk ai_tasks`
- `reviewer_id fk users`
- `decision text` — approve|reject|edit
- `notes text`

## Billing

### `subscriptions`
- `org_id fk orgs unique`
- `stripe_subscription_id text`
- `status text`
- `current_period_end timestamptz`

### `invoices`
- `org_id fk orgs`
- `stripe_invoice_id text`
- `amount_cents int`
- `status text`

## Observability

### `audit_logs`
- `org_id fk orgs`
- `actor_id fk users`
- `action text`
- `target_type text`
- `target_id text`
- `metadata jsonb`
- `ip inet`
- `user_agent text`

### `webhook_deliveries`
- `webhook_id fk webhooks`
- `event text`
- `payload jsonb`
- `response_status int`
- `attempt_count int`
- `delivered_at timestamptz`

## Indexes

- `(org_id, created_at desc)` on heavy tables
- GIN index on `payload jsonb`
- Partial index on `deleted_at is null`

## RLS

All org-scoped tables enforce `org_id = current_setting('app.org_id')`.
