"""Add speaker notes to every slide of AI-CoE-VBD-Reference-Deck.pptx.

Additive only: opens the existing deck, writes notes_text_frame content per
slide (creating the notes slide on demand via python-pptx), and saves back to
the same file. Slide shapes, layouts, and order are untouched.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation

DECK = Path(__file__).parent / "AI-CoE-VBD-Reference-Deck.pptx"

# One entry per slide. Index 0 == Slide 1. First item in each list becomes the
# notes header paragraph; remaining items become bullet paragraphs.
NOTES: list[list[str]] = [
    # S1 - Title
    [
        "Slide 1 - Title / opener.",
        "Greet the room. Introduce yourself: Yuri Baijnath, Senior CSA Manager, RSA CSU, Microsoft South Africa.",
        "Set the deck's purpose in one line: a single, opinionated menu of every AI VBD a CSA can run, mapped to outcomes, CoE pillars, and MCEM stages.",
        "Frame the audience: CSAs, CSAMs, STUs, and partner sellers who need to translate VBD names into customer outcomes.",
        "Caveat up front: VERIFY-flagged items (marked with *) must be re-checked on the MCAPS Catalog before any customer commit - the catalog evolves quarterly.",
        "Source of truth: csu-ai-vbd-reference-report.md (the long-form companion to this deck).",
        "Time-box: this is a 25-slide dense reference - skim live, deep-read offline.",
    ],
    # S2 - Agenda
    [
        "Slide 2 - Agenda.",
        "Walk the eight blocks: 01 Why this deck; 02 The framing (5+1 pillars x 3 tiers x MCEM 1-5); 03 Family A - M365 Copilot (MW), 8 VBDs (A1-A8); 04 Family B - Copilot Studio + Power Platform (BA), 7 VBDs (B1-B7); 05 Family C - Foundry + Data + Apps (CAI), 19 VBDs (C1-C19); 06 Factory engine - 10 zero-cost plays (F1-F10); 07 Cross-CSU spine (D1-D3); 08 Synthesis and next steps.",
        "Signal pace: blocks 03-05 are the heaviest - expect 2-3 slides per family covering full menu plus a spotlight.",
        "Encourage interruptions on Family C - that is where most CSA pipeline lives.",
    ],
    # S3 - Why this deck
    [
        "Slide 3 - Why this deck.",
        "Lead with the problem stats: McKinsey 2025 - 88% of enterprises use AI but only 1 in 3 has scaled it; BCG 2024 - 60% of AI programs report little or no measurable value, and only ~1/3 of employees are trained on the tools they have.",
        "Translate: VBD names alone (e.g. 'Innovate with AI', 'Agents to Action') do not articulate the customer outcome - CSAs end up reinventing the pitch.",
        "What this deck does: lists every VBD with its outcome and the CoE pillar(s) it contributes to; maps each VBD to the 5+1 x 3-tier model; sequences delivery against MCEM 1-5; and flags FY26 H2 VERIFY items so we do not over-commit.",
        "Punchline: turn a fragmented catalog into one menu that a CSA can use in front of a customer tomorrow.",
    ],
    # S4 - The framing
    [
        "Slide 4 - The framing.",
        "Six pillars (5+1): 1 Business Strategy; 2 Organisation and Culture; 3 AI Strategy and Experimentation; 4 Technology and Data; 5 Governance and Security; +1 Co-sell and Partner. Every VBD contributes to one or more of these - that is how CoE value gets credited.",
        "Three tiers of delivery: T1 Envisioning - workshops, assessments, ATO Checkpoint 1; T2 Build - Azure Accelerate engagements, ATO Checkpoints 2 and 3; T3 Managed Run - GenAIOps, MSP relay, partner-led operate.",
        "MCEM 1-5 strip: Listen / Inspire (1), Envision (2), Design (3), Empower (4), Realize (5). Each VBD has a sweet-spot MCEM stage - that is how we sequence them in a pursuit.",
        "Mental model: pick the pillar -> pick the tier -> sequence on MCEM. Everything else in the deck is a lookup.",
    ],
    # S5 - VBD landscape
    [
        "Slide 5 - VBD landscape (one page).",
        "Five surfaces, 40+ plays: Family A - M365 Copilot (MW), 8 VBDs A1-A8; Family B - Copilot Studio and Power Platform (BA), 7 VBDs B1-B7; Family C - Foundry, Data, and Apps (CAI), 19 VBDs C1-C19; D-bis - Cloud Accelerate Factory, 10 zero-cost plays F1-F10; D - Cross-CSU spine, 3 motions D1-D3.",
        "Factory caveat: F1-F10 are zero-cost to the customer but require either active Unified Support OR a signed 2-page Factory agreement - do not promise without one of those in place.",
        "This single slide is the print-and-pin reference. Most customer conversations start by pointing at one card.",
    ],
    # S6 - How to read each VBD card
    [
        "Slide 6 - How to read each VBD card.",
        "Every VBD entry has six columns: Outcomes (what the customer gets); CoE contribution (which pillar(s) it advances); MCEM (sweet-spot stage 1-5); Funding instrument (ECIF, AMM, MAICPP, ACO, SA, or customer-funded); Owner (CSA / partner / STU); and the VERIFY flag (*).",
        "Funding cheatsheet: ECIF = pre-sales Azure consumption credits; AMM = AI Migration and Modernization; MAICPP = Microsoft AI Cloud Partner Program; ACO = Azure Consumption Offer; SA = Software Assurance.",
        "Asterisk (*) = re-verify on MCAPS Catalog this quarter. Do not commit without re-checking.",
        "Reading rhythm: scan Outcomes column first; then check funding to see if it is fundable; then check MCEM to know when to introduce it in the pursuit.",
    ],
    # S7 - Family A menu (M365 Copilot - MW)
    [
        "Slide 7 - Family A menu: M365 Copilot (MW), 8 VBDs A1-A8.",
        "Owned by the Modern Work (MW) solution area. Outcomes orbit knowledge-worker productivity, content creation, meeting intelligence, and Copilot-in-the-flow-of-work.",
        "Use this menu when the customer's lead question is 'how do my employees use AI day to day?' rather than 'how do I build an AI product?'",
        "Funding pattern: most A-family plays pair with ECIF for envisioning and Software Assurance benefits for adoption activation.",
    ],
    # S8 - Family A spotlight
    [
        "Slide 8 - Family A spotlight.",
        "Deep-dive one or two A-family VBDs that the room cares about (typical picks: Copilot Chat envisioning, Copilot adoption / value realization).",
        "Highlight the CoE contribution: A-family plays disproportionately advance Pillar 2 (Org and Culture) and Pillar 1 (Business Strategy) - this is where change management meets AI.",
        "MCEM sweet spot: Envision (2) and Empower (4). Pair with the Skilling spine (D2) for stickiness.",
    ],
    # S9 - Family B menu (Copilot Studio + PP - BA)
    [
        "Slide 9 - Family B menu: Copilot Studio + Power Platform (BA), 7 VBDs B1-B7.",
        "Owned by the Business Applications (BA) solution area. Outcomes orbit low-code agents, line-of-business process automation, and Copilot extensibility.",
        "Use this menu when the customer wants custom copilots or agents grounded on their data but does not yet want a full Foundry build.",
        "Funding pattern: BA plays often combine ECIF (envisioning) with MAICPP-funded partner build, especially for sector templates (FSI, retail, public sector).",
    ],
    # S10 - Family B spotlight
    [
        "Slide 10 - Family B spotlight.",
        "Spotlight VBDs typically: Agents-to-Action and Copilot Studio agent build.",
        "Position B-family as the bridge between MW (out-of-the-box Copilot) and CAI (full Foundry custom builds) - many customers land here first.",
        "CoE contribution: heavy on Pillar 3 (AI Strategy and Experimentation) and Pillar 4 (Technology and Data); MCEM sweet spot Design (3) to Realize (5).",
    ],
    # S11 - Family C menu (Foundry + Data + Apps - CAI)
    [
        "Slide 11 - Family C menu: Foundry + Data + Apps (CAI), 19 VBDs C1-C19.",
        "Owned by Cloud and AI (CAI). The largest and most heterogeneous family - covers Innovate-with-AI, Build-and-Modernize-AI-Apps, AI-ready data platforms, app modernization, and the full Foundry stack.",
        "Use this menu when the customer wants a custom AI product, an agentic application, or a data foundation for AI.",
        "Funding pattern: ECIF -> AMM -> ACO chain is the standard path. Most C-family pursuits also draw on Azure Accelerate engagements in the build phase.",
    ],
    # S12 - Family C spotlight (Innovate with AI)
    [
        "Slide 12 - Family C spotlight: Innovate with AI.",
        "Innovate-with-AI is the flagship envisioning play for CAI - it produces a customer-specific AI use-case backlog ranked by value and feasibility.",
        "CoE contribution: advances Pillar 1 (Business Strategy) and Pillar 3 (AI Strategy and Experimentation) simultaneously - rare in the catalog.",
        "MCEM 2 (Envision). Funding: ECIF. Typical follow-on: an Azure Accelerate engagement to build the top-ranked use case.",
    ],
    # S13 - Family C spotlight (Build & Modernize AI Apps)
    [
        "Slide 13 - Family C spotlight: Build and Modernize AI Apps.",
        "The default build engagement for any customer with an envisioned use case ready to go to production.",
        "Couples Foundry (models, agents, eval) with Azure App Platform (Container Apps, App Service, AKS) and the AI-ready data platform (Fabric, Cosmos DB, AI Search).",
        "MCEM 3-5 (Design / Empower / Realize). Funding: AMM and ACO. Usually a partner-led delivery with CSA oversight.",
    ],
    # S14 - ATO HIGH-TRUST
    [
        "Slide 14 - ATO HIGH-TRUST checkpoints.",
        "ATO = Architecture Tollgate / Adoption-To-Operate review. Three checkpoints: C1 (after envisioning), C2 (after architecture and security review), C3 (pre-go-live operational readiness).",
        "HIGH-TRUST means the CSA signs off that the design follows Well-Architected and Responsible AI standards.",
        "Use ATO to lock customer expectations and to qualify pursuits for AMM or ACO funding - many funding desks ask for ATO C2 sign-off as evidence of design maturity.",
    ],
    # S15 - Factory engine (F1-F10)
    [
        "Slide 15 - Cloud Accelerate Factory: 10 zero-cost plays F1-F10.",
        "Factory = Microsoft-delivered, partner-supported, fixed-scope deployments at zero cost to the customer when entitlement is in place.",
        "Entitlement gate: customer must have active Unified Support OR sign a 2-page Factory agreement. Without one of those, do NOT promise Factory.",
        "Use Factory to remove friction on foundational deployments (landing zone, AKS, AI Search, Fabric, Foundry workspace) so the customer's spend goes to the value workload, not the plumbing.",
    ],
    # S16 - Factory engine integration
    [
        "Slide 16 - How Factory plugs into a pursuit.",
        "Pattern: T1 envisioning surfaces the use case -> Factory deploys the foundational platform (F-play) at no cost -> T2 build engagement delivers the value workload on top.",
        "This is how a CSA stretches limited ECIF dollars - Factory absorbs the platform setup so funding instruments cover only the differentiated build.",
        "Always sequence Factory BEFORE the paid build engagement, never after.",
    ],
    # S17 - Delivery stack
    [
        "Slide 17 - Delivery stack.",
        "Three layers feed every pursuit: (1) the VBD catalog (what we sell); (2) the delivery instruments - workshops, Azure Accelerate, GenAIOps, MSP relay (how we deliver); (3) the funding instruments - ECIF, AMM, MAICPP, ACO, SA (how we fund).",
        "A pursuit is the product of one VBD x one delivery instrument x one (or more) funding instrument(s). Mismatches kill deals.",
        "Use this slide as a sanity check when reviewing a pursuit: name the VBD, name the delivery, name the funding. If any is missing, the pursuit is not ready.",
    ],
    # S18 - Cross-CSU spine (D1-D3)
    [
        "Slide 18 - Cross-CSU spine: D1 Frontier CoE, D2 Skilling, D3 Value Realization.",
        "These three motions sit across all three families and across the entire CSU - they are not owned by a single solution area.",
        "D1 Frontier CoE: pattern reuse, reference architectures, IP harvesting from customer engagements.",
        "D2 Skilling: customer and partner enablement (Cloud Skills Challenges, Hack Together, AI Tour) - critical for stickiness on A-family Copilot adoption.",
        "D3 Value Realization: instrumented outcome tracking post-go-live; this is what wins renewal and expansion.",
    ],
    # S19 - Tier x Pillar map
    [
        "Slide 19 - Tier x Pillar map.",
        "Matrix view: rows = the 3 delivery tiers (T1/T2/T3), columns = the 5+1 pillars. Each cell shows which VBDs land there.",
        "Look for gaps: pillars with few VBDs in T3 (Managed Run) often indicate where MSP partners or GenAIOps must fill in.",
        "Use this matrix in account planning to spot 'pillar overweight' - customers buying lots of T2 builds with no T1 envisioning or T3 run plan are at risk of stalled value.",
    ],
    # S20 - Family contribution synthesis
    [
        "Slide 20 - Family contribution synthesis.",
        "Synthesised view of how each family loads the six pillars: A-family carries Org and Culture; B-family carries Business Strategy through process automation; C-family carries AI Strategy, Tech and Data, and Governance.",
        "Co-sell and Partner (+1) is loaded primarily by D3 Value Realization and by Factory (D-bis).",
        "Use this view to explain to a customer why one family is not enough - real CoE maturity requires plays from at least two families plus the Cross-CSU spine.",
    ],
    # S21 - MCEM-stage shortlist
    [
        "Slide 21 - MCEM-stage shortlist.",
        "If you only remember one VBD per stage: MCEM 1 (Listen) - D3 Value Realization conversation; MCEM 2 (Envision) - C-family Innovate-with-AI or A-family Copilot envisioning; MCEM 3 (Design) - ATO C2 plus Azure Accelerate engagement; MCEM 4 (Empower) - Skilling (D2) plus Copilot adoption; MCEM 5 (Realize) - GenAIOps plus D3 instrumented outcomes.",
        "Use this list when a deal review asks 'what is the next best action for this customer?' - map them to MCEM stage, then pick from the shortlist.",
    ],
    # S22 - Pre-mortem: 4 risks
    [
        "Slide 22 - Pre-mortem: four risks that kill AI pursuits.",
        "Risk 1 - No envisioning: customer skips T1 and goes straight to build; outcome drifts, value cannot be measured.",
        "Risk 2 - No data foundation: build starts before AI-ready data is in place; pilots fail in production.",
        "Risk 3 - No governance: Responsible AI and security are bolted on at the end; ATO C2 fails, go-live slips.",
        "Risk 4 - No value tracking: D3 is skipped; customer cannot articulate ROI at renewal.",
        "Hand-rule: if a pursuit lacks an answer for any one of these four risks, pause and add the missing VBD before continuing.",
    ],
    # S23 - Five next steps
    [
        "Slide 23 - Five next steps.",
        "1. Print and pin slide 5 (the VBD landscape) - it is your daily lookup.",
        "2. For every active opportunity, name the VBD, the delivery instrument, and the funding instrument before the next deal review.",
        "3. Re-verify all (*)-flagged items on MCAPS Catalog this quarter.",
        "4. Schedule a Family C deep-dive with your CAI specialist team - that is where most pipeline gain is available.",
        "5. Add D3 Value Realization to every pursuit at MCEM 1 - do not wait until Realize stage.",
    ],
    # S24 - Sources & verification
    [
        "Slide 24 - Sources and verification.",
        "Long-form companion: csu-ai-vbd-reference-report.md (in the repo root) - contains the full evidence base, with trust grades per claim.",
        "Trust grades used in the report: A (Microsoft official source or MCAPS Catalog); B (analyst report - McKinsey, BCG, Gartner); C (Microsoft blog or session); * VERIFY (must re-check on MCAPS Catalog).",
        "Cadence: re-verify VERIFY items quarterly. Re-pull McKinsey / BCG numbers annually.",
        "If you see a claim in this deck that contradicts MCAPS Catalog today, MCAPS Catalog wins - and please ping me so I can update the source report.",
    ],
    # S25 - Close
    [
        "Slide 25 - Close.",
        "Anchor phrase: 'Outcomes over offerings.' VBDs are the means; pillar-aligned, MCEM-sequenced, funded delivery is the end.",
        "Numbers to remember walking out: 40+ VBDs across 5 surfaces; 5+1 pillars x 3 tiers; ATO at 3 checkpoints; D3 from MCEM 1.",
        "Call to action: pick one customer this week, name the VBD / delivery / funding triple, and book the next conversation. That is how this deck pays for itself.",
        "Thank the room. Offer to share the source report and to pair on one live pursuit.",
    ],
]


def main() -> None:
    if not DECK.exists():
        raise SystemExit(f"Deck not found: {DECK}")

    prs = Presentation(str(DECK))

    if len(prs.slides) != len(NOTES):
        raise SystemExit(
            f"Slide count mismatch: deck has {len(prs.slides)} slides, "
            f"NOTES has {len(NOTES)} entries"
        )

    total_paragraphs = 0
    for idx, (slide, paragraphs) in enumerate(zip(prs.slides, NOTES), start=1):
        if not paragraphs:
            continue
        tf = slide.notes_slide.notes_text_frame
        # First paragraph: set on the existing paragraph (do not add a blank one).
        tf.text = paragraphs[0]
        for line in paragraphs[1:]:
            tf.add_paragraph().text = line
        total_paragraphs += len(paragraphs)
        print(f"  Slide {idx:>2}: {len(paragraphs)} paragraphs")

    prs.save(str(DECK))
    print(
        f"\nSaved {DECK.name}: {len(prs.slides)} slides, "
        f"{total_paragraphs} notes paragraphs total."
    )


if __name__ == "__main__":
    main()
