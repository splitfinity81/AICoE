# AI CoE Pitch Re-spine — Specification

**Author:** Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft
**Date:** 2026-06-03
**Status:** Approved for build (Issue #9)

## Why re-spine

The current `AI-CoE-Pitch-Deck.pptx` leads with the **5+1 Pillars**. Pillars are an *internal CoE construct* — useful for delivery RACI and coverage, weak as a customer hook. Competitive review (Accenture, Deloitte, IBM Consulting RSA decks Q1-Q2 2026) shows customers respond to a **moat narrative**, not a maturity-model narrative. Microsoft's actual moat is the **three AI surfaces × three funding streams** matrix — no competitor can match it because no competitor controls the M365 install base, the agent runtime, AND the model substrate simultaneously, AND can fund landing + factory + partner build-run from three distinct instruments.

The Pillars do not disappear — they move from spine to **coverage checklist** (slide ~18, appendix-adjacent). Sellers still use them; customers no longer have to learn them in the first 10 minutes.

## The new spine (first 8 slides)

| # | Slide | Headline | What's on it |
|---|---|---|---|
| 1 | Title | **Microsoft AI Center of Excellence for RSA** | Sub: three surfaces, three funding streams, one operating model |
| 2 | The customer's problem | "We have AI initiatives. We don't have an AI capability." | Three failure modes: pilot purgatory, shadow AI sprawl, governance debt |
| 3 | **The moat grid** (anchor slide) | Three surfaces × three streams = nine intersections only Microsoft can deliver | M365 Copilot / Copilot Studio / Foundry × MCAPS-sponsored / Factory zero-cost / Partner build-run. Each cell named with a 1-line offer. |
| 4 | Why this grid is unmatched | Per-cell competitive read | "Hyperscaler X has surface 3 but no stream 1. SI Y has stream 3 but no surface 1." |
| 5 | ATO economics — the funding spine | Up to $1M ACR commitment funds the landing zone, the factory, and the first three production use-cases | $1 customer commit unlocks $3-$5 in Microsoft + partner-funded delivery |
| 6 | The operating model | One CoE charter, three surfaces, three streams, four governance gates, quarterly attestation | Visual: CoE at centre, surfaces as petals, streams as funding inflows, gates as outflow filters |
| 7 | Proof — what customers ship in 90 days | Three named outcomes per surface (M365 / Studio / Foundry) with measurable KPI shape | Tie to AI-CoE-AI-TCO-Calculator.xlsx unit economics |
| 8 | What we ask of you | One sponsor, one baseline, one signed ATO, one quarterly review | Close-the-meeting CTA |

## Slides 9-17 (substance, re-ordered, not re-built)

- 9: Three-surface deep-dive — M365 Copilot economics + adoption curve
- 10: Three-surface deep-dive — Copilot Studio agent patterns
- 11: Three-surface deep-dive — Foundry build-and-run with RAI guardrails
- 12: F1-F10 Factory (lifted from current deck slide 11) — re-framed as "stream 2 execution mechanic"
- 13: Partner build-run — MAICPP economics + the 12 named RSA partners
- 14: Sovereign AI for regulated buyers — collapse three sovereignty dimensions to one slide pointing to `AI-CoE-Sovereign-AI-RSA.pptx`
- 15: Governance & RAI posture — four gates + Purview AI Hub + Defender for Cloud AI, point to `AI-CoE-AI-Governance-Playbook.docx`
- 16: KPI scaffold — adoption, value, risk, cost (4-quadrant)
- 17: Reference customers — NTT DATA, Capgemini, + 2 new RSA-named anonymised wins

## Slides 18-22 (appendix / coverage)

- 18: **The 5+1 Pillars — coverage checklist** (demoted from spine; now used as "did we cover everything?" gate)
- 19: 3-tier CoE Ladder — when to climb, when not to
- 20: Industry verticals — pointer to six sector briefings
- 21: Commercial archetypes — pointer to Addendum (risk-share)
- 22: Linked artefacts index — one-page map to the pack

## Customer-Pitch (5 slides) re-spine

Mirror slides 1, 3, 5, 6, 8 of the full deck — title, moat grid, ATO economics, operating model, CTA. No pillars at all in the 5-slide variant.

## Deliverables

| Path | Purpose |
|---|---|
| `ai-coe-pitch-respine-spec.md` | This document |
| `build_respined_pitch_deck.py` | python-pptx generator → `AI-CoE-Pitch-Deck-Respined.pptx` |
| `build_respined_customer_pitch.py` | python-pptx generator → `AI-CoE-Customer-Pitch-Respined.pptx` |
| `improvements-plan.md` | Append section noting re-spine landed against improvement theme "lead with the moat" |

## Why not modify the existing decks

Both `AI-CoE-Pitch-Deck.pptx` and `AI-CoE-Customer-Pitch.pptx` are RMS-protected. Re-spined variants ship alongside; the old decks remain for sellers who prefer the pillars-first spine until the re-spined versions are validated in 3+ live customer meetings.

## Validation gate

Re-spined decks promoted from `-Respined` suffix to primary file names only after:
1. Three sellers run the new spine in live customer meetings.
2. Two of the three report customer engagement at slide 3 (moat grid) measurably higher than at slide 3 of the old deck (pillars).
3. CSU lead sign-off.
