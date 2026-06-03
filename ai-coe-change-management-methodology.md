# AI CoE Change-Management Methodology

**Author:** Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft
**Version:** 1.0 · 2026-06-03
**Companion artefact:** `AI-CoE-Change-Readiness-Instrument.xlsx`
**Issue:** Closes #13 (deepen change-management methodology — replace one-bullet VBD A3)

---

## 1. Why this exists

VBD **A3** ("Change management for AI adoption") today is a one-bullet line item. Adoption-led failures are now the single largest cause of stalled Copilot and Foundry deployments in the RSA portfolio — not the technology, the change. Competitors (Accenture, Deloitte, EY) lead with named change frameworks; Microsoft's CoE pack must do the same.

This document is the named framework. It is an **ADKAR-based** methodology purpose-built for AI rollouts (M365 Copilot, Copilot Studio agents, Foundry agents), with a readiness assessment instrument, a Champions enablement kit, an adoption KPI scaffold, and a measurement cadence.

## 2. The framework — ADKAR for AI

Prosci's ADKAR (Awareness · Desire · Knowledge · Ability · Reinforcement) is selected because it is **person-centred** — AI adoption fails one user at a time, not in aggregate — and because it is the most widely adopted enterprise CM model in RSA already (banks, telcos, public sector).

| Stage | Question the user is asking | AI-specific intervention |
|---|---|---|
| **Awareness** | "Why are we doing this?" | Exec town hall + LOB-tailored "day in the life" videos; tie to a named business outcome (cost-out, revenue, risk reduction). |
| **Desire** | "What's in it for me?" | Persona-mapped value statements; remove fear ("you are not being replaced — you are being augmented"); WIIFM aligned to performance review. |
| **Knowledge** | "How do I use it?" | Role-based learning paths from `AI-CoE-Academy-Curriculum.xlsx`; prompt patterns library; sandbox tenant. |
| **Ability** | "Can I actually do this in my job?" | Hands-on labs on real (sanitised) work; Champions one-on-one coaching; in-flow nudges. |
| **Reinforcement** | "Will this stick?" | KPIs in scorecards; recognition for Champions; success-story drumbeat; manager accountability for team usage. |

The fifth stage — **Reinforcement** — is the one most often skipped, and the one most predictive of sustained adoption past month 6.

## 3. Readiness assessment

Before any Copilot or Foundry rollout above 50 seats, run the **Change Readiness Instrument** (`AI-CoE-Change-Readiness-Instrument.xlsx`). It scores readiness across five dimensions:

| Dimension | What it measures | Score range |
|---|---|---|
| **Sponsorship** | Visible C-suite ownership, named exec sponsor, public commitment | 1–5 |
| **Workforce** | Digital fluency baseline, prior change fatigue, openness to AI | 1–5 |
| **Use-case clarity** | Top 3 use-cases defined with named LOB owners and measurable outcome | 1–5 |
| **Enablement capacity** | Champions identified (1 per 25 users target), learning paths assigned, in-house trainer or partner contracted | 1–5 |
| **Measurement** | Adoption KPIs agreed, baseline measured, dashboard owner named | 1–5 |

**Total / 25 → readiness band:**
- **20–25** Green: proceed at full pace.
- **14–19** Amber: proceed with mitigations on the low-scoring dimensions; build a 30-day pre-launch plan.
- **<14** Red: do not launch broadly. Run a 90-day fixture programme to lift the weakest dimensions; pilot only on willing teams.

The workbook auto-computes the score and lights the band; outputs a one-page summary suitable for steering-committee distribution.

## 4. Champions enablement kit

The Champions network is the single highest-leverage CM intervention. Target **1 Champion per 25 users**; recruit from LOB, not IT.

| Element | What it is | Owner |
|---|---|---|
| Champion charter | One-page role description, time commitment (~10%), recognition path | CoE lead |
| Champion onboarding (½-day) | Role, expectations, support routes, KPIs they own | CoE enablement lead |
| Bi-weekly Champions community | 45-min call: tips, blockers, success stories, new feature drops | CoE enablement lead |
| Office-hours rota | Champions hold 1hr/week open office for their LOB | Champion |
| Prompt patterns library | Curated, vetted prompt examples per LOB | CoE + Champion contributions |
| Recognition mechanism | LinkedIn certificate badge, annual awards, exec call-out | Exec sponsor |
| Champion-to-Champion mentoring | New Champions paired with experienced for first 30 days | CoE enablement lead |

The Champions community is a **standing programme**, not a project — it persists indefinitely.

## 5. Adoption KPI scaffold

Five KPIs, in two layers. Activity KPIs are leading indicators; outcome KPIs are what the business actually pays for.

**Activity (leading):**
| KPI | Definition | Target by month 3 | Target by month 6 |
|---|---|---|---|
| **Active users** | Unique users invoking the agent / Copilot in last 28 days, ÷ licensed seats | ≥ 40% | ≥ 60% |
| **Depth** | Avg turns per session (Copilot) or avg invocations per active user per week | ≥ 5/week | ≥ 10/week |
| **Habit** | % of active users active ≥ 3 days/week | ≥ 25% | ≥ 40% |

**Outcome (lagging):**
| KPI | Definition | Target by month 6 |
|---|---|---|
| **Hours recovered** | Self-reported + observed time saved per active user per week, validated quarterly | ≥ 2 hrs/user/wk |
| **Business outcome metric** | One named, LOB-specific outcome (e.g., handle-time reduction, draft-to-final cycle time, deal-cycle compression) | Use-case specific |

KPIs are tracked in the **Adoption & Value** dashboard from `AI-CoE-GenAIOps-Reference.docx` §6.

## 6. Measurement cadence

| Cadence | Audience | Content |
|---|---|---|
| **Weekly** | CoE lead + Champions | Active users, depth, habit, support tickets, blocker themes |
| **Monthly** | Exec sponsor + LOB heads | All KPIs, success stories, Champion spotlights, asks of leadership |
| **Quarterly** | Steering committee + CISO | Outcome KPIs, ROI evidence, readiness re-score, programme adjustments |
| **Annually** | C-suite | Full programme review, next-year scope, investment reallocation |

## 7. Eight-week change plan (template)

| Week | Activity | Owner |
|---|---|---|
| -4 | Readiness assessment completed; gaps assigned | CoE lead |
| -3 | Sponsor video recorded; comms plan signed off | Comms + sponsor |
| -2 | Champions identified and onboarded; learning paths assigned | CoE enablement lead |
| -1 | Sandbox tenant live; pilot cohort selected | CoE + IT |
| 0 | Launch comms; exec town hall; sandbox open | Exec sponsor + comms |
| +1 | First office hours; first Champions call; baseline KPIs captured | Champions + CoE |
| +2 | First success story published; manager scorecard updated | Comms + HR |
| +4 | Month-1 review with sponsor; KPI checkpoint vs target | CoE lead |
| +8 | Month-2 review; expand cohort or remediate | Steering committee |

## 8. Linked artefacts

- `AI-CoE-Academy-Curriculum.xlsx` — role-based learning paths plug into Knowledge + Ability stages.
- `AI-CoE-Objection-Handling.pptx` — objections 2.1 ("our people aren't ready"), 2.2 (change fatigue), 2.3 (adoption will stall) all anchor here.
- `AI-CoE-Horizon-Assessment.xlsx` — workforce-readiness dimension feeds into Readiness Instrument scoring.
- `AI-CoE-GenAIOps-Reference.docx` §6 — Adoption & Value dashboard is the measurement surface for the KPIs above.
- `accelerators/acc-3-copilot-soe-adoption.md` — pre-built M365 Copilot adoption motion using this methodology.

## 9. What this document is NOT

- Not a replacement for a customer's own change-management function — this is the AI-specific overlay on top of it.
- Not certification training — Prosci ADKAR certification is a separate, paid path; this document re-uses the framework under fair-reference.
- Not a managed service — the CoE provides the methodology and instrument; customer or partner runs the change programme.
