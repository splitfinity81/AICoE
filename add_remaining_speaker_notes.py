"""Add speaker notes to AI CoE decks that are missing them.

Targets the decks the existing add_*_speaker_notes.py scripts don't cover:

  - AI-CoE-Customer-Pitch-Respined.pptx (5 slides)
  - AI-CoE-Pitch-Deck-Respined.pptx (22 slides)
  - AI-CoE-Sector-Briefing-*.pptx (6 decks, 9 slides each)

Sector briefings share a fixed 9-slide spine, so notes are generated from a
template with the sector name parsed from each deck's title slide. The two
respined pitch decks get bespoke per-slide notes keyed by slide index.

Idempotent: overwrites existing notes, so the script is safe to re-run after
the build scripts are regenerated.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.util import Pt

ROOT = Path(__file__).parent


# --------------------------------------------------------------------------- #
# Bespoke notes for the respined pitch decks
# --------------------------------------------------------------------------- #

CUSTOMER_PITCH_RESPINED: list[str] = [
    # Slide 1 — title
    "Opening. Frame the 25 minutes: we will not present 5+1 pillars. We will present a 3x3 moat (three AI surfaces times three funding streams) that only Microsoft can fill in RSA, and the four asks that turn ambition into a funded programme. Confirm the named exec sponsor in the room.",
    # Slide 2 — moat grid
    "The core slide. Walk the grid left-to-right: M365 Copilot, Copilot Studio, Azure AI Foundry. Then top-to-bottom on the funding streams: MCAPS-sponsored landing, zero-cost Factory, partner build-run via MAICPP. Land that no hyperscaler or SI fills all nine cells in RSA. This is the moat.",
    # Slide 3 — ATO economics
    "Show the funding spine. For every $1 of ACR commitment, Microsoft plus partner-funded delivery returns $3-5 in landed value through ECIF, MCI, MAICPP and Factory hours. ATO is not a discount; it is the engine that funds the first three production use cases.",
    # Slide 4 — operating model
    "One CoE, three surfaces, three streams, four gates (G1 Envision, G2 Pre-pilot, G3 Pre-production, G4 Attestation). Emphasise the gates: every use case is registered, impact-assessed, RAI-controlled, and quarterly-attested. This is how we scale without losing the plot on risk.",
    # Slide 5 — the ask
    "Close with the four asks. We do not need a strategy phase. We need: one named exec sponsor; one measurable baseline; one Azure Consumption commitment to anchor ATO; one 90-day window to ship outcomes. If the room can commit to those four asks today, we send the engagement letter this week.",
]


PITCH_DECK_RESPINED: list[str] = [
    # 1 title
    "Opening. This is the long-form pitch behind the short customer deck. 45-60 minutes with executive sponsor and senior leaders. The arc: 13 pain points -> 3x3 moat -> ATO economics -> operating model -> 90-day outcomes -> four asks -> governance and references.",
    # 2 pain points
    "Anchor in the customer's reality. 13 pain points sorted by persona (CEO/CFO/CIO/CRO/CDO). Ask the room which three resonate most. Their answer chooses which surfaces and use cases lead the engagement. Do not pitch the moat until they have named their pain.",
    # 3 moat
    "Now the moat. Three AI surfaces by three funding streams = nine cells. Make the point firmly: AWS does not have M365 surface; Google has Workspace below 15% in RSA enterprise; SI partners have no equivalent of MCAPS or Factory. Microsoft fills all nine cells.",
    # 4 competitive read
    "Walk the competitive landscape explicitly. Do not be defensive. Each competitor wins a slice. Microsoft wins the whole grid because the moat is a combination, not a feature. Use the table to answer 'why not AWS / why not Accenture' before they ask.",
    # 5 ATO economics
    "ATO is the funding spine. One Azure Consumption commit unlocks ECIF for landing, Factory hours for build, MAICPP for partner scale. Show the $1 -> $3-5 ratio. Customer CFOs respond to leverage; this is the slide to land.",
    # 6 operating model
    "The CoE charter, RACI, three surfaces, three streams, four gates. Emphasise the four gates as the audit-ready spine. Show governance is built in, not bolted on. This unlocks the regulated buyers (banks, insurers, public sector).",
    # 7 90-day outcomes
    "Three concrete outcomes per surface in 90 days. Every outcome is measurable; every cost is modelled in the TCO calculator. Avoid abstraction. Pick the surface their pain points map to and walk the outcome they will ship by day 90.",
    # 8 the ask
    "The four asks. One sponsor, one baseline, one ACR commit, one 90-day window. Repeat at every milestone. If the room cannot commit, we are not pitching the right level - escalate or de-scope.",
    # 9 Surface 1 deep
    "Surface 1: M365 Copilot. Economics ($30/user/month, ACO offsets ACR), adoption curve, T&M measurement methodology. Adoption is the variable that determines ROI; the SOE Adoption Playbook is the asset that moves the curve. Quote the RSA reference cohort.",
    # 10 Surface 2 deep
    "Surface 2: Copilot Studio. Four agent patterns cover ~85% of first-agent demand: intent-routing, document, process, analytics. Show containment ranges (40-60% by month 3). Anchor on the HITL queue - this is what makes the agent trustworthy.",
    # 11 Surface 3 deep
    "Surface 3: Azure AI Foundry. Build-and-run platform with RAI guardrails. Walk the 5-layer reference (experience, orchestration, reasoning, data/grounding, governance). Stress the model mix - cost-and-latency routing matters at scale. This is where Foundry beats single-model alternatives.",
    # 12 Factory
    "Stream 2: the F1-F10 Factory. Zero-cost-to-customer engineering through Microsoft delivery. Walk F1 Envision through F10 Attestation. Factory hours are funded; the customer commits Azure Consumption and a sponsor; we bring the engineers.",
    # 13 MAICPP
    "Stream 3: partner build-run via MAICPP. RSA partner shortlist is 12 named. MAICPP funds partner envisioning, build, deploy, adoption. The CoE governs; the partner executes. This is how we scale beyond what Microsoft can deliver directly.",
    # 14 sovereignty
    "Sovereign AI for regulated buyers. Three dimensions: data residency, operational sovereignty, digital sovereignty. SA North + SA West regions; CMK in customer Key Vault; Purview lineage. For the full offer point to AI-CoE-Sovereign-AI-RSA.pptx and the ACC-2 POPIA Landing Zone.",
    # 15 governance & gates
    "Four gates plus the control plane. G1 registers the use case; G2 selects controls and signs the impact assessment; G3 stands up the eval harness, HITL queue, kill-switch and Purview AI Hub; G4 is the quarterly attestation. Governance is the spine, not a tax.",
    # 16 KPIs
    "KPI scaffold. Adoption, value, risk, cost/FinOps. Every quarter the CoE reports against these four families. If a use case cannot be measured on this scaffold, it does not earn another quarter of investment.",
    # 17 references
    "References. NTT DATA and Capgemini on the global SI side; anonymised RSA tier-1 bank and SOE. Use the bank reference for regulated buyers, the SOE reference for public sector, NTT/Capgemini for partner-led customers. Always offer a peer-reference call.",
    # 18 5+1 appendix
    "Appendix only. The 5+1 Pillars are how the CoE confirms an engagement covers the surface area - they are not the customer-facing spine. If a buyer asks for the pillars view, this is the checklist.",
    # 19 ladder appendix
    "Appendix: the 3-tier CoE ladder. T1 Foundational (0-6 months), T2 Scaling (6-18 months), T3 Industrialised (18+ months). Stress: climb only as far as the value hypothesis justifies. T3 is not the goal; the goal is durable value.",
    # 20 verticals appendix
    "Appendix: six sector briefings (Banking, Insurance, Telco, Retail, Healthcare, Mining, Public Sector). Each is a 9-slide deck naming regulators, top 3 use-cases, anonymised RSA reference, ATO sizing. Hand the right one to the buyer at the right moment.",
    # 21 commercials appendix
    "Appendix: commercial archetypes. Per-resolved-case, per-document, per-hour-recovered, gain-share. These are the conversation starters for risk-share commercial conversations once a baseline exists.",
    # 22 artefacts
    "Closing reference. The pack at a glance: customer-facing artefacts, governance artefacts, internal delivery, economics. Make sure the room leaves with the next-step artefact they need - usually the Customer-Pitch and the sector briefing for their industry.",
]


# --------------------------------------------------------------------------- #
# Sector-briefing template (9 slides, identical spine across 6 decks)
# --------------------------------------------------------------------------- #


def sector_notes(sector_display: str, sector_subtitle: str) -> list[str]:
    """Return 9 speaker-notes paragraphs for a sector briefing."""
    s = sector_display
    return [
        # 1 title
        f"Opening. This is the {s} sector briefing - 9 slides, ~20 minutes. "
        f"Spine: sector context -> regulators -> top 3 use-cases -> reference architecture -> "
        f"sovereignty -> ATO sizing -> accelerators -> next steps. Set expectation that we will "
        f"name regulators, name use-cases, and name the ATO envelope. No abstractions.",
        # 2 context
        f"Sector context for {s}. Lead with the structural drivers from the slide. Translate market "
        f"pressure into AI demand: which board-level metrics move when AI is applied here? Ask the "
        f"room to validate or reorder the drivers - their answer informs which of the top 3 use-cases "
        f"to lead with in slide 4.",
        # 3 regulators
        f"Regulators and frameworks for {s}. Walk the sector-specific regulators first, then the "
        f"cross-cutting frameworks (RAI v2, ISO 42001, NIST AI RMF). Land the point: every use-case "
        f"in slide 4 is engineered to map to these controls. Governance is the spine, not a tax. "
        f"If the buyer is a CRO or compliance officer, dwell here.",
        # 4 use-cases
        f"The three named use-cases. For each: surface (M365 / Studio / Foundry), value range, what it "
        f"does, key controls. Ask the room which one their executive sponsor would fund first - that is "
        f"the workload for the pilot. Do not pitch all three; let them pick.",
        # 5 architecture
        f"Reference architecture for {s}. Five layers: experience, orchestration, reasoning and "
        f"retrieval, data and grounding, governance. Stress the governance wrap - Purview, Defender, "
        f"impact assessments, eval harness. Architecture is sector-tailored but built on the same "
        f"CoE foundation, so partner delivery scales.",
        # 6 sovereignty
        f"Sovereignty posture for {s}. Map data residency, network segregation, key custody, and "
        f"audit posture to this sector's specific regulators (named on slide 3). For regulated "
        f"buyers, this slide alongside AI-CoE-Sovereign-AI-RSA.pptx is the unlock. ACC-2 POPIA "
        f"Landing Zone is the underlying platform.",
        # 7 engagement
        f"ATO sizing for {s}. Walk the envelopes by phase: Envision workshop, pilot, scale. Numbers "
        f"in USD; vehicles named (ECIF, MCI, MAICPP). The point: every phase has a funding vehicle, "
        f"so the customer commits ACR and we fund the work around it.",
        # 8 accelerators
        f"Pre-built CoE accelerators that compress weeks 1-8 for {s}. Point to ACC-2 POPIA Landing "
        f"Zone, ACC-3 SOE Adoption Playbook, sector-specific patterns from accelerators/. These are "
        f"what make 'first outcome by day 90' a default, not a stretch.",
        # 9 next steps
        f"Close. Three concrete next steps: book the Envision workshop ($50K ECIF); stand up the "
        f"M365 SOE adoption path in parallel; reserve the lead agent build for the post-Envision "
        f"window. Pair this briefing with the Pitch-Deck, Sovereign-AI deck, and Objection-Handling "
        f"in the follow-up pack. Confirm sponsor and baseline before the meeting ends.",
    ]


# --------------------------------------------------------------------------- #
# Apply
# --------------------------------------------------------------------------- #


def set_notes(slide, text: str) -> None:
    """Overwrite the slide's notes text frame with text."""
    notes = slide.notes_slide
    tf = notes.notes_text_frame
    tf.clear()
    paras = text.split("\n")
    for i, line in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        run = p.add_run()
        run.text = line
        run.font.size = Pt(11)


def apply(path: Path, notes: list[str]) -> None:
    prs = Presentation(str(path))
    if len(notes) != len(prs.slides):
        raise ValueError(
            f"{path.name}: {len(notes)} notes provided but deck has {len(prs.slides)} slides"
        )
    for slide, text in zip(prs.slides, notes):
        set_notes(slide, text)
    prs.save(str(path))
    print(f"OK   {path.name}: {len(notes)} slide-notes written")


def main() -> int:
    apply(ROOT / "AI-CoE-Customer-Pitch-Respined.pptx", CUSTOMER_PITCH_RESPINED)
    apply(ROOT / "AI-CoE-Pitch-Deck-Respined.pptx", PITCH_DECK_RESPINED)

    sectors = {
        "AI-CoE-Sector-Briefing-Banking-Insurance.pptx": "Banking & Insurance",
        "AI-CoE-Sector-Briefing-Healthcare.pptx": "Healthcare",
        "AI-CoE-Sector-Briefing-Mining.pptx": "Mining",
        "AI-CoE-Sector-Briefing-Public-Sector.pptx": "Public Sector & SOE",
        "AI-CoE-Sector-Briefing-Retail.pptx": "Retail & Consumer Goods",
        "AI-CoE-Sector-Briefing-Telco.pptx": "Telco",
    }
    for fname, sector in sectors.items():
        apply(ROOT / fname, sector_notes(sector, ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
