# PropertyPilot — Product Specification

## 1. Vision

**PropertyPilot** is a real estate SaaS that **listing management**.

> Sync listings to MLS, Zillow, Realtor.com. Track showings and leads in one inbox.

## 2. Target Customer

- **Primary persona:** Listing agent
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** MLS syndication

## 3. Jobs To Be Done

1. When listing agents face a chaotic workflow, they want a single tool, so PropertyPilot consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so PropertyPilot ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so PropertyPilot is built compliance-first.

## 4. Core Features

### 4.1 MLS syndication
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Lead inbox
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Showing scheduler
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

- **Q1:** MVP with MLS syndication
- **Q2:** Add Lead inbox + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: MLS syndication |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
