# NotiNest — Product Specification

## 1. Vision

**NotiNest** is a communication SaaS that **notification routing**.

> Route alerts from monitoring tools to the right person via Slack/SMS/PagerDuty.

## 2. Target Customer

- **Primary persona:** SRE
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Alert routing

## 3. Jobs To Be Done

1. When sres face a chaotic workflow, they want a single tool, so NotiNest consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so NotiNest ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so NotiNest is built compliance-first.

## 4. Core Features

### 4.1 Alert routing
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 On-call schedules
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Escalation policies
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

- **Q1:** MVP with Alert routing
- **Q2:** Add On-call schedules + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Alert routing |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
