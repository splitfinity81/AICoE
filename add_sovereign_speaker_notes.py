"""Add speaker notes to every slide of AI-CoE-Sovereign-AI-RSA.pptx.

Additive only: opens the existing deck, writes notes_text_frame content per
slide, saves back to the same file. Shapes, layouts, order untouched.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation

DECK = Path(__file__).parent / "AI-CoE-Sovereign-AI-RSA.pptx"

NOTES: list[list[str]] = [
    # S1 - Title
    [
        "Slide 1 - Title / opener.",
        "Greet the room. Introduce yourself: Yuri Baijnath, CSU Cloud & AI Lead (South Africa), Microsoft.",
        "Frame the deck in one sentence: a productised Sovereign-AI offer for RSA regulated customers, taking the conversation from slide-caveats to a signed pilot gate.",
        "Audience: RSA CoE, ATU sellers, regulated-customer sponsors, partner CSAs. This deck is the field-facing artefact; the long-form report (ai-coe-sovereign-ai-rsa-report.md) is the source of truth.",
        "Quarterly verification reminder: anything region-specific or service-availability-specific must be re-checked on aka.ms/AzureRegions before any customer commit.",
    ],
    # S2 - Why this offer exists
    [
        "Slide 2 - Why this offer exists.",
        "Anchor: sovereignty in RSA has moved from a checkbox to a deal qualifier. SOEs, banks, insurers, large public-sector buyers no longer accept 'the data stays in Azure' - they want a named offer with named controls.",
        "Competitive context: Capgemini sells 'Sovereign Cloud for AI'; Atos/Eviden, Thales, Orange Business publish sovereign-AI catalogues. Microsoft fielding only caveats loses the architecture review before it starts.",
        "The customer-side trigger: AGSA, SARB, FSCA, Information Regulator reviews are explicit about residency, controls, and operating model. The CISO/DPO/Internal Audit triad needs an artefact they can sign against.",
        "Position this deck as the answer to: 'Show me a productised sovereign-AI offer I can take to my CISO.'",
    ],
    # S3 - What we sell
    [
        "Slide 3 - What we sell.",
        "Five components - emphasise that this is ONE offer with five named pieces, not a menu the customer assembles themselves.",
        "Residency commitment: SA North + SA West, evidenced via Azure Policy + Purview lineage. Not a verbal promise - a policy-enforced control.",
        "Governance posture: Purview AI Hub + Defender for Cloud AI + Sentinel connector + Azure Policy initiative, all wired day 1. This is what ACC-2 (POPIA Landing Zone) delivers.",
        "Control crosswalk: the single most valuable artefact. One matrix mapping our controls to POPIA, PFMA, NERSA, SARB Directive 7, FSCA, AGSA, ISO/IEC 42001, NIST AI RMF, EU AI Act. CISOs love this because it lets them map one control once and discharge it across eight frameworks.",
        "Operating model: RACI customised per customer, covering Microsoft, the customer's CISO/DPO/IA, and the partner.",
        "Artefact pack: board-ready summary, regulator-facing brief, audit evidence template, kill-switch run-book - the customer keeps these.",
    ],
    # S4 - Three sovereignty dimensions
    [
        "Slide 4 - The three sovereignty dimensions.",
        "Customers conflate three different concerns. Your job is to separate them on the whiteboard - because each has a different control set and a different owner.",
        "Data sovereignty: at rest, in flight, in vector indexes, in logs. The simplest and most-understood. Anchor: POPIA section 72 list governs cross-border. Foundry data-zone scoping enforces in-region.",
        "Operational sovereignty: SA-based support, in-region operations, customer-controlled keys (CMK via Key Vault HSM), customer-controlled break-glass. Microsoft global support routed only on customer consent.",
        "Decision sovereignty - the most overlooked, and the one that wins the architecture review. The customer retains decision authority over what the AI does: owns system prompts, approves the model catalogue (no shadow models), exposes reasoning trace to internal audit, holds the kill-switch, gets quarterly attestation that no model behaviour changed without notice.",
        "Walking a CISO through all three with named controls under each is the difference between 'interesting' and 'signed'.",
    ],
    # S5 - Region posture
    [
        "Slide 5 - Region posture (SA North + SA West).",
        "The honest availability picture. Do NOT over-promise. If a service is 'partial' or 'EU/US', say so on the slide and document it in the offer.",
        "Foundry: GA progressing - verify quarterly. SA North is the primary anchor today.",
        "M365 Copilot: tenant-region determines processing. For SA tenants today this is typically EU. This is the most common 'gotcha' - lead with it; don't let the customer find it themselves.",
        "Purview AI Hub, Defender for Cloud AI, Document Intelligence: in-region. These are the day-1 governance plane.",
        "Quarterly attestation discipline: re-verify on aka.ms/AzureRegions before any customer commit. Write the verification date on every customer-facing version of this slide.",
    ],
    # S6 - M365 Copilot honest answer
    [
        "Slide 6 - M365 Copilot - the honest answer.",
        "The single most common objection from regulated buyers: 'M365 Copilot processes in EU, so you're not sovereign.' Correct for M365 Copilot today. Pretending otherwise destroys credibility.",
        "What to say: M365 Copilot prompts and responses aren't stored long-term, transit is encrypted, tenant data is not used to train models. EU Data Boundary commitments apply.",
        "What to offer: for the DEEPEST sovereignty posture on sensitive workloads, route via Azure AI Foundry in SA regions through Copilot Studio agents - not directly via M365 Copilot. This is the architecture that converts the objection.",
        "Coaching: this slide is what regulated customers respect us for. The competitor sells 'sovereign AI' on the slide and then can't deliver. We name the gap and give the customer the workaround.",
    ],
    # S7 - Control crosswalk
    [
        "Slide 7 - Control crosswalk (master matrix).",
        "The single most useful artefact in this offer. One Microsoft control discharges across up to eight frameworks. The CISO maps once.",
        "Walk two or three rows live: data residency -> POPIA s72, ISO 42001 A.6.2, NIST GOVERN-1.3, EU AI Act Art. 10. CMK encryption -> POPIA s19, PFMA s45, ISO 42001 A.8.24, EU AI Act Art. 15.",
        "The full matrix lives in AI-CoE-AI-Impact-Assessment.xlsx (governance pack). This deck shows the excerpt; the spreadsheet is the per-use-case working artefact.",
        "Coaching: if a CISO pushes back on a single control, find the row, point to the eight columns it satisfies, and ask which framework they want to start with. Reframes a defence into a sequencing conversation.",
    ],
    # S8 - Operating model
    [
        "Slide 8 - Operating model (RACI).",
        "The artefact that converts the customer's CISO + DPO + Internal Audit from blockers into co-owners. Each gets a named row.",
        "Microsoft: architecture authority, region availability changes (12-month notice), quarterly attestation pack, incident L3.",
        "Customer CISO: policy ownership, control attestation sign-off, kill-switch authority. This last point matters - the kill-switch sits with THEM, not us.",
        "Customer DPO: POPIA DPIA owner, cross-border transfer approver, subject-access response.",
        "Customer Internal Audit: quarterly evidence review, AGSA liaison.",
        "Partner: day-to-day operations, L1/L2 incident response, change-request execution. Builds the partner into the offer rather than bolting them on.",
        "Customise the RACI per customer in the workshop - do not ship the generic version into production.",
    ],
    # S9 - Engagement shape
    [
        "Slide 9 - Engagement shape and commercials.",
        "Four phases, named funding for each. Removes the 'what does this cost' friction in meeting one.",
        "Envision workshop (4 weeks, $50K ECIF): crosswalk tailored to the customer, gap analysis, regulator-correspondence pack drafted.",
        "Landing-zone deploy (2 weeks, Cloud Accelerate Factory $0): ACC-2 in SA North. This is the proof point that we can move fast on the platform.",
        "Pilot (8-12 weeks, $250-500K ATO + partner): first production workload + audit evidence pack. KPIs in time-to-decision and FTE-recovery terms, not 'accuracy %'.",
        "Quarterly attestation (ongoing, customer-funded): re-verify controls, region availability, model catalogue. This is the recurring artefact AGSA cares about.",
        "Always link to ACC-2 (Landing Zone) and ACC-4 (Regulated-Industry Pilot Kit) in the customer pack - they are the delivery scaffolding behind this commercial shape.",
    ],
    # S10 - What this is NOT
    [
        "Slide 10 - What this is NOT.",
        "Three explicit disclaimers. Naming them up-front is what makes the rest of the offer credible.",
        "Not air-gapped. We do not operate Azure Stack Edge / disconnected scenarios under this SKU. If the customer needs air-gap, that's a different conversation (and likely a different SKU).",
        "Not a workaround for services not yet GA in SA. Where a service is missing, this offer documents the gap and the customer's risk acceptance - it does not pretend coverage.",
        "Not a substitute for the customer's own POPIA compliance programme. We provide the controls; the customer remains the responsible party under POPIA.",
        "Coaching: if the customer presses on any of these three, the answer is 'correct, and here's what we'd do instead' - not a defensive reframe.",
    ],
    # S11 - Counter-objections
    [
        "Slide 11 - Counter-objections (the four that always land).",
        "M365 Copilot processes in EU - correct for M365 Copilot today; for deep-sovereignty workloads we route via Foundry in SA. This offer makes that explicit, not implicit.",
        "You can't promise in-region forever - correct; we commit to quarterly attestation and 12-month notice on region changes via the operating model. The discipline is the commitment.",
        "AGSA will reject this - AGSA reviews evidence, not vendor promises. The evidence template in the artefact pack is built to what an AGSA reviewer wants to see.",
        "EU AI Act for our multinational parent - the crosswalk includes EU AI Act categories; this offer is co-deployable with the EU Data Boundary commitments if the multinational parent needs both.",
        "Coaching: practise these four out loud before any first meeting. They land in 8 of 10 regulated pursuits.",
    ],
    # S12 - Linked artefacts
    [
        "Slide 12 - Linked artefacts.",
        "This offer does not stand alone - it lives inside the broader AI CoE pack.",
        "ACC-2 (POPIA Landing Zone): the platform foundation. Deploy this first - everything else assumes it.",
        "ACC-4 (Regulated-Industry Pilot Kit): the 4-week workshop and control library that scaffold the first pilot.",
        "AI Governance Playbook (AI-CoE-AI-Governance-Playbook.docx): the operating-model detail.",
        "AI Impact Assessment (AI-CoE-AI-Impact-Assessment.xlsx): the per-use-case crosswalk working tool - this is where the master matrix lives in full.",
        "Eskom Executive Briefing: reference customer narrative for SOE regulated buyers.",
        "Bring two or three of these into every meeting; don't try to walk all of them in one session.",
    ],
    # S13 - Sources
    [
        "Slide 13 - Sources.",
        "Every claim in this deck is backed by a public source. Sellers should be ready to cite the source if asked.",
        "aka.ms/AzureRegions - the canonical region/service map. Quarterly verification anchor.",
        "Microsoft Trust Center (Data Residency and Sovereignty) - the public commitment surface.",
        "Foundry Data Zone documentation - the technical control surface for in-region scoping.",
        "Microsoft Responsible AI Standard v2 - the internal control framework we map outward from.",
        "POPI Act, PFMA, NERSA Act, SARB Directive 7 - publicly available; do not paraphrase, cite the section number.",
        "ISO/IEC 42001:2023, NIST AI RMF 1.0, EU AI Act (Regulation 2024/1689) - international frameworks the crosswalk maps to.",
    ],
    # S14 - Close
    [
        "Slide 14 - Close.",
        "Anchor phrase: 'Sovereignty is a control set, not a slogan.' If we can't name the control, we don't claim the sovereignty.",
        "Three numbers to remember: 5 components (residency, governance, crosswalk, operating model, artefact pack); 3 sovereignty dimensions (data, operational, decision); 8 frameworks in the crosswalk.",
        "Call to action: pick one regulated pursuit this quarter, run the 4-week envision workshop, land ACC-2 in SA North, and put the signed pilot gate on the table by week 6.",
        "Thank the room. Offer to pair on one live regulated pursuit and to feed new control patterns back into the source report.",
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
