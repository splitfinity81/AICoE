# ACC-5 — Document Intelligence + Foundry Pattern (Claims / Permits / KYC)

**Owner:** RSA CoE · **Maturity:** v1.0 · **Last updated:** 2026-06-03

## One-line
A reference pattern combining Azure AI Document Intelligence, Azure AI Foundry agents, and human-in-the-loop review for high-volume regulated document workflows. KPIs in time-to-decision and FTE-recovery terms — not "accuracy %".

## Customer problem
Document-heavy regulated processes (insurance claims, building permits, KYC onboarding, medical pre-authorisation) run on 2–10 day cycle times with backlogs, exception queues, and inconsistent decisions across reviewers. RPA / OCR projects from 2020–2024 plateaued at ~40% straight-through processing.

## Solution shape
- **Capture:** Document Intelligence custom + prebuilt models extract structured fields
- **Reason:** Foundry agent compares extracted fields against policy rules + historical decisions
- **Decide:** Confidence-tiered routing — high-confidence auto-decided, medium HITL, low full-manual
- **Audit:** Every decision carries full reasoning trace + source-doc citation
- **Learn:** Reviewer overrides feed back into eval set; monthly model refresh

## Where this beats RPA / classical OCR
- **Variable layout tolerance:** Foundry handles new layouts without retraining
- **Reasoning beyond extraction:** "Does this medical claim match the policy schedule?" — RPA can't, this can
- **Auditability:** LLM reasoning trace is more inspectable than a 200-step UiPath flow
- **Scalability:** Cost scales with tokens, not bots; doesn't break on Windows updates

## Reference KPIs (typical first 90 days)
| KPI | Baseline | Target | Stretch |
|---|---|---|---|
| Straight-through processing | 35–45% | 65% | 80% |
| Median cycle time | 4 days | 1 day | 4 hours |
| Reviewer FTE-hours/100 docs | 12 | 5 | 3 |
| Decision overturn rate (QA sample) | 8% | <5% | <3% |

## Architecture
- Document Intelligence (premium tier for low-confidence layouts)
- Foundry agent: GPT-4o-mini for extraction QA, GPT-4o for policy reasoning
- Storage: ADLS Gen2 with retention policy aligned to sector (POPIA + sector-specific)
- HITL UI: Power Pages with Dataverse queues, role-based routing
- Eval: PromptFlow eval harness, monthly refresh on reviewer overrides

## Sector cuts
| Sector | Document types | Special considerations |
|---|---|---|
| Insurance | Claim forms, medical reports, police reports | PA conduct standards, fraud signals |
| Banking | KYC docs, FICA Schedule 1 evidence | FICA, SARB Reg 50 |
| Public sector | Building permits, business licences, social grants | PFMA + sector legislation |
| Healthcare | Pre-authorisation, claims, referrals | HPCSA, medical scheme rules |

## Funding stack
| Phase | Vehicle | Envelope |
|---|---|---|
| Envision | Pre-sales ECIF | $50K |
| Pilot (10 wk, single doc type) | ATO ACO + ECIF | $300–600K |
| Scale (6 months, full backlog) | Partner MAICPP | Partner-funded |

## Partner role
Vertical SI (insurance / banking / healthcare specialist) leads build and HITL UI; Microsoft leads Foundry + Document Intelligence architecture and eval design.

## Anti-patterns
- Don't measure "model accuracy" — measure decision overturn rate on QA sample (it's what auditors care about)
- Don't auto-decide below the eval-validated confidence threshold; the bad-decision cost dominates the cost-savings
- Don't skip the HITL queue UI investment — reviewer experience determines override-feedback quality, which determines eval-set quality, which determines next quarter's STP rate

## Linked artefacts
- VBD B7 (Document Intelligence Workshop) for the envision phase
- ACC-1 (Banking CX Agent) for the channel-side counterpart
- ACC-2 (POPIA Landing Zone) as the platform foundation
