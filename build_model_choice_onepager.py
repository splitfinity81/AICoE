"""Generate AI-CoE-Model-Choice-OnePager.docx from ai-coe-model-choice-guide.md content.

Companion Word artefact for issue #12 (strengthen multi-model / ecosystem narrative).
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).parent / "AI-CoE-Model-Choice-OnePager.docx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)


def shade(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def H(doc, text, level):
    p = doc.add_heading(text, level=level)
    for r in p.runs:
        r.font.name = "Segoe UI"
        if level == 0:
            r.font.color.rgb = NAVY; r.font.size = Pt(24)
        elif level == 1:
            r.font.color.rgb = BLUE; r.font.size = Pt(15)
        else:
            r.font.color.rgb = NAVY; r.font.size = Pt(12)


def P(doc, text, italic=False, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Segoe UI"; r.font.size = Pt(11)
    r.italic = italic; r.bold = bold


def B(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.font.name = "Segoe UI"; r.font.size = Pt(11)


def T(doc, headers, rows):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tbl.style = "Light Grid Accent 1"
    hdr = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        shade(hdr[i], "0067B8")
        for para in hdr[i].paragraphs:
            for r in para.runs:
                r.font.name = "Segoe UI"; r.font.size = Pt(10); r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for r_i, row in enumerate(rows, start=1):
        for c_i, val in enumerate(row):
            cell = tbl.rows[r_i].cells[c_i]
            cell.text = str(val)
            for para in cell.paragraphs:
                for r in para.runs:
                    r.font.name = "Segoe UI"; r.font.size = Pt(10)


def main() -> None:
    doc = Document()
    for s in doc.sections:
        s.left_margin = Cm(2); s.right_margin = Cm(2)
        s.top_margin = Cm(2); s.bottom_margin = Cm(2)

    H(doc, "AI CoE — Model Choice One-Pager", 0)
    P(doc, "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft", italic=True)
    P(doc, "Version 1.0 · 2026-06-03 · Anchors objection 3.5 (multi-model) and Pitch-Deck-Respined slide 11", italic=True)

    H(doc, "1. The lead message", 1)
    P(doc, "Microsoft's AI surface in Azure AI Foundry runs the broadest curated model catalog of any hyperscaler — OpenAI, Anthropic, Meta Llama, Mistral, Cohere, NVIDIA NIM, Hugging Face, and Microsoft's own Phi small-language-model family — under one identity, one billing, one governance plane, one set of RAI guardrails. Competitors with multi-model partnerships do not ship them under a single posture-managed control plane. We do.")
    P(doc, "This is no longer a defensive answer to \"are you OpenAI-only?\" — it is a lead positioning point and the primary anchor for objection 3.5.")

    H(doc, "2. The model catalog (RSA-available)", 1)
    T(doc, ["Family", "Sample models", "Where it shines", "Where it does not"], [
        ["OpenAI", "gpt-4o, gpt-4o-mini, gpt-4-turbo, o1, embeddings", "General reasoning, agent workflows, broadest tool-use ecosystem", "Lowest unit cost (use Phi or mini-class instead)"],
        ["Anthropic Claude", "Claude 3.5 Sonnet, Haiku, Opus (region-dependent)", "Long-context reasoning, structured extraction, careful tone in regulated copy", "Tool-use ecosystem narrower than OpenAI"],
        ["Meta Llama", "Llama 3.x 8B / 70B / 405B", "Open weights; on-VM or on-AKS for full data-plane sovereignty", "Higher operational overhead than managed endpoints"],
        ["Mistral", "Mistral Large, Mixtral, Codestral", "Multilingual European-language workloads, code", "Smaller English benchmark presence"],
        ["Cohere", "Command R+, Embed, Rerank", "RAG-optimised retrieval + rerank pipelines", "Not a general-purpose chat default"],
        ["NVIDIA NIM", "NeMo-tuned variants, healthcare/finance verticals", "Pre-tuned vertical models with NIM serving", "Procurement adds vendor surface"],
        ["Hugging Face", "Curated catalog (1000s)", "Specialised research models, niche domain pre-training", "Long-tail support varies; treat as bring-your-own"],
        ["Microsoft Phi", "Phi-3 mini/small/medium, Phi-3.5 vision", "On-device or low-cost in-cloud SLM; sovereign-friendly", "Below frontier on hard reasoning"],
    ])

    H(doc, "3. Selection criteria — how the CoE picks", 1)
    P(doc, "Five criteria, in order:")
    P(doc, "1. Quality bar required", bold=True)
    B(doc, "Frontier reasoning, multi-step, agent tool-use → gpt-4o or Claude 3.5 Sonnet.")
    B(doc, "Simple extraction, classification, intent routing → gpt-4o-mini or Phi-3-medium.")
    B(doc, "On-device, edge, or extreme cost sensitivity → Phi-3 mini.")
    P(doc, "2. Latency budget", bold=True)
    B(doc, "<1s p95 → mini / Phi class; consider streaming.")
    B(doc, "1-3s p95 → mid-tier (mini-plus, Claude Haiku, Mistral Mixtral).")
    B(doc, ">3s acceptable → frontier (gpt-4o, Claude Sonnet, Llama 70B+).")
    P(doc, "3. Cost target", bold=True)
    P(doc, "Sourced from AI-CoE-AI-TCO-Calculator.xlsx. Router mixes models to hit unit-cost targets.")
    P(doc, "4. Sovereignty requirement", bold=True)
    B(doc, "Data-plane in SA region + Microsoft-controlled posture → Foundry-hosted OpenAI / Mistral / Phi in SA North/West.")
    B(doc, "Customer-controlled weights → Llama or Mistral self-hosted on AKS in customer VNet.")
    B(doc, "Hardest sovereign cases → Phi-3 on-device or in customer datacentre via Azure Local.")
    P(doc, "5. Vertical tuning available", bold=True)
    P(doc, "NVIDIA NIM healthcare/finance, Cohere RAG, Hugging Face niche models. Check before defaulting to frontier.")

    H(doc, "4. Routing pattern — the practical implementation", 1)
    P(doc, "Foundry deployments rarely use one model. The CoE pattern is a 3-tier router:")
    T(doc, ["Tier", "Default model", "Triggered when"], [
        ["Tier 1 (fast/cheap)", "Phi-3-medium or gpt-4o-mini", "Default for new prompts; ~70-80% of traffic"],
        ["Tier 2 (mid)", "Claude Haiku or Mistral Large", "Tier 1 confidence below threshold OR task class requires deeper reasoning"],
        ["Tier 3 (frontier)", "gpt-4o or Claude Sonnet", "Tier 2 escalation OR high-impact / HITL-flagged path"],
    ])
    P(doc, "Cache layer (Azure AI Search semantic cache or Cosmos DB cache) sits in front of all tiers; cache-hit short-circuits routing.")
    P(doc, "Expected outcome: 30-50% unit-cost reduction vs frontier-only baseline, with quality maintained because the router escalates only on the prompts that actually need it.")

    H(doc, "5. When NOT to multi-model", 1)
    B(doc, "First production agent for a customer just starting their AI journey — pick one frontier model (gpt-4o) and ship. Add routing in iteration 2.")
    B(doc, "Highly regulated workflows where every model change requires re-eval + re-attestation — operational cost of multi-model exceeds unit-cost savings until volume is high.")
    B(doc, "Customers without a working eval harness — multi-model without measurement is gambling. Land AI-CoE-GenAIOps-Reference.docx first.")

    H(doc, "6. Linked artefacts", 1)
    B(doc, "AI-CoE-Pitch-Deck-Respined.pptx slide 11 (Foundry deep-dive) names the catalog; future slide 8b will lead with model choice.")
    B(doc, "AI-CoE-Objection-Handling.pptx objection 3.5 — multi-model — shortened to a pointer to this one-pager.")
    B(doc, "AI-CoE-AI-TCO-Calculator.xlsx — model mix is an input; router economics flow directly from the model-mix sliders.")
    B(doc, "AI-CoE-GenAIOps-Reference.docx — L3 Reasoning layer enumerates this catalog.")
    B(doc, "ai-coe-pitch-stats-report.md — Foundry model-count stat to be re-verified at next refresh.")

    doc.save(str(OUT))
    print(f"Wrote {OUT.name}")


if __name__ == "__main__":
    main()
