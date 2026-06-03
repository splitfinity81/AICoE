# AI CoE Academy (RSA) — Curriculum Blueprint

**Owner:** RSA CoE · **Audience:** customer learner cohorts (25–100 per wave) · **Maturity:** v1.0 · **Last updated:** 2026-06-03
**Companion artefact:** `AI-CoE-Academy-Curriculum.xlsx` (role × tier × MS Learn path × cert matrix)

---

## 1. Why this exists

The single biggest constraint on AI value-realisation in RSA customers is not licensing, not platform, not data — it is named people with named skills. CSU and partners run ad-hoc Skill Navigator engagements; customers exit with PDF skilling plans that no one operationalises. The Academy converts that plan into a 12-week cohort with named tracks, sector labs, and certification gates.

Competitive context: Accenture LearnVantage, Deloitte AI Academy, BCG University AI Track, Capgemini Cloud School all sell named programmes. Microsoft fielding only "we have Microsoft Learn" loses the talent conversation.

## 2. The five role tracks

Every customer wave runs the same five tracks. The mix of seats per track varies by customer profile.

### Track 1 — Executive Sponsor (5–10 seats per cohort)
**Persona:** C-suite, EGM/GM, Board members.
**Outcome:** can defend the AI investment in front of CFO, AGSA, Board.
**Format:** 4 × half-day sessions over 12 weeks (not weekly — they won't show up).
**Anchor Microsoft Learn path:** AI for Business Leaders (curated subset).
**Sector labs:** PFMA business-case construction; AGSA evidence-pack walkthrough; sector-specific regulator briefing simulation.
**Certification gate:** None (executives don't sit certs); replaced by a 30-minute peer-review of their own customer's pilot business case.
**Pass criteria:** Executive can answer the four sponsor objections from `AI-CoE-Objection-Handling.pptx` Pillar 1 without coaching.

### Track 2 — AI Product Owner (10–15 seats per cohort)
**Persona:** BU heads, product managers, transformation leads.
**Outcome:** can scope, prioritise, and run an AI use-case from envision through pilot gate.
**Format:** 1 day/week for 12 weeks (12 days total).
**Anchor Microsoft Learn paths:** Microsoft Copilot Foundations + AI-900 + Foundry Product Owner path (curated).
**Sector labs:** use-case scoping with the Horizon Assessment template; pilot-gate dry-run using ACC-4 Regulated-Industry Pilot Kit; KPI tree construction (time-to-decision and FTE-recovery, not "accuracy").
**Certification gate:** AI-900 (Azure AI Fundamentals).
**Pass criteria:** ship a scoped, signed-off use-case brief into the customer's pilot intake by week 10.

### Track 3 — AI Engineer (15–30 seats per cohort)
**Persona:** Senior developers, ML engineers, platform engineers.
**Outcome:** can build a production agent on Foundry / Copilot Studio with eval harness + observability + governance hooks.
**Format:** 2 days/week for 12 weeks (24 days, instructor-led + lab).
**Anchor Microsoft Learn paths:** AI-102 (Azure AI Engineer Associate) + Foundry Agent Service deep dive + GenAIOps with PromptFlow.
**Sector labs:** build the ACC-1 Banking CX Agent reference implementation; integrate Purview AI Hub; deploy via Bicep against ACC-2 Landing Zone; eval against PromptFlow harness with reviewer-override feedback loop.
**Certification gate:** AI-102.
**Pass criteria:** committed agent passing eval threshold + Purview onboarded + Defender for Cloud AI clean.

### Track 4 — Data Engineer (10–20 seats per cohort)
**Persona:** Data engineers, analytics engineers, BI leads.
**Outcome:** can land regulated data into Fabric / OneLake with lineage, classification, and policy hooks ready for AI grounding.
**Format:** 2 days/week for 12 weeks.
**Anchor Microsoft Learn paths:** DP-700 (Fabric Analytics Engineer) + Fabric for AI grounding + Purview Data Map.
**Sector labs:** POPIA-classified ingestion into OneLake; Purview lineage end-to-end; ground a Foundry agent against Fabric semantic model with row-level security.
**Certification gate:** DP-700.
**Pass criteria:** end-to-end pipeline live with sensitivity labels + Purview lineage + RLS-bound agent grounding.

### Track 5 — Copilot Champion (25–50 seats per cohort)
**Persona:** Business power-users across HR, Finance, Ops, Legal — the people who will evangelise inside the BU.
**Outcome:** can build role-specific prompt libraries, run office hours, and produce monthly value-capture evidence.
**Format:** 2 hours/week for 12 weeks (24 hours total).
**Anchor Microsoft Learn paths:** Copilot Champion path + Copilot Studio Maker path (lightweight agents).
**Sector labs:** role-based prompt library construction; FTE-hour recovery survey design; agent build for one BU pain point in Copilot Studio.
**Certification gate:** Microsoft 365 Copilot Specialist (Applied Skill).
**Pass criteria:** published prompt library + at least one shipped Copilot Studio agent + first month value-capture survey returned.

## 3. Cohort blueprint (per wave)

A standard wave runs 12 weeks with five concurrent tracks. Cohort mix recommended for first wave at a regulated SOE / bank / insurer:

| Track | First-wave seats | Steady-state seats (waves 2+) |
|---|---|---|
| Executive Sponsor | 6 | 6 |
| AI Product Owner | 12 | 15 |
| AI Engineer | 20 | 30 |
| Data Engineer | 12 | 18 |
| Copilot Champion | 30 | 50 |
| **Total per wave** | **80** | **119** |

Customers typically run 2–4 waves per fiscal year. A two-wave year covers ~160 named-and-skilled people.

## 4. Delivery rhythm (the 12 weeks)

| Week | Activity | All tracks | Notes |
|---|---|---|---|
| -2 | Baseline assessment + track placement | yes | Skill-Navigator-style placement test routes learners to track |
| 1 | Kickoff + sponsor address + cohort norms | yes | Executive Sponsor track opens the wave |
| 2–4 | Foundation modules (per track) | per track | Microsoft Learn paths anchor the self-paced load |
| 5 | Mid-wave checkpoint + sector lab #1 | per track | First sector-specific lab, anchored on customer's vertical |
| 6–8 | Build / specialise | per track | Engineers building, PMs scoping, Champions running first office hours |
| 9 | Sector lab #2 + mock cert (Engineer/Data tracks) | per track | Run AI-102/DP-700 mock under exam conditions |
| 10 | Pilot-gate dry-run (Product Owner track lead) | yes | Other tracks attend as panellists |
| 11 | Certification sittings | per track | AI-900/AI-102/DP-700/Applied Skill |
| 12 | Showcase + value-capture report + next-wave nomination | yes | Customer Exco attends; sets up wave 2 |

## 5. Funding stack

| Phase | Vehicle | Envelope | Notes |
|---|---|---|---|
| Wave 1 (pilot) | ECIF + MAICPP partner-co-funded | $100–200K | Microsoft anchors curriculum; partner delivers instructor labour |
| Wave 2+ | MAICPP partner-funded + customer | $80–150K/wave | Partner runs the engine; customer co-pays via training budget |
| Certification vouchers | Microsoft Learn cloud vouchers | $0–$50/learner | Bundled where available |
| Sector lab content | RSA CoE IP | $0 to customer | Microsoft contribution; reused across customers |

## 6. KPIs (per wave)

| KPI | Target | Source |
|---|---|---|
| Cohort completion rate | ≥ 80% | LMS attendance |
| Certification pass rate (gated tracks) | ≥ 75% on first attempt | Pearson VUE / Credly |
| Sponsor track pass criteria met | 100% | Peer review |
| Use-cases shipped into pilot intake (Product Owner track) | ≥ 1 per learner | Customer intake log |
| Engineer track agents committed to repo | ≥ 1 per learner | GitHub / DevOps |
| Champion track prompt libraries published | ≥ 1 per learner | Customer SharePoint |
| Net Promoter Score | ≥ +30 | End-of-wave survey |

## 7. Partner role

Skilling partners (RSA examples: BCX, Dimension Data, EOH, Synthesis Software, Bytes, Wipro, TCS local practice) run instructor labour and LMS. Microsoft retains curriculum authority, sector lab content, and the certification-gate calibration. Partner contracts under MAICPP with named co-funding from Microsoft.

## 8. Sector cuts

Five sector overlays, each adding ~15% additional content to the base curriculum:

| Sector | Additional content | Sector cert overlay |
|---|---|---|
| Banking | SARB Directive 7 module, FICA Schedule 1, FAIS conduct | none |
| Insurance | PA SAM module, FSCA Conduct Standards | none |
| Public sector / SOE | PFMA s.45 + MFMA s.62 cost-justification, AGSA evidence | none |
| Telco | RICA call-record handling, ICASA frameworks | none |
| Healthcare | HPCSA, NDOH, medical scheme rules | none |

## 9. Anti-patterns

- Don't bundle all five tracks into a single classroom. Tracks have different cadences and personas; mixing them halves engagement.
- Don't skip the placement assessment. Engineers in Champion track will disengage by week 3; Champions in Engineer track will drop out.
- Don't run waves longer than 12 weeks. Beyond that, business-as-usual reasserts and completion collapses.
- Don't accept "we'll send our people to Microsoft Learn" as a substitute. Self-paced without cohort scaffolding lands at ~15% completion in RSA enterprise contexts.

## 10. Linked artefacts

- VBD D2 (this offer's catalogue row)
- `AI-CoE-Academy-Curriculum.xlsx` (role × tier × MS Learn path × cert matrix)
- ACC-3 (M365 Copilot SOE Adoption Playbook) — Champion track integration
- ACC-1, ACC-2 (Engineer track sector labs build against these)
- AI-CoE-Operating-Playbook.docx (overall delivery rhythm)

## 11. Sources

- Microsoft Learn AI Skill Navigator (`aka.ms/AISkillsNavigator`)
- Microsoft Learn role-based paths (AI-900, AI-102, DP-700, Copilot Specialist)
- MAICPP partner-funding documentation
- RSA CoE field experience (FY26 H1–H2 customer waves)
