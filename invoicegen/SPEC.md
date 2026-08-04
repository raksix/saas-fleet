# InvoiceGen — Product Specification

## 1. Vision

**InvoiceGen** is a finance / accounting SaaS that **recurring invoicing**.

> Subscription + usage + milestone billing with dunning and Stripe/GoCardless integration.

## 2. Target Customer

- **Primary persona:** Biller
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Recurring + usage billing

## 3. Jobs To Be Done

1. When billers face a chaotic workflow, they want a single tool, so InvoiceGen consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so InvoiceGen ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so InvoiceGen is built compliance-first.

## 4. Core Features

### 4.1 Recurring + usage billing
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Dunning sequences
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Stripe/GoCardless
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

- **Q1:** MVP with Recurring + usage billing
- **Q2:** Add Dunning sequences + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Recurring + usage billing |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
