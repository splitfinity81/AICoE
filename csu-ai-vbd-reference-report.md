# CSU AI / AI CoE VBD Reference Appendix

**Audience:** RSA CSU — CSU Cloud & AI Lead (Yuri Baijnath) and CSA team
**Purpose:** Reference appendix for the AI CoE artefact pack — every CSU-deliverable AI / AI CoE VBD with delivery owner, scope, MCEM stage, funding instrument, 5+1 pillar, and CoE-ladder tier
**As of:** FY26 H2 (catalogue refreshes each fiscal year — re-verify on MCAPS Catalog before commit)
**Confidence note:** This appendix is grounded in (a) internal grounding files in `/mnt/workspace/input` and `/mnt/workspace/working` (HIGH trust — MCAPS-sourced), and (b) Microsoft VBD/Azure-Accelerate knowledge as of May 2025 (MODERATE — the FY26 H2 catalogue may have renamed or retired entries). Items flagged `VERIFY` should be cross-checked on MCAPS Catalog / Microsoft Partner Center / aka.ms VBD index before quoting in customer-facing material.

---

## Executive Summary

- The CSU-deliverable AI VBD catalogue clusters into **three AI surfaces** that map cleanly to the three CSU sub-teams: M365 Copilot (Modern Work CSU), Copilot Studio / Power Platform AI (Business Applications CSU), Azure AI Foundry / Fabric / Azure AI (Cloud & AI Platforms CSU).
- **Funding has consolidated in FY26.** AMM (Azure Migrate & Modernize) and AIRA (Azure Innovate / AI Ready) were rolled into the **Azure Accelerate** umbrella with three solution plays — *Migrate & Modernize*, *Unify Data Platform*, *Innovate with AI Apps & Agents*. ECIF, ACO, and MAICPP partner-funding mechanisms continue to back individual VBDs (confirmed by `/mnt/workspace/working/ato-content.md` slides 10–12).
- The flagship CSU AI delivery in RSA scope is the **AI Transformation Offer (ATO) powered by Azure Frontier**, owned by Cloud & AI Platforms CSU with STU coordination — three components (CoE & Envisioning / AI Foundation Architecture / GenAI Factory) covering all three CoE-ladder tiers and all five core 5+1 pillars.
- **Tier 1 (Envisioning)** is dominated by workshops and Solution Assessments; **Tier 2 (Build)** by landing-zone implementations, hackathons, and co-builds; **Tier 3 (Managed Run)** by GenAIOps maturity, optimization, and scale engagements. Most CSU VBDs are **Tier 1 + Tier 2**; Tier 3 is typically partner-led with CSU oversight.
- **Confidence:** HIGH for the ATO line-items (verified in grounding); MODERATE for the broader Azure Innovate / Solution Assessment / Modern Work Copilot list (training-data, 2025-05 cutoff); flag-for-VERIFY for any FY26 H2 renamings.

---

## Legend

| Code | Meaning |
|---|---|
| MW | Modern Work CSU (M365 + M365 Copilot) |
| BA | Business Applications CSU (D365, Copilot Studio, Power Platform) |
| CAI | Cloud & AI Platforms CSU (Azure AI Foundry, Fabric, AI Infra) |
| X | Cross-CSU |
| MCEM 1–5 | 1 Listen & Consult / 2 Inspire & Design / 3 Empower & Achieve / 4 Realize Value / 5 Manage & Optimize |
| Pillars | 1 Business Strategy / 2 Org & Culture / 3 AI Strategy & Experience / 4 Tech & Data / 5 Governance & Security / +1 Co-sell & Partner |
| Tier | T1 Envisioning / T2 Build / T3 Managed Run / X cross-tier |
| Funding | ECIF / AMM / MAICPP / ACO / SA (Solution Assessment) / CF (Customer-Funded) |

---

## A. M365 Copilot Family — owner: Modern Work CSU

| # | VBD (official name) | Owner | Scope (1–2 sentences) | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| A1 | **Microsoft 365 Copilot Art of the Possible / Envisioning Workshop** | MW | Executive-level inspiration session covering Copilot value, scenarios, and roadmap; produces a prioritized scenario shortlist. | 0.5–1 day | 1–2 | ECIF, MAICPP | 1, 3 | T1 | MCAPS Catalog — Copilot Adoption playbook |
| A2 | **M365 Copilot Scenario Workshop ("Day in the Life")** | MW | Role/persona-based scenario design (Sales, Finance, HR, Service) mapping Copilot prompts to top-time-spend activities; outputs a per-role scenario library. | 1–2 days | 2 | ECIF, MAICPP | 1, 3 | T1 | Copilot Scenario Library on adoption.microsoft.com |
| A3 | **M365 Copilot Adoption Accelerator (Adoption Engagement)** | MW | Structured 8–12 week champions-network, comms, training, and measurement program covering deployment readiness through usage telemetry. | 8–12 weeks | 3–4 | ECIF, MAICPP | 2, 3 | T1+T2 | M365 Copilot Adoption Hub (adoption.microsoft.com/copilot) |
| A4 | **M365 Copilot Optimization Assessment / Value Realization Engagement** | MW | Telemetry-driven analysis of Copilot usage, license utilization, and business-value realization with corrective actions to lift active-use %. | 4–6 weeks | 4–5 | ECIF, SA | 1, 2, 3 | T3 | MCAPS Catalog — Copilot Optimization (`VERIFY` — naming changed mid-FY26) |
| A5 | **M365 Copilot Chat & Agents Workshop** *(FY26 addition)* | MW | Hands-on exposure to Copilot Chat with agents (no-license entry point) and to building lightweight agents that surface in M365 Copilot. | 1 day | 2 | ECIF | 3 | T1 | FY26 H2 Copilot Execution doc (`input/FY26 H2 Copilot Execution.xlsx`) — `VERIFY` |
| A6 | **Copilot Readiness / Data Security Assessment for M365 Copilot** | MW (with CAI assist on Purview) | Pre-deployment assessment of oversharing risk, sensitivity-label coverage, SharePoint permissions, and DLP; remediates before grounding Copilot to tenant data. | 2–4 weeks | 2 | ECIF, SA | 5 | T1 | Microsoft Purview / SharePoint Advanced Management docs |
| A7 | **Copilot for Security Workshop** *(cross-product)* | MW (sometimes Security STU) | Half-day / 1-day workshop demonstrating Copilot for Security in SOC scenarios; produces a use-case shortlist. | 0.5–1 day | 2 | ECIF | 3, 5 | T1 | Security Copilot RFP / aka.ms/copilotforsecurity |
| A8 | **Microsoft 365 Copilot Center of Excellence Engagement** | MW | Stand-up of an internal Copilot CoE — governance board, prompt library, role-mapping, KPI scorecard — institutionalizes scaling. | 4–8 weeks | 3–4 | ECIF, MAICPP | 1, 2, 5 | T2+T3 | M365 Copilot Adoption Hub — CoE template (`VERIFY` — partner-led variants exist) |

**Retired / superseded note:** Earlier "Modern Work Solution Assessment — Copilot Readiness" was rebadged into A4/A6 during FY26 H1.

---

## B. Copilot Studio / Power Platform AI Family — owner: Business Applications CSU

| # | VBD (official name) | Owner | Scope | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| B1 | **Copilot Studio Workshop ("Agent in a Day")** | BA | Hands-on lab building a no-code/low-code agent in Copilot Studio over generative actions, knowledge sources, and Power Automate connectors. | 1 day | 2 | ECIF, MAICPP | 3 | T1 | aka.ms/CopilotStudioWorkshop / Power Platform partner playbook |
| B2 | **Copilot Studio Agent Build (Co-build) Engagement** | BA | 4–8 week co-build of one production-grade Copilot Studio agent with handoff and ALM; commonly funded by MAICPP. | 4–8 weeks | 3 | MAICPP, ECIF | 3, 4 | T2 | Copilot Studio partner build engagement (`VERIFY` — sometimes packaged under Power Platform Adoption Accelerator) |
| B3 | **Power Platform AI Builder Workshop** | BA | Half-day to 1-day session demonstrating prebuilt and custom AI models in Power Apps / Power Automate (forms processing, prediction, sentiment). | 0.5–1 day | 2 | ECIF | 3 | T1 | Microsoft Learn — AI Builder catalog |
| B4 | **Dynamics 365 Copilot Envisioning Workshop** | BA | Sales / Service / Customer Insights / Finance Copilot envisioning by workload; outputs scenario backlog and license-uplift business case. | 1–2 days | 1–2 | ECIF, MAICPP | 1, 3 | T1 | D365 partner-led envisioning playbook |
| B5 | **D365 + Copilot Studio Agentic Workflow Build** | BA (CAI assist for Foundry) | Cross-product co-build connecting D365 data, Copilot Studio agents, and (optionally) Foundry custom skills for an end-to-end revenue/service workflow. | 6–10 weeks | 3 | MAICPP, ECIF, ACO | 3, 4 | T2 | FY26 BizApps + AI agentic workflow play (`VERIFY` — naming evolving) |
| B6 | **Power Platform Center of Excellence Starter Kit Engagement** | BA | Deploys the Power Platform CoE Starter Kit (admin, governance, nurture, ALM); precondition for Copilot Studio at scale. | 2–4 weeks | 3 | ECIF | 2, 5 | T2 | Microsoft Learn — Power Platform CoE Starter Kit |
| B7 | **Copilot Studio Solution Assessment** *(where available)* | BA | Pre-build assessment of agent landscape, license footprint, governance gaps, and prioritized agent roadmap. | 3–6 weeks | 2 | SA, ECIF | 3, 5 | T1 | MCAPS Catalog — Solution Assessment family (`VERIFY` — listed under Power Platform SA in some regions) |

**Note on partner-led delivery:** B2, B5, and B6 are most often delivered by an MAICPP-funded partner with CSU oversight; B1, B3, B4 are routinely CSU-led.

---

## C. Azure AI Foundry / Fabric / Azure AI Family — owner: Cloud & AI Platforms CSU

### C.1 Azure Accelerate — "Innovate with AI Apps & Agents" solution play

In FY26 the funding mechanic moved into **Azure Accelerate**, a single umbrella covering three solution plays, with both Microsoft-field-nominated and partner-nominated paths and ECIF/ACO/partner funding (`/mnt/workspace/working/ato-content.md` slides 10–11). The AI-relevant plays are:

| # | VBD | Owner | Scope | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| C1 | **Azure Innovate — Innovate with AI (Plan phase)** | CAI | Funded assessment + proof-of-value scoping for an Azure AI / Foundry workload; partner co-funding $15K–$50K depending on T-shirt size. | 4–8 weeks | 2 | ECIF, MAICPP, SA, partner-funding | 3, 4 | T1 | Azure Accelerate offers — `aka.ms/AzureAccelerate` (slide 10) |
| C2 | **Azure Innovate — Innovate with AI (Implement phase)** | CAI | Funded production landing-zone build / go-live for AI Apps, Agents & Developer workload; partner funding XS–L tiers + up-to-20% ACR uplift. | 8–24 weeks | 3 | ACO, MAICPP, partner-funding | 3, 4, 5 | T2 | Azure Accelerate offers (slide 11) |
| C3 | **Azure Innovate — Build & Modernize AI Apps** | CAI | App-modernization variant of C2 — refactors existing apps to AI-app architecture (Foundry, AOAI, embeddings, vector). | 8–16 weeks | 3 | ACO, MAICPP, ECIF | 4 | T2 | Azure Accelerate — Build & Modernize AI Apps SKU |
| C4 | **Azure Innovate — AI App and Agent Factory** | CAI | Operating-model + delivery-line build to industrialize agent delivery (templates, GenAIOps, golden paths). | 10–16 weeks | 3–4 | ACO, MAICPP, ECIF | 3, 4, 5 | T2+T3 | aka.ms/AIAppAgentFactory (`VERIFY`) |
| C5 | **Azure Innovate — Analytics & AI with Microsoft Fabric** | CAI | Fabric-led data + AI workload — OneLake, Direct Lake, Fabric Data Agents, Foundry grounding. | 8–16 weeks | 3 | ACO, MAICPP, ECIF | 3, 4 | T2 | Azure Accelerate — Unify Data Platform play |

### C.2 Solution Assessments

| # | VBD | Owner | Scope | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| C6 | **Azure OpenAI / Azure AI Foundry Solution Assessment** | CAI | Funded assessment that quantifies AI use-case portfolio, landing-zone readiness, security/governance gaps, and consumption forecast. | 4–8 weeks | 2 | SA, ECIF | 3, 4, 5 | T1 | MCAPS Solution Assessment Catalog — AI Foundry SA (`VERIFY`) |
| C7 | **Microsoft Fabric Solution Assessment** | CAI | Fabric capacity sizing, OneLake architecture, Power BI/Copilot-in-Fabric readiness assessment. | 4–8 weeks | 2 | SA, ECIF | 4 | T1 | MCAPS Solution Assessment Catalog — Fabric SA |
| C8 | **AI Migrate / "Migrate AI workloads to Azure" Assessment** | CAI | Assesses 3rd-party LLM/AI workloads (AWS Bedrock, GCP Vertex, OSS) for migration to Azure AI Foundry / AOAI. | 4–6 weeks | 2 | SA, ECIF, partner-funding | 4 | T1 | AI Migrate offer (`VERIFY` — newer FY26 SKU) |

### C.3 Workshops, Hackathons, and CoE engagements (CSU-led or CSU-overseen)

| # | VBD | Owner | Scope | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| C9 | **Generative AI / Azure AI Foundry Workshop** | CAI | 1–2 day technical workshop covering AOAI, Foundry, RAG, agent patterns, evaluation, responsible AI. | 1–2 days | 2 | ECIF, MAICPP | 3, 4 | T1 | Microsoft Learn — Azure AI Foundry workshop |
| C10 | **AI Hackathon (Foundry / GenAI)** | CAI | 2–5 day customer-team hackathon producing 1–3 PoCs against prioritized scenarios; commonly bundled with C1. | 2–5 days | 2 | ECIF, MAICPP, partner-funding | 3 | T1+T2 | aka.ms/AIHackathon |
| C11 | **AI Landing Zone Implementation Workshop** | CAI | Half-day to 2-hour intro followed by 1–2 week hands-on deployment of the AI landing zone (identity, networking, policy, Foundry hub & projects). | 1–2 weeks | 3 | ECIF, ACO | 4, 5 | T2 | CAF for AI / Azure Essentials AI landing zone |
| C12 | **Well-Architected for AI Workshop** | CAI | WAF assessment focused on AI workloads — reliability, security, cost, ops, performance, and responsible-AI cross-cutting. | 1 day | 4 | ECIF | 4, 5 | T3 | Microsoft Learn — WAF AI workload |
| C13 | **GenAIOps / AgentOps Maturity Assessment** | CAI | Half-day workshop assessing prompt mgmt, evaluation, observability, lifecycle, FinOps for AI; outputs a maturity score and remediation backlog. | 0.5 day | 4 | ECIF | 5 | T3 | ATO Component 3.1 (`/mnt/workspace/working/ato-content.md` slide 14) — HIGH trust |
| C14 | **Azure Essentials AI Adoption Workshop** | CAI | Aligns customer to Azure Essentials AI adoption pillars (strategy, ready, govern, secure, manage); CAF-derived. | 1 day | 1–2 | ECIF | 1, 4, 5 | T1 | Microsoft Learn — Azure Essentials |
| C15 | **Responsible AI / AI Governance Workshop** | CAI (with Compliance STU) | Operationalises the Microsoft Responsible AI Standard — impact assessments, content safety, policy, red-team patterns. | 1–2 days | 2 | ECIF | 5 | T1 | Microsoft Responsible AI Standard v2 |
| C16 | **AI Transformation Offer (ATO) — Component 1: AI CoE & Solution Envisioning** | CAI (CSA + Strategy/Workshop Lead; ATU initiates) | AI CoE introduction (2-hr exec session) + Process Envisioning, Capability Mapping & Architecture (1 day) + Rapid Prototyping (1–2 days). | 1–2 weeks elapsed | 1–2 | ECIF (up to $50K pre-sales) | 1, 2, 3 | T1 | ATO grounding — slides 7–9, 14 (HIGH trust) |
| C17 | **ATO — Component 2: AI Foundation Architecture** | CAI (AI & Apps Architect; STU Azure SSP coordinates) | GenAI Building Blocks (1.5 hr) + Intro to Landing Zones (2 hr) + Agentic AI Landing Zone Implementation (1–2 weeks) + optional Apps & Infra Landing Zone (1–2 weeks). | 2–4 weeks | 3 | ECIF + ACO post-sales (up to $1M total: $500K ECIF + $500K ACO) | 4, 5 | T2 | ATO grounding — slides 7–14 (HIGH trust) |
| C18 | **ATO — Component 3: GenAI / Agent Factory** | CAI (AI & Apps Architect; STU Azure SSP coordinates) | GenAIOps Intro & Maturity Assessment (0.5 day) + MVP & GenAIOps Co-Build (6–8 weeks) + MVP Readout & GenAIOps Review + Solution Optimization Intro (0.5 day). | 6–10 weeks | 3–4 | ECIF + ACO + MAICPP partner | 3, 4, 5 | T2+T3 | ATO grounding — slides 7–14 (HIGH trust) |
| C19 | **AI Patterns Scorecard for Capability Envisioning** | CAI | Pattern-led use-case prioritisation against the 5 repeatable AI patterns (IDP, Extraction & Summarisation, Workflow Automation, Multimodal Interfaces, Next-Best-Action). | Embedded in C16 (1 day) | 2 | ECIF | 1, 3 | T1 | ATO grounding — slides 5, 14 (HIGH trust) |

**Retired / superseded notes (Cloud & AI Platforms):**
- **AMM (Azure Migrate & Modernize) and AIRA (Azure Innovate / AI Ready)** — folded into **Azure Accelerate** in FY26 H1. The funding mechanic continues; the SKU naming changed.
- Earlier "AI Build VBD" / "AI Ready VBD" — superseded by C1–C2 within Azure Accelerate. (`VERIFY` — some regions still surface legacy names in early FY26.)
- "Azure OpenAI Workshop" — rebadged as **Azure AI Foundry Workshop (C9)** following the rename of AI Studio to AI Foundry.

---

## D-bis. Cloud Accelerate Factory (CAF) — zero-cost CSU delivery engine

**What it is.** The Cloud Accelerate Factory ("the Factory") is the CSU's industrialised, remote-delivery engine that performs predictable, repeatable Azure deployment work at **zero additional cost** to the customer or partner. It is a benefit available within Azure Migrate & Modernize and Azure Innovate (now under the Azure Accelerate umbrella). Hands-on-keyboard delivery requires the customer to have an active **Unified Support agreement** in place OR to sign a **2-page Factory agreement**. No partner contract with Microsoft is needed — Factory contracts directly with the customer side-by-side with the partner SOW.

**Operating model.** Factory operates a remote on-shore + off-shore workforce across ASIA, EMEA, and the Americas (English + JA, KO, ZH, DE, FR, ES, PT). Resources are available **within 2 weeks of nomination**. Factory does NOT own project governance — Customer/Partner does. Factory's PM coordinates Factory scope under the Customer/Partner Project Manager. Factory will NOT rewrite or re-architect solutions, modify business logic, or perform consulting work — these stay with the partner / ISD / CSA. Factory has limited/no ability to support engagements requiring in-country presence, local citizenship, or cleared resources.

**Why it matters for the AI CoE.** Factory absorbs the **predictable foundation tasks** — landing zone, migrations, GenAI Assistant MVP — at **zero cost**, freeing ECIF, ACO, and partner services budgets for the **strategic work** (envisioning, agent design, change management, managed run, federation). It is the third stream alongside MCAPS-led envisioning and partner-led build/run.

### D-bis.1 Factory AI-relevant offerings (FY26 H2 catalogue)

| # | Factory Offering | Scope summary | Duration | MCEM | Pillars | Tier | Pairs with |
|---|---|---|---|---|---|---|---|
| F1 | **AI — GenAI Assistant** | MVP for an initial AOAI use case: Landing Zone for AOAI deployment + data migration + first use-case build + solution optimisation. Use cases supported: conversational AI / search, virtual assistant, doc intelligence, personalised content, image analysis. **Out of scope:** M365 Copilot. | 4–8 weeks | 3 | 3, 4 | T2 | ATO C3 (Agent Factory MVP) |
| F2 | **Azure Landing Zone — new deployment & validation** | Enterprise-scale platform LZ via Portal Accelerator: scalable Mgmt Group hierarchy, dedicated platform subs, hub-and-spoke topology. Validation of existing LZ also in scope. **Foundation for every AI workload** in C2/C3/C4/C5. | 2–4 weeks | 3 | 4, 5 | T2 | ATO C2 (Foundation Architecture); Azure Innovate Implement |
| F3 | **Analytics — Real-time intelligence MVP** | Lakehouse Landing Zone (Databricks or Fabric) + data migration + first use case. Provides the data substrate for AI agent grounding. | 4–8 weeks | 3 | 4 | T2 | ATO C2; Foundry grounding |
| F4 | **Analytics — Lakehouse + DW migration** | Synapse → Fabric, Databricks LH migration, data warehouse modernisation — enables AI grounding on enterprise data. | 4–10 weeks | 3 | 4 | T2 | C5 Analytics & AI with Fabric |
| F5 | **Analytics — Power BI migration to Fabric** | SSRS → Power BI; SSAS → Power BI; Power BI Premium → Fabric SKU. Foundation for Copilot in Fabric and AI-grounded reporting. | 2–6 weeks | 3 | 4 | T2 | Modern Work Copilot scenarios |
| F6 | **Arc Enablement (Windows + SQL)** | Automated Arc agent deployment; required for hybrid/edge AI workloads, governance, ESU. | 2–3 weeks | 3 | 4, 5 | T2 | Hybrid AI / sovereign deployments |
| F7 | **App Migration (App Service / AKS / ACA)** | .NET / Java Tomcat / Spring Boot — on-prem/IaaS to PaaS; containerised apps to PaaS or AKS. Enables AI embedding into modernised apps. | 4–12 weeks | 3 | 4 | T2 | C3 Build & Modernize AI Apps |
| F8 | **Security — Defender for Cloud deployment** | CSPM + CWP rollout (Servers, DBs, storage, App Service, containers, APIs, ARM, Key Vault). Underpins AI Governance & Security pillar. | 2–6 weeks | 3 | 5 | T2 | C15 Responsible AI; Pillar 5 |
| F9 | **Security — Sentinel greenfield / Splunk → Sentinel** | SIEM deployment / migration — required for AI workload observability, prompt-injection detection, abuse monitoring. | 4–10 weeks | 3 | 5 | T2 | Pillar 5 governance |
| F10 | **Infra & DB migration (Win/Linux, AVS, SQL, OSS DB, NoSQL)** | Lift-and-shift to Azure — prerequisite to AI workload migration when source data lives on legacy infra. | 4–12 weeks | 3 | 4 | T2 | C8 AI Migrate (3rd-party LLM workloads) |

**Explicitly OUT of Factory scope for AI:** M365 Copilot (any deployment), Copilot Studio agent build, business-logic code changes, custom architectures requiring rewrite, advisory/consulting, in-country sovereign delivery requiring cleared resources.

### D-bis.2 How Factory plugs into the AI CoE delivery stack

```
┌──────────────────────────────────────────────────────────────────┐
│  STREAM 1 — MCAPS-led envisioning (CSA + ATU + STU + EPS)        │
│  MCEM 1–2 · ATO C1 · ECIF pre-sales · Pillars 1–2 · Tier 1       │
├──────────────────────────────────────────────────────────────────┤
│  STREAM 2 — FACTORY-delivered foundation (zero cost)             │
│  MCEM 3 · ATO C2 + parts of C3 MVP · Pillars 4–5 · Tier 2        │
│  Offerings: F1 GenAI Assistant · F2 ALZ · F3–F5 Data · F6–F9     │
├──────────────────────────────────────────────────────────────────┤
│  STREAM 3 — Partner-led build & managed run                      │
│  MCEM 3–5 · ATO C3 + scale · Pillars 1–5 + co-sell · Tier 1–3    │
│  Funded via: MAICPP, ACO uplift, ECIF, customer-funded           │
└──────────────────────────────────────────────────────────────────┘
```

**Decision rule (when to nominate Factory):**
1. Is the task on the Factory catalogue (F1–F10 above)? → If no, do not nominate.
2. Does the customer have Unified Support OR are they willing to sign the 2-page Factory agreement? → If no, no Factory.
3. Is the task standardised (no rewrite, no business-logic change, no custom architecture)? → If no, partner-deliver.
4. Can the work tolerate a 2-week nomination-to-start lead time? → If yes, nominate via the Factory portal (`aka.ms/CloudAccelerateFactory`).

### D-bis.3 Factory references

- Factory program SharePoint: `aka.ms/CloudAccelerateFactory`
- Customer deck: `aka.ms/FactoryCustomerDeck`
- Partner deck: `aka.ms/FactoryPartnerDeck`
- Engagement guide (FY26 H2 service descriptions): on the CSU Migration Factory SharePoint — covers all 15 Factory offerings including AI–GenAI Assistant, ALZ, Analytics, Security, Arc, AVS, AVD, App, Infra & DB
- Public partner page: `partner.microsoft.com/en-us/asset/collection/cloud-accelerate-factory`
- GitHub utilities: `github.com/Azure/cloud-accelerate-factory` (incl. `OpenAI/` folder for GenAI Assistant scripts)

---

## D. Cross-CSU / AI CoE Operating-Model VBDs

| # | VBD | Owner | Scope | Duration | MCEM | Funding | Pillars | Tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| D1 | **Frontier AI CoE Stand-up Engagement (5+1 pillar build)** | X (CAI lead, MW + BA support) | Stands up the customer's AI CoE across Business Strategy, Org & Culture, AI Strategy, Tech & Data, Governance & Security + Co-sell/Partner pillar. | 6–12 weeks | 1–3 | ECIF, MAICPP | 1, 2, 3, 4, 5, +1 | T1+T2 | Frontier CoE pillar decks (`/mnt/workspace/input/Frontier CoE - *.PPTX`) — HIGH trust |
| D2 | **AI CoE Academy (RSA) — role-based skilling programme** | X (CAI lead) | Productised 12-week skilling programme delivering five named role-tracks (Executive Sponsor, AI Product Owner, AI Engineer, Data Engineer, Copilot Champion) against Microsoft Learn AI paths, sector-specific labs, and certification gates. MAICPP-co-funded learner cohorts of 25–100. Replaces ad-hoc Skill Navigator delivery with a named curriculum and cohort blueprint. | 12 weeks per cohort | 2–4 | MAICPP, ECIF | 2, +1 | T1+T2+T3 | `ai-coe-academy-curriculum.md` + `AI-CoE-Academy-Curriculum.xlsx` |
| D3 | **AI Value Realization (Stage-4 Realize) Engagement** | X (CSA-led, Stage 4 owner) | Telemetry-driven value-tracking across Copilot, Foundry, Fabric usage and outcomes; outputs CFO-grade business-case validation. | Quarterly cadence | 4–5 | ECIF | 1 | T3 | MCEM Stage 4 Playbook — CSA-owned (HIGH trust per content brief) |

---

## Tier × Pillar coverage map (sanity check)

| Pillar | T1 Envisioning | T2 Build | T3 Managed Run |
|---|---|---|---|
| 1 Business Strategy | A1, A2, B4, C16, C19, D1 | — | A4, D3 |
| 2 Org & Culture | A3, A8, B6 | A8, B6, D1 | A4 |
| 3 AI Strategy & Experience | A1–A7, B1, B3, B4, B7, C1, C9, C10, C16, C19 | A3, B2, B5, C2–C5, C18 | A4, C18 |
| 4 Tech & Data | C6–C8, C11, C14 | B5, C2–C5, C11, C17, C18 | C12, C18 |
| 5 Governance & Security | A6, B7, C6, C13, C15 | A8, B6, C2, C17 | A4, C12, C13, D3 |
| +1 Co-sell & Partner | D1 (partner archetype mapping) | All MAICPP-funded items (B2, B5, C2–C5, D1) | — |

Coverage is dense at T1+T2 and across pillars 3–5; T3 (Managed Run) is comparatively thin and is the right place for partner-MSP (Tier-3) handoff per the content-brief 3-tier ladder.

---

## Pre-mortem — what could be wrong with this list 6 months out

1. **Catalogue churn.** FY26 H2 → FY27 transition will rename or retire 3–6 of these SKUs; A4, A5, A8, B2, B7, C4, C8 are flagged `VERIFY` because they are on the moving edge. Re-pull MCAPS Catalog before each customer commit.
2. **Funding-instrument substitution.** The Azure Accelerate funding tables (slide 11 in `ato-content.md`) are FY26 H2 rates and T-shirt sizes; the partner-nominated vs Microsoft-field-nominated split and the per-scenario % uplift are the highest-volatility numbers in this appendix — verify on `aka.ms/AzureAccelerate` before quoting.
3. **CSU-vs-partner ownership.** Several rows (C18, B2, B5, D1) are listed as CSU-owned because the CSA orchestrates the engagement, but actual hands-on-keyboard delivery is regularly subcontracted to an MAICPP partner. The "owner" column reflects MCEM-stage accountability, not delivery labour.
4. **Sandbox limitation.** This appendix was compiled without internet access; entries A1–A8, B1–B7, C6–C15, D2 reflect training-data knowledge as of 2025-05 and have not been re-verified against today's MCAPS Catalog. ATO entries (C16–C19) and Frontier CoE pillar entries (D1) are HIGH trust because they are sourced from the user's own internal grounding files.

---

## Conclusion

The CSU-deliverable AI VBD landscape, viewed through the **5+1 pillar × 3-tier CoE ladder** lens, is well-covered for **Tier 1 Envisioning** and **Tier 2 Build** across all three CSU sub-teams, with the **AI Transformation Offer (ATO)** acting as the keystone end-to-end engagement that spans pillars 1–5 and tiers 1–2. **Tier 3 Managed Run** is intentionally thin in the CSU catalogue — it is where the partner ladder (MSP archetype, Frontier CoE Tier-3) takes the relay, consistent with the content-brief two-stream model.

For RSA CSU operationalization, the recommended customer-facing shortlist is:

- **Inspire & Design (MCEM 1–2):** A1, A2, A6, B1, B4, C9, C16 (ATO C1)
- **Empower & Achieve (MCEM 3):** A3, A8, B2, C2/C3/C5, C11, C17 (ATO C2), C18 (ATO C3)
- **Realize & Optimize (MCEM 4–5):** A4, C12, C13, D3

This shortlist is what the CSA team should operate as the standard "VBD menu" inside the AI CoE artefact pack — with full re-verification on MCAPS Catalog before each customer commit.

---

## Named Accelerators (RSA CoE IP)

These are the named, packaged accelerators the RSA CoE leads with — competitors lead with named IP (Accenture **AI Refinery**, Deloitte **Atlas AI**, BCG **GENE**, Cognizant **Neuro AI**, TCS **WisdomNext**, Infosys **Topaz**, Wipro **ai360**); we lead with these.

Each accelerator follows: **ID** · purpose · MCEM stage · pillar(s) · funding stack · time-box · partner-deliverable y/n · artefact link.

### ACC-1 — RSA Banking Customer-Service Agent Pattern
- **Purpose:** Reference architecture + Copilot Studio + Foundry Agent Service pattern for tier-1 customer-service automation in SA banks (SARB / FSCA-regulated).
- **MCEM:** 3 → 4 (Build & Land)
- **Pillars:** P3 AI Strategy & Experience, P4 Tech & Data, P5 Governance & Security
- **Funding stack:** ATO $250–500K (ACO + ECIF), partner MAICPP for build
- **Time-box:** 8–12 weeks pilot → 16 weeks scale
- **Partner-deliverable:** Yes (MAICPP build partner)
- **Artefact:** [`accelerators/acc-1-banking-cx-agent.md`](accelerators/acc-1-banking-cx-agent.md)

### ACC-2 — POPIA-Compliant Foundry Landing-Zone Blueprint
- **Purpose:** Bicep/Terraform landing-zone for Azure AI Foundry in SA North / SA West with POPIA, PFMA, Purview AI Hub, Defender for Cloud AI baked in. Deployable in <2 weeks.
- **MCEM:** 2 → 3 (Design & Build foundations)
- **Pillars:** P4 Tech & Data, P5 Governance & Security
- **Funding stack:** Cloud Accelerate Factory (F1, F3, F4) at $0
- **Time-box:** 2 weeks
- **Partner-deliverable:** No (Microsoft Factory delivered)
- **Artefact:** [`accelerators/acc-2-popia-landing-zone.md`](accelerators/acc-2-popia-landing-zone.md)

### ACC-3 — M365 Copilot Adoption Playbook for SOEs
- **Purpose:** SOE-tailored Copilot adoption motion — change-management, sponsor coalition, PFMA cost-justification template, AGSA-ready audit trail. Drop-in for Eskom-class customers.
- **MCEM:** 4 → 5 (Land & Realise Value)
- **Pillars:** P1 Business Strategy, P2 Org & Culture, P5 Governance & Security
- **Funding stack:** ATO $150–250K + Copilot Adoption Acceleration
- **Time-box:** 12-week wave (cohorts of 250–500 seats)
- **Partner-deliverable:** Yes (Change-management partner)
- **Artefact:** [`accelerators/acc-3-copilot-soe-adoption.md`](accelerators/acc-3-copilot-soe-adoption.md)

### ACC-4 — Regulated-Industry Pilot Kit (POPIA / PFMA / NERSA)
- **Purpose:** Reusable controls + workshop + risk register for any SA-regulated entity running its first GenAI pilot. Eskom-tested, generalised.
- **MCEM:** 2 → 3 (Envision & Design)
- **Pillars:** P5 Governance & Security, P3 AI Strategy & Experience
- **Funding stack:** ATO Pre-sales ECIF $50K + Factory F6 (Governance)
- **Time-box:** 4-week workshop + 8-week pilot
- **Partner-deliverable:** Optional (Microsoft-led or partner-led)
- **Artefact:** [`accelerators/acc-4-regulated-pilot-kit.md`](accelerators/acc-4-regulated-pilot-kit.md)

### ACC-5 — Document Intelligence + Foundry Pattern (Claims / Permits / KYC)
- **Purpose:** Reference pattern combining Document Intelligence (formerly Form Recognizer), Foundry agents, and human-in-the-loop review for high-volume regulated document workflows. KPIs in time-to-decision and FTE-recovery terms.
- **MCEM:** 3 → 4 (Build & Land)
- **Pillars:** P3 AI Strategy & Experience, P4 Tech & Data
- **Funding stack:** ATO $300–600K + partner MAICPP
- **Time-box:** 10-week pilot (single document type) → 6-month scale
- **Partner-deliverable:** Yes (Build partner, often vertical SI)
- **Artefact:** [`accelerators/acc-5-docintel-foundry-pattern.md`](accelerators/acc-5-docintel-foundry-pattern.md)

> **How to use these:** Lead the CSA pitch with the accelerator that maps to the customer's first use-case — not with the pillar framework. The pillars are how we *check coverage*; accelerators are how we *open the conversation*.

---

## Sources

1. `/mnt/workspace/working/content-brief.md` — AI CoE offering content brief, 5+1 pillar definition, MCEM mapping, content-pack scope (HIGH trust — author Yuri Baijnath).
2. `/mnt/workspace/working/ato-content.md` — AI Transformation Offer slide deck export (slides 1–15) covering ATO components, deliveries-at-a-glance, governance/role clarity, and Azure Accelerate funding tables (HIGH trust — Microsoft internal slides).
3. `/mnt/workspace/input/FY26 H2 Copilot Execution.xlsx` — FY26 H2 Copilot execution motions (referenced for A5 Copilot Chat & Agents Workshop) (`VERIFY` — not opened in this pass).
4. `/mnt/workspace/input/Frontier CoE - Business Strategy.PPTX`, `… Organization & Culture.PPTX`, `… AI Strategy & Experience.PPTX`, `… Technology & Data Strategy.PPTX`, `… AI Governance & Security.PPTX` — Frontier CoE pillar decks (HIGH trust — Microsoft internal Frontier CoE assets, source for D1 and pillar definitions).
5. `/mnt/workspace/grounding/downloads/Datasheet AI Agents Center of Excellence COE_English.pdf` — present in grounding but rights-protected and not openable in this sandbox; user has direct access (re-read internally).
6. `/mnt/workspace/.memories/notes/sources-ai-coe-pitch-stats.md` — Source registry from the prior pitch-stats research thread (HIGH trust — for cross-reference of stats only, not VBDs).
7. Microsoft public references (training-data, 2025-05 cutoff — MODERATE trust, re-verify on MCAPS Catalog):
   - Azure Accelerate offer page — `aka.ms/AzureAccelerate`
   - MCAPS Solution Assessment Catalog (internal)
   - Microsoft Learn — Cloud Adoption Framework for AI / Azure Essentials AI workload
   - Microsoft Learn — Azure AI Foundry, Microsoft Fabric, Power Platform CoE Starter Kit, AI Builder
   - M365 Copilot Adoption Hub — `adoption.microsoft.com/copilot`
   - Copilot Studio partner workshop — `aka.ms/CopilotStudioWorkshop`
   - Microsoft Responsible AI Standard v2
   - MAICPP partner program — `partner.microsoft.com/maicpp`

**Verification methodology:** SIFT applied to grounding files (HIGH trust — internal Microsoft authorship, recent dates, corroboration across files); Chain-of-Verification applied to ATO funding numbers (cross-checked between slide 11 and slide 12 of `ato-content.md` — values match: $50K pre-sales ECIF, $1M post-sales = $500K ECIF + $500K ACO, ECIF 1:5 / 1:2 ratios). Adversarial pass surfaced 4 residual risks captured in the Pre-mortem.

**Limitations disclosure:** This appendix was compiled in a sandboxed environment without live partner-portal access. The user (CSU Cloud & AI Lead, South Africa) has direct internal access and should re-verify FY26 H2 entries flagged `VERIFY` against MCAPS Catalog before any customer commit. The list is intended as a starting reference, not a single source of truth.
