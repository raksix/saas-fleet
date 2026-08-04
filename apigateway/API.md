# APIGateway — API Surface

All endpoints under `/api/v1`. Auth via Bearer token (PAT) or session cookie.

## Auth

- `POST /auth/signup` — create account
- `POST /auth/login` — magic link
- `POST /auth/refresh` — refresh access token
- `POST /auth/logout` — invalidate session

## Organizations

- `POST /orgs` — create org
- `GET /orgs/:id` — fetch org
- `PATCH /orgs/:id` — update org
- `POST /orgs/:id/members` — invite user

## Core Resources

### API key + OAuth
- `GET /resources` — list (paginated, filterable)
- `POST /resources` — create
- `GET /resources/:id` — fetch
- `PATCH /resources/:id` — update
- `DELETE /resources/:id` — soft delete

### Rate limiting
- `GET /secondary` — list
- `POST /secondary` — trigger

### Auto-generated docs
- `POST /ai/tasks` — submit AI task
- `GET /ai/tasks/:id` — poll result
- `POST /ai/tasks/:id/approve` — human-in-loop approval

## Webhooks

- `POST /webhooks` — register endpoint
- `GET /webhooks/:id/deliveries` — list deliveries
- `POST /webhooks/:id/replay` — replay failed delivery

## Errors

Standard error envelope:

```json
{
  "error": {
    "code": "rate_limited",
    "message": "Too many requests",
    "request_id": "req_..."
  }
}
```

Common codes: `unauthorized`, `forbidden`, `not_found`, `validation_error`, `rate_limited`, `conflict`, `internal`.

## Rate Limits

| Tier | RPS | Burst |
|------|-----|-------|
| Free | 5 | 10 |
| Starter | 20 | 40 |
| Pro | 100 | 200 |
| Team | 500 | 1000 |
| Enterprise | Custom | Custom |

## SDKs

- TypeScript (`@apigateway/sdk`)
- Python (`apigateway-sdk`)
- Go (`go.apigateway.dev`)

## OpenAPI

Spec auto-generated from server; available at `/api/v1/openapi.json`.
