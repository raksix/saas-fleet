# SalesCoach — Product Specification

## 1. Vision

**SalesCoach** is a sales / crm SaaS that **ai sales coaching**.

> Score every call against your sales playbook. SalesCoach gives reps weekly coaching cards.

## 2. Target Customer

- **Primary persona:** Sales manager
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Call scoring

## 3. Jobs To Be Done

1. When sales managers face a chaotic workflow, they want a single tool, so SalesCoach consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so SalesCoach ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so SalesCoach is built compliance-first.

## 4. Core Features

### 4.1 Call scoring
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Coaching cards
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Rep leaderboard
- **Spec:** AI-assisted with human override.
- **Edge cases:** hallucination guards, citation required.
- **KPIs:** task completion rate, override rate.

## 5. User Flows

1. **Signup:** Magic link → workspace → first-run checklist.
2. **Activation:** Connect data source → see first insight in <5 min.
3. **Expansion:** Invite teammate → assign role → unlock team features.
4. **Billing:** Free → Pro on usage threshold; Team on SSO request.

## 6. Success Metrics (NSM, North Star)

- Weekly Active Workspaces (WAW)
- Weekly value-action completion rate
- Net revenue retention (NRR) > 110%

## 7. Roadmap

- **Q1:** MVP with Call scoring
- **Q2:** Add Coaching cards + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Call scoring |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
