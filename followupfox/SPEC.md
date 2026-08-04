# FollowUpFox — Product Specification

## 1. Vision

**FollowUpFox** is a sales / crm SaaS that **automated follow-up sequences**.

> Multi-step cadences across email/LinkedIn/SMS with reply detection and human handoff.

## 2. Target Customer

- **Primary persona:** SDR / AE
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** Multi-channel cadences

## 3. Jobs To Be Done

1. When sdr / aes face a chaotic workflow, they want a single tool, so FollowUpFox consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so FollowUpFox ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so FollowUpFox is built compliance-first.

## 4. Core Features

### 4.1 Multi-channel cadences
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 Reply detection
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 Reply classification
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

- **Q1:** MVP with Multi-channel cadences
- **Q2:** Add Reply detection + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: Multi-channel cadences |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
