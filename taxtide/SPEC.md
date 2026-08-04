# TaxTide — Product Specification

## 1. Vision

**TaxTide** is a finance / accounting SaaS that **tax calculation**.

> Sales tax, VAT, GST — across jurisdictions. TaxTide calculates, files, and remits.

## 2. Target Customer

- **Primary persona:** E-commerce founder
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Multi-jurisdiction rates

## 3. Jobs To Be Done

1. When e-commerce founders face a chaotic workflow, they want a single tool, so TaxTide consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so TaxTide ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so TaxTide is built compliance-first.

## 4. Core Features

### 4.1 Multi-jurisdiction rates
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Auto-file
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Nexus monitoring
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

- **Q1:** MVP with Multi-jurisdiction rates
- **Q2:** Add Auto-file + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Multi-jurisdiction rates |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
