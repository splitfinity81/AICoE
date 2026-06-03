# ACC-4 — Regulated-Industry Pilot Kit (POPIA / PFMA / NERSA)

**Owner:** RSA CoE · **Maturity:** v1.0 · **Last updated:** 2026-06-03

## One-line
A reusable workshop + control library + risk register for any South African regulated entity running its first generative-AI pilot. Eskom-tested, generalised for banking (SARB/FSCA), insurance (PA/FSCA), telco (ICASA), public sector (PFMA/MFMA), and mining (DMRE).

## Customer problem
First-pilot customers stall in the controls conversation. CISO, DPO, Internal Audit, and Legal each want assurance, but no one has aggregated their concerns into a single artefact. The pilot delays 2–4 months.

## What's in the kit
1. **4-week pre-pilot workshop** (eight 2-hour sessions across CISO, DPO, Legal, IA, business sponsor, IT lead, data owner, project lead)
2. **Control library** — 42 controls covering data, model, prompt, output, audit, third-party, and incident
3. **Risk register template** (Excel) — pre-populated with the 18 most-common GenAI risks plus mitigations
4. **POPIA AI-specific impact assessment** — DPIA template tuned for GenAI use-cases
5. **Pilot gate document** — single-page go/no-go binding the eight personas above
6. **Communication template** — board / Exco / regulator briefing decks

## Workshop agenda (4 weeks, 8 sessions)
| # | Topic | Persona | Output |
|---|---|---|---|
| 1 | Use-case scoping + value hypothesis | Business sponsor | Pilot success criteria |
| 2 | Data scope + classification | DPO + Data owner | POPIA DPIA draft |
| 3 | Model + prompt + output controls | CISO + IT lead | Control selection from library |
| 4 | Sector-specific regulatory mapping | Legal | Regulator-correspondence pack |
| 5 | Audit + monitoring plan | Internal Audit | Evidence collection design |
| 6 | Third-party + partner controls | Project lead | Partner DPA addendum |
| 7 | Incident response + kill-switch | CISO | Run-book |
| 8 | Pilot gate review | All | Signed gate document |

## Control library (excerpt)
*Full library in `controls-library.xlsx` — to be added*
- **C-DATA-01:** Source data classified before ingestion (POPIA §22)
- **C-DATA-04:** Cross-border transfer prohibited unless on §72 list
- **C-MODEL-02:** Model selection from Foundry catalog only (no shadow models)
- **C-PROMPT-03:** System prompt versioned and reviewed quarterly
- **C-OUTPUT-05:** All financial / clinical / legal outputs HITL-gated
- **C-AUDIT-01:** Purview AI Hub onboarded before pilot launch
- **C-INCIDENT-02:** Kill-switch tested in pilot; SLA documented

## Regulator mapping (sector lookup)
| Sector | Primary regulators | Sector-specific addendum |
|---|---|---|
| Banking | SARB, FSCA, PA | FAIS conduct + Reg 39 IT risk |
| Insurance | PA, FSCA | SAM (Solvency Assessment & Management) |
| Telco | ICASA | RICA call-record handling |
| Public sector / SOE | AGSA, National Treasury | PFMA s.45 + MFMA s.62 |
| Mining | DMRE | MHSA digital records |
| Healthcare | HPCSA, NDOH | NHA + (pending) NHI Act provisions |

## Funding stack
| Phase | Vehicle | Envelope |
|---|---|---|
| Workshop (4 wk) | Pre-sales ECIF | $50K |
| Pilot (8 wk) | Cloud Accelerate Factory F6 (Governance) | $0 |
| Scale | Customer + ATO | Customer |

## Time-box
- 4 weeks workshop → 8 weeks pilot → gate decision → scale

## Partner role
Optional. Microsoft-led for first-pilot customers; partner-led for repeat customers where partner is the prime SI.

## Anti-patterns
- Don't compress the workshop below 4 weeks — controls conversations need calendar time across legal/audit
- Don't ship the pilot without the signed gate document; audit will surface this within a quarter
- Don't reuse the control library wholesale — sector mapping matters

## Linked artefacts
- ACC-2 (Landing Zone) — platform foundation
- AI Governance Playbook (`AI-CoE-AI-Governance-Playbook.docx`)
- AI Impact Assessment (`AI-CoE-AI-Impact-Assessment.xlsx`)
- AI-CoE-Sovereign-AI-RSA.pptx
