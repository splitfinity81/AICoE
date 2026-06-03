"""Add speaker notes to every slide of AI-CoE-Objection-Handling.pptx.

Additive only: opens the existing deck, writes notes_text_frame content per
slide, and saves back to the same file. Slide shapes, layouts, and order
are untouched.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation

DECK = Path(__file__).parent / "AI-CoE-Objection-Handling.pptx"

# One entry per slide. Index 0 == Slide 1. First item in each list becomes the
# notes header paragraph; remaining items become bullet paragraphs.
NOTES: list[list[str]] = [
    # S1 - Title
    [
        "Slide 1 - Title / opener.",
        "Greet the room. Introduce yourself: Yuri Baijnath, CSU Cloud & AI Lead (South Africa), Microsoft.",
        "Set the deck's purpose in one line: a single internal reference of the recurring objections that show up in AI CoE pursuits, with seller-ready responses and the artefact to reach for next.",
        "Frame the audience: ATU, STU, CSAMs, and MAICPP partner sellers who run first/second customer meetings.",
        "Note: this is INTERNAL only. The customer never sees this deck. The responses are talking points, not slides to show.",
        "Time-box: 30-40 minutes if walked, or use as a lookup reference. The Top-10 battle card (slide 17) is the print-and-pin version.",
        "Source of truth: ai-coe-objection-handling-report.md - longer rationale, more objections, and the 'why they're asking' framing per objection.",
    ],
    # S2 - How to use
    [
        "Slide 2 - How to use this deck.",
        "Anchor rule: address the concern, not the words. 'We'll wait' usually means 'I'm afraid of being first', not 'we have a thought-out timing strategy'. 'Data isn't clean enough' usually means 'I want a reason to defer'. Diagnose first, then respond.",
        "Persona discipline: a CFO objection takes a CFO answer. Don't answer 'ROI is unproven' with a technical architecture diagram - answer it with the ATO economics ($1 ECIF unlocks $3-5 of consumption) and the up-to-$1M envelope.",
        "Always close the loop with an artefact: Horizon Assessment for 'where do we start'; Pitch Deck ATO slide for ROI; Eskom briefing for regulated industries; the right VBD for capability-specific objections.",
        "Sequencing for first meetings: lead with Pillar 1 (value) and Pillar 5 (governance). Pillars 2, 3, 4 surface in meeting two. +1 (partner politics) usually comes up by meeting three.",
        "Escalation: if the same objection lands twice from different stakeholders, escalate to the named pillar lead (see slide 18). Once is friction; twice is a pattern.",
    ],
    # S3 - Pillars refresher
    [
        "Slide 3 - The 5+1 Pillars refresher.",
        "Quick recap because not everyone in the room knows the 5+1 by heart. Pillar 1 Business Strategy: value cases, ROI, P&L impact. Pillar 2 Org & Culture: adoption, skills, change management. Pillar 3 AI Strategy & Experience: use-case design, surface choice (M365 / Studio / Foundry), capability questions like hallucinations. Pillar 4 Tech & Data: platform readiness, integration, data quality, FinOps. Pillar 5 Governance & Security: POPIA, model risk, IP, prompt injection, EU AI Act. +1 Co-sell & Partner: incumbent SI politics, hyperscaler choice, MAICPP economics.",
        "Why route objections to pillars: it tells you who the right CoE owner is, what artefact to reach for, and whether the customer's pain clusters on one pillar (often Pillar 5 for regulated, Pillar 1 for cost-pressed, Pillar 2 for org-mature-but-AI-immature customers).",
        "If 70% of objections in a meeting land on one pillar, escalate to that lead before the next meeting - the customer is telling you which conversation matters.",
    ],
    # S4 - Objection map
    [
        "Slide 4 - Objection map (persona x pillar).",
        "Read down to find your persona; read across to see which pillars they pressure. This is the routing table.",
        "Three high-density rows to watch: CIO (lights up across 4 pillars - usually the central interlocutor), CISO/CRO (concentrated on Pillar 5 - bring Legal and Purview SME), CFO (Pillar 1 dominant + Pillar 4 cost concern - bring FinOps).",
        "Diagonal density tells the story: if pain is concentrated on one row+column, you have a focused objection set you can address head-on. If pain sprays across the grid, the customer is unsettled at programme level - escalate to the CoE owning lead (often Pillar 1) and re-set with the Horizon Assessment.",
        "Use this slide live with a CSAM to triage which pillar leads to bring to the next meeting.",
    ],
    # S5 - Pillar 1 overview
    [
        "Slide 5 - Pillar 1 Business Strategy - overview.",
        "Where most 'no' lives. CFOs, CEOs, Procurement. Anchor every response in two numbers: $1 of ECIF unlocks $3-5 of Azure consumption (the multiplier); ATO envelope up to $1M (the friction removal).",
        "The classic six: ROI is unproven; we'll wait; per-seat doesn't pencil; we'll build it ourselves; show me an in-industry peer; what's the exit cost.",
        "Mental model: every Pillar 1 objection is really a question about whether the customer can defend the spend internally. Your job is to give them the language and the evidence to win that internal argument.",
        "Bring the Pitch Deck ATO slide to every Pillar 1 conversation - it's the single most-used artefact in the pack.",
    ],
    # S6 - Pillar 1 table
    [
        "Slide 6 - Pillar 1 objection menu (table).",
        "Six objections, each with persona + short response + proof point. Use the table live; long-form rationale is in the source report under section 'Pillar 1 - Business Strategy'.",
        "Spotlight #1 'ROI is unproven': the response leads with discipline ('the CoE forces a value case per use-case BEFORE we build'). Customers who've been burned by undisciplined pilots respond to that framing.",
        "Spotlight #4 'We'll build it ourselves': don't argue against build. Reframe to co-build (VBD C18 Agent Factory) - they keep IP and team, we keep the platform pattern.",
        "Spotlight #6 'Exit cost': the three optionality layers (free T1; multi-model Foundry; data in tenant) is the answer that disarms procurement.",
        "If two or more Pillar 1 objections block: escalate to Pillar 1 lead + ATU lead + CSU GM for the next meeting.",
    ],
    # S7 - Pillar 2 overview
    [
        "Slide 7 - Pillar 2 Org & Culture - overview.",
        "The pillar that decides whether the deal actually creates value or quietly stalls post-signature. The data is unambiguous: only 1 in 3 employees has been trained on the AI tools they already have (BCG 2024).",
        "The CoE's answer is the Adoption Accelerator (VBD A3) and the Skilling Navigator (VBD D2) - the two engagements designed for this pillar.",
        "Key metric to introduce in every Pillar 2 conversation: the three adoption signals - Active Use, Sentiment, Habit. If they don't move by week 6, you re-scope. That discipline is what separates a stalled rollout from a successful one.",
        "Personas: CHRO, COO, CIO, LOB heads. HR/works council questions sit here too - get them surfaced early because they kill deals politically.",
    ],
    # S8 - Pillar 2 table
    [
        "Slide 8 - Pillar 2 objection menu (table).",
        "Six objections covering readiness, change fatigue, history of stalled rollouts, jobs anxiety, skills gap, and adoption fragmentation.",
        "Highest-stakes objection: 'Will AI take our jobs?' Wrong answer kills the deal politically. The right framing: AI changes job content not headcount in wave one; track hours-recovered-per-role; co-design reinvestment with HR; never sequence a rollout to a RIF (adoption metrics collapse the moment workforce believes that's the play).",
        "Most common objection: 'We have change fatigue'. Don't argue. Sequence accordingly - thin first wave, fold into existing change programme, co-funded so it doesn't compete for budget.",
        "If the customer has a strong HR sponsor, bring them into the Pillar 2 conversation directly - they own the workforce trust story, not us.",
    ],
    # S9 - Pillar 3 overview
    [
        "Slide 9 - Pillar 3 AI Strategy & Experience - overview.",
        "Where surface confusion and capability scepticism live. The three Microsoft AI surfaces (M365 Copilot, Copilot Studio, Foundry) feel overlapping to customers - this is your chance to disambiguate.",
        "The 30-second framing: M365 Copilot for knowledge-worker productivity inside Office; Copilot Studio for low-code custom agents inside business processes (D365, ServiceNow, intranet); Azure AI Foundry for code-first production agents and bespoke models. Most CoEs run all three eventually.",
        "Bring the Horizon Assessment to every Pillar 3 conversation - it scores the customer's portfolio against the three surfaces in a week and removes the 'which surface' debate.",
        "Hallucinations is the most-feared objection in this pillar. The production pattern (grounding + evals + human-in-loop) is non-negotiable and you should walk through it confidently - VBDs C13 and C15 operationalise all three.",
    ],
    # S10 - Pillar 3 table
    [
        "Slide 10 - Pillar 3 objection menu (table).",
        "Six objections covering surface choice, hallucinations, agents-vs-chat, GenAI-vs-classic-ML, open-source models, and industry-specific proof.",
        "Concede openly on 'GenAI is hype - we want classic ML': not every problem is a GenAI problem. The winning move is to position the hybrid pattern (ML predicts, GenAI explains or interfaces) and offer the Pattern Scorecard (VBD C19) to identify where each fits.",
        "On 'open-source models are better/cheaper': don't fight the premise. Foundry hosts AOAI plus Mistral plus Llama plus DeepSeek under one API. You give them model optionality with platform discipline.",
        "For industry-specific proof: lead with the Eskom briefing as the regulated-industry template. Where there's no in-segment public reference in RSA, offer an NDA peer call from an adjacent segment.",
    ],
    # S11 - Pillar 4 overview
    [
        "Slide 11 - Pillar 4 Tech & Data - overview.",
        "The readiness pillar. 'Our data isn't clean enough' is the modal blocker in this pillar across every industry.",
        "Two counter-moves to know cold: (1) Scope around the dirty data - Fabric SA (VBD C7) finds the AI-ready domains today; we start there. (2) The Cloud Accelerate Factory (F1-F10) puts the foundation under everything at zero cost to the customer, so customer-funded work is business logic only, not infrastructure.",
        "FinOps is the rising objection - bring the WAF-for-AI review (VBD C12) and Value Realization (VBD D3) into every Pillar 4 conversation involving a CFO.",
        "Personas: CIO, CTO, CDO, Head of Cloud, Architect, FinOps lead. Bring FastTrack and a FinOps SME when this pillar dominates.",
    ],
    # S12 - Pillar 4 table
    [
        "Slide 12 - Pillar 4 objection menu (table).",
        "Six objections: data cleanliness, legacy integration, Azure lock-in, landing zone timeline, technical debt, and cost spiral.",
        "Landing-zone objection ('18 months') has the cleanest counter in the deck: F1+F2+F8+F9 are zero-cost and deliver an AI-ready landing zone in 6-10 weeks. This is often the moment a Pillar 4 conversation flips.",
        "Lock-in objection: separate the layers. Data layer = your tenant, your region. Model layer = multi-vendor in Foundry. Platform layer = Azure, but the IP you build (agents, ALZ pattern, CoE charter) is portable. The lock-in argument doesn't apply at the model layer where it matters most.",
        "Technical-debt objection: the F-series Factory plays net-REDUCE platform count by migrating off legacy - this is the counter-intuitive answer that lands.",
    ],
    # S13 - Pillar 5 overview
    [
        "Slide 13 - Pillar 5 Governance & Security - overview.",
        "In RSA, non-negotiable. POPIA is the floor. SOEs add PFMA; sector regulators add PA, FSCA, NERSA depending on industry; cross-border firms increasingly add EU AI Act.",
        "The single most important artefact in the entire pack for this pillar is the Eskom Executive Briefing - the regulated-industry template that walks through POPIA, NERSA, PFMA, SA region residency, and Purview AI Hub slide by slide. Adapt it for banking (PA, FSCA), public sector (PFMA), healthcare.",
        "Pillar 5 objections rarely block a deal alone - they typically delay it. Address them with concrete controls (RAI v2, GenAIOps eval, Prompt Shields, Sentinel) not with policy promises.",
        "Always bring Legal, Compliance, and a Purview SME when Pillar 5 dominates a meeting. Pillar 5 objections need named SMEs on the line, not generalists.",
    ],
    # S14 - Pillar 5 table
    [
        "Slide 14 - Pillar 5 objection menu (table).",
        "Six objections: data residency / POPIA; model risk and explainability; IP and copyright; shadow AI; prompt injection / jailbreaks; EU AI Act.",
        "Data residency answer should be precise: SA North (JNB) and SA West (CPT) regions with paired residency; Copilot processes M365 data in geo; Foundry/AOAI is data-zone-scoped. Don't be vague here - regulated customers will probe.",
        "IP / copyright answer should always name the Copilot Copyright Commitment - Microsoft indemnifies customers against third-party IP claims on Copilot outputs (M365 Copilot, Copilot for Security, Azure OpenAI Service) when guardrails are configured. The Data Security Assessment (VBD A6) verifies tenant configuration qualifies.",
        "Shadow-AI answer: a ban is the worst response (it moves usage to phones). Give a sanctioned alternative plus Purview AI Hub discovery. A6 produces the discovery report in two weeks - quote that timeline confidently.",
        "Prompt injection: three layers (Content Safety + Prompt Shields at the boundary; GenAIOps telemetry into Sentinel via F9 free; human-in-loop architecturally for irreversible actions). Sophisticated CISOs respect this layered answer.",
    ],
    # S15 - Pillar +1 overview
    [
        "Slide 15 - Pillar +1 Co-sell & Partner - overview.",
        "Objections in this pillar are political, not technical. Don't take incumbents head-on - route the work through them.",
        "The single most useful framing: Microsoft sells the platform; MAICPP partners deliver; the CoE methodology plus funding (ECIF, MAICPP, ACO) is the glue. That framing turns 'we already have an SI' from an objection into the engagement model.",
        "Bring the Partner Recruitment Kit and the Partner Scorecard to every Pillar +1 conversation - they show the customer that partner selection is structured, not arbitrary.",
        "Personas: CIO, CTO, Procurement. ATU partner manager is your co-pilot on every Pillar +1 conversation that goes beyond one objection.",
    ],
    # S16 - Pillar +1 table
    [
        "Slide 16 - Pillar +1 objection menu (table).",
        "Four objections: incumbent SI ownership, why-Microsoft-vs-AWS-Google, partner margin, MS-vs-partner misalignment.",
        "On 'we already have an SI': name them. 'Brilliant - we'd bring [their SI] into the pursuit explicitly; MAICPP co-funds their delivery and you get one throat to choke.' That answer wins the room.",
        "On 'why Microsoft and not [hyperscaler]': three AI-specific reasons (three surfaces under one identity; $1M ATO envelope; RSA in-country presence). Don't make a generic cloud argument - it'll lose.",
        "On MS-vs-partner misalignment: own it as a delivery hygiene problem. Reset with the Delivery RACI as the contract - MS owns MCEM 1-2, joint on 3, partner-led on 4-5 with MS assurance. If a partner can't align to the RACI, bring a different one. That's the move that rebuilds trust.",
    ],
    # S17 - Top-10 battle card
    [
        "Slide 17 - Top-10 battle card.",
        "This is the print-and-pin slide. Memorise the ten one-liners - they should survive interruption mid-sentence.",
        "Use the battle card in three scenarios: live customer call where you can't pull up the deck; coaching a junior seller before a meeting; quick-prep on a flight to a customer.",
        "Notice the structure: every one-liner does three things at once - acknowledge the concern, reframe the question, name the next artefact or VBD. That's the seller pattern: acknowledge, reframe, advance.",
        "If a seller can deliver all ten cleanly without notes, they're ready to run an AI CoE first meeting solo.",
    ],
    # S18 - Escalation matrix
    [
        "Slide 18 - Escalation matrix.",
        "Rule of thumb to repeat in the room: 'Once is friction; twice is a pattern.' Don't escalate on the first time you hear an objection - that signals weakness. Escalate when the same objection lands twice from different stakeholders.",
        "Per-pillar escalation owners are NAMED at the CoE level (Pillar 1 lead, Pillar 2 lead, etc.) - not 'someone from CSU'. If you don't know who the named lead is, find out before your next pursuit.",
        "Bring-also column matters: Pillar 1 needs CSU GM presence to make exec-level reassurances; Pillar 2 needs the customer's HR sponsor; Pillar 5 needs Legal plus Purview SME on the line.",
        "Document escalations in the pursuit notes - the patterns across pursuits feed back into the improvements-plan and the next refresh of this report.",
    ],
    # S19 - Linked artefacts
    [
        "Slide 19 - Linked artefacts.",
        "This is the index slide. Every objection theme maps to a specific file in the AI CoE pack root - don't improvise.",
        "Three most-reached-for artefacts: AI-CoE-Pitch-Deck.pptx (ATO slide for value objections), AI-CoE-Horizon-Assessment.xlsx (for 'where do we start'), and AI-CoE-Eskom-Executive-Briefing.pptx (for regulated industries).",
        "If a theme is listed here but the artefact doesn't yet exist in the repo, raise it via improvements-plan.md - that's how the pack grows.",
        "New joiners: read AI-CoE-How-To-Use.pptx first; then come back to this deck.",
    ],
    # S20 - Sources & methodology
    [
        "Slide 20 - Sources & methodology.",
        "Trust grades are honest: HIGH for content authored or cross-checked against internal Microsoft sources (ATO deck, Frontier CoE pillar decks, csu-ai-vbd-reference-report.md). MODERATE for external stats (BCG 2024, McKinsey 2025) which are time-bounded.",
        "Re-verification gates: any quoted VBD funding amount, ECIF cap, ATO envelope size, or regional residency policy must be re-checked on MCAPS Catalog before a customer commit. The catalogue changes quarterly.",
        "Methodology disclosure: objections were seeded from RSA CSU recurring patterns (not exhaustive); responses drafted against existing VBDs and Pitch-Deck proof points; the battle-card was distilled to one-liners that survive interruption mid-sentence.",
        "Closing the loop: when sellers encounter new objections in the field, raise them back into ai-coe-objection-handling-report.md so the next refresh captures them. The report is the living artefact; this deck is the delivery surface.",
    ],
    # S21 - Close
    [
        "Slide 21 - Close.",
        "Anchor phrase: 'Address the concern, not the words.' Every objection in this deck is a translation problem - convert the words to the underlying concern, route to the pillar, deliver the response, name the next artefact.",
        "Numbers to remember: 5+1 pillars; 34 objections catalogued; 10 on the battle card; 1 source-of-truth report.",
        "Call to action: pick one pursuit this week, walk the objection map for that customer's known personas, and pre-brief your pillar leads BEFORE the next meeting. That's how this deck pays for itself.",
        "Thank the room. Offer to pair on one live pursuit and to add any new objections back into the source report.",
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
