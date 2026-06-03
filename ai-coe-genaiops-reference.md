# AI CoE GenAIOps & Agent-Ops Reference

**Author:** Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft
**Version:** 1.0 · 2026-06-03
**Companion artefact:** `AI-CoE-GenAIOps-Reference.docx`
**Diagram:** `docs/images/genaiops-reference-architecture.svg`
**Issue:** Closes #11 (VBD C13 — productise beyond a workshop)

---

## 1. Why this exists

VBD **C13** today reads as a workshop. Competitors lead with productised offerings: IBM **watsonx Orchestrate**, Salesforce **Agentforce**, ServiceNow **Now Assist**, Accenture **Switchboard**. Each of those is a named registry + lifecycle plane on top of an agent runtime. Microsoft's stack has the equivalent — better, in fact, because it covers all three surfaces (M365 Copilot, Copilot Studio, Foundry) — but the CoE pack does not package it as one named artefact.

This document is that artefact. It replaces the C13 workshop pitch with a named **GenAIOps reference architecture + agent-registry pattern + lifecycle gates + telemetry & eval blueprint**, grounded in shipping Microsoft products.

## 2. The agent inventory model — the registry

Every agent in the customer estate is registered in a single inventory regardless of surface. This is the spine of GenAIOps: you cannot govern, evaluate, or cost what you cannot enumerate.

| Inventory field | Source | Required |
|---|---|---|
| Agent ID | Generated (GUID) | Yes |
| Display name | Author | Yes |
| Surface | M365 / Copilot Studio / Foundry / 3rd-party | Yes |
| Owner (named human) | CoE charter | Yes |
| Sponsor (LOB) | Use-case sign-off | Yes |
| Lifecycle stage | Build / Eval / Pilot / Prod / Sunset | Yes |
| Models invoked | Foundry catalog reference(s) | Yes |
| Data sources | AI Search index, SharePoint label, Dataverse table, API | Yes |
| HITL gate | Required: yes/no; if yes, queue identifier | Yes |
| RAI impact tier | T1 limited / T2 augmented / T3 autonomous | Yes |
| Eval suite | PromptFlow / Azure AI Evaluations run ID | Yes |
| Kill-switch | Azure Policy assignment ID | Yes |
| Cost centre | FinOps tag | Yes |

**Implementation:** the inventory is a Dataverse table (`coe_AgentRegistry`) fronted by a Power App that CoE leads, sponsors, and CISOs read. The registry is the **single source of truth** that every other GenAIOps mechanism (eval, monitoring, gates) reads from.

## 3. Reference architecture — six layers

The architecture has six layers. Every layer maps to a shipping Microsoft product.

| Layer | Microsoft product | Purpose |
|---|---|---|
| **L1 — Experience** | Microsoft 365, Copilot Studio canvas, custom UI, embedded chat | Where the human interacts with the agent |
| **L2 — Orchestration & registry** | Copilot Studio, Foundry Agent Service, Semantic Kernel, Dataverse `coe_AgentRegistry` | Which agent, which flow, which tool — and tracked centrally |
| **L3 — Reasoning** | Foundry model catalog (OpenAI, Anthropic, Meta Llama, Mistral, Cohere, NVIDIA NIM, Hugging Face, Microsoft Phi) + routing | The model(s) doing the inference; routing chooses cost/latency-appropriate model |
| **L4 — Grounding & memory** | AI Search, Cosmos DB vector, Microsoft Graph connectors, Dataverse, Fabric OneLake | Where retrieval, structured grounding, and short/long-term memory live |
| **L5 — Eval & telemetry** | PromptFlow, Azure AI Evaluations, Application Insights, Log Analytics, Foundry tracing | Continuous offline + online eval, drift detection, cost telemetry |
| **L6 — Governance & safety** | Azure AI Content Safety, Prompt Shields, Microsoft Purview AI Hub, Defender for Cloud AI, Azure Policy kill-switch | Pre-prompt filtering, post-response filtering, audit, posture management, emergency disable |

A simplified visual is published as `docs/images/genaiops-reference-architecture.svg`.

## 4. Agent lifecycle gates — build → eval → release → monitor → retire

Every agent traverses five gates. The four governance gates in `AI-CoE-AI-Governance-Playbook.docx` (Envision / Pre-pilot / Pre-prod / Attestation) bind to these; the lifecycle gates are the technical execution view.

| Gate | Owner | Mandatory artefact | Tool |
|---|---|---|---|
| **G-Build** | Agent author | Registry record + system-prompt + tool list, version-pinned | GitHub + Dataverse |
| **G-Eval** | CoE eval lead | Offline eval pack ≥ 50 reference cases; safety + quality + grounding scores at or above threshold | PromptFlow + Azure AI Evaluations |
| **G-Release** | Customer CISO + business sponsor | Pilot approval; kill-switch tested; HITL queue live (if T2/T3); monitoring dashboards green | Foundry deployment + Azure Policy |
| **G-Monitor** | Customer ops (run-time) | Online eval samples weekly; drift report monthly; cost dashboard weekly; incident channel staffed | App Insights + AI Hub + Sentinel |
| **G-Retire** | Agent owner | Sunset notice + 30-day grace + user comms + cost-tag closeout | Registry + Azure Policy disable |

Skipping a gate requires written sign-off from CoE lead + CISO logged in the registry.

## 5. Eval harness blueprint

Eval is the heartbeat. The pack ships a single named pattern; customers can extend it.

**Offline (pre-release, per change):**
- Reference set: ≥ 50 cases per agent, expanded to ≥ 200 for T2/T3 agents.
- Scorers: groundedness, relevance, fluency, safety (Content Safety integration), task-success.
- Threshold gating: configured per agent in the registry; release blocked if any scorer falls below threshold.
- Tooling: PromptFlow flows checked into GitHub; Azure AI Evaluations SDK run via Azure DevOps pipeline.

**Online (continuous, per N% sample):**
- Sample rate: 1-5% of production traffic, sampled on prompt category.
- Scorers: groundedness, safety, user-feedback signal (thumbs up/down or implicit), reviewer override (HITL cases).
- Drift detector: weekly rolling-window comparison; alert if any scorer drops > 5% vs trailing 30-day baseline.
- Tooling: Application Insights → Log Analytics → Workbook ; export to Fabric for trend analysis.

**Reviewer feedback loop:**
- Every HITL override is captured (prompt, response, override reason, reviewer ID).
- Override pack auto-ingested into the next offline eval set monthly.
- Closes the loop: reviewer pain becomes future eval coverage.

## 6. Telemetry & cost dashboards

Four dashboards ship with the pattern. Each is a Power BI workbook on top of App Insights + Foundry tracing + the registry.

| Dashboard | Audience | KPIs |
|---|---|---|
| **Agent operations** | CoE lead, ops team | Latency p50/p95, error rate, throughput, deployment freshness |
| **Quality & safety** | CISO, RAI lead | Eval-score trends, safety-block rate, drift alerts, HITL override rate |
| **Adoption & value** | Sponsor, LOB lead | DAU/WAU/MAU, depth (turns per session), containment, satisfaction |
| **FinOps for AI** | FinOps lead, CoE lead | $/query, $/user, model-mix economics, cache-hit %, routing efficiency — sourced from `AI-CoE-AI-TCO-Calculator.xlsx` model |

## 7. Drift, safety, cost monitoring — what triggers what

| Signal | Threshold (default) | Owner | Action |
|---|---|---|---|
| Safety block rate spike | > 2× trailing 7-day avg | RAI lead | Investigate prompts; tune Content Safety; potentially hotfix system-prompt |
| Groundedness drop | > 5% vs 30-day baseline | CoE eval lead | Re-evaluate retrieval pipeline; check index freshness |
| $/query rising | > 15% vs 30-day baseline | FinOps lead | Inspect model mix, cache-hit, fallback rate |
| HITL override rate up | > 1.5× trailing 7-day | Sponsor + eval lead | Add to next eval set; iterate prompt or retrieval |
| Kill-switch invoked | Any | CISO | IR run-book; root-cause within 24h; gate review |

## 8. Sample repo layout (publishable)

```
/coe-genaiops-starter
  /infra
    bicep/agent-runtime.bicep        # Foundry + AI Search + Content Safety + Key Vault
    bicep/observability.bicep        # App Insights + Log Analytics + Workbooks
    policy/kill-switch-initiative.json
  /agents
    /agent-template
      prompts/system.md
      tools/manifest.json
      eval/reference_cases.jsonl
      eval/promptflow.yaml
      registry.json                  # Dataverse-bound registry record
  /ops
    powerbi/agent-ops.pbix
    powerbi/quality-safety.pbix
    powerbi/adoption-value.pbix
    powerbi/finops-for-ai.pbix
  /docs
    runbook-incident.md
    runbook-killswitch.md
    runbook-eval-failure.md
```

The repo is not in this pack; this layout is the canonical reference for partners building under MAICPP and for customer build teams under VBD C13.

## 9. RACI

| Activity | CoE lead | Agent author | CISO | RAI lead | FinOps | Sponsor |
|---|---|---|---|---|---|---|
| Register agent | A | R | I | I | I | C |
| Run offline eval | A | R | C | C | I | I |
| Approve release | A | C | A | C | C | A |
| Operate (run) | A | R | C | C | C | I |
| Quarterly drift review | A | C | A | R | C | C |
| Retire | A | R | I | I | C | C |

## 10. Linked artefacts

- `AI-CoE-VBD-Reference-Deck.pptx` — C13 entry updated to point to this document.
- `AI-CoE-AI-Governance-Playbook.docx` — four governance gates this lifecycle binds to.
- `AI-CoE-AI-Impact-Assessment.xlsx` — risk tier and control selection drive registry fields.
- `AI-CoE-AI-TCO-Calculator.xlsx` — FinOps-for-AI dashboard data source.
- `AI-CoE-Objection-Handling.pptx` — objection 3.3 ("we need agents, not chat") rebuttal anchors here.
- `ACC-5` Document Intelligence + Foundry Pattern — first agent pattern customers build on this lifecycle.

## 11. What this document is NOT

- Not a replacement for Foundry, Copilot Studio, or M365 admin docs — those are authoritative.
- Not a managed service: the CoE provides the pattern; customer or partner runs the registry.
- Not pre-built code: the sample repo layout is canonical; the repo itself is customer-instantiated under MAICPP.
