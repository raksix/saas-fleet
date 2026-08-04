# LearnPath — Product Specification

## 1. Vision

**LearnPath** is a hr / recruiting SaaS that **employee learning paths**.

> Assign role-based learning paths with content from Coursera/Udemy/internal LMS, and track completion.

## 2. Target Customer

- **Primary persona:** L&D lead
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Path builder

## 3. Jobs To Be Done

1. When l&d leads face a chaotic workflow, they want a single tool, so LearnPath consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so LearnPath ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so LearnPath is built compliance-first.

## 4. Core Features

### 4.1 Path builder
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 SCORM/xAPI support
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Manager dashboards
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

- **Q1:** MVP with Path builder
- **Q2:** Add SCORM/xAPI support + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Path builder |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
