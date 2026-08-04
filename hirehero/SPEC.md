# HireHero — Product Specification

## 1. Vision

**HireHero** is a hr / recruiting SaaS that **ai recruiting assistant**.

> Source, screen, and schedule candidates. HireHero scores applicants against the role and shortlists in minutes.

## 2. Target Customer

- **Primary persona:** Recruiter
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** AI resume scoring

## 3. Jobs To Be Done

1. When recruiters face a chaotic workflow, they want a single tool, so HireHero consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so HireHero ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so HireHero is built compliance-first.

## 4. Core Features

### 4.1 AI resume scoring
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Auto-scheduling
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Bias auditing
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

- **Q1:** MVP with AI resume scoring
- **Q2:** Add Auto-scheduling + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: AI resume scoring |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
