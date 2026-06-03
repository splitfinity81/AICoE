# AI Center of Excellence - Improvements Plan

**Author:** Review prepared for the RSA AI CoE offer team
**Scope:** Strategic & content-level improvements to the customer-facing and internal AI CoE artefact set
**Repo:** [`rsa_ai_coe`](https://github.com/yubaijna_microsoft/rsa_ai_coe)
**Date:** Original review cycle (superseded — see status note below)
**Status:** Historical snapshot — most recommendations have since been implemented

---

> **Status note (current cycle).** This document is a **historical snapshot** from
> an earlier review cycle and has been superseded by the current artefact set.
> When this plan was written, 9 of the 13 office artefacts were IRM-encrypted and
> could not be fully audited (see §2.2 below). All artefacts in the current repo
> are open OOXML and have been re-reviewed end-to-end. The majority of the Tier-1
> and Tier-2 recommendations in this plan — ATO economics, factory $0
> differentiator, $1:$3-5 services-to-ACR ratio, KPI scaffold, CTA, refreshed
> stats, three-stream model, partner motion, governance posture — are now
> reflected in the live artefacts (Pitch-Deck, Customer-Pitch, Eskom briefing,
> How-To-Use, Operating Playbook, Partner Recruitment Kit, Executive One-Pager,
> FY27 Launch Plan, RACI). Slide counts referenced below (e.g. Eskom briefing
> "9 slides") are also out of date — Eskom briefing is now **10 slides** and the
> Pitch-Deck is **19 slides**. Treat this file as **context for how the offer
> evolved**, not as an open work list.

---

## 1. Executive summary

The AI CoE offer is **strategically strong**: it has a defensible 5+1 Pillar framework, a credible delivery factory (F1-F10), a clear partner motion, ATO-aligned funding hooks, and proof points from NTT DATA + Capgemini. The Pitch-Deck (19 slides) and the Eskom Executive Briefing demonstrate that the offer can flex between horizontal and regulated-industry verticals.

The improvements below are organised in three tiers:

- **Tier 1 - Customer-facing alignment (HIGH).** The internal Pitch-Deck contains the strongest commercial assets (ATO economics, factory $0 differentiator, $1:$3-5 economics, KPI scaffold, CTA). Several of these are missing or under-played in the Customer-Pitch deck and the Eskom briefing.
- **Tier 2 - Portfolio breadth (HIGH).** The offer's "3 AI surfaces" framing is correct but understated. The user has flagged that the offer must be **"valid across all Microsoft offerings"** - Security Copilot, GitHub Copilot, D365 Copilots, Intune Copilot, Industry Clouds, Fabric, and Foundry agents - and the current artefacts under-represent that breadth.
- **Tier 3 - Governance, currency, and operational hygiene (MED/LOW).** Refresh stats, modernise governance posture (EU AI Act, ISO 42001), and tighten cross-deck consistency.

A consolidated table of all 14 themes appears in [§5](#5-improvement-themes-prioritised).

---

## 2. Methodology & limitations

### 2.1 Artefacts reviewed (fully captured)

| # | Artefact | Bytes | Coverage |
|---|---|---:|---|
| 1 | `ai-coe-pitch-stats-report.md` | 21,555 | 100% read |
| 2 | `csu-ai-vbd-reference-report.md` | 30,763 | 100% read |
| 3 | `AI-CoE-Pitch-Deck.pptx` | 682,132 | 19/19 slides extracted |
| 4 | `AI-CoE-Customer-Pitch.pptx` | 197,391 | 5/5 slides extracted |
| 5 | `AI-CoE-Eskom-Executive-Briefing.pptx` | 347,305 | 9/9 slides extracted |

### 2.2 Artefacts NOT reviewed (IRM-encrypted)

Nine artefacts are protected by Microsoft Information Protection / Azure RMS. The Office files are OLE2 compound containers with `EncryptedPackage`, `DataSpaces`, and `DRMEncryptedDataSpace` streams - i.e., the OOXML payload is sealed inside an encrypted package per `[MS-OFFCRYPTO]`. They cannot be opened or extracted programmatically without your IP-label authorisation.

| Artefact | Likely scope (inferred from filename) |
|---|---|
| `AI-CoE-Operating-Playbook.docx` | Internal delivery operating model |
| `AI-CoE-Delivery-RACI.docx` / `.xlsx` | Roles & accountabilities matrix |
| `AI-CoE-Executive-OnePager.docx` | Exec summary leave-behind |
| `AI-CoE-FY27-Launch-Plan.docx` | GTM launch plan |
| `AI-CoE-Horizon-Assessment.xlsx` | Customer maturity / horizon scoring |
| `AI-CoE-How-To-Use.pptx` | Internal enablement |
| `AI-CoE-Partner-Recruitment-Kit.pptx` | Partner GTM kit |
| `AI-CoE-Partner-Scorecard.xlsx` | Partner qualification scorecard |

**Implication for this plan.** The five readable artefacts cover the strategic core (offer narrative, economics, ATO funding, KPIs, delivery factory, partner archetypes, vertical instantiation). The nine encrypted artefacts are predominantly **tactical / operational** - RACI, FY plan, scorecards, how-to guides. Recommendations in §5 apply with confidence to the strategic surface. The Operational and Partner sections (§5.11-§5.14) should be re-validated once the encrypted artefacts are accessible.

**To unblock full review:** Open each encrypted file in Office (signed in with your account), remove the sensitivity label, save a copy, and the full content can be ingested.

---

## 3. What is working (preserve these)

These are the offer's strongest assets and should be retained / amplified - not changed:

1. **The 5+1 Pillar framework** (Strategy, Data & Platform, Engineering & MLOps, Adoption & Change, Governance & Risk + the integrating Operating Model). It is the right mental model and is consistent across all readable decks.
2. **Three AI surfaces taxonomy** - Copilot (out-of-box), Studio agents (low-code), Foundry agents (pro-code). This is a clean, defensible architecture story.
3. **The F1-F10 delivery factory with five quality gates** (Pitch-Deck S8). This is the single most differentiated and difficult-to-copy asset in the offer.
4. **ATO funding alignment** (Pitch-Deck S17 + VBD reference C16/C17/C18: $50K pre-sales ECIF + $1M post-sales ($500K ECIF + $500K ACO), 15% MoM AI ACR commitment). This is the commercial lever competitors lack.
5. **$1 : $3-5 economics** (Pitch-Deck S12). Strong, memorable, and tied to the factory.
6. **Proof points** - NTT DATA + Capgemini (Pitch-Deck S14).
7. **LEADING vs LAGGING KPI separation** (Pitch-Deck S15). This is unusual rigour and should be more visible.
8. **Eskom briefing as a vertical template** - POPIA / PFMA / NERSA + SA North/West residency + Purview AI Hub + the 8-12-week first-agent commitment is a reusable regulated-industry pattern.

---

## 4. Cross-Microsoft portfolio coverage gap

The user has explicitly stated that the AI CoE offer must be **"valid across all Microsoft offerings."** The current "3 AI surfaces" framing (Copilot / Studio / Foundry) is technically correct but is not exhaustive when read against Microsoft's commercial AI portfolio. The matrix below shows current artefact coverage vs. portfolio scope.

| Microsoft AI offering | Where it lives in the offer today | Gap |
|---|---|---|
| **M365 Copilot** | Explicit (3 AI surfaces) | None |
| **Copilot Studio** (Maker / low-code agents) | Explicit (3 AI surfaces) | None |
| **Azure AI Foundry** (pro-code agents, models, agent service) | Explicit (3 AI surfaces) | None |
| **GitHub Copilot** (developer productivity, Copilot Workspace, coding agent) | Implicit at best | **HIGH** - distinct buyer (CTO/VP Eng), distinct KPIs, distinct ROI model |
| **Security Copilot** | Not visible | **HIGH** - distinct buyer (CISO), distinct ATO motion, regulated-industry hook |
| **Dynamics 365 Copilots** (Sales, Service, Finance, Supply Chain) | Not visible | **MED** - biggest BDM/LoB beachhead |
| **Intune Copilot / Copilot for IT** | Not visible | **LOW-MED** - completes the IT-ops story |
| **Industry Clouds** (Financial Services, Healthcare, Sustainability, Sovereign) | Implicit in Eskom only | **MED** - regulated-industry compounding |
| **Microsoft Fabric + Data Agents** | Implicit in Pillar 2 | **MED** - the data foundation story |
| **Power Platform AI Builder / Power Automate AI flows** | Implicit in Studio | **LOW** - citizen-dev tail |
| **Azure OpenAI direct (model-only consumption)** | Implicit in Foundry | **LOW** - covered |

### Recommendation

Reframe the "3 AI surfaces" slide (Pitch-Deck S6) as a **"Microsoft AI offering coverage matrix"** with three columns:

1. **AI for the workforce** - M365 Copilot, Copilot Studio, D365 Copilots, Intune Copilot
2. **AI for the developer** - GitHub Copilot, Foundry agents, Fabric Data Agents
3. **AI for the regulated enterprise** - Security Copilot, Industry Clouds, Sovereign hosting, Purview AI Hub

This preserves the existing three-surface elegance, doesn't require restructuring the factory (F1-F10 still apply across all of these), and answers the user's "valid across all Microsoft offerings" requirement directly.

---

## 5. Improvement themes (prioritised)

| # | Theme | Priority | Effort | Where |
|---|---|---|---|---|
| 1 | Cross-Microsoft portfolio coverage | HIGH | M | §6.1 |
| 2 | Promote ATO economics into customer-facing decks | HIGH | S | §6.2 |
| 3 | Promote factory $0 differentiator into Customer-Pitch | HIGH | S | §6.3 |
| 4 | Promote $1:$3-5 economics into Customer-Pitch | HIGH | S | §6.4 |
| 5 | Add CTA slide to Customer-Pitch | HIGH | S | §6.5 |
| 6 | Modernise governance: EU AI Act + ISO 42001 + NIST AI RMF | HIGH | M | §6.6 |
| 7 | Surface LEADING/LAGGING KPIs in customer artefacts | MED | S | §6.7 |
| 8 | Surface proof points (NTT DATA, Capgemini) earlier | MED | S | §6.8 |
| 9 | Extract Eskom briefing into a reusable vertical template | MED | M | §6.9 |
| 10 | Clarify partner archetype gating ("M365 Copilot → Partner, NOT Factory") | MED | S | §6.10 |
| 11 | Surface ISD models A/B/C in Operating Playbook & Customer-Pitch | MED | S | §6.11 |
| 12 | Verify/refresh stats and date-stamp | LOW | S | §6.12 |
| 13 | Define "frontier organisation" explicitly | LOW | S | §6.13 |
| 14 | Brand, accessibility, versioning & footer hygiene | LOW | S | §6.14 |

Effort key: **S** ≤ 1 day, **M** 2-5 days, **L** > 1 week.

---

## 6. Theme detail & specific edits

### 6.1 Cross-Microsoft portfolio coverage (HIGH)

**Problem.** The user requires the offer to be "valid across all Microsoft offerings," but the readable decks index almost entirely on Copilot / Studio / Foundry. Security Copilot, GitHub Copilot, and D365 Copilots are essentially invisible.

**Specific edits:**

- **Pitch-Deck S6** - rename to "Microsoft AI coverage matrix" and replace the 3-surfaces graphic with the workforce / developer / regulated-enterprise grouping in §4 above.
- **Pitch-Deck S8 (Factory)** - add a column to the F1-F10 table showing which Microsoft offering each factory station has been validated against (e.g., F4 *Build* validated against M365 Copilot agents, Studio agents, Foundry agents, GitHub Copilot extensions, Security Copilot plugins).
- **Customer-Pitch** - add one slide between current S2 and S3 titled *"Where AI lives in your business today - and where Microsoft already has the answer"* showing the same matrix.
- **VBD reference report** - add an explicit cross-reference table mapping each VBD (A1-A8, B1-B7, C1-C19, F1-F10, D1-D3) to the Microsoft offering it primarily exercises.

### 6.2 ATO economics in customer-facing decks (HIGH)

**Problem.** Pitch-Deck S17 details the ATO motion ($50K ECIF pre-sales / $1M post-sales / 15% MoM AI ACR / VBDs C16-C17-C18). This is the **single most commercially compelling slide** in the entire pack. It does not appear in `AI-CoE-Customer-Pitch.pptx` and is only obliquely referenced in the Eskom briefing.

**Specific edits:**

- Port S17 into Customer-Pitch as a new slide titled *"How Microsoft co-invests in your AI journey."* Soften the internal-only language ("ECIF" → "Microsoft co-investment funding"; "ACR" → "consumption commitment") but keep the dollar figures and the 15% MoM growth target.
- Add the same slide (regionalised) to the Eskom briefing - POPIA-compliant residency + ATO co-investment is a powerful combination for state-owned regulated entities.

### 6.3 Factory $0 differentiator (HIGH)

**Problem.** Pitch-Deck S8 makes clear that customers do not pay for the F1-F10 factory tooling/IP - they only pay for the consumed Azure / M365 / GitHub services. This is a major competitive moat against Accenture/Deloitte/IBM Consulting and is **entirely absent** from the Customer-Pitch deck.

**Specific edits:**

- Add a Customer-Pitch slide titled *"The factory is on us - you pay for the AI, not the assembly line."*
- Include a side-by-side cost comparison: Big-4 advisory engagement (typical: $1.5M-$3M for a comparable scope) vs. AI CoE engagement ($0 factory + metered consumption).
- Cross-reference the $1:$3-5 economics from S12 (theme 6.4).

### 6.4 $1 : $3-5 economics in Customer-Pitch (HIGH)

**Problem.** Pitch-Deck S12 establishes that every $1 of Microsoft / partner services generates $3-5 of customer value over 18 months. The Customer-Pitch deck has no equivalent commercial argument.

**Specific edits:**

- Port S12 to Customer-Pitch with one customer-grounded example (use the NTT DATA or Capgemini proof point from S14 if cleared for external use; otherwise anonymise as "Tier-1 financial services client, 14-month engagement").
- Tie the slide directly to the LEADING/LAGGING KPIs of theme 6.7 so the customer sees how the ratio is measured.

### 6.5 Customer-Pitch needs a CTA slide (HIGH)

**Problem.** Pitch-Deck S19 closes with a 4-step CTA (executive briefing → horizon assessment → pilot → factory engagement) and an owner (Yuri.Baijnath@microsoft.com). The Customer-Pitch deck ends without a clear next step.

**Specific edits:**

- Add a final Customer-Pitch slide replicating S19's four-step CTA.
- Make step 2 ("Horizon Assessment") a free, 2-week, no-commitment offer. This converts more meetings than a generic "let's chat."
- Add the owner's email + a QR code linking to a calendaring page.

### 6.6 Modernise governance posture (HIGH)

**Problem.** The artefacts reference governance (Pillar 5) but the current scaffolding leans on POPIA / PFMA / NERSA (Eskom-specific) and generic "Responsible AI." For a portfolio-wide offer, the governance pillar must explicitly cover the international frameworks that customer GCs and CISOs are now asking about:

- **EU AI Act** (in force August 2024, prohibitions February 2025, GPAI obligations August 2025, high-risk full effect August 2026)
- **ISO/IEC 42001** (AI management system - first certifications appearing 2024-2025)
- **NIST AI RMF 1.0** + the **Generative AI Profile** (July 2024)
- **Microsoft Responsible AI Standard v2** mapping
- **Purview AI Hub + Defender for Cloud AI posture management** as the *enforcement* layer

**Specific edits:**

- Rebuild Pitch-Deck Pillar 5 content with a 4-quadrant graphic: International frameworks (EU AI Act / ISO 42001 / NIST) ↔ Microsoft tooling (Purview / Defender / Foundry guardrails / Content Safety) ↔ Regional regulation (POPIA / PFMA / sector regs) ↔ Customer governance (RACI / model card / DPIA process).
- Add a 1-slide governance summary to the Customer-Pitch deck.
- Update the Eskom briefing to lead with EU AI Act applicability (Eskom exports to neighbouring SADC grids; cross-border data flows trigger EU AI Act for some use cases).

### 6.7 LEADING vs LAGGING KPIs in customer artefacts (MED)

**Problem.** Pitch-Deck S15's separation of LEADING (adoption, prompt counts, agent usage) from LAGGING (revenue lift, cost-to-serve, NPS) is genuinely rare and should be a customer-visible differentiator.

**Specific edits:**

- Add the S15 KPI scaffold to Customer-Pitch as the slide immediately following the new economics slide (theme 6.4) - KPIs *justify* the $3-5 ratio.
- Cross-reference Eskom-specific KPIs (load-shedding minutes avoided, regulatory submission turnaround, employee tooling adoption %) in the Eskom briefing.

### 6.8 Proof points earlier (MED)

**Problem.** Pitch-Deck S14 (NTT DATA + Capgemini) appears late. In customer meetings, proof of execution should arrive **before** detailed economics.

**Specific edits:**

- In Customer-Pitch, move proof points to slide 2 or 3 (immediately after the stats slide).
- Expand each proof point with: scope, duration, three measurable outcomes, and named senior sponsor (if cleared).
- Add at least one **regulated-industry** proof point (banking, public sector, healthcare) - currently both proof points read as horizontal/IT-services flavoured.

### 6.9 Eskom briefing as a reusable vertical template (MED)

**Problem.** The Eskom briefing is exceptionally well-tailored (POPIA, PFMA, NERSA, SA North/West residency, 8-12 week first agent). It is a wasted asset if it remains Eskom-only.

**Specific edits:**

- Extract a "Regulated Industry Briefing Template" with placeholder fields: `{Regulator}`, `{Privacy law}`, `{Data residency region}`, `{Sovereign hosting requirement Y/N}`, `{Sector-specific KPI set}`.
- Build three pre-filled instances:
  - Public sector / utilities (Eskom is the reference)
  - Financial services (FSCA / SARB / Basel III / DORA for EMEA clients)
  - Healthcare (HPCSA / HIPAA-equivalent / pharmacovigilance)
- Store them in the repo under `templates/vertical-briefings/`.

### 6.10 Partner archetype gating (MED)

**Problem.** The 4 Partner Archetypes (Pitch-Deck S10) + the 3-Tier Ladder (S11) imply a routing logic - *"M365 Copilot agent work routes to Partner, not Factory"* - but this rule is not stated explicitly anywhere readable.

**Specific edits:**

- Add a one-line gating rule to S10: *"Default routing: M365/D365 Copilot Studio agent work → Partner tier ladder; Foundry pro-code agent work → Factory. Hybrid engagements → joint."*
- Reflect the same gate in the Operating Playbook (currently IRM-encrypted; revisit when accessible).

### 6.11 ISD models A/B/C (MED)

**Problem.** Pitch-Deck S18 details three optional Integrated Service Delivery models (A/B/C) but they're internal-only. Customers asking "how do you actually staff this with us?" get no clear answer.

**Specific edits:**

- Surface a customer-friendly version in Customer-Pitch: *"Three ways to engage - Embedded (we sit with you), Federated (we co-locate, you lead), Advisory (we coach your CoE)."*
- Cross-reference in the (encrypted) Operating Playbook - revisit when accessible.

### 6.12 Verify and refresh stats (LOW)

**Problem.** `ai-coe-pitch-stats-report.md` instructs the team to *retire* 99% / 60% / 33% / 79% and lead with BCG 5×/3×, McKinsey 88%, ⅔-not-scaling, ⅓-trained, BCG 60%-no-value, 5%-future-built. Need to confirm:

- All decks (Pitch-Deck S2, Eskom briefing) use the *new* stats and have purged the retired figures.
- Each statistic has a footnote with source + publication year.
- The dataset is < 18 months old where possible (BCG/McKinsey AI surveys are refreshed annually).

**Specific edits:**

- Audit pass across all 5 readable decks.
- Add a `/stats-bibliography.md` to the repo with citation entries.

### 6.13 Define "frontier organisation" (LOW)

**Problem.** The term "frontier organisation" / "future-built 5%" appears in stats messaging but is not operationally defined. Customers will ask *"Are we one?"*

**Specific edits:**

- Add a 5-criterion definition (e.g., AI in P&L, executive AI literacy, agent operations capability, governance maturity, talent strategy).
- Add a 1-slide self-scoring rubric to the (encrypted) Horizon Assessment - revisit when accessible.

### 6.14 Brand, accessibility, versioning (LOW)

- Add a version footer (e.g., `v1.2 · FY25Q4 · MS Confidential`) to every slide.
- Run an accessibility check (alt text, colour contrast ≥ 4.5:1, table reading order).
- Confirm consistent typography across all decks (the Customer-Pitch and the Pitch-Deck appear to use slightly different title fonts on visual inspection of embedded assets).
- Add a `CHANGELOG.md` to the repo for the artefact set.

---

## 7. Quick wins (≤ 2 weeks)

These are the highest-leverage, lowest-cost edits and should ship first:

1. **Port ATO + factory $0 + $1:$3-5 + CTA from Pitch-Deck into Customer-Pitch** (themes 6.2, 6.3, 6.4, 6.5). One afternoon's work. Materially upgrades the customer deck.
2. **Rename the "3 AI surfaces" slide to the Microsoft AI coverage matrix** (theme 6.1). Half a day. Closes the user's explicit "valid across all Microsoft offerings" gap.
3. **Insert proof-point slide #2 into Customer-Pitch** (theme 6.8).
4. **Add `templates/vertical-briefings/` folder with three regulated-industry briefing templates** (theme 6.9).
5. **Audit stats currency** (theme 6.12).

---

## 8. Strategic improvements (≤ 8 weeks)

1. **Modernise the governance pillar** (theme 6.6) - requires legal/compliance review and Purview / Defender / Foundry guardrails mapping.
2. **Reconcile and republish the 9 encrypted artefacts** with a consistent sensitivity-label policy that still permits reviewability inside the offer team.
3. **Build a Microsoft-portfolio coverage scorecard** (theme 6.1) where each VBD is tagged to specific Microsoft offerings; publish in the VBD reference report.
4. **Add a fourth proof point from a regulated-industry engagement** (theme 6.8).
5. **Add Microsoft-Fabric-Data-Agent as an explicit fourth AI surface** if pursued strategically (decision needed).

---

## 9. Open questions for the offer owner

1. **IRM remediation.** Will you re-save the 9 encrypted artefacts without the sensitivity label so the operational layer can be reviewed (RACI, Operating Playbook, FY27 Launch Plan, Horizon Assessment, Partner Scorecard)? Or should those be reviewed in a live working session?
2. **Portfolio scope.** Is GitHub Copilot in scope for the AI CoE? It has a distinct buyer (VP Eng/CTO) and a separate adoption motion. Including it materially expands the offer; excluding it leaves a visible portfolio hole.
3. **Industry verticals.** Beyond utilities (Eskom), which 2-3 verticals should the offer pre-build briefing templates for in FY25/FY26? Recommended: financial services, healthcare, public sector.
4. **Partner gating.** Confirm the "M365 Copilot agent work → Partner not Factory" rule - is that the actual routing logic, or is it scenario-specific?
5. **Proof-point clearance.** Are the NTT DATA and Capgemini proof points cleared for external use in Customer-Pitch? If not, what is the named-customer pipeline?
6. **Frontier-organisation definition.** Is there an existing internal definition we should adopt, or do we need to author one (theme 6.13)?
7. **Governance frameworks.** Confirm priority order: EU AI Act > ISO 42001 > NIST AI RMF > regional (POPIA / PFMA / sector). Or different?

---

## 10. Suggested next actions

| Step | Action | Owner | Timing |
|---|---|---|---|
| 1 | Review & ratify this plan; answer §9 open questions | Offer owner | Week 1 |
| 2 | Unblock the 9 IRM-encrypted artefacts | Offer owner | Week 1 |
| 3 | Ship the 5 quick wins (§7) | Content lead | Weeks 1-2 |
| 4 | Modernise governance pillar (§6.6) | Governance lead + Legal | Weeks 2-5 |
| 5 | Build vertical briefing templates (§6.9) | Industry leads | Weeks 3-6 |
| 6 | Republish full artefact set v2.0 + CHANGELOG | Offer owner | Week 8 |

---

## 11. Update log — 2026-06-03 (P2 execution)

Issues #7, #8, #9, #10 landed in a single execution pass:

- **#7 (Commercial archetypes)** — `AI-CoE-Operating-Playbook-Addendum.docx` published as standalone companion (parent playbook is MIP-protected). Four named archetypes: per-resolved-case, per-document-processed, per-hour-recovered, gain-share. Each with baseline, measurement, partner role, MAICPP/ECIF treatment, exit terms, typical price floor. Cross-refs objection 1.1 and the TCO calculator.
- **#8 (TCO / FinOps calculator)** — `AI-CoE-AI-TCO-Calculator.xlsx` shipped with 7 sheets. Pricing reference editable; inputs editable; per-token Foundry forecast composes from users × queries × tokens × model-mix × (1+retry+fallback) × cache adjustment. Per-seat M365 vs per-token Foundry comparison sheet. Three pre-loaded scenarios. WAF cost-optimisation principle binding.
- **#9 (Pitch re-spine)** — `ai-coe-pitch-respine-spec.md` documents the new spine: lead with the three-surface × three-stream **moat grid** (slide 3 = anchor), pillars demoted to coverage checklist (slide 18). Shipped as `AI-CoE-Pitch-Deck-Respined.pptx` (22 slides) and `AI-CoE-Customer-Pitch-Respined.pptx` (5 slides). Promotes to primary file names after three live customer meetings + CSU sign-off.
- **#10 (Sector verticalisation)** — Six 9-slide briefings published using the Eskom briefing as the template: Banking & Insurance, Retail, Telco, Mining, Public Sector / SOE, Healthcare. Each names regulators, three top use-cases, anonymised RSA reference, ATO sizing, and matching accelerators.

This pass closes the highest-leverage P2 themes (commercial flexibility, unit economics, customer-facing spine, sector specificity). P3 themes (frontier-organisation positioning, governance framework re-ordering, partner-margin transparency) remain open.

---

*End of plan.*
