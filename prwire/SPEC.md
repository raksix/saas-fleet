# PRWire — Product Specification

## 1. Vision

**PRWire** is a marketing SaaS that **press release distribution**.

> Draft, distribute, and measure PR. PRWire syndicates to 500+ outlets with journalist matching.

## 2. Target Customer

- **Primary persona:** Comms lead
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Distribution network

## 3. Jobs To Be Done

1. When comms leads face a chaotic workflow, they want a single tool, so PRWire consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so PRWire ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so PRWire is built compliance-first.

## 4. Core Features

### 4.1 Distribution network
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Journalist matching
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Pickup tracking
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

- **Q1:** MVP with Distribution network
- **Q2:** Add Journalist matching + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Distribution network |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
