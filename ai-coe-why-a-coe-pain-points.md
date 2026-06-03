---
title: "Why an AI CoE — the 13 buyer pain points"
author: "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft"
version: "1.0"
date: "2026-06-03"
audience: "C-suite (CEO, CFO, CIO, CISO, CDO, COO) — first conversation"
purpose: "Single customer-facing artefact that names every pain point an AI CoE exists to solve, with the CoE response and the proof artefact for each."
---

# Why an AI CoE — the 13 buyer pain points

## Lead message

You do not have an AI problem. You have **thirteen AI problems**, and they compound. Most enterprises in South Africa have addressed two or three in isolation — a pilot here, a policy there, a Copilot deployment somewhere else — and discovered that the unaddressed ten quietly cancel the value of the three that worked.

An **AI Centre of Excellence** is the operating capability that collapses all thirteen into a single delivery, governance, and measurement system. It is not a team, a tool, or a slide; it is the set of rituals, controls, and reusable patterns that turn AI from a portfolio of disconnected bets into a compounding capability.

This document names the thirteen pain points, in the language we hear them in the room, and points to the artefact in the Microsoft AI CoE pack that closes each one.

---

## The 13 pain points, grouped

The pain points sort into four buckets that map directly to the CoE's 5+1 pillars.

| Bucket | # | Pillar | Owner role |
|---|---|---|---|
| Strategy & ROI | 1–4 | Pillar 1 — Business Strategy | CEO / CFO |
| People & Adoption | 5–8 | Pillar 2 — Org & Culture | CHRO / COO |
| Tech & Data | 9–11 | Pillars 3 & 4 — AI Strategy + Tech & Data | CIO / CDO |
| Governance & Risk | 12–13 | Pillar 5 — Governance & Security | CISO / Risk |

Pillar +1 (Co-sell & Partner) shows up in how the CoE is *delivered*, not as a standalone pain point — partner choice is a lever, not a wound.

---

## Bucket 1 — Strategy & ROI (CEO / CFO)

### Pain 1 — Pilot purgatory

**What we hear:** *"We've run twelve proofs-of-concept. None of them are in production. Every executive review starts with the same slide."*

**Why it hurts:** Cost without compounding. Pilot budgets recur annually; benefits do not. Executive patience expires before the third refresh cycle.

**CoE response:** A funded path from pilot to platform — the F1–F10 factory pattern, with a Tier-2 (mid) and Tier-3 (frontier) router that turns pilots into reusable building blocks instead of disposable demos.

**Proof artefact:** `AI-CoE-Pitch-Deck-Respined.pptx` slides 4–6 (moat grid, factory) · `AI-CoE-VBD-Reference-Deck.pptx` (the 25-VBD menu replaces ad-hoc pilots).

---

### Pain 2 — ROI is unproven

**What we hear:** *"Show me the business case. I cannot defend per-seat Copilot to the CFO without a number."*

**Why it hurts:** Without a defensible ROI model, AI competes against every other capex line on instinct, and instinct loses to a spreadsheet.

**CoE response:** A unit-economics TCO model that the CFO can re-run with their own inputs — not a vendor slide. Industry-anchored $1 : $3–$5 benchmark, with the assumptions visible.

**Proof artefact:** `AI-CoE-AI-TCO-Calculator.xlsx` (7-sheet model) · Pitch-Deck-Respined slide 9 (ATO economics).

---

### Pain 3 — Build-vs-buy paralysis

**What we hear:** *"Do we build this internally with our team, buy it from an ISV, or wait for Microsoft to ship it as a feature?"*

**Why it hurts:** The wrong answer costs 18 months. Build-internally underestimates the eval + governance + change effort. Buy-from-ISV creates a fourth surface to govern. Wait-for-feature misses the window.

**CoE response:** A repeatable decision frame — Build (factory pattern, sovereign data, durable IP) · Buy (commodity workflow, vendor owns the eval) · Wait (feature is on a known roadmap inside 2 quarters). The CoE owns the call, not the LOB.

**Proof artefact:** `AI-CoE-Objection-Handling.pptx` Pillar 1 (build-vs-buy objection) · `AI-CoE-Model-Choice-OnePager.docx` (when not to multi-model).

---

### Pain 4 — Wait-and-see

**What we hear:** *"The tech is moving too fast. We'll wait for it to stabilise before we invest."*

**Why it hurts:** Waiting is a position, not a neutral. Competitors who started in 2024 now have proprietary evals, change muscle, and reusable patterns. The cost of catching up in 2027 exceeds the cost of starting in 2026.

**CoE response:** A 90-day landing pattern that produces evidence, not infrastructure — one funded VBD, one platform pattern, one governance attestation. The CoE is designed so that "wait" becomes the more expensive option after the first quarterly review.

**Proof artefact:** `AI-CoE-Horizon-Assessment.xlsx` (where you sit vs RSA peers) · `AI-CoE-Pitch-Deck-Respined.pptx` slides 14–16 (90-day landing).

---

## Bucket 2 — People & Adoption (CHRO / COO)

### Pain 5 — Shadow AI sprawl

**What we hear:** *"My CISO tells me 40% of our knowledge workers are already pasting customer data into ChatGPT. We have no visibility and no policy that holds."*

**Why it hurts:** POPIA exposure, IP leakage, and a governance position that is unenforceable by the time you write it.

**CoE response:** Sanctioned alternatives (M365 Copilot, Foundry-hosted chat under tenant controls), Purview DLP on consumer-AI endpoints, and a Champions network that pulls usage onto the sanctioned surface faster than policy pushes it off the unsanctioned one.

**Proof artefact:** `AI-CoE-Sovereign-AI-RSA-Report.md` (Purview controls) · `AI-CoE-Change-Readiness-Workbook.xlsx` (Champions ratio target 1:25).

---

### Pain 6 — Skills gap

**What we hear:** *"We don't have prompt engineers. We don't have ML engineers. We don't have AI product managers. Where do we hire from?"*

**Why it hurts:** The local talent market for senior AI roles is thin. Building inside takes 9–12 months. Outside hires turn over in 14.

**CoE response:** A role ladder the CoE itself enables — prompt engineer (built from BAs in 6 weeks), Copilot Studio maker (built from power users in 4 weeks), Foundry engineer (built from senior dev in 12 weeks). Microsoft Learn paths, Champions enablement kit, and partner co-delivery cover the gap.

**Proof artefact:** `AI-CoE-Change-Management-Methodology.md` (Champions kit) · `AI-CoE-How-To-Use.pptx` (role enablement).

---

### Pain 7 — Change fatigue

**What we hear:** *"We just rolled out SAP S/4, we're mid-migration on the data platform, and the COO told finance there are no more transformations this year."*

**Why it hurts:** Every prior transformation makes the next one harder. AI initiatives launched into change-fatigued organisations land at 12% adoption, not 60%, and the CFO writes off the licences.

**CoE response:** ADKAR-based readiness scoring **before** broad-launch, with Green / Amber / Red gates. Amber means proceed with a 30-day pre-launch plan; Red means do not broad-launch — run a 90-day fixture programme first. The CoE protects adoption rate by refusing to launch into a Red.

**Proof artefact:** `AI-CoE-Change-Readiness-Workbook.xlsx` (5-dimension rubric, auto-banded) · `AI-CoE-Change-Management-Methodology.md`.

---

### Pain 8 — Adoption stall

**What we hear:** *"We bought 8,000 Copilot licences. Six months in, 1,400 are active and the CFO wants to cancel the renewal."*

**Why it hurts:** Licence cost is fixed; value scales with active use. A 17% activation rate destroys the business case on the next renewal.

**CoE response:** A 5-KPI measurement scaffold — three activity-leading (active users, prompts/user, scenario coverage), two outcome-lagging (hours-saved per role, quality lift). Weekly Champions ritual that closes the loop between usage data and use-case backlog.

**Proof artefact:** `AI-CoE-Change-Management-Methodology.md` (5-KPI scaffold) · `AI-CoE-Operating-Playbook.docx` (rituals).

---

## Bucket 3 — Tech & Data (CIO / CDO)

### Pain 9 — Data is not ready

**What we hear:** *"Our data is in 47 systems, nobody trusts the customer master, and the data lake is read-only because the lineage is broken. AI on top of that is fiction."*

**Why it hurts:** AI quality is a function of data quality. Bad inputs produce hallucinations that the business correctly does not trust, which kills adoption faster than any change-management failure.

**CoE response:** A data-readiness gate inside the F1–F10 factory pattern — every use case is scored Green / Amber / Red on data fitness before build starts. Fabric + Purview as the platform pattern; the CoE refuses to build on data graded Red.

**Proof artefact:** `AI-CoE-GenAIOps-Reference.docx` (L4 Data layer) · `AI-CoE-VBD-Reference-Deck.pptx` (data-foundation VBDs).

---

### Pain 10 — Integration debt

**What we hear:** *"The use case is obvious — but it needs to call SAP, write to ServiceNow, and read from the mainframe. The integration cost is bigger than the AI cost."*

**Why it hurts:** AI value lives in workflows, not chat. Workflows live in systems-of-record built in 2008. The integration line item silently doubles the project.

**CoE response:** Copilot Studio + Logic Apps + the agent registry pattern — connectors for SAP, ServiceNow, Dynamics, mainframe, and 1,400+ pre-built endpoints. The CoE owns a reusable integration library so the second use case pays a fraction of the first one's tax.

**Proof artefact:** `AI-CoE-VBD-Reference-Deck.pptx` slides on Copilot Studio agents · `AI-CoE-Pitch-Deck-Respined.pptx` slide 10 (Studio deep-dive).

---

### Pain 11 — Surface confusion

**What we hear:** *"M365 Copilot, Copilot Studio, Azure AI Foundry — what's the difference and which one do we buy?"*

**Why it hurts:** The wrong surface choice produces the right capability in the wrong place. Six months of build on Foundry that should have been a Copilot Studio agent. A Studio agent that needs the data plane of Foundry. The cost is rework.

**CoE response:** A single decision frame — M365 Copilot for productivity at the desktop, Copilot Studio for low-code agents on workflows, Azure AI Foundry for custom build with full model choice and data-plane control. The CoE makes the call per use case and prevents shopping by department.

**Proof artefact:** `AI-CoE-Pitch-Deck-Respined.pptx` slides 9–11 (three-surface moat grid) · `AI-CoE-Model-Choice-OnePager.docx`.

---

## Bucket 4 — Governance & Risk (CISO / Risk)

### Pain 12 — Governance debt

**What we hear:** *"We have a Responsible AI policy. It's in a SharePoint deck. The regulator asked us to demonstrate it in controls and we couldn't."*

**Why it hurts:** Policy without controls is slideware. AGSA, SARB, FSCA, and the Information Regulator increasingly ask for evidence, not assertion. The quarterly attestation gap is now a regulator-graded risk.

**CoE response:** Five lifecycle gates — G-Build · G-Eval · G-Release · G-Monitor · G-Retire — wired into Foundry, Purview, and Azure AI Content Safety. Every agent in production has an evidence trail the regulator can sample. Quarterly attestation is a report, not a project.

**Proof artefact:** `AI-CoE-Responsible-AI-Governance.md` · `AI-CoE-GenAIOps-Reference.docx` (L6 Governance layer) · `AI-CoE-Eskom-Executive-Briefing.pptx` (regulated-industry template).

---

### Pain 13 — Sovereignty / POPIA / data residency

**What we hear:** *"The data must stay in South Africa. The CISO needs to demonstrate it. And the model weights must not leak to a US-hosted endpoint we don't control."*

**Why it hurts:** Sovereignty is no longer an objection — it is a procurement gate. SA North and SA West regions, Foundry-hosted OpenAI in-region, Phi and Mistral as sovereign-friendly defaults, and Azure Local for the hardest cases all need to be on the table from slide one.

**CoE response:** A three-tier sovereignty pattern — Microsoft-managed posture in SA region (default), customer-controlled weights on AKS (sensitive), on-customer-premise via Azure Local (extreme). The CoE specifies which tier per workload and produces the residency evidence.

**Proof artefact:** `AI-CoE-Sovereign-AI-RSA-Report.md` · `AI-CoE-Pitch-Deck-Respined.pptx` slide 12 (sovereignty) · `AI-CoE-Eskom-Executive-Briefing.pptx`.

---

## The compounding argument

Each pain point in isolation is solvable. Many enterprises have solved two or three.

The reason an **AI CoE** exists is that the *combination* of all thirteen — running concurrently, across business, technology, and governance — exceeds the operating capacity of any line-of-business team, any single platform team, and any one vendor relationship.

The CoE is the seam. It owns the rituals (Pillar 1–2), the patterns (Pillar 3–4), the controls (Pillar 5), and the partner motion (Pillar +1). Stand it up once, and the marginal cost of the fourteenth use case approaches zero.

That is the offer.

---

## How to use this document

| You are… | Read… |
|---|---|
| Preparing a first executive meeting | The whole document, in order — it sequences the conversation. |
| Briefing a single C-suite role | The bucket for that role + the proof-artefact links. |
| Responding to a specific objection | Find the pain point that contains it; hand the prospect the linked artefact. |
| Building the business case | Pain 2 → TCO Calculator. Pain 8 → 5-KPI scaffold. Pain 12 → attestation evidence. |

---

## Linked artefacts (full pack)

- `AI-CoE-Pitch-Deck-Respined.pptx` — the full pitch; slide 2 now enumerates these 13 pain points.
- `AI-CoE-Customer-Pitch-Respined.pptx` — 5-slide outside-in version.
- `AI-CoE-VBD-Reference-Deck.pptx` — 25 ready-to-run VBDs.
- `AI-CoE-Objection-Handling.pptx` — internal seller reference for the harder follow-ups.
- `AI-CoE-AI-TCO-Calculator.xlsx` — unit economics, CFO-runnable.
- `AI-CoE-Horizon-Assessment.xlsx` — where you sit vs N=20 RSA peer cohort.
- `AI-CoE-Change-Readiness-Workbook.xlsx` — ADKAR-anchored Green/Amber/Red.
- `AI-CoE-Change-Management-Methodology.md` — Champions + 5-KPI scaffold.
- `AI-CoE-Model-Choice-OnePager.docx` — multi-model surface decision.
- `AI-CoE-GenAIOps-Reference.docx` — 6-layer architecture, 5 lifecycle gates.
- `AI-CoE-Responsible-AI-Governance.md` — RAI controls and quarterly attestation.
- `AI-CoE-Sovereign-AI-RSA-Report.md` — POPIA, residency, three-tier sovereignty.
- `AI-CoE-Eskom-Executive-Briefing.pptx` — regulated-industry template.
- `AI-CoE-Operating-Playbook.docx` — internal delivery rituals.
- `AI-CoE-How-To-Use.pptx` — seller / CSA enablement.
