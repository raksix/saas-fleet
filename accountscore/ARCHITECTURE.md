# AccountScore — System Architecture

## High-Level Diagram

```
            ┌──────────────────────────┐
            │   Web (Next.js)          │
            │   Mobile (PWA / RN)      │
            └────────────┬─────────────┘
                         │ HTTPS / WSS
                         ▼
            ┌──────────────────────────┐
            │   API Gateway (Fastify)  │
            │   Auth, Rate Limit       │
            └────┬─────────┬───────────┘
                 │         │
       ┌─────────▼─┐   ┌───▼─────────────�
       │ Core API   │   │ Async Workers   │
       │ (REST/GQL) │   │ (BullMQ)        │
       └────┬───────┘   └───┬─────────────┘
            │                │
   ┌────────▼────────┐  ┌────▼────────────┐
   │ PostgreSQL      │  │ Redis cache     │
   │ (primary)       │  │ + queue         │
   └─────────────────┘  └─────────────────┘

  Analytics: ClickHouse / BigQuery (ETL via Kafka)
  AI:        LiteLLM gateway → OpenAI / Anthropic / OSS
  Storage:   S3 (uploads, exports)
  Search:    Meilisearch
  Realtime:  Pusher / Socket.io
  Billing:   Stripe
```

## Components

### API Gateway
- Fastify + TypeScript
- JWT + API key auth
- Rate limiting (token bucket per org)
- Request signing for webhooks
- OpenAPI → typed SDK generation

### Core Services
- Tenants (orgs), users, RBAC
- Composite health score service
- Churn early-warning service
- Playbook triggers service (AI-backed)
- Billing service (Stripe webhooks)
- Audit log service

### Data Layer
- PostgreSQL (primary OLTP) with row-level security
- Redis (cache, rate limit, ephemeral state)
- Meilisearch (full-text + faceted)
- ClickHouse (analytics warehouse)
- S3 (uploads, exports)

### Async Workers
- BullMQ on Redis for background jobs
- Workers: email, exports, AI batch, webhooks fan-out
- Dead-letter queue + retries

### Frontend
- Next.js 14 (App Router) + RSC
- Tailwind + shadcn/ui
- tRPC or REST
- React Query for client cache
- PWA for mobile

### AI Layer
- LiteLLM gateway (OpenAI, Anthropic, OSS)
- Vector DB (pgvector) for RAG
- Caching layer (semantic cache)
- Human-in-loop UI for sensitive tasks

## Cross-Cutting Concerns

- **Observability:** OpenTelemetry traces, Grafana dashboards, Highlight.io session replay.
- **Secrets:** Vault or AWS Secrets Manager.
- **Feature flags:** internal FeatureFlag service (or LaunchDarkly).
- **CI/CD:** GitHub Actions → Buildkite → Fly.io / Railway.
- **Compliance:** SOC 2 controls baked into code review checklist.

## Scaling Plan

| Stage | Bottleneck | Action |
|-------|------------|--------|
| 0–1K users | None | Single-region, small DB |
| 1K–50K | DB read load | Add read replica + Redis |
| 50K–500K | Queue lag | Shard workers, Kafka |
| 500K+ | Multi-region | Active-active, edge API |

## Cost Notes

- DB + cache dominate at low scale
- AI inference dominates at high scale → cache aggressively
- Observability stays under 10% of infra via sampling
