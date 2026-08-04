# RevOpsAI — Product Specification

## 1. Vision

**RevOpsAI** is a sales / crm SaaS that **revenue operations dashboard**.

> Single pane of glass for ARR, churn, expansion, and pipeline coverage — with anomaly detection.

## 2. Target Customer

- **Primary persona:** RevOps lead
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** ARR/churn dashboard

## 3. Jobs To Be Done

1. When revops leads face a chaotic workflow, they want a single tool, so RevOpsAI consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so RevOpsAI ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so RevOpsAI is built compliance-first.

## 4. Core Features

### 4.1 ARR/churn dashboard
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Anomaly detection
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Cohort views
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

- **Q1:** MVP with ARR/churn dashboard
- **Q2:** Add Anomaly detection + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: ARR/churn dashboard |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
