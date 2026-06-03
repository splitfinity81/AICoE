# ACC-3 — M365 Copilot Adoption Playbook for SOEs

**Owner:** RSA CoE · **Maturity:** v1.0 · **Last updated:** 2026-06-03

## One-line
A 12-week M365 Copilot adoption motion tuned for South African State-Owned Enterprises — sponsor coalition, PFMA cost-justification template, AGSA-ready audit trail, change-management at SOE scale.

## Customer problem
SOEs buy seats and watch them sit idle. Drivers: weak executive sponsorship, no PFMA-defensible business case, change-fatigue from concurrent ERP/HR transformations, and a workforce trained on Office 2016 muscle memory.

## What's different about SOEs (vs. private sector)
- **Procurement:** PFMA s.45 requires demonstrable value-for-money; "productivity uplift" alone won't pass AGSA scrutiny — needs FTE-recovery or cycle-time evidence
- **Workforce composition:** Wider span (graduate to executive), more union engagement required, often dual-shift environments
- **Audit posture:** AGSA may sample Copilot interactions during annual audit — instrument from day 1
- **Sponsor model:** CEO + CFO + COO triad, not just CIO; HR Exco involvement non-negotiable

## 12-week wave structure (cohorts of 250–500 seats)

| Week | Activity | Owner |
|---|---|---|
| -2 to 0 | Sponsor coalition formed, baseline survey, KPI tree signed off | CoE + customer Exco |
| 1 | Cohort 1 launch, role-based prompt libraries, champions identified | Change partner |
| 2–4 | Weekly office hours, micro-learning drip (5-min videos), use-case bounty | Champions |
| 5 | Mid-wave pulse + intervention on stalled personas | CoE |
| 6–10 | Use-case bank expansion (HR, Finance, Ops verticals), agent piloting (Copilot Studio) | Champions + IT |
| 11 | Value capture: FTE-hour recovery survey, time-and-motion sample, sentiment | CoE + customer |
| 12 | AGSA-ready value evidence pack, next-wave hand-off | CoE |

## PFMA cost-justification template
Spreadsheet output: `(Baseline FTE hours/task × tasks/month) – (Post-Copilot FTE hours/task × tasks/month) × Loaded cost/hour = Recovered value/month`. Plus a 12-month payback waterfall.

## AGSA audit trail (built in)
- M365 Copilot interaction logs preserved 7 years in Purview eDiscovery
- Audit Tenant Admin actions in Defender XDR
- Quarterly AGSA-ready export pack scripted from `audit-export.ps1` *(to be added)*

## KPIs
- Active use ≥ 75% by week 8 (was 35% in 2024 SOE baseline)
- Average sessions/user/week ≥ 4
- Self-reported time-saved ≥ 3 hrs/user/week
- Cohort NPS ≥ +20

## Funding stack
| Phase | Vehicle | Envelope |
|---|---|---|
| Pre-wave | Copilot Adoption Acceleration | $50K |
| Wave (12 wk) | ATO ACO + partner | $150–250K |
| Scale (multi-wave) | Customer-funded | Customer |

## Partner role
Change-management partner runs cohorts, owns champions network, delivers value-capture report. Microsoft retains strategic sponsor engagement and value-realisation gate.

## Anti-patterns
- Don't run more than 500 seats per cohort — engagement collapses
- Don't skip the PFMA business case; it kills the next wave
- Don't position Copilot as "another tool"; position it as a role-redesign lever

## Linked artefacts
- VBD A3 (Adoption & Change Management) — uses this as its SOE variant
- AI-CoE-Eskom-Executive-Briefing.pptx — reference customer narrative
- AI-CoE-Operating-Playbook.docx — overall delivery rhythm
