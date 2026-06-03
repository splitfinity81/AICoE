# Sovereign AI for RSA — Long-form Report

**Author:** Yuri Baijnath, CSU Cloud & AI Lead (South Africa), Microsoft
**Audience:** RSA CoE, ATU sellers, regulated-customer sponsors, partner CSAs
**Companion deck:** `AI-CoE-Sovereign-AI-RSA.pptx`
**Last updated:** 2026-06-03

---

## 1. Why this offer exists

Sovereignty has graduated from a checkbox to a deal qualifier in South Africa. State-Owned Enterprises, banks, insurers, and large public-sector buyers no longer accept "the data stays in Azure" — they want a named offer with named controls, named regions, and a named operating model that survives an AGSA / SARB / Information Regulator review.

Competitors have productised this: Capgemini sells **Sovereign Cloud for AI**; Atos/Eviden, Thales, and Orange Business each publish sovereign-AI catalogues. Microsoft RSA fielding only caveats on slides loses the conversation before the architecture review.

This offer packages Microsoft's existing sovereign-AI capability into a single named artefact that an RSA CSA can take to a CISO / DPO / Internal Audit triad and walk out with a signed pilot gate.

## 2. What we sell

**AI-CoE-Sovereign-AI-RSA** is a productised offer with five components:

1. **Residency commitment** — workload and data confined to South Africa North + South Africa West regions, evidenced via Azure Policy + Purview lineage
2. **Governance posture** — Purview AI Hub, Defender for Cloud AI, Sentinel data connector, Azure Policy initiative, all wired on day 1
3. **Control crosswalk** — single matrix mapping our controls to POPIA, PFMA, NERSA, SARB Directive 7, FSCA Conduct Standards, AGSA audit expectations, ISO/IEC 42001, NIST AI RMF, EU AI Act (for multinationals with EU exposure)
4. **Operating model** — RACI for the customer's CISO / DPO / IA + Microsoft + partner across run-time controls, incident response, audit support, and quarterly attestation
5. **Customer-deliverable artefact pack** — board-ready summary, regulator-facing brief, audit evidence template, kill-switch run-book

## 3. The three sovereignty dimensions

Customers conflate three different sovereignty concerns. The offer separates them, because each has a different control set.

### 3.1 Data sovereignty
The data — at rest, in flight, in vector indexes, in logs — stays in SA North / SA West. Cross-border transfer governed by POPIA §72 list. Foundry data-zone scoping enforced. Vector stores, eval datasets, and prompt logs all in-region.

### 3.2 Operational sovereignty
SA-based support, in-region operations during business hours, customer-controlled keys (CMK via Key Vault HSM), customer-controlled break-glass procedures. Microsoft global support routed only on customer consent and only for service-level incidents.

### 3.3 Decision sovereignty
The customer retains decision authority on what the AI does. This is the most-overlooked dimension. Includes: customer owns the system prompts; customer-approved model catalogue (no shadow models); reasoning trace exposed to internal audit; kill-switch under customer control; quarterly attestation that no model behaviour changed without notice.

Walking a CISO through all three dimensions, with named controls under each, is what wins the architecture review.

## 4. Region posture (SA North + SA West)

| Capability | SA North | SA West | Notes |
|---|---|---|---|
| Azure AI Foundry | ✓ | partial | Service GA progression — `VERIFY` quarterly |
| Azure OpenAI models | ✓ | partial | Model rollout differs — see Foundry data-zone docs |
| M365 Copilot processing | EU/US | EU/US | Tenant-region determines; not in-SA today |
| Purview AI Hub | ✓ | ✓ | Tenant-region service |
| Defender for Cloud AI | ✓ | ✓ | |
| Document Intelligence | ✓ | ✓ | |
| Communication Services | ✓ | partial | For WhatsApp / SMS channels |

> **`VERIFY` quarterly:** All "✓ / partial" entries above must be re-verified on `aka.ms/AzureRegions` and Foundry data-zone documentation before any customer commit.

## 5. M365 Copilot — the honest answer

M365 Copilot tenant-region determines processing region. For SA-tenanted customers today, this is typically EU. The honest position to take with a customer:

- M365 Copilot **prompts and responses** are not stored long-term; transit is encrypted; tenant data is not used to train models.
- For the **deepest** sovereignty posture, route sensitive AI workloads to **Azure AI Foundry in SA regions** via Copilot Studio agents, not directly via M365 Copilot.
- For the M365 Copilot SKU itself, present Microsoft's published privacy commitments and the EU Data Boundary commitments — do not over-promise SA in-region processing where it does not exist.

## 6. Control crosswalk (master matrix)

The single most useful artefact in this offer is the crosswalk that lets a CISO map one control once and see it discharge across all eight frameworks. Excerpt:

| Microsoft control | POPIA | PFMA | RAI v2 | ISO 42001 | NIST AI RMF | EU AI Act |
|---|---|---|---|---|---|---|
| Data residency to SA regions | §72 | n/a | n/a | A.6.2 | GOVERN-1.3 | Art. 10 |
| CMK encryption at rest | §19 | s.45 | n/a | A.8.24 | PROTECT | Art. 15 |
| Purview AI Hub audit trail | §17, §22 | s.38 | RAI-G3 | A.5.10 | MEASURE-2.5 | Art. 12 |
| Defender for Cloud AI posture | §19 | n/a | RAI-S2 | A.8.16 | MANAGE-3 | Art. 9 |
| Content Safety + Prompt Shields | n/a | n/a | RAI-S1 | A.5.34 | MANAGE-2.3 | Art. 15 |
| System-prompt versioning | §22 | n/a | RAI-T2 | A.5.37 | GOVERN-1.5 | Art. 11 |
| HITL gate on regulated outputs | §11 | n/a | RAI-A1 | A.6.4 | MANAGE-2.4 | Art. 14 |
| Kill-switch run-book + test | n/a | s.45 | RAI-S3 | A.5.30 | MANAGE-3 | Art. 9 |

Full matrix lives in `AI-CoE-AI-Impact-Assessment.xlsx` (P1 issue #6 deliverable).

## 7. Operating model

A two-page RACI customised per customer:

- **Microsoft (CSA + Field Engineering):** Architecture authority, region availability changes, quarterly attestation pack, incident L3
- **Customer CISO:** Policy ownership, control attestation sign-off, kill-switch authority
- **Customer DPO:** POPIA DPIA owner, cross-border transfer approver, subject-access response
- **Customer Internal Audit:** Quarterly evidence review, AGSA liaison
- **Partner (MAICPP build):** Day-to-day operations, L1/L2 incident response, change-request execution

## 8. Engagement shape

| Phase | Duration | Funded by | Deliverables |
|---|---|---|---|
| Sovereign-AI Envision Workshop | 4 weeks | Pre-sales ECIF $50K | Crosswalk tailored, gap analysis, regulator-correspondence pack |
| Landing-Zone deploy (ACC-2) | 2 weeks | Cloud Accelerate Factory $0 | Production landing-zone in SA North |
| Pilot (use-case dependent) | 8–12 weeks | ATO $250–500K + partner | First production workload + audit evidence pack |
| Quarterly attestation | Ongoing | Customer | Re-verify controls, region availability, model catalogue |

## 9. What this is NOT

- **Not** an air-gapped offer. We do not operate Azure Stack Edge / disconnected scenarios under this SKU.
- **Not** a workaround for Foundry / Copilot services that are not yet GA in SA regions. Where a service is not in-region, this offer documents the gap and the customer's risk acceptance — it does not pretend coverage.
- **Not** a substitute for the customer's own POPIA compliance programme. We provide the controls; the customer remains the responsible party.

## 10. Counter-objections (most-common)

1. **"M365 Copilot processes in EU, so you're not sovereign."** → Correct for M365 Copilot today. For deep-sovereignty workloads, route via Foundry in SA. This offer makes that explicit.
2. **"You can't promise in-region forever."** → Correct. We commit to quarterly attestation and 12-month notice on region changes via the operating model.
3. **"AGSA will reject this."** → AGSA reviews evidence, not vendor promises. The evidence template in this pack is what an AGSA reviewer wants to see.
4. **"What about EU AI Act for our multinational parent?"** → Crosswalk includes EU AI Act categories; offer is co-deployable with EU Data Boundary if needed.

## 11. Sources

- `aka.ms/AzureRegions` (verify quarterly)
- Microsoft Trust Center — Data Residency and Sovereignty
- Foundry Data Zone documentation
- Microsoft Responsible AI Standard v2
- POPI Act, PFMA, NERSA Act, SARB Directive 7 (publicly available)
- ISO/IEC 42001:2023, NIST AI RMF 1.0, EU AI Act (Regulation 2024/1689)

## 12. Glossary

- **POPIA** — Protection of Personal Information Act (RSA)
- **PFMA** — Public Finance Management Act (RSA)
- **NERSA** — National Energy Regulator of South Africa
- **SARB** — South African Reserve Bank
- **FSCA** — Financial Sector Conduct Authority
- **AGSA** — Auditor-General of South Africa
- **CMK** — Customer-Managed Key
- **HITL** — Human-in-the-loop
- **DPIA** — Data Protection Impact Assessment
- **RAI v2** — Microsoft Responsible AI Standard, version 2
