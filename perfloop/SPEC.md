# PerfLoop — Product Specification

## 1. Vision

**PerfLoop** is a hr / recruiting SaaS that **performance review cycles**.

> Run 360s, manager reviews, and calibration with templates and AI-suggested comments (editable).

## 2. Target Customer

- **Primary persona:** HRBP
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** 360 review engine

## 3. Jobs To Be Done

1. When hrbps face a chaotic workflow, they want a single tool, so PerfLoop consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so PerfLoop ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so PerfLoop is built compliance-first.

## 4. Core Features

### 4.1 360 review engine
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Calibration mode
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 AI-suggested feedback
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

- **Q1:** MVP with 360 review engine
- **Q2:** Add Calibration mode + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: 360 review engine |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
