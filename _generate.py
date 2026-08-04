"""Generate 100 detailed SaaS app specs into subfolders."""
import os
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d")

APPS = [
    # (name, category, tagline, description, primary_feature, secondary_feature, tertiary_feature, target_persona)
    ("TaskForge", "Productivity", "AI task management for distributed teams",
     "Distributed teams need clarity. TaskForge auto-prioritizes work using AI, syncs with Slack/Linear, and surfaces blockers before they escalate.",
     "AI prioritization engine", "Slack & Linear sync", "Blocker detection radar", "Engineering manager"),
    ("MeetingMind", "Productivity", "Meeting summarizer with action items",
     "Stop wasting hours in meetings. MeetingMind joins calls, records, transcribes, and extracts decisions + action items with owners.",
     "Real-time transcription", "Action-item extraction", "Decision log", "Product manager"),
    ("Calendo", "Productivity", "Smart calendar with focus time protection",
     "Calendo auto-blocks focus time based on your work patterns and politely deflects meetings into focus-friendly slots.",
     "Focus-time auto-blocking", "Deflection templates", "Energy-aware scheduling", "Knowledge worker"),
    ("Notedeck", "Productivity", "Voice-to-structured-notes",
     "Brain dump by voice. Notedeck transcribes, organizes into notebooks, tags entities, and links to your calendar/PKM tools.",
     "Voice capture (mobile)", "Entity extraction", "Bidirectional links", "Writer / researcher"),
    ("FocusFlow", "Productivity", "Deep work session tracker",
     "Track deep-work sessions, measure flow state, and get team-level analytics without surveillance.",
     "Pomodoro + flow tracking", "Aggregate (non-surveillance) analytics", "Calendar integration", "Engineering team lead"),
    ("DocBridge", "Productivity", "Collaborative document co-pilot",
     "DocBridge is the AI co-author for long-form docs. Suggests restructuring, fixes inconsistencies, and keeps voice consistent.",
     "Style consistency AI", "Restructure suggestions", "Comment summarization", "Technical writer"),
    ("WikiWeave", "Productivity", "Internal knowledge base builder",
     "Turn tribal knowledge into searchable wiki. WikiWeave crawls Slack/Notion/Google Drive, deduplicates, and links concepts.",
     "Multi-source ingestion", "Dedup & merge", "Concept graph", "Head of operations"),
    ("Standuply", "Productivity", "Async standup automation",
     "Run async standups across timezones. Standuply collects updates, surfaces blockers, and ships a digest to managers.",
     "Configurable prompts", "Blocker heatmap", "Manager digest", "Remote team lead"),
    ("TimeBlock", "Productivity", "Time-blocking productivity coach",
     "Plan your day in 25-minute blocks. TimeBlock learns your patterns and suggests a realistic plan each morning.",
     "Daily plan suggestion", "Pattern learning", "Energy tracking", "Founder / IC"),
    ("GoalGrid", "Productivity", "OKR tracking with weekly check-ins",
     "OKRs die in spreadsheets. GoalGrid makes them alive with weekly check-ins, automatic rollups, and visual progress.",
     "OKR hierarchy", "Weekly check-in flow", "Visual progress charts", "Strategy lead"),

    ("ReachWave", "Marketing", "Multi-channel campaign manager",
     "Plan, launch, and measure campaigns across email, social, paid, and content — from one canvas.",
     "Unified campaign canvas", "Cross-channel attribution", "Asset library", "Marketing manager"),
    ("SegmentSense", "Marketing", "Customer segmentation engine",
     "Slice your customer base into actionable segments using product usage, RFM, and AI-discovered cohorts.",
     "RFM + behavioral segments", "AI cohort discovery", "Segment export to ad platforms", "Growth marketer"),
    ("EmailForge", "Marketing", "AI email copy generator",
     "Generate on-brand email copy for every lifecycle stage. Train on your best performers, A/B test variants.",
     "Brand-voice training", "Variant generation", "Auto A/B testing", "Lifecycle marketer"),
    ("SocialPulse", "Marketing", "Social media analytics",
     "Stop juggling 6 dashboards. SocialPulse unifies organic + paid social with content performance scoring.",
     "Cross-platform metrics", "Content scoring", "Competitor benchmarking", "Social media manager"),
    ("BrandKit", "Marketing", "Brand asset manager",
     "Central source of truth for logos, colors, fonts, and copy. BrandKit serves approved assets via CDN to all tools.",
     "Asset library", "Brand guidelines", "CDN-served embeds", "Brand manager"),
    ("SEOBoost", "Marketing", "SEO content optimizer",
     "Brief writers, score drafts, and track rankings. SEOBoost closes the loop between content production and SERP movement.",
     "Content brief generator", "Draft scoring", "SERP tracking", "Content SEO lead"),
    ("AdPilot", "Marketing", "Programmatic ad campaign manager",
     "Launch Google/Meta/LinkedIn ads from one place with budget pacing, creative rotation, and incrementality tests.",
     "Cross-platform launch", "Budget pacing", "Creative rotation", "Performance marketer"),
    ("LandingLab", "Marketing", "A/B testing for landing pages",
     "Variant editor with built-in stats engine. LandingLab ships winning variants without dev tickets.",
     "Visual variant editor", "Bayesian stats engine", "Auto-promote winner", "Growth PM"),
    ("LeadMagnet", "Marketing", "Lead capture and nurture",
     "Forms, quizzes, gated content, drip campaigns — LeadMagnet turns cold traffic into qualified pipeline.",
     "Drag-drop form builder", "Drip campaign engine", "Lead scoring", "Demand gen manager"),
    ("PRWire", "Marketing", "Press release distribution",
     "Draft, distribute, and measure PR. PRWire syndicates to 500+ outlets with journalist matching.",
     "Distribution network", "Journalist matching", "Pickup tracking", "Comms lead"),

    ("PipePilot", "Sales / CRM", "Sales pipeline visualizer",
     "Kanban for deals with forecasting built in. PipePilot flags slipping deals and suggests next actions.",
     "Pipeline kanban", "AI forecasting", "Next-best-action", "Sales rep"),
    ("DealDesk", "Sales / CRM", "Quote and proposal generator",
     "CPQ with approvals. DealDesk configures products, applies discount rules, routes approvals, and e-signs.",
     "CPQ configurator", "Discount guardrails", "DocuSign integration", "Sales engineer"),
    ("RevOpsAI", "Sales / CRM", "Revenue operations dashboard",
     "Single pane of glass for ARR, churn, expansion, and pipeline coverage — with anomaly detection.",
     "ARR/churn dashboard", "Anomaly detection", "Cohort views", "RevOps lead"),
    ("ContactCloud", "Sales / CRM", "Unified contact database",
     "One record per person across email, calendar, product, and support. ContactCloud dedupes and enriches.",
     "Cross-source dedup", "Auto-enrichment", "Identity resolution", "Sales ops"),
    ("FollowUpFox", "Sales / CRM", "Automated follow-up sequences",
     "Multi-step cadences across email/LinkedIn/SMS with reply detection and human handoff.",
     "Multi-channel cadences", "Reply detection", "Reply classification", "SDR / AE"),
    ("DemoDeck", "Sales / CRM", "Interactive product demo builder",
     "Record a demo once. Re-cut it per persona, add interactivity, and track what prospects actually watch.",
     "Record-once persona cuts", "Interactive overlays", "Viewer analytics", "Sales engineer"),
    ("WinLossAI", "Sales / CRM", "Win/loss analysis platform",
     "Auto-categorize why deals are won or lost using call transcripts, emails, and CRM notes.",
     "Win/loss categorizer", "Trend dashboards", "Buyer-sentiment scoring", "Sales leader"),
    ("PartnerHub", "Sales / CRM", "Channel partner management",
     "Onboard partners, share leads, track registrations, and pay commissions — all in one portal.",
     "Partner onboarding", "Lead sharing", "Commission engine", "Channel manager"),
    ("AccountScore", "Sales / CRM", "Account health scoring",
     "Composite health score from product usage, NPS, support tickets, and CRM signals.",
     "Composite health score", "Churn early-warning", "Playbook triggers", "CSM"),
    ("SalesCoach", "Sales / CRM", "AI sales coaching",
     "Score every call against your sales playbook. SalesCoach gives reps weekly coaching cards.",
     "Call scoring", "Coaching cards", "Rep leaderboard", "Sales manager"),

    ("HireHero", "HR / Recruiting", "AI recruiting assistant",
     "Source, screen, and schedule candidates. HireHero scores applicants against the role and shortlists in minutes.",
     "AI resume scoring", "Auto-scheduling", "Bias auditing", "Recruiter"),
    ("OnboardPro", "HR / Recruiting", "Employee onboarding workflows",
     "30/60/90 plans, checklists, document e-sign, buddy assignment, and Slack nudges.",
     "30/60/90 templates", "Doc e-sign", "Slack nudges", "People ops"),
    ("PulseCheck", "HR / Recruiting", "Employee engagement surveys",
     "Run eNPS, pulse surveys, and exit interviews. PulseCheck surfaces themes with AI clustering.",
     "Pulse surveys", "AI theme clustering", "Anonymity guarantees", "HR lead"),
    ("SkillMap", "HR / Recruiting", "Internal talent marketplace",
     "Match employees to internal gigs, projects, and stretch assignments based on skills and goals.",
     "Skill graph", "Internal gig board", "Manager visibility", "Head of people"),
    ("PayrollPal", "HR / Recruiting", "Multi-country payroll",
     "Run payroll in 50+ countries with contractor + EOR support, taxes, and payslips.",
     "Multi-country engine", "Contractor + EOR", "Tax filing add-on", "Finance / HR"),
    ("TimeOff", "HR / Recruiting", "PTO management",
     "Accruals, carryover, blackout dates, and team calendars — TimeOff replaces the spreadsheet chaos.",
     "Accrual engine", "Team calendar", "Slack approvals", "Office manager"),
    ("LearnPath", "HR / Recruiting", "Employee learning paths",
     "Assign role-based learning paths with content from Coursera/Udemy/internal LMS, and track completion.",
     "Path builder", "SCORM/xAPI support", "Manager dashboards", "L&D lead"),
    ("PerfLoop", "HR / Recruiting", "Performance review cycles",
     "Run 360s, manager reviews, and calibration with templates and AI-suggested comments (editable).",
     "360 review engine", "Calibration mode", "AI-suggested feedback", "HRBP"),
    ("CompCalc", "HR / Recruiting", "Compensation planning",
     "Plan raises, bonuses, and equity refreshes with budget guardrails and pay-equity checks.",
     "Budget modeling", "Pay-equity audit", "Approval workflow", "Compensation lead"),
    ("CultureDeck", "HR / Recruiting", "Culture and values management",
     "Define values, attach them to review criteria, and run culture surveys with consistent scoring.",
     "Value definitions", "Behavior anchors", "Culture survey", "Founder / CEO"),

    ("BooksBot", "Finance / Accounting", "AI bookkeeping",
     "BooksBot ingests bank/Plaid feeds, categorizes transactions, and prepares books for your accountant.",
     "Bank feed ingest", "Auto-categorization", "Accountant handoff", "Small business owner"),
    ("ExpensEasy", "Finance / Accounting", "Expense management",
     "Snap receipts, auto-extract line items, enforce policy, and reimburse via Stripe/ACH.",
     "Receipt OCR", "Policy engine", "Reimbursement payouts", "Finance team"),
    ("BudgetBurn", "Finance / Accounting", "Budget vs actuals tracking",
     "Roll up budgets from departments, track actuals in real-time, and alert on overruns.",
     "Department hierarchies", "Real-time actuals", "Overrun alerts", "FP&A"),
    ("CashCast", "Finance / Accounting", "Cash flow forecasting",
     "Combine AR, AP, payroll, and runway scenarios into a rolling 13-week cash forecast.",
     "13-week forecast", "Scenario modeling", "Bank integration", "CFO"),
    ("TaxTide", "Finance / Accounting", "Tax calculation",
     "Sales tax, VAT, GST — across jurisdictions. TaxTide calculates, files, and remits.",
     "Multi-jurisdiction rates", "Auto-file", "Nexus monitoring", "E-commerce founder"),
    ("AuditLog", "Finance / Accounting", "Audit trail manager",
     "Tamper-evident logs of every financial action with reviewer signatures for SOX compliance.",
     "Tamper-evident logs", "Reviewer signatures", "SOX templates", "Controller"),
    ("InvoiceGen", "Finance / Accounting", "Recurring invoicing",
     "Subscription + usage + milestone billing with dunning and Stripe/GoCardless integration.",
     "Recurring + usage billing", "Dunning sequences", "Stripe/GoCardless", "Biller"),
    ("VendorVault", "Finance / Accounting", "Vendor management",
     "Vendor onboarding, W-9 collection, 1099 generation, and AP automation.",
     "Vendor onboarding", "W-9 + 1099", "AP automation", "AP clerk"),
    ("Subscriptly", "Finance / Accounting", "Subscription billing",
     "Modern recurring billing with plans, coupons, proration, and churn analytics.",
     "Plan/proration engine", "Coupons & trials", "Churn analytics", "Subscription founder"),
    ("LedgerLite", "Finance / Accounting", "Double-entry accounting",
     "Clean double-entry with multi-entity consolidation and accountant-friendly reports.",
     "Double-entry engine", "Multi-entity", "Financial reports", "Startup CFO"),

    ("LearnLoop", "Education", "Course platform builder",
     "Launch a Teachable-like school in hours: video lessons, quizzes, payments, and cohort analytics.",
     "Video drip", "Quiz engine", "Cohort analytics", "Creator / educator"),
    ("QuizCraft", "Education", "AI quiz generator",
     "Turn any document into a quiz with multiple choice, short answer, and rubric-graded essays.",
     "Doc-to-quiz AI", "Auto grading", "LMS export", "K-12 teacher"),
    ("TutorMatch", "Education", "1-on-1 tutoring marketplace",
     "Match students with vetted tutors by subject, level, timezone, and budget. TutorMatch handles booking + payment.",
     "Tutor vetting", "Matching engine", "Booking + payouts", "Parent / student"),
    ("ClassCloud", "Education", "Virtual classroom",
     "Live classes with whiteboard, breakout rooms, attendance, and recording — no Zoom required.",
     "Live whiteboard", "Breakout rooms", "Recording", "Online school admin"),
    ("SkillForge", "Education", "Coding bootcamp platform",
     "Cohort-based bootcamps with code review, project rubrics, mentor matching, and outcomes tracking.",
     "Code review queue", "Project rubrics", "Outcomes tracking", "Bootcamp founder"),
    ("EssayGrade", "Education", "AI essay grading",
     "Score essays against rubrics with explainable feedback. Teachers review and override.",
     "Rubric-based scoring", "Teacher override", "Class analytics", "High school teacher"),
    ("FlashFlex", "Education", "Spaced repetition flashcards",
     "FSRS algorithm with shared decks, image occlusion, and cross-device sync.",
     "FSRS scheduler", "Image occlusion", "Shared decks", "Med student"),
    ("MentorMix", "Education", "Mentor-mentee matching",
     "Match mentees with mentors by goals, industry, and availability. Manage sessions and feedback.",
     "Smart matching", "Session notes", "Feedback loop", "Career coach"),
    ("Proctool", "Education", "Online exam proctoring",
     "Browser lockdown, webcam AI, and identity verification for high-stakes online exams.",
     "Browser lockdown", "Webcam AI", "ID verification", "University admin"),
    ("CourseCraft", "Education", "Curriculum designer",
     "Standards-aligned curriculum mapping with lesson plans, materials, and assessments.",
     "Standards mapping", "Lesson planner", "Assessment bank", "Curriculum director"),

    ("ClinicOps", "Healthcare", "Practice management",
     "Scheduling, charting, billing, and telehealth in one HIPAA-ready platform for small clinics.",
     "Scheduling", "EMR charting", "Telehealth", "Clinic owner"),
    ("RxPad", "Healthcare", "E-prescription system",
     "EPCS-certified e-prescribing with formulary, drug-interaction checks, and pharmacy network.",
     "EPCS e-prescribing", "Formulary + interactions", "Pharmacy network", "Physician"),
    ("PatientPing", "Healthcare", "Patient communication",
     "Two-way SMS, reminders, recalls, and broadcast messages — HIPAA compliant.",
     "Two-way SMS", "Recalls", "Broadcasts", "Office manager"),
    ("TeleCare", "Healthcare", "Telemedicine platform",
     "Video visits with waiting room, screen-share, e-prescribe handoff, and integrated payments.",
     "Waiting room", "Screen share", "Rx handoff", "Telemedicine doctor"),
    ("LabFlow", "Healthcare", "Lab results manager",
     "Ingest HL7/FHIR lab results, route to providers, and notify patients through PatientPing.",
     "HL7/FHIR ingest", "Provider routing", "Patient notifications", "Lab director"),

    ("PropertyPilot", "Real Estate", "Listing management",
     "Sync listings to MLS, Zillow, Realtor.com. Track showings and leads in one inbox.",
     "MLS syndication", "Lead inbox", "Showing scheduler", "Listing agent"),
    ("RentRelay", "Real Estate", "Rental management",
     "Tenant screening, leases, rent collection, and maintenance tickets for landlords.",
     "Tenant screening", "E-sign leases", "Rent collection", "Small landlord"),
    ("ShowingScheduler", "Real Estate", "Tour scheduling",
     "Self-serve tour booking with availability sync, ID verification, and feedback capture.",
     "Self-serve booking", "ID verification", "Feedback capture", "Buyer's agent"),
    ("LeadLock", "Real Estate", "Real estate lead CRM",
     "Speed-to-lead text-back, drip campaigns, and source attribution for buyer/seller leads.",
     "Speed-to-lead text", "Drip campaigns", "Source attribution", "Team broker"),
    ("Mortgauge", "Real Estate", "Mortgage calculator",
     "Embeddable mortgage widget with live rates, amortization, and lender matching.",
     "Live rate feed", "Amortization", "Lender matching", "Real estate site owner"),

    ("StoreForge", "E-commerce", "Headless commerce backend",
     "API-first commerce with cart, checkout, and order management. Bring your own frontend.",
     "Cart/checkout API", "Order management", "Multi-currency", "Headless dev"),
    ("CartCraft", "E-commerce", "Conversion-optimized cart",
     "Drop-in cart with upsells, A/B testing, and recovery emails that beat Shopify defaults.",
     "Upsell engine", "Cart A/B testing", "Recovery emails", "DTC founder"),
    ("ReviewRocket", "E-commerce", "Product review platform",
     "Photo/video reviews, post-purchase email, and on-site widgets. ReviewRocket beats Yotpo for SMBs.",
     "Photo/video reviews", "Post-purchase email", "On-site widgets", "DTC marketer"),
    ("ShipStation", "E-commerce", "Shipping label manager",
     "Compare carrier rates, print labels, and track packages — across UPS, FedEx, USPS, DHL.",
     "Carrier rate compare", "Bulk label print", "Tracking page", "Fulfillment lead"),
    ("DropshipHub", "E-commerce", "Dropshipping automation",
     "Find products, push to store, auto-fulfill. DropshipHub replaces 5 tools with one.",
     "Product research", "Auto-fulfill", "Margin tracking", "Solo dropshipper"),
    ("InventoryIQ", "E-commerce", "Inventory optimizer",
     "Demand forecasting, reorder point automation, and multi-warehouse balancing.",
     "Demand forecasting", "Reorder automation", "Multi-WH balancing", "Operations lead"),
    ("ReturnRocket", "E-commerce", "Returns management",
     "Branded returns portal, exchanges, and restocking automation with reverse logistics.",
     "Branded portal", "Exchange-first flow", "Reverse logistics", "DTC ops"),
    ("BundleBuilder", "E-commerce", "Product bundling",
     "Drag-drop bundle builder with discount rules and inventory-aware upsells.",
     "Bundle builder", "Discount rules", "Inventory-aware", "DTC marketer"),
    ("LoyaltyLoop", "E-commerce", "Customer loyalty program",
     "Points, tiers, referrals, and VIP perks — LoyaltyLoop replaces Smile/LoyaltyLion for less.",
     "Points + tiers", "Referrals", "VIP perks", "DTC founder"),
    ("AffiliateArc", "E-commerce", "Affiliate program manager",
     "Recruit affiliates, track referrals with coupons/links/UTMs, and pay commissions automatically.",
     "Affiliate recruitment", "Coupon/UTM tracking", "Auto payouts", "DTC growth"),

    ("APIGateway", "Developer Tools", "API management platform",
     "API keys, rate limits, OAuth, docs, and analytics — all in one. Drop-in for any backend.",
     "API key + OAuth", "Rate limiting", "Auto-generated docs", "Platform engineer"),
    ("LogLens", "Developer Tools", "Log aggregation and search",
     "Ingest logs from any source, full-text + structured search, alerting, and dashboards.",
     "Multi-source ingest", "Structured search", "Alert rules", "SRE"),
    ("StatusPage", "Developer Tools", "Incident status communication",
     "Public + private status pages, incident timelines, and customer notifications.",
     "Public/private pages", "Incident timelines", "Subscriber notifications", "SRE"),
    ("WebhookFlow", "Developer Tools", "Webhook orchestration",
     "Receive, filter, transform, retry, and replay webhooks. WebhookFlow tames vendor chaos.",
     "Webhook receiver", "Filter + transform", "Retry + replay", "Integration engineer"),
    ("FeatureFlag", "Developer Tools", "Feature flag service",
     "Boolean and multivariate flags with percentage rollouts, kill switches, and audit logs.",
     "Boolean + multivariate", "Percentage rollouts", "Audit log", "Product engineer"),
    ("CodeMentor", "Developer Tools", "AI code review",
     "PR-level review with security, performance, and style checks tuned to your repo.",
     "PR review", "Security checks", "Style tuning", "Senior engineer"),
    ("DocuBot", "Developer Tools", "API doc generator",
     "Generate beautiful API docs from OpenAPI, gRPC reflection, or source code.",
     "OpenAPI import", "gRPC reflection", "Source-code scan", "DX lead"),
    ("SDKForge", "Developer Tools", "SDK generator from OpenAPI",
     "Generate idiomatic TypeScript, Python, Go, and Java SDKs from your OpenAPI spec.",
     "Multi-language output", "Idiomatic code", "CI integration", "Platform team"),
    ("SandboxCloud", "Developer Tools", "Ephemeral dev environments",
     "Spin up per-PR environments in seconds with seeded DBs and PR-specific URLs.",
     "Per-PR envs", "Seeded DBs", "PR URLs", "Frontend lead"),
    ("BuildPipe", "Developer Tools", "CI/CD pipeline manager",
     "Pipelines-as-code with matrix builds, secrets, and deploy targets.",
     "Pipelines-as-code", "Matrix builds", "Deploy targets", "DevOps lead"),

    ("DashDeck", "Analytics", "Custom dashboard builder",
     "Drag-drop dashboards with 50+ data sources and embeddable sharing.",
     "Drag-drop dashboards", "50+ sources", "Embeddable share", "BI analyst"),
    ("EventFlow", "Analytics", "Product analytics",
     "Event tracking, funnels, retention, and feature adoption — without the Amplitude price tag.",
     "Event tracking", "Funnels + retention", "Feature adoption", "Product analyst"),
    ("CohortCompass", "Analytics", "Cohort analysis",
     "Slice users by signup week, plan, or behavior. CohortCompass makes retention answers obvious.",
     "Cohort retention", "Behavior slicing", "Plan cohorts", "Growth analyst"),
    ("FunnelFox", "Analytics", "Conversion funnel analysis",
     "Multi-step funnels with drop-off reasons, segmentation, and recommendations.",
     "Multi-step funnels", "Drop-off reasons", "Segmentation", "Conversion analyst"),
    ("MetricMix", "Analytics", "Custom metric tracking",
     "Define business metrics in plain English; MetricMix builds the SQL, charts, and alerts.",
     "Plain-English metrics", "Auto SQL", "Alerts", "Founder / ops"),

    ("InboxIQ", "Communication", "Unified inbox",
     "One inbox for email, Slack, SMS, and WhatsApp. InboxIQ prioritizes what matters.",
     "Multi-channel inbox", "AI prioritization", "Snooze rules", "Executive"),
    ("ChatCraft", "Communication", "Team chat with AI summaries",
     "Threaded chat with daily AI digests so you can actually unplug.",
     "Threaded channels", "AI daily digests", "Async-friendly", "Remote team"),
    ("VoiceVault", "Communication", "Voicemail transcription",
     "Transcribe voicemails, route them to the right person, and reply by text.",
     "Voicemail transcription", "Smart routing", "Text reply", "Sales rep"),
    ("NotiNest", "Communication", "Notification routing",
     "Route alerts from monitoring tools to the right person via Slack/SMS/PagerDuty.",
     "Alert routing", "On-call schedules", "Escalation policies", "SRE"),
    ("Threadly", "Communication", "Async team messaging",
     "Replace Slack with truly async threads. Threadly kills real-time pressure.",
     "Async threads", "Status updates", "Do-not-disturb mode", "Distributed team"),
]

assert len(APPS) == 100, f"Expected 100 apps, got {len(APPS)}"


def readme(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    return f"""# {name}

> {tagline}

**Category:** {cat}
**Primary persona:** {persona}
**Generated:** {NOW}

## Overview

{desc}

## Core Features

- **{f1}** — flagship capability.
- **{f2}** — differentiator.
- **{f3}** — retention driver.

## Suggested Tech Stack

- **Frontend:** Next.js 14 (App Router), TypeScript, Tailwind, shadcn/ui
- **Backend:** Node.js + Fastify or Python + FastAPI
- **Database:** PostgreSQL + Redis
- **Auth:** Clerk / Auth0 (SAML/SSO on higher tiers)
- **Storage:** S3-compatible
- **Queue:** BullMQ / Sidekiq
- **Realtime:** Pusher / Socket.io / Liveblocks
- **AI:** OpenAI / Anthropic / open-source LLMs via LiteLLM
- **Billing:** Stripe + Stripe Tax
- **Observability:** OpenTelemetry + Grafana / Highlight.io

## Pricing Sketch

| Tier | Price | Limits |
|------|-------|--------|
| Free | $0 | 1 user, capped usage |
| Starter | $19/mo | 3 users, full features |
| Pro | $49/mo | 10 users, integrations |
| Team | $99/mo | 25 users, SSO |
| Enterprise | Custom | Unlimited, SLA |

## Folder Map

- `README.md` — this file
- `SPEC.md` — product specification
- `ARCHITECTURE.md` — system design
- `API.md` — API surface
- `DB_SCHEMA.md` — data model

---

*Auto-generated SaaS concept. See sibling files for full detail.*
"""


def spec(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    return f"""# {name} — Product Specification

## 1. Vision

**{name}** is a {cat.lower()} SaaS that **{tagline.lower()}**.

> {desc}

## 2. Target Customer

- **Primary persona:** {persona}
- **Segment:** SMB to mid-market
- **Geography:** US, EU, APAC
- **Wedge:** {f1}

## 3. Jobs To Be Done

1. When {persona.lower()}s face a chaotic workflow, they want a single tool, so {name} consolidates it.
2. When teams collaborate across timezones, they want async-friendly UX, so {name} ships async-first.
3. When compliance matters, they want SOC 2 / GDPR-ready, so {name} is built compliance-first.

## 4. Core Features

### 4.1 {f1}
- **Spec:** Production-grade implementation with audit logs and analytics events.
- **Edge cases:** empty state, rate-limit, conflict resolution.
- **KPIs:** activation rate, weekly active usage.

### 4.2 {f2}
- **Spec:** Multi-tenant safe; per-org settings.
- **Edge cases:** timezone drift, locale formatting.
- **KPIs:** retention, expansion.

### 4.3 {f3}
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

- **Q1:** MVP with {f1}
- **Q2:** Add {f2} + public API
- **Q3:** Mobile PWA + integrations marketplace
- **Q4:** Enterprise tier + SOC 2 Type II

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Competitive market | Niche wedge: {f1} |
| Compliance burden | SOC 2 from day 1 |
| AI cost creep | Caching + model routing |
| Churn | Quarterly business reviews |
"""


def architecture(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    return f"""# {name} — System Architecture

## High-Level Diagram

```
            ┌──────────────────────────┐
            │   Web (Next.js)          │
            │   Mobile (PWA / RN)      │
            └────────────┬─────────────┘
                         │ HTTPS / WSS
                         ▼
            ┌──────────────────────────┐
            │   API Gateway (Fastify)  │
            │   Auth, Rate Limit       │
            └────┬─────────┬───────────┘
                 │         │
       ┌─────────▼─┐   ┌───▼─────────────�
       │ Core API   │   │ Async Workers   │
       │ (REST/GQL) │   │ (BullMQ)        │
       └────┬───────┘   └───┬─────────────┘
            │                │
   ┌────────▼────────┐  ┌────▼────────────┐
   │ PostgreSQL      │  │ Redis cache     │
   │ (primary)       │  │ + queue         │
   └─────────────────┘  └─────────────────┘

  Analytics: ClickHouse / BigQuery (ETL via Kafka)
  AI:        LiteLLM gateway → OpenAI / Anthropic / OSS
  Storage:   S3 (uploads, exports)
  Search:    Meilisearch
  Realtime:  Pusher / Socket.io
  Billing:   Stripe
```

## Components

### API Gateway
- Fastify + TypeScript
- JWT + API key auth
- Rate limiting (token bucket per org)
- Request signing for webhooks
- OpenAPI → typed SDK generation

### Core Services
- Tenants (orgs), users, RBAC
- {f1} service
- {f2} service
- {f3} service (AI-backed)
- Billing service (Stripe webhooks)
- Audit log service

### Data Layer
- PostgreSQL (primary OLTP) with row-level security
- Redis (cache, rate limit, ephemeral state)
- Meilisearch (full-text + faceted)
- ClickHouse (analytics warehouse)
- S3 (uploads, exports)

### Async Workers
- BullMQ on Redis for background jobs
- Workers: email, exports, AI batch, webhooks fan-out
- Dead-letter queue + retries

### Frontend
- Next.js 14 (App Router) + RSC
- Tailwind + shadcn/ui
- tRPC or REST
- React Query for client cache
- PWA for mobile

### AI Layer
- LiteLLM gateway (OpenAI, Anthropic, OSS)
- Vector DB (pgvector) for RAG
- Caching layer (semantic cache)
- Human-in-loop UI for sensitive tasks

## Cross-Cutting Concerns

- **Observability:** OpenTelemetry traces, Grafana dashboards, Highlight.io session replay.
- **Secrets:** Vault or AWS Secrets Manager.
- **Feature flags:** internal FeatureFlag service (or LaunchDarkly).
- **CI/CD:** GitHub Actions → Buildkite → Fly.io / Railway.
- **Compliance:** SOC 2 controls baked into code review checklist.

## Scaling Plan

| Stage | Bottleneck | Action |
|-------|------------|--------|
| 0–1K users | None | Single-region, small DB |
| 1K–50K | DB read load | Add read replica + Redis |
| 50K–500K | Queue lag | Shard workers, Kafka |
| 500K+ | Multi-region | Active-active, edge API |

## Cost Notes

- DB + cache dominate at low scale
- AI inference dominates at high scale → cache aggressively
- Observability stays under 10% of infra via sampling
"""


def api_doc(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    return f"""# {name} — API Surface

All endpoints under `/api/v1`. Auth via Bearer token (PAT) or session cookie.

## Auth

- `POST /auth/signup` — create account
- `POST /auth/login` — magic link
- `POST /auth/refresh` — refresh access token
- `POST /auth/logout` — invalidate session

## Organizations

- `POST /orgs` — create org
- `GET /orgs/:id` — fetch org
- `PATCH /orgs/:id` — update org
- `POST /orgs/:id/members` — invite user

## Core Resources

### {f1}
- `GET /resources` — list (paginated, filterable)
- `POST /resources` — create
- `GET /resources/:id` — fetch
- `PATCH /resources/:id` — update
- `DELETE /resources/:id` — soft delete

### {f2}
- `GET /secondary` — list
- `POST /secondary` — trigger

### {f3}
- `POST /ai/tasks` — submit AI task
- `GET /ai/tasks/:id` — poll result
- `POST /ai/tasks/:id/approve` — human-in-loop approval

## Webhooks

- `POST /webhooks` — register endpoint
- `GET /webhooks/:id/deliveries` — list deliveries
- `POST /webhooks/:id/replay` — replay failed delivery

## Errors

Standard error envelope:

```json
{{
  "error": {{
    "code": "rate_limited",
    "message": "Too many requests",
    "request_id": "req_..."
  }}
}}
```

Common codes: `unauthorized`, `forbidden`, `not_found`, `validation_error`, `rate_limited`, `conflict`, `internal`.

## Rate Limits

| Tier | RPS | Burst |
|------|-----|-------|
| Free | 5 | 10 |
| Starter | 20 | 40 |
| Pro | 100 | 200 |
| Team | 500 | 1000 |
| Enterprise | Custom | Custom |

## SDKs

- TypeScript (`@{name.lower()}/sdk`)
- Python (`{name.lower()}-sdk`)
- Go (`go.{name.lower()}.dev`)

## OpenAPI

Spec auto-generated from server; available at `/api/v1/openapi.json`.
"""


def db_schema(app):
    name, cat, tagline, desc, f1, f2, f3, persona = app
    return f"""# {name} — Database Schema

PostgreSQL 16. All tables include `id uuid pk`, `created_at`, `updated_at`, `deleted_at`.

## Identity

### `users`
- `email text unique`
- `name text`
- `avatar_url text`
- `email_verified_at timestamptz`

### `orgs`
- `name text`
- `slug text unique`
- `plan text` — free|starter|pro|team|enterprise
- `stripe_customer_id text`

### `org_members`
- `org_id fk orgs`
- `user_id fk users`
- `role text` — owner|admin|member|viewer
- unique `(org_id, user_id)`

## Domain — {f1}

### `{f1.lower().replace(' ', '_')[:20]}s`
- `org_id fk orgs`
- `name text`
- `status text`
- `payload jsonb`
- `created_by fk users`

### `{f1.lower().replace(' ', '_')[:20]}_events`
- `parent_id fk`
- `actor_id fk users`
- `event jsonb`
- `occurred_at timestamptz`

## Domain — {f2}

### `{f2.lower().replace(' ', '_')[:20]}_configs`
- `org_id fk orgs`
- `config jsonb`

## Domain — {f3} (AI)

### `ai_tasks`
- `org_id fk orgs`
- `kind text`
- `input jsonb`
- `output jsonb`
- `status text` — queued|running|done|failed
- `cost_cents int`
- `model text`
- `approved_by fk users`

### `ai_task_reviews`
- `task_id fk ai_tasks`
- `reviewer_id fk users`
- `decision text` — approve|reject|edit
- `notes text`

## Billing

### `subscriptions`
- `org_id fk orgs unique`
- `stripe_subscription_id text`
- `status text`
- `current_period_end timestamptz`

### `invoices`
- `org_id fk orgs`
- `stripe_invoice_id text`
- `amount_cents int`
- `status text`

## Observability

### `audit_logs`
- `org_id fk orgs`
- `actor_id fk users`
- `action text`
- `target_type text`
- `target_id text`
- `metadata jsonb`
- `ip inet`
- `user_agent text`

### `webhook_deliveries`
- `webhook_id fk webhooks`
- `event text`
- `payload jsonb`
- `response_status int`
- `attempt_count int`
- `delivered_at timestamptz`

## Indexes

- `(org_id, created_at desc)` on heavy tables
- GIN index on `payload jsonb`
- Partial index on `deleted_at is null`

## RLS

All org-scoped tables enforce `org_id = current_setting('app.org_id')`.
"""


def main():
    created = []
    for app in APPS:
        name = app[0]
        slug = name.lower()
        path = os.path.join(BASE, slug)
        os.makedirs(path, exist_ok=True)
        files = {
            "README.md": readme(app),
            "SPEC.md": spec(app),
            "ARCHITECTURE.md": architecture(app),
            "API.md": api_doc(app),
            "DB_SCHEMA.md": db_schema(app),
        }
        for fname, content in files.items():
            with open(os.path.join(path, fname), "w", encoding="utf-8") as fh:
                fh.write(content)
        created.append(slug)

    # Top-level INDEX
    by_cat = {}
    for app in APPS:
        by_cat.setdefault(app[1], []).append(app)

    with open(os.path.join(BASE, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# SaaS Fleet — 100 App Concepts\n\nGenerated {NOW}.\n\n")
        for cat in sorted(by_cat):
            fh.write(f"\n## {cat} ({len(by_cat[cat])})\n\n")
            for app in by_cat[cat]:
                fh.write(f"- **{app[0]}** — {app[2]}\n")

    print(f"Created {len(created)} apps under {BASE}")


if __name__ == "__main__":
    main()
