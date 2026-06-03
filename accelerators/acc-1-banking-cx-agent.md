# ACC-1 — RSA Banking Customer-Service Agent Pattern

**Owner:** RSA CoE · **Maturity:** v1.0 · **Last updated:** 2026-06-03

## One-line
A reference architecture and delivery pattern for tier-1 customer-service automation in SA banks, built on Copilot Studio + Azure AI Foundry Agent Service, hardened for SARB / FSCA / POPIA.

## Customer problem
Tier-1 contact-centre AHT > 6 minutes, FCR < 70%, agent attrition > 25% p.a., and a regulatory environment that punishes mis-selling. Customers want deflection and assist, not just a chatbot.

## Solution shape
- **Channel layer:** WhatsApp Business + web + IVR (via ACS) → Copilot Studio agent
- **Reasoning layer:** Foundry Agent Service with grounded retrieval over T24 / SAP CRM / policy KB
- **Action layer:** ServiceNow / Microsoft Dataverse tickets, OTP via ACS
- **Safety layer:** Prompt Shields, content filters tuned for ZA financial terminology, full Purview AI Hub instrumentation
- **HITL:** All transactional actions (payment, limit change) routed to human queue with full reasoning trace

## Reference architecture
See `docs/images/acc-1-architecture.svg` *(to be added)*

## KPIs (first 90 days)
- AHT ↓ 30–45%
- Deflection 25–40% of tier-1 volume
- CSAT ≥ baseline (do no harm)
- Zero POPIA / FSCA findings on audit sample

## Funding stack
| Phase | Vehicle | Envelope |
|---|---|---|
| Envision | ECIF pre-sales | $50K |
| Pilot (8–12 wk) | ATO ACO + ECIF | $250–500K |
| Scale (16 wk) | Partner MAICPP | Partner-funded |

## Partner role
MAICPP build partner runs the integration sprint; Microsoft retains the Foundry / Copilot Studio architecture authority and the governance gate.

## Risks & mitigations
- **PII leakage into model context** → Purview DLP labels + Foundry data-zone scoping; never send unmasked account numbers
- **Hallucinated balances or rates** → All numeric facts come from T24 tool calls, never from the model; eval harness blocks any free-text dollar/rand amount
- **Regulator nervousness** → Walk SARB / FSCA through the architecture pre-launch; share Purview audit export quarterly

## Anti-patterns (do not do this)
- Don't ship without a kill-switch on the agent topic
- Don't let the agent draft customer-facing letters without a human reviewer
- Don't use a single shared Foundry project across multiple business lines — split for blast radius

## Linked artefacts
- VBD A5 (Copilot Chat & Agents Workshop) for the envision phase
- ACC-2 (POPIA Landing Zone) as the platform foundation
- AI Impact Assessment (`AI-CoE-AI-Impact-Assessment.xlsx`)
