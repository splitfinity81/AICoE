# ACC-2 — POPIA-Compliant Foundry Landing-Zone Blueprint

**Owner:** RSA CoE · **Maturity:** v1.0 · **Last updated:** 2026-06-03

## One-line
A Bicep / Terraform landing-zone that deploys an Azure AI Foundry workload in SA North or SA West with POPIA, PFMA, Purview AI Hub, and Defender for Cloud AI controls pre-wired — deployable in under two weeks by the Microsoft Cloud Accelerate Factory.

## Customer problem
"We can't put customer data into AI until we know where it goes." Customers stall in pre-deployment because they cannot evidence data-residency, audit, or DLP controls to their CISO / DPO / SARB or AGSA.

## What you get
- **Resource topology:** Hub-and-spoke with private endpoints to all Foundry services; no public ingress
- **Region:** SA North primary, SA West DR (or both for active-active where AI services GA)
- **Identity:** Entra ID with Conditional Access; managed identity throughout — no service principals with secrets
- **Data plane:** Storage with CMK (Key Vault HSM-backed), private DNS zones, vector store in-region
- **Governance:** Purview AI Hub onboarded day 1, Defender for Cloud AI workload protection, Sentinel data connector
- **Network:** Azure Firewall premium, WAF on Front Door, NSG flow logs
- **Cost guardrails:** Budgets + alerts, tag policy enforced at MG level

## What you do NOT get (out of scope)
- Application code or use-case-specific agents (see ACC-1, ACC-5)
- Data ingestion pipelines for source systems (separate engagement)
- Model fine-tuning infrastructure (separate landing-zone variant)

## Compliance crosswalk
| Control | POPIA | PFMA | RAI v2 | ISO 42001 |
|---|---|---|---|---|
| Data residency in-region | §72 | n/a | n/a | A.6.2 |
| Encryption at rest (CMK) | §19 | s.45 | n/a | A.8.24 |
| Access audit (Purview + Sentinel) | §17, §22 | s.38 | RAI-G3 | A.5.10 |
| DLP on egress | §19 | n/a | RAI-S2 | A.8.12 |

## Deploy
```bash
# Prerequisites: Owner on target subscription, Bicep CLI, Azure CLI logged in
cd infra/landing-zone
az deployment sub create \
  --name aicoe-lz-prod \
  --location southafricanorth \
  --template-file main.bicep \
  --parameters @prod.bicepparam
```
*(Bicep templates to be added in a subsequent commit — placeholder for v1.0 release)*

## Funding
Microsoft Cloud Accelerate Factory delivers F1 (Landing Zone), F3 (Security Hardening), F4 (Governance Onboarding) at **$0** to the customer when the workload is Azure AI Foundry.

## Time-box
- Day 1–3: Customer subscription readiness, naming standards, IP planning
- Day 4–8: Bicep deploy + smoke tests
- Day 9–10: Purview / Defender / Sentinel onboarding + handover

## Partner role
None. This is Microsoft Factory-delivered. Partner picks up from here for build (see ACC-1).

## Linked artefacts
- VBD C9 (Azure Landing Zone for AI)
- ACC-4 (Regulated Pilot Kit) — uses this as its platform
- `AI-CoE-Sovereign-AI-RSA.pptx`
