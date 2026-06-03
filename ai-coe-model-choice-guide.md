# AI CoE Model Choice One-Pager

**Author:** Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft
**Version:** 1.0 · 2026-06-03
**Issue:** Closes #12 (strengthen multi-model / ecosystem narrative)
**Companion artefact:** `AI-CoE-Model-Choice-OnePager.docx`

---

## The lead message

Microsoft's AI surface in Azure AI Foundry runs **the broadest curated model catalog of any hyperscaler** — OpenAI, Anthropic, Meta Llama, Mistral, Cohere, NVIDIA NIM, Hugging Face, and Microsoft's own Phi small-language-model family — under one identity, one billing, one governance plane, one set of RAI guardrails. Competitors with multi-model partnerships do not ship them under a single posture-managed control plane. We do.

This is no longer a defensive answer to "are you OpenAI-only?" — it is a **lead positioning slide** in the re-spined pitch (`AI-CoE-Pitch-Deck-Respined.pptx`) and the primary anchor for objection 3.5.

## The model catalog (RSA-available)

| Family | Sample models | Where it shines | Where it does not |
|---|---|---|---|
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, o1, embeddings | General reasoning, agent workflows, broadest tool-use ecosystem | Lowest unit cost (use Phi or mini-class instead) |
| **Anthropic Claude** | Claude 3.5 Sonnet, Haiku, Opus (region-dependent) | Long-context reasoning, structured extraction, careful tone in regulated copy | Tool-use ecosystem narrower than OpenAI |
| **Meta Llama** | Llama 3.x 8B / 70B / 405B | Open weights; on-VM or on-AKS for full data-plane sovereignty | Higher operational overhead than managed endpoints |
| **Mistral** | Mistral Large, Mixtral, Codestral | Multilingual European-language workloads, code | Smaller English benchmark presence |
| **Cohere** | Command R+, Embed, Rerank | RAG-optimised retrieval + rerank pipelines | Not a general-purpose chat default |
| **NVIDIA NIM** | NeMo-tuned variants, healthcare/finance verticals | Pre-tuned vertical models with NIM serving | Procurement adds vendor surface |
| **Hugging Face** | Curated catalog (1000s) | Specialised research models, niche domain pre-training | Long-tail support varies; treat as bring-your-own |
| **Microsoft Phi** | Phi-3 mini/small/medium, Phi-3.5 vision | On-device or low-cost in-cloud SLM; sovereign-friendly | Below frontier on hard reasoning |

## Selection criteria — how the CoE picks

Five criteria, in order:

1. **Quality bar required**
   - Frontier reasoning, multi-step, agent tool-use → gpt-4o or Claude 3.5 Sonnet.
   - Simple extraction, classification, intent routing → gpt-4o-mini or Phi-3-medium.
   - On-device, edge, or extreme cost sensitivity → Phi-3 mini.

2. **Latency budget**
   - <1s p95 → mini / Phi class; consider streaming.
   - 1-3s p95 → mid-tier (mini-plus, Claude Haiku, Mistral Mixtral).
   - >3s acceptable → frontier (gpt-4o, Claude Sonnet, Llama 70B+).

3. **Cost target** — sourced from `AI-CoE-AI-TCO-Calculator.xlsx`. Router mixes models to hit unit-cost targets.

4. **Sovereignty requirement**
   - Data-plane in SA region + Microsoft-controlled posture → Foundry-hosted OpenAI / Mistral / Phi in SA North/West.
   - Customer-controlled weights → Llama or Mistral self-hosted on AKS in customer VNet.
   - Hardest sovereign cases → Phi-3 on-device or in customer datacentre via Azure Local.

5. **Vertical tuning available** — NVIDIA NIM healthcare/finance, Cohere RAG, Hugging Face niche models. Check before defaulting to frontier.

## Routing pattern (the practical implementation)

Foundry deployments rarely use one model. The CoE pattern is a **3-tier router**:

| Tier | Default model | Triggered when |
|---|---|---|
| Tier 1 (fast/cheap) | Phi-3-medium or gpt-4o-mini | Default for new prompts; ~70-80% of traffic |
| Tier 2 (mid) | Claude Haiku or Mistral Large | Tier 1 confidence below threshold OR task class requires deeper reasoning |
| Tier 3 (frontier) | gpt-4o or Claude Sonnet | Tier 2 escalation OR high-impact / HITL-flagged path |

Cache layer (Azure AI Search semantic cache or Cosmos DB cache) sits in front of all tiers; cache-hit short-circuits routing.

Expected outcome: 30-50% unit-cost reduction vs frontier-only baseline, with quality maintained because the router escalates on the prompts that actually need it.

## When NOT to multi-model

- First production agent for a customer just starting their AI journey — pick **one** frontier model (gpt-4o) and ship. Add routing in iteration 2.
- Highly regulated workflows where every model change requires re-eval + re-attestation — the operational cost of multi-model exceeds the unit-cost savings until volume is high.
- Customers without a working eval harness — multi-model without measurement is gambling. Land `AI-CoE-GenAIOps-Reference.docx` first.

## Linked artefacts

- `AI-CoE-Pitch-Deck-Respined.pptx` slide 11 (Foundry deep-dive) names the catalog; future slide 8b will lead with model choice.
- `AI-CoE-Objection-Handling.pptx` objection 3.5 — multi-model — shortened to a pointer to this one-pager.
- `AI-CoE-AI-TCO-Calculator.xlsx` — model mix is an input; router economics flow directly from the model-mix sliders.
- `AI-CoE-GenAIOps-Reference.docx` — L3 Reasoning layer enumerates this catalog.
- `ai-coe-pitch-stats-report.md` — Foundry model-count stat to be re-verified at next refresh.
