# Responsible AI & Governance — AI CoE (RSA)

**Author:** Yuri Baijnath, CSU Cloud & AI Lead (South Africa), Microsoft
**Audience:** RSA CoE pillar 5 leads, customer CISOs / DPOs / Internal Audit, partner governance leads
**Companion artefacts:** `AI-CoE-AI-Impact-Assessment.xlsx`, `AI-CoE-AI-Governance-Playbook.docx`
**Last updated:** 2026-06-03

---

## 1. Why this exists

Microsoft has a public Responsible AI Standard v2 and a strong internal RAI Impact Assessment template. What it has *not* had inside the RSA CoE pack is a single field-facing artefact that:

1. Maps Microsoft RAI v2 to the frameworks RSA regulated customers cite (POPIA, PFMA, ISO/IEC 42001, NIST AI RMF, EU AI Act).
2. Gives a CSA or partner CSA a per-use-case working tool — not a slide — that walks impact assessment, control selection, and evidence capture in one workbook.
3. Wraps both into an operating playbook that names roles, gates, and cadences so the governance posture survives staff churn.

Competitive context: Accenture sells a Responsible AI Compliance solution; Deloitte sells Trustworthy AI; BCG sells Responsible AI Leader. Microsoft fielding only the public RAI v2 PDF loses the governance buyer conversation. This artefact pack closes that.

## 2. What governance buyers want (RSA)

The four personas around the governance table:

- **CISO** — wants control catalogue, evidence of enforcement, incident response, and a clean Defender for Cloud AI posture.
- **DPO** — wants POPIA DPIA discharged, cross-border lawful basis, subject-access response capability, retention discipline.
- **Internal Audit** — wants evidence template, sample-able trail, AGSA-ready quarterly pack.
- **Legal** — wants regulator-correspondence pack, contractual flow-down to partners, IP/copyright posture.

The Impact Assessment workbook produces an artefact each persona signs against, in one document. That is the operating goal.

## 3. The control crosswalk (master)

Single matrix mapping Microsoft RAI v2 control families to the external frameworks. Excerpt below; full crosswalk in `AI-CoE-AI-Impact-Assessment.xlsx` sheet 2.

| Control family | RAI v2 | ISO/IEC 42001 | NIST AI RMF | EU AI Act | POPIA | PFMA |
|---|---|---|---|---|---|---|
| Accountability & governance | G1, G2 | A.5.1, A.5.2 | GOVERN-1 | Art. 9, 17 | §22 | s.38 |
| Data governance & residency | F1, T3 | A.6.2, A.8.24 | GOVERN-1.3, PROTECT | Art. 10, 15 | §19, §72 | s.45 |
| Impact assessment | T1 | A.6.4 | MAP-1, MAP-2 | Art. 9, 27 | §11, §22 | n/a |
| Risk identification | T2 | A.6.1.4 | MAP-3, MAP-5 | Art. 9 | §19 | n/a |
| System-prompt versioning | T2 | A.5.37 | GOVERN-1.5 | Art. 11 | §22 | n/a |
| Content Safety / Prompt Shields | S1 | A.5.34 | MANAGE-2.3 | Art. 15 | n/a | n/a |
| HITL gate on regulated outputs | A1 | A.6.4 | MANAGE-2.4 | Art. 14 | §11 | n/a |
| Kill-switch + tested run-book | S3 | A.5.30 | MANAGE-3 | Art. 9 | n/a | s.45 |
| Audit trail (Purview AI Hub) | G3 | A.5.10 | MEASURE-2.5 | Art. 12 | §17, §22 | s.38 |
| Defender for Cloud AI posture | S2 | A.8.16 | MANAGE-3 | Art. 9 | §19 | n/a |
| Reviewer override feedback loop | T4 | A.6.4 | MEASURE-3 | Art. 14 | n/a | n/a |
| Quarterly attestation | G2 | A.5.36 | GOVERN-1.6 | Art. 17 | §22 | s.38 |

## 4. Per-use-case workflow (Impact Assessment workbook)

The workbook is the working tool. One row per use-case. Eight tabs:

1. **Use-case register** — name, sponsor, business problem, expected value, MCEM stage, pilot/production status.
2. **Crosswalk** — the master matrix above.
3. **Impact assessment** — RAI v2 questions adapted: who is affected, severity, reversibility, scale, contestability, demographic fairness.
4. **Risk register** — 18 pre-populated GenAI risks (hallucination, prompt injection, data leakage, model drift, oversharing, etc.) with severity × likelihood × mitigation × residual.
5. **Control selection** — pick controls from the crosswalk; auto-discharges across frameworks.
6. **Evidence log** — what evidence will be collected, where stored, who reviews, what cadence.
7. **Sign-off** — CISO / DPO / IA / Legal / Business sponsor signature block + date.
8. **Quarterly attestation** — rolling log of what was attested and when, per use-case.

Output of the workbook is the artefact AGSA / SARB / FSCA / Information Regulator will sample.

## 5. Governance gates (the four)

Every AI use-case passes four gates before production:

- **Gate 1 — Envision** (MCEM 1–2): use-case registered, sponsor named, value hypothesis stated, sector mapped.
- **Gate 2 — Pre-pilot** (MCEM 2–3): impact assessment signed, controls selected, risk register reviewed, partner DPA addendum in place.
- **Gate 3 — Pre-production** (MCEM 3): eval harness in place, HITL queue live, kill-switch tested, Purview AI Hub onboarded.
- **Gate 4 — Quarterly attestation** (MCEM 4–5): re-verify all of the above; refresh evidence; surface drift.

The four-gate model is the spine of the Governance Playbook (`AI-CoE-AI-Governance-Playbook.docx`).

## 6. Operating model (RACI summary)

| Role | Gate 1 | Gate 2 | Gate 3 | Gate 4 |
|---|---|---|---|---|
| Business sponsor | A | C | C | I |
| Microsoft CSA | R | R | R | R |
| Partner CSA / build lead | I | R | R | R |
| Customer CISO | I | A | A | A |
| Customer DPO | I | A | I | A |
| Customer Internal Audit | I | C | C | A |
| Customer Legal | I | A | I | C |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

## 7. Engagement shape

| Phase | Vehicle | Envelope | Output |
|---|---|---|---|
| Envision workshop | Pre-sales ECIF | $50K | Crosswalk tailored; first 1–3 use-cases registered |
| Per-use-case impact assessment | Customer + Microsoft CSA | n/a | Signed assessment workbook |
| Pilot governance (8–12 wk) | ATO + partner | bundled | Evidence pack v1 |
| Quarterly attestation | Customer-owned, Microsoft-supported | n/a | Refreshed pack |

## 8. What this is NOT

- **Not** a substitute for the customer's own POPIA compliance programme. Microsoft provides tools; the customer is the responsible party.
- **Not** legal advice. Sector-specific regulator interactions still require the customer's own legal counsel.
- **Not** static. The crosswalk needs quarterly refresh as ISO 42001, EU AI Act secondary legislation, and POPIA enforcement evolve.

## 9. Counter-objections

1. **"Microsoft RAI is a marketing artefact."** → RAI v2 is the public surface of internal review boards that gate Microsoft's own product shipments. The crosswalk shows it discharges against ISO 42001 and NIST AI RMF too — independent third-party frameworks.
2. **"ISO 42001 isn't certifiable yet at our scale."** → Correct in most cases. The workbook tracks readiness even before formal certification, so when the customer's certification body shows up, the evidence already exists.
3. **"EU AI Act doesn't apply to us."** → True for purely-domestic SA workloads. Apply for multinational customers, any customer with EU citizen data flows, or any customer providing AI to EU markets. The crosswalk lets you scope-out cleanly where it doesn't apply.
4. **"This is a lot of paperwork."** → Less than the alternative. The workbook converts 4–8 weeks of bespoke control mapping per use-case into a 1–2 week structured exercise that produces a sign-off-ready artefact.

## 10. Linked artefacts

- `AI-CoE-AI-Impact-Assessment.xlsx` — the working tool
- `AI-CoE-AI-Governance-Playbook.docx` — operating model + gates + roles
- `AI-CoE-Sovereign-AI-RSA.pptx` — sovereignty offer that consumes this governance pack
- ACC-4 (Regulated-Industry Pilot Kit) — pre-pilot workshop that completes Gate 2
- `AI-CoE-Objection-Handling.pptx` — pillar 5 responses

## 11. Sources

- Microsoft Responsible AI Standard v2 (public)
- ISO/IEC 42001:2023 — AI Management System
- NIST AI Risk Management Framework 1.0
- EU AI Act (Regulation (EU) 2024/1689)
- POPI Act (Protection of Personal Information Act), PFMA (Public Finance Management Act)
- Microsoft Trust Center, Purview AI Hub documentation, Defender for Cloud AI documentation

## 12. Glossary

- **RAI v2** — Microsoft Responsible AI Standard, version 2
- **HITL** — Human-in-the-loop
- **DPIA** — Data Protection Impact Assessment
- **CMK** — Customer-Managed Key
- **POPIA / PFMA / NERSA / SARB / FSCA / AGSA** — see Sovereign AI report glossary
