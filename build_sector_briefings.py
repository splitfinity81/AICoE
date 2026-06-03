"""Generate six RSA sector executive briefings (9 slides each).

Modelled on AI-CoE-Eskom-Executive-Briefing.pptx (RMS-protected; not editable).
Output files:
  AI-CoE-Sector-Briefing-Banking-Insurance.pptx
  AI-CoE-Sector-Briefing-Retail.pptx
  AI-CoE-Sector-Briefing-Telco.pptx
  AI-CoE-Sector-Briefing-Mining.pptx
  AI-CoE-Sector-Briefing-Public-Sector.pptx
  AI-CoE-Sector-Briefing-Healthcare.pptx

Each deck has 9 slides:
  1. Title
  2. Sector context (RSA pressures, market shape, AI maturity)
  3. Regulators & frameworks map
  4. Top 3 named AI use-cases
  5. Sample reference architecture (text-described surfaces)
  6. Sovereignty + governance posture
  7. Engagement shape (ATO sizing + envelope)
  8. Anchored accelerators (from accelerators/)
  9. Close + call-to-action

Author: Yuri Baijnath - CSU Cloud & AI Lead (South Africa), Microsoft.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

ROOT = Path(__file__).parent

BLUE = RGBColor(0x00, 0x67, 0xB8)
CYAN = RGBColor(0x50, 0xE6, 0xFF)
PURPLE = RGBColor(0x74, 0x2A, 0x9B)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
LIGHT = RGBColor(0xEA, 0xF4, 0xFB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x59, 0x59, 0x59)

W, H = Inches(13.333), Inches(7.5)


def set_bg(slide, color: RGBColor) -> None:
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    bg.fill.solid(); bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    bg.shadow.inherit = False
    # Send to back
    spTree = bg._element.getparent()
    spTree.remove(bg._element); spTree.insert(2, bg._element)


def add_text(slide, left, top, width, height, text, *, size=18, bold=False,
             color=NAVY, align=PP_ALIGN.LEFT, font="Segoe UI") -> None:
    tx = slide.shapes.add_textbox(left, top, width, height)
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run(); r.text = text
    r.font.name = font; r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color


def add_bullets(slide, left, top, width, height, items, *, size=14, color=NAVY) -> None:
    tx = slide.shapes.add_textbox(left, top, width, height)
    tf = tx.text_frame; tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run(); r.text = "\u2022  " + item
        r.font.name = "Segoe UI"; r.font.size = Pt(size); r.font.color.rgb = color
        p.space_after = Pt(4)


def add_rect(slide, left, top, width, height, fill: RGBColor, *, line=None) -> None:
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
    s.shadow.inherit = False
    return s


def add_footer(slide, sector_name: str, page: int, total: int) -> None:
    add_rect(slide, 0, Inches(7.15), W, Inches(0.35), NAVY)
    add_text(slide, Inches(0.3), Inches(7.18), Inches(8), Inches(0.3),
             f"AI CoE | RSA Sector Briefing | {sector_name}",
             size=10, color=WHITE)
    add_text(slide, Inches(11.5), Inches(7.18), Inches(1.5), Inches(0.3),
             f"{page} / {total}", size=10, color=WHITE, align=PP_ALIGN.RIGHT)


def slide_title(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, NAVY)
    add_rect(slide, 0, Inches(0), Inches(0.4), H, BLUE)
    add_rect(slide, Inches(0.4), Inches(0), Inches(0.15), H, CYAN)
    add_text(slide, Inches(0.9), Inches(1.6), Inches(11.8), Inches(0.5),
             f"AI Center of Excellence | {sector['name']} (RSA)",
             size=18, bold=True, color=CYAN)
    add_text(slide, Inches(0.9), Inches(2.2), Inches(11.8), Inches(1.5),
             sector["tagline"],
             size=36, bold=True, color=WHITE)
    add_text(slide, Inches(0.9), Inches(4.5), Inches(11.8), Inches(0.5),
             "Executive briefing | 9 slides | Internal seller reference",
             size=14, color=LIGHT)
    add_text(slide, Inches(0.9), Inches(5.1), Inches(11.8), Inches(0.4),
             "Yuri Baijnath - CSU Cloud & AI Lead (South Africa), Microsoft",
             size=12, color=LIGHT)
    add_text(slide, Inches(0.9), Inches(5.5), Inches(11.8), Inches(0.4),
             "Version 1.0 | 2026-06-03",
             size=11, color=GREY)
    add_footer(slide, sector["name"], 1, 9)


def slide_context(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "2. Sector context | what's driving AI in this market", size=18, bold=True, color=WHITE)
    add_text(slide, Inches(0.4), Inches(0.85), Inches(12.5), Inches(0.4),
             sector["context_lead"], size=14, bold=True, color=NAVY)
    add_bullets(slide, Inches(0.5), Inches(1.5), Inches(12.3), Inches(5.4),
                sector["context_points"], size=14)
    add_footer(slide, sector["name"], 2, 9)


def slide_regulators(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "3. Regulators & frameworks | what governs the AI use-case", size=18, bold=True, color=WHITE)
    # Two column: regulators left, frameworks right
    add_rect(slide, Inches(0.4), Inches(0.9), Inches(6.2), Inches(0.5), NAVY)
    add_text(slide, Inches(0.6), Inches(0.96), Inches(6), Inches(0.4),
             "Sector regulators (RSA)", size=14, bold=True, color=WHITE)
    add_bullets(slide, Inches(0.5), Inches(1.5), Inches(6), Inches(5.4),
                sector["regulators"], size=13)
    add_rect(slide, Inches(6.85), Inches(0.9), Inches(6.2), Inches(0.5), PURPLE)
    add_text(slide, Inches(7.05), Inches(0.96), Inches(6), Inches(0.4),
             "Cross-cutting frameworks", size=14, bold=True, color=WHITE)
    add_bullets(slide, Inches(6.95), Inches(1.5), Inches(6), Inches(5.4),
                sector["frameworks"], size=13)
    add_footer(slide, sector["name"], 3, 9)


def slide_use_cases(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "4. Top 3 named AI use-cases for this sector", size=18, bold=True, color=WHITE)
    col_w = Inches(4.1); gap = Inches(0.15); left0 = Inches(0.4)
    for i, uc in enumerate(sector["use_cases"]):
        left = left0 + (col_w + gap) * i
        add_rect(slide, left, Inches(0.9), col_w, Inches(0.6), [BLUE, PURPLE, CYAN][i])
        add_text(slide, left + Inches(0.1), Inches(0.97), col_w - Inches(0.2), Inches(0.5),
                 uc["title"], size=14, bold=True,
                 color=NAVY if i == 2 else WHITE)
        add_rect(slide, left, Inches(1.5), col_w, Inches(5.4), LIGHT)
        add_text(slide, left + Inches(0.15), Inches(1.6), col_w - Inches(0.3), Inches(0.5),
                 f"Surface: {uc['surface']}", size=11, bold=True, color=PURPLE)
        add_text(slide, left + Inches(0.15), Inches(2.1), col_w - Inches(0.3), Inches(0.5),
                 f"Value: {uc['value']}", size=11, bold=True, color=NAVY)
        add_text(slide, left + Inches(0.15), Inches(2.7), col_w - Inches(0.3), Inches(0.4),
                 "What it does:", size=11, bold=True, color=NAVY)
        add_bullets(slide, left + Inches(0.15), Inches(3.05), col_w - Inches(0.3), Inches(2.5),
                    uc["does"], size=10)
        add_text(slide, left + Inches(0.15), Inches(5.6), col_w - Inches(0.3), Inches(0.4),
                 "Key controls:", size=11, bold=True, color=NAVY)
        add_bullets(slide, left + Inches(0.15), Inches(5.95), col_w - Inches(0.3), Inches(0.95),
                    uc["controls"], size=10)
    add_footer(slide, sector["name"], 4, 9)


def slide_architecture(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "5. Sample reference architecture", size=18, bold=True, color=WHITE)
    add_text(slide, Inches(0.4), Inches(0.85), Inches(12.5), Inches(0.4),
             sector["arch_lead"], size=13, bold=True, color=NAVY)
    layers = [
        ("Experience layer", sector["arch"]["experience"], BLUE),
        ("Orchestration / agents", sector["arch"]["orchestration"], PURPLE),
        ("Reasoning & retrieval", sector["arch"]["reasoning"], CYAN),
        ("Data foundation", sector["arch"]["data"], NAVY),
        ("Governance & security", sector["arch"]["governance"], BLUE),
    ]
    y = Inches(1.4); rh = Inches(1.05); gap = Inches(0.08)
    for label, items, color in layers:
        add_rect(slide, Inches(0.4), y, Inches(3), rh, color)
        add_text(slide, Inches(0.55), y + Inches(0.3), Inches(2.7), Inches(0.5),
                 label, size=13, bold=True,
                 color=NAVY if color == CYAN else WHITE)
        add_rect(slide, Inches(3.5), y, Inches(9.4), rh, LIGHT)
        add_text(slide, Inches(3.65), y + Inches(0.2), Inches(9.1), rh - Inches(0.3),
                 items, size=11, color=NAVY)
        y += rh + gap
    add_footer(slide, sector["name"], 5, 9)


def slide_sovereignty(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "6. Sovereignty & governance posture", size=18, bold=True, color=WHITE)
    add_text(slide, Inches(0.4), Inches(0.85), Inches(12.5), Inches(0.4),
             sector["sov_lead"], size=13, bold=True, color=NAVY)
    add_bullets(slide, Inches(0.5), Inches(1.5), Inches(12.3), Inches(5.4),
                sector["sov_points"], size=13)
    add_footer(slide, sector["name"], 6, 9)


def slide_engagement(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "7. Engagement shape | ATO sizing & funding", size=18, bold=True, color=WHITE)
    headers = ["Phase", "Vehicle", "Envelope (USD)", "Output"]
    rows = sector["engagement"]
    col_widths = [Inches(2.8), Inches(3.2), Inches(2.2), Inches(4.7)]
    x = Inches(0.4); y = Inches(0.9)
    # header
    for i, h in enumerate(headers):
        add_rect(slide, x, y, col_widths[i], Inches(0.5), BLUE)
        add_text(slide, x + Inches(0.1), y + Inches(0.07), col_widths[i], Inches(0.4),
                 h, size=12, bold=True, color=WHITE)
        x += col_widths[i]
    y += Inches(0.5)
    for r_i, row in enumerate(rows):
        x = Inches(0.4)
        bg = LIGHT if r_i % 2 == 0 else WHITE
        for i, val in enumerate(row):
            add_rect(slide, x, y, col_widths[i], Inches(0.6), bg)
            add_text(slide, x + Inches(0.1), y + Inches(0.1), col_widths[i] - Inches(0.15), Inches(0.5),
                     val, size=11, color=NAVY)
            x += col_widths[i]
        y += Inches(0.6)
    # Reference customer block
    add_rect(slide, Inches(0.4), Inches(5.5), Inches(12.5), Inches(0.5), PURPLE)
    add_text(slide, Inches(0.55), Inches(5.57), Inches(12.3), Inches(0.4),
             f"Anonymised reference: {sector['reference']}", size=12, bold=True, color=WHITE)
    add_text(slide, Inches(0.55), Inches(6.1), Inches(12.3), Inches(1.0),
             sector["reference_note"], size=11, color=NAVY)
    add_footer(slide, sector["name"], 7, 9)


def slide_accelerators(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, WHITE)
    add_rect(slide, 0, 0, W, Inches(0.6), BLUE)
    add_text(slide, Inches(0.3), Inches(0.1), Inches(13), Inches(0.5),
             "8. Anchored accelerators (from accelerators/)", size=18, bold=True, color=WHITE)
    add_text(slide, Inches(0.4), Inches(0.85), Inches(12.5), Inches(0.4),
             "Pre-built CoE assets that compress weeks 1-8 of pilot delivery for this sector.",
             size=12, color=NAVY)
    add_bullets(slide, Inches(0.5), Inches(1.5), Inches(12.3), Inches(5.4),
                sector["accelerators"], size=13)
    add_footer(slide, sector["name"], 8, 9)


def slide_close(prs, sector) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide, NAVY)
    add_rect(slide, 0, Inches(0), Inches(0.4), H, BLUE)
    add_rect(slide, Inches(0.4), Inches(0), Inches(0.15), H, CYAN)
    add_text(slide, Inches(0.9), Inches(1.0), Inches(11.8), Inches(0.5),
             "9. What to do next", size=18, bold=True, color=CYAN)
    add_text(slide, Inches(0.9), Inches(1.7), Inches(11.8), Inches(1.2),
             sector["close_headline"], size=28, bold=True, color=WHITE)
    add_bullets(slide, Inches(0.9), Inches(3.4), Inches(11.8), Inches(3.0),
                sector["close_actions"], size=16, color=LIGHT)
    add_text(slide, Inches(0.9), Inches(6.5), Inches(11.8), Inches(0.4),
             "Pair with: AI-CoE-Pitch-Deck.pptx | AI-CoE-Sovereign-AI-RSA.pptx | AI-CoE-Objection-Handling.pptx",
             size=11, color=GREY)
    add_footer(slide, sector["name"], 9, 9)


def build_deck(sector) -> Path:
    prs = Presentation()
    prs.slide_width = W; prs.slide_height = H
    slide_title(prs, sector)
    slide_context(prs, sector)
    slide_regulators(prs, sector)
    slide_use_cases(prs, sector)
    slide_architecture(prs, sector)
    slide_sovereignty(prs, sector)
    slide_engagement(prs, sector)
    slide_accelerators(prs, sector)
    slide_close(prs, sector)
    out = ROOT / sector["filename"]
    prs.save(str(out))
    return out


SECTORS = [
    {
        "name": "Banking & Insurance",
        "filename": "AI-CoE-Sector-Briefing-Banking-Insurance.pptx",
        "tagline": "AI for prudential, conduct, and customer-experience leverage",
        "context_lead": "RSA financial services: thin margins, conduct scrutiny, and a regulator stack that treats AI as model risk.",
        "context_points": [
            "Big-4 banks + insurers run on mainframe + SAP + bespoke; AI must integrate, not replace, core systems.",
            "SARB Directive 7 on model risk applies to AI used in credit / pricing / fraud decisions - explainability is mandatory.",
            "PA Joint Standard 1 of 2023 (cybersecurity & cyber resilience) extends to AI components.",
            "FSCA Conduct Standards require demonstrable fairness in customer-facing automated decisions (TCF principles).",
            "Cost-to-serve pressure: tier-1 contact-centre cost-per-call is the #1 board-level AI target.",
            "Fraud signal volumes outpace human review - AI co-pilot for fraud analysts is a force-multiplier, not a replacement.",
        ],
        "regulators": [
            "SARB (Prudential Authority) - Directive 7 model risk; Joint Standard 1 cyber",
            "FSCA - Conduct Standards; TCF (Treating Customers Fairly)",
            "FAIS Act - financial advice disclosure",
            "FICA - AML / KYC obligations",
            "Information Regulator - POPIA",
            "JSE Listings Requirements - disclosure of material AI risk",
        ],
        "frameworks": [
            "Microsoft RAI v2 (control families G1-G3, T1-T4)",
            "ISO/IEC 42001:2023 - AI Management System",
            "NIST AI RMF 1.0",
            "EU AI Act (spillover for SA banks operating in EU)",
            "BCBS 239 (risk data aggregation) for AI inputs",
            "Microsoft WAF + Cloud Adoption Framework for FSI",
        ],
        "use_cases": [
            {
                "title": "Tier-1 contact-centre agent",
                "surface": "Copilot Studio + Foundry",
                "value": "30-45% AHT reduction",
                "does": [
                    "Authenticated customer intent recognition",
                    "Policy / product retrieval over SharePoint + core",
                    "Drafted response with citation to source",
                    "HITL handoff on regulated topics (advice, complaints)",
                ],
                "controls": ["Purview AI Hub log; FSCA TCF eval slice; kill-switch"],
            },
            {
                "title": "KYC / FICA document processing",
                "surface": "Azure AI Foundry + DocIntel",
                "value": "70% faster onboarding",
                "does": [
                    "Extract identity + proof-of-address fields",
                    "Cross-check sanctions / PEP lists",
                    "Reasoning trace for auditor sample",
                    "Risk-rated routing to analyst queue",
                ],
                "controls": ["CMK; private endpoint; auditor-sample log"],
            },
            {
                "title": "Fraud-analyst co-pilot",
                "surface": "Foundry agent + Sentinel",
                "value": "2-3x analyst throughput",
                "does": [
                    "Pattern explanation over alert cluster",
                    "Similar-case retrieval",
                    "Suggested next-best-action with confidence",
                    "Audit-trail-grade reasoning capture",
                ],
                "controls": ["Defender for Cloud AI; reasoning trace; HITL on freeze decisions"],
            },
        ],
        "arch_lead": "Five-layer reference: Copilot surfaces over Foundry agents over PostgreSQL + Synapse + Purview, all under POPIA landing zone.",
        "arch": {
            "experience": "M365 Copilot for ops + Power Pages portal for HITL; Teams for case collaboration.",
            "orchestration": "Copilot Studio agents for tier-1; Foundry orchestrators for tier-2/3 with tool calls.",
            "reasoning": "gpt-4o + gpt-4o-mini routing; Azure AI Search vector index over policy + case corpus.",
            "data": "Synapse + PostgreSQL HyperScale; core-banking via API gateway; Purview lineage end-to-end.",
            "governance": "Purview AI Hub + Defender for Cloud AI + Azure Policy POPIA initiative; Customer-Managed Keys.",
        },
        "sov_lead": "POPIA + SARB + FSCA compliance is the entry ticket; sovereignty is the trust ticket.",
        "sov_points": [
            "SA North + SA West dual-region for active-active resilience; data-zone scoping prevents EU/US drift.",
            "Customer-Managed Keys in Azure Key Vault HSM (FIPS 140-2 Level 3).",
            "Private endpoints; VNet integration; no public model endpoints.",
            "Purview AI Hub provides reasoning trace for AGSA / SARB / FSCA inspection.",
            "Defender for Cloud AI surfaces shadow-AI in M365 + dev environments.",
            "Quarterly attestation via AI-CoE-AI-Impact-Assessment.xlsx; 18 controls default-on.",
            "Use AI-CoE-Sovereign-AI-RSA.pptx as the long-form companion when CISO/DPO ask for depth.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "Use-case shortlist + crosswalk"],
            ["Impact assessment", "ECIF", "100,000", "Signed assessment per use-case"],
            ["Pilot (8-12 wk)", "ATO + partner", "500,000-1,000,000", "Production-ready agent + eval pack"],
            ["Production hardening", "MAICPP + partner", "by partner", "Scale + run-rate governance"],
            ["Quarterly attestation", "Customer + Microsoft", "n/a", "Refreshed AGSA-ready evidence pack"],
        ],
        "reference": "Tier-1 SA bank - Banking CX Agent (ACC-1) production case",
        "reference_note": "Tier-1 bank scaled contact-centre agent from 90-day pilot to 1.2M monthly customer interactions; cost-per-call reduced 32%; FSCA TCF complaint rate held flat. Reference available under NDA via account team.",
        "accelerators": [
            "ACC-1 Banking CX Agent - end-to-end Copilot Studio + Foundry blueprint for tier-1.",
            "ACC-2 POPIA Landing Zone - Azure Policy initiative + Purview baseline for regulated workloads.",
            "ACC-4 Regulated-Industry Pilot Kit - Gate-2 pre-pilot workshop pack.",
            "ACC-5 DocIntel + Foundry Pattern - KYC / claims / contract processing blueprint.",
            "AI-CoE-AI-Impact-Assessment.xlsx - per-use-case governance working tool.",
            "AI-CoE-AI-TCO-Calculator.xlsx - per-token vs per-seat trade-off (issue #8).",
        ],
        "close_headline": "From envisioning to production agent in 8-12 weeks, governance-clean.",
        "close_actions": [
            "Book the Envision workshop (ECIF-funded, $50K).",
            "Nominate one tier-1 use-case + one document-processing use-case to run in parallel.",
            "Bring CISO + DPO + Internal Audit to Gate 2 - that is when value compounds.",
            "Use the TCO Calculator before committing seat counts; cross-over usually at 15-20 queries/user/day.",
        ],
    },
    {
        "name": "Retail & Consumer Goods",
        "filename": "AI-CoE-Sector-Briefing-Retail.pptx",
        "tagline": "AI for omnichannel CX, supply-chain resilience, and store operations",
        "context_lead": "RSA retail: thin margins, POPIA + PCI-DSS overlap, supply-chain volatility, omnichannel CX expectation gap.",
        "context_points": [
            "Top-5 SA retailers chasing single-digit gross-margin pickup - AI in supply chain is board-priority.",
            "POPIA + PCI-DSS overlap on payment-personal-data; AI use-cases must respect both.",
            "Store-ops Copilot for managers is the highest-engagement first wave (Teams + M365 already deployed).",
            "Omnichannel CX: AI co-pilot reduces returns + abandonment; instrument carefully or you create new complaint vectors.",
            "Loyalty data + personalisation: Consumer Protection Act + POPIA constrain segmentation models.",
            "Mobile-first market - WhatsApp / SMS channels for CX agents are non-negotiable.",
        ],
        "regulators": [
            "Information Regulator - POPIA (data subject rights, marketing opt-in)",
            "PCI-DSS (card-not-present + tokenisation)",
            "Consumer Protection Act (CPA) - automated-decision disclosure",
            "Competition Commission - pricing-algorithm scrutiny",
            "Department of Trade, Industry & Competition - B-BBEE supply scoring",
            "FSCA - if private-label credit",
        ],
        "frameworks": [
            "Microsoft RAI v2",
            "ISO/IEC 42001:2023",
            "NIST AI RMF 1.0",
            "PCI-DSS v4",
            "Microsoft WAF (Retail)",
            "Cloud Adoption Framework - Retail",
        ],
        "use_cases": [
            {
                "title": "Omnichannel CX agent",
                "surface": "Copilot Studio + Foundry",
                "value": "25-35% deflection from human",
                "does": [
                    "Order status + returns initiation",
                    "Loyalty redemption + tier guidance",
                    "Product recommendation grounded in catalogue",
                    "WhatsApp / web / app channels unified",
                ],
                "controls": ["POPIA opt-in check; PCI-DSS tokenised reads only; HITL on refunds > threshold"],
            },
            {
                "title": "Supply-chain reasoning agent",
                "surface": "Azure AI Foundry",
                "value": "Stock-out reduction 15-25%",
                "does": [
                    "Demand-signal synthesis (POS + weather + events)",
                    "Replenishment recommendation with rationale",
                    "Supplier-risk scoring",
                    "Buyer co-pilot for category-management review",
                ],
                "controls": ["Reasoning trace; planner HITL; Defender posture"],
            },
            {
                "title": "Store-ops Copilot",
                "surface": "M365 Copilot + Copilot Studio",
                "value": "1-2 hr/manager/day",
                "does": [
                    "Shift planning over Teams Shifts",
                    "Compliance check-in templates",
                    "Incident reporting with auto-classification",
                    "Daily-flash from store KPIs",
                ],
                "controls": ["Purview sensitivity labels; Copilot SOE adoption playbook (ACC-3)"],
            },
        ],
        "arch_lead": "Five-layer reference: omnichannel surfaces over agent orchestration over a retail data foundation, governance-wrapped for POPIA + PCI.",
        "arch": {
            "experience": "M365 Copilot for HQ + store managers; Copilot Studio for WhatsApp / web CX; Power Pages for clienteling.",
            "orchestration": "Copilot Studio for CX intents; Foundry for supply-chain reasoning; Logic Apps for events.",
            "reasoning": "gpt-4o-mini default; gpt-4o for supply reasoning; vector index over catalogue + policy.",
            "data": "Fabric + Synapse + Dataverse; POS + loyalty + ERP via APIM; tokenised payment store separate.",
            "governance": "Purview AI Hub; Defender for Cloud AI; PCI tokenisation in scope-restricted VNet; POPIA landing zone.",
        },
        "sov_lead": "POPIA + PCI-DSS together: residency for personal data, network segregation for payment data, both audited by Purview.",
        "sov_points": [
            "SA North + SA West regions; data-zone scoping for personal data.",
            "PCI-CDE in dedicated VNet with private endpoints; quarterly ASV scan.",
            "Tokenisation surface excludes raw PAN from model inputs.",
            "POPIA opt-in stored in Dataverse; AI prompts gated on consent state.",
            "Purview AI Hub provides reasoning trace for Information Regulator + PCI assessor.",
            "Defender for Cloud AI surfaces shadow-AI in marketing tools.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "CX + supply-chain use-case shortlist"],
            ["Store-ops pilot (6 wk)", "ECIF + ACO", "150,000", "Manager Copilot adoption + KPI baseline"],
            ["CX agent pilot (10 wk)", "ATO + partner", "400,000-800,000", "WhatsApp agent + reasoning eval"],
            ["Supply-chain pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "Category-management co-pilot"],
            ["Production run-rate", "MAICPP + partner", "by partner", "Scale + FinOps + governance"],
        ],
        "reference": "Top-5 SA omnichannel retailer - store-ops Copilot adoption",
        "reference_note": "Adoption cohort of 800 store managers reached 65% weekly active in 90 days; self-reported 90 minutes/day recovered; CSAT held flat. Reference under NDA via account team.",
        "accelerators": [
            "ACC-3 M365 Copilot SOE Adoption Playbook - the store-ops adoption path.",
            "ACC-2 POPIA Landing Zone - PCI + POPIA dual-control foundation.",
            "ACC-5 DocIntel + Foundry Pattern - returns + invoice reconciliation.",
            "AI-CoE-AI-Impact-Assessment.xlsx - per-use-case governance.",
            "AI-CoE-AI-TCO-Calculator.xlsx - per-seat vs per-token for CX agent.",
        ],
        "close_headline": "Stand up store-ops Copilot first; let the wins fund the agent build.",
        "close_actions": [
            "Book the Envision workshop ($50K ECIF).",
            "Launch ACC-3 SOE Copilot for store managers in parallel with envisioning.",
            "Reserve CX agent for week 6 onwards - WhatsApp integration takes runway.",
            "Use TCO calculator to choose per-seat vs per-token for the agent build.",
        ],
    },
    {
        "name": "Telco",
        "filename": "AI-CoE-Sector-Briefing-Telco.pptx",
        "tagline": "AI for network ops, customer-care, and OSS/BSS modernisation",
        "context_lead": "RSA telco: spectrum scarcity, churn pressure, OSS/BSS aging, and a regulator focused on consumer outcomes.",
        "context_points": [
            "Three big operators competing on network quality + price; AIOps in the NOC is the operating-cost lever.",
            "Churn AI: predictive + agent-assisted retention is the highest near-term ROI for the CX team.",
            "OSS/BSS modernisation: AI doesn't replace the stack, it wraps it - Foundry agents over API gateway.",
            "ICASA: consumer-protection scrutiny on automated decisions in billing / disconnection.",
            "RICA: subscriber-identity controls extend to AI components touching that data.",
            "Mobile-money / fintech adjacency - SARB / FSCA controls also apply where relevant.",
        ],
        "regulators": [
            "ICASA - End-User & Subscriber Service Charter regulations",
            "RICA - subscriber identity registration",
            "Information Regulator - POPIA",
            "SARB / FSCA - where mobile-money / fintech is in scope",
            "Competition Commission - pricing + bundle scrutiny",
            "National Treasury - if SOE telco",
        ],
        "frameworks": [
            "Microsoft RAI v2",
            "ISO/IEC 42001:2023",
            "NIST AI RMF 1.0",
            "TM Forum AI maturity model",
            "ETSI ZSM - zero-touch network management",
            "Microsoft Cloud for Sovereignty",
        ],
        "use_cases": [
            {
                "title": "Network AIOps co-pilot",
                "surface": "Foundry + Sentinel + Log Analytics",
                "value": "MTTR reduction 30-40%",
                "does": [
                    "Alarm correlation + root-cause hypothesis",
                    "Run-book retrieval + suggested next-step",
                    "Change-window guidance",
                    "Post-incident write-up draft",
                ],
                "controls": ["Reasoning trace; HITL on production changes; Defender for Cloud"],
            },
            {
                "title": "Customer-care agent",
                "surface": "Copilot Studio + Foundry",
                "value": "AHT reduction 25-35%",
                "does": [
                    "Account + billing inquiry resolution",
                    "Plan-change with eligibility check",
                    "Network-issue triage + ticket creation",
                    "WhatsApp / app / IVR channels",
                ],
                "controls": ["ICASA charter eval slice; HITL on disconnection; POPIA opt-in"],
            },
            {
                "title": "OSS/BSS reasoning agent",
                "surface": "Azure AI Foundry over API gateway",
                "value": "Order-to-activate 50% faster",
                "does": [
                    "Order validation across product catalogue + inventory",
                    "Provisioning orchestration with error reasoning",
                    "SLA breach prediction + escalation draft",
                    "Workforce-management co-pilot",
                ],
                "controls": ["Reasoning trace; APIM rate-limits; SOC2-aligned controls"],
            },
        ],
        "arch_lead": "Five-layer reference: care + ops surfaces over agent orchestration over OSS/BSS API gateway + telemetry lake.",
        "arch": {
            "experience": "Copilot Studio for care channels; M365 Copilot for ops; Teams + Power Pages for HITL queues.",
            "orchestration": "Foundry orchestrators for OSS/BSS + AIOps; Copilot Studio for care intents.",
            "reasoning": "gpt-4o-mini default; gpt-4o for AIOps reasoning; vector index over run-books + tariffs.",
            "data": "Fabric + Synapse + Event Hubs; OSS/BSS exposed via APIM; telemetry via Log Analytics + Sentinel.",
            "governance": "Purview AI Hub; Defender for Cloud AI; POPIA + RICA controls; APIM policy enforcement.",
        },
        "sov_lead": "POPIA + RICA + ICASA charter form the governance perimeter; Foundry data-zone gives the residency story.",
        "sov_points": [
            "SA North + SA West dual-region for network-critical services.",
            "Foundry data-zone scoping for SA-resident subscriber data.",
            "Customer-Managed Keys; private endpoints; VNet integration.",
            "Purview AI Hub for reasoning trace; ICASA + Information Regulator audit-ready.",
            "Defender for Cloud AI surfaces shadow-AI in care / marketing tools.",
            "RICA-protected identity data tokenised before model input.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "AIOps + care use-case shortlist"],
            ["AIOps pilot (10 wk)", "ATO + partner", "400,000-800,000", "NOC co-pilot in 1 region"],
            ["Care agent pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "WhatsApp + web care agent"],
            ["OSS/BSS pilot (12 wk)", "ATO + partner", "750,000-1,000,000", "Order-to-activate agent"],
            ["Production run-rate", "MAICPP + partner", "by partner", "Scale + FinOps + governance"],
        ],
        "reference": "RSA mobile operator - care agent + AIOps co-pilot pilots",
        "reference_note": "12-week care agent pilot deflected 28% of inbound from human; AIOps co-pilot reduced sev-2 MTTR by 36%. Reference under NDA via account team.",
        "accelerators": [
            "ACC-1 Banking CX Agent - architectural pattern reusable for telco care.",
            "ACC-2 POPIA Landing Zone - foundation for RICA-protected data.",
            "ACC-4 Regulated-Industry Pilot Kit - ICASA + RICA scoping.",
            "ACC-5 DocIntel + Foundry Pattern - bill explanation + complaint triage.",
            "AI-CoE-AI-Impact-Assessment.xlsx - per-use-case governance.",
            "AI-CoE-AI-TCO-Calculator.xlsx - per-token costing for high-volume care.",
        ],
        "close_headline": "AIOps first - own the NOC story; care agent compounds it.",
        "close_actions": [
            "Book the Envision workshop ($50K ECIF).",
            "Anchor on AIOps - the operating-cost story is the easiest CFO win.",
            "Sequence care agent after AIOps; reuse the orchestration patterns.",
            "Bring ICASA + RICA into Gate 2 - regulator-readiness is the moat.",
        ],
    },
    {
        "name": "Mining",
        "filename": "AI-CoE-Sector-Briefing-Mining.pptx",
        "tagline": "AI for safety, ESG reporting, and predictive operations",
        "context_lead": "RSA mining: MHSA-driven safety obligation, ESG-driven disclosure obligation, capex-heavy operations where prediction is leverage.",
        "context_points": [
            "MHSA safety regime makes every incident regulator-actionable - AI must support, not replace, the SHE function.",
            "ESG disclosure (JSE + GRI + ISSB) is now data-intensive; AI co-pilots for sustainability reporting are board-priority.",
            "Predictive maintenance on haul trucks + crushers is the highest-ROI operations AI use-case.",
            "Geological reasoning agents over historical core + assay data shorten exploration cycles.",
            "Workforce safety: edge AI for hazard detection (PPE, exclusion zones) is mature; cloud is for reasoning + reporting.",
            "DMRE oversight is data-driven - regulator engagement increasingly relies on auditable submissions.",
        ],
        "regulators": [
            "DMRE (Department of Mineral Resources & Energy)",
            "MHSA (Mine Health & Safety Act) - DMR Inspectorate",
            "AGSA - if state-affiliated entity",
            "DFFE - environmental authorisation",
            "Information Regulator - POPIA",
            "JSE / ISSB - sustainability disclosure",
        ],
        "frameworks": [
            "Microsoft RAI v2",
            "ISO/IEC 42001:2023",
            "ISO 45001 + 14001 (SHE)",
            "GRI Standards + ISSB",
            "NIST AI RMF 1.0",
            "Microsoft Industry Cloud (Sustainability + Mining patterns)",
        ],
        "use_cases": [
            {
                "title": "Safety & ESG reporting co-pilot",
                "surface": "M365 Copilot + Foundry",
                "value": "Reporting cycle 60% faster",
                "does": [
                    "Synthesise incident + observation data",
                    "Draft DMRE submissions with citations",
                    "GRI / ISSB-aligned narrative drafting",
                    "Trend reasoning over 12-month window",
                ],
                "controls": ["Reasoning trace; SHE-officer HITL; Purview AI Hub log"],
            },
            {
                "title": "Predictive maintenance reasoning",
                "surface": "Foundry + IoT + Fabric",
                "value": "Unplanned downtime -25%",
                "does": [
                    "Telemetry pattern synthesis (vibration / heat / load)",
                    "Failure-mode hypothesis with confidence",
                    "Work-order draft for planner",
                    "Spares pre-positioning recommendation",
                ],
                "controls": ["HITL on shutdown decision; Defender posture; cost guard-rails"],
            },
            {
                "title": "Geological reasoning agent",
                "surface": "Azure AI Foundry over IP-protected corpus",
                "value": "Exploration cycle 30% shorter",
                "does": [
                    "Historical core + assay synthesis",
                    "Drill-target recommendation with rationale",
                    "Resource-classification co-pilot for CRIRSCO / SAMREC",
                    "Cross-tenement comparison",
                ],
                "controls": ["IP-sensitive corpus in CMK-encrypted store; reasoning trace; restricted access"],
            },
        ],
        "arch_lead": "Five-layer reference: SHE + ops + geology surfaces over agents over telemetry + ERP + IP corpus.",
        "arch": {
            "experience": "M365 Copilot for SHE + reporting; Power Apps for incident capture; Teams for shift handover.",
            "orchestration": "Foundry agents for predictive + geological reasoning; Copilot Studio for SHE intents.",
            "reasoning": "gpt-4o for geological reasoning; gpt-4o-mini default; vector index over IP-protected corpus.",
            "data": "Fabric + Synapse + Event Hubs (IoT); SAP / ERP via APIM; CMK-encrypted IP corpus.",
            "governance": "Purview AI Hub; Defender for Cloud AI; MHSA + ISO 45001 + 14001 controls.",
        },
        "sov_lead": "IP protection on geological data + MHSA on safety: sovereignty is operational, not optional.",
        "sov_points": [
            "SA North + SA West dual-region; geological IP in CMK-encrypted store with private endpoints.",
            "Foundry data-zone scoping for SA-resident operational data.",
            "Reasoning trace for DMRE + AGSA + audit firm review.",
            "Defender for Cloud AI surfaces shadow-AI in engineering tools.",
            "Quarterly attestation via the Impact Assessment workbook.",
            "Air-gapped option (sovereign AI cloud) available for state-affiliated operators.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "Safety + ops + geology shortlist"],
            ["Safety/ESG co-pilot (8 wk)", "ECIF + ACO", "250,000", "Reporting cycle prototype"],
            ["Predictive maintenance (12 wk)", "ATO + partner", "500,000-1,000,000", "Pilot on 1 site / 1 fleet"],
            ["Geological pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "Reasoning agent over 1 tenement"],
            ["Production run-rate", "MAICPP + partner", "by partner", "Scale + FinOps + governance"],
        ],
        "reference": "SA-listed diversified miner - safety + ESG reporting co-pilot",
        "reference_note": "DMRE submission cycle reduced from 14 to 5 days; SHE-officer satisfaction up; auditor-sample pass-rate 100%. Reference under NDA via account team.",
        "accelerators": [
            "ACC-3 M365 Copilot SOE Adoption - the SHE-team adoption path.",
            "ACC-2 POPIA Landing Zone - foundation for personal + operational data.",
            "ACC-4 Regulated-Industry Pilot Kit - DMRE + MHSA scoping.",
            "ACC-5 DocIntel + Foundry Pattern - incident-report processing.",
            "AI-CoE-AI-Impact-Assessment.xlsx - per-use-case governance.",
            "AI-CoE-AI-TCO-Calculator.xlsx - cost forecast for IoT-driven workloads.",
        ],
        "close_headline": "Safety + ESG first - the regulator wins fund the operations build.",
        "close_actions": [
            "Book the Envision workshop ($50K ECIF).",
            "Anchor on safety + ESG co-pilot - DMRE-facing wins compound.",
            "Sequence predictive maintenance once IoT telemetry is in Fabric.",
            "Reserve geological reasoning for tenement-by-tenement rollout; IP controls first.",
        ],
    },
    {
        "name": "Public Sector & SOE",
        "filename": "AI-CoE-Sector-Briefing-Public-Sector.pptx",
        "tagline": "AI for citizen services, document workflows, and PFMA-grade accountability",
        "context_lead": "RSA public sector: PFMA/MFMA accountability, AGSA scrutiny, citizen-facing service backlogs, and the highest bar on sovereignty.",
        "context_points": [
            "PFMA + MFMA make accounting officers personally accountable - AI introductions must produce evidence, not just outcomes.",
            "AGSA's audit findings drive board-level urgency; AI is being approached as an audit-readiness investment.",
            "Citizen-facing service backlogs (Home Affairs, SARS, SASSA) make conversational + document agents the highest-leverage wins.",
            "National Treasury procurement frameworks make ATO + ECIF + MAICPP the natural commercial path.",
            "Sovereignty: data residency in SA is mandatory for most departments; some workloads require air-gap option.",
            "Skills constraint is the throttle; partner-led delivery with strong Microsoft technical underpin is the operating shape.",
        ],
        "regulators": [
            "AGSA - Auditor-General of South Africa",
            "National Treasury - PFMA + MFMA + SCM frameworks",
            "Information Regulator - POPIA",
            "Department of Communications - DPSA AI guideline",
            "SITA (where applicable) - government IT framework",
            "Accounting officer / accounting authority (entity level)",
        ],
        "frameworks": [
            "Microsoft RAI v2",
            "ISO/IEC 42001:2023",
            "NIST AI RMF 1.0",
            "Microsoft Cloud for Sovereignty",
            "WAF + CAF (Government)",
            "DPSA Guidelines on AI Adoption",
        ],
        "use_cases": [
            {
                "title": "Citizen services agent",
                "surface": "Copilot Studio + Foundry",
                "value": "First-contact resolution +30%",
                "does": [
                    "Service-status enquiry + next-step guidance",
                    "Document-required checklist by service",
                    "Appointment booking + reminders",
                    "WhatsApp / web / IVR channels",
                ],
                "controls": ["POPIA opt-in; Purview AI Hub log; HITL on regulated decisions"],
            },
            {
                "title": "Document workflow co-pilot",
                "surface": "Azure AI Foundry + DocIntel",
                "value": "Cycle time 60-80% reduction",
                "does": [
                    "Extract + classify incoming submissions",
                    "Compliance check against policy / regulation",
                    "Routing + assignment to officer queue",
                    "Reasoning trace for AGSA sample",
                ],
                "controls": ["CMK; private endpoint; auditor-grade trace; HITL on edge cases"],
            },
            {
                "title": "Programme-management co-pilot",
                "surface": "M365 Copilot + Copilot Studio",
                "value": "1-2 hr/officer/day",
                "does": [
                    "Drafting briefing notes from source documents",
                    "Risk-register synthesis across programmes",
                    "AGSA-finding cross-reference + remediation tracking",
                    "Audit-readiness pack assembly",
                ],
                "controls": ["Purview labels; sensitivity-aware grounding; Copilot SOE adoption path"],
            },
        ],
        "arch_lead": "Five-layer reference: citizen + officer surfaces over agents over departmental data + workflow systems, all under PFMA-grade controls.",
        "arch": {
            "experience": "M365 Copilot for officers; Copilot Studio for citizen channels; Power Pages for HITL + portals.",
            "orchestration": "Foundry orchestrators for document + reasoning; Copilot Studio for service intents.",
            "reasoning": "gpt-4o-mini default; gpt-4o for reasoning; vector index over policy + regulation corpus.",
            "data": "Fabric + Synapse + Dataverse; departmental systems via APIM; CMK-encrypted citizen-data store.",
            "governance": "Purview AI Hub; Defender for Cloud AI; AGSA-ready evidence pack; sovereign cloud option.",
        },
        "sov_lead": "PFMA accountability + POPIA residency + AGSA audit posture: sovereignty is the entry condition.",
        "sov_points": [
            "SA North + SA West dual-region default; sovereign / air-gapped option for sensitive workloads.",
            "Customer-Managed Keys; private endpoints; VNet isolation.",
            "Purview AI Hub provides AGSA-ready reasoning trace.",
            "Defender for Cloud AI surfaces shadow-AI in officer toolchains.",
            "Quarterly attestation via Impact Assessment workbook - signed by accounting officer.",
            "Use AI-CoE-Sovereign-AI-RSA.pptx as the long-form companion when DPSA / AGSA ask for depth.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "Service + document use-case shortlist"],
            ["Officer Copilot adoption", "ECIF + ACO", "200,000", "1-2 directorates, AGSA-readiness focus"],
            ["Document pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "Production-ready document agent"],
            ["Citizen agent pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "WhatsApp + web service agent"],
            ["Production + attestation", "MAICPP + partner", "by partner", "Scale + AGSA-ready quarterly pack"],
        ],
        "reference": "RSA national department - document workflow co-pilot",
        "reference_note": "Document cycle reduced from 12 to 4 days on 60K monthly submissions; AGSA auditor-sample pass-rate 100%; accounting-officer attestation signed. Reference under NDA via account team.",
        "accelerators": [
            "ACC-2 POPIA Landing Zone - the foundation under everything here.",
            "ACC-3 M365 Copilot SOE Adoption - officer adoption path.",
            "ACC-4 Regulated-Industry Pilot Kit - PFMA + AGSA scoping.",
            "ACC-5 DocIntel + Foundry Pattern - document workflow blueprint.",
            "AI-CoE-AI-Impact-Assessment.xlsx + AI-CoE-AI-Governance-Playbook.docx - the AGSA-ready governance pack.",
            "AI-CoE-Sovereign-AI-RSA.pptx - long-form sovereignty companion.",
        ],
        "close_headline": "Officer Copilot adoption first - AGSA-readiness compounds from day one.",
        "close_actions": [
            "Book the Envision workshop ($50K ECIF).",
            "Stand up officer Copilot adoption in parallel with envisioning.",
            "Sequence document workflow agent before citizen agent - lower risk, higher AGSA leverage.",
            "Bring AGSA-aligned Internal Audit into Gate 2 - that is the trust moment.",
        ],
    },
    {
        "name": "Healthcare",
        "filename": "AI-CoE-Sector-Briefing-Healthcare.pptx",
        "tagline": "AI for clinical documentation, pre-authorisation, and medical-scheme rules",
        "context_lead": "RSA healthcare: HPCSA-regulated clinical decisions, NHI in flight, capacity-constrained workforce, medical-scheme rule complexity.",
        "context_points": [
            "HPCSA: any AI that touches clinical reasoning must remain clearly clinician-assistive, not clinician-replacing.",
            "NHI roll-in: medical schemes + private providers face regulatory uncertainty; AI investments must be NHI-portable.",
            "Clinical documentation burden is the #1 clinician complaint - ambient + drafted notes are the highest-trust first wave.",
            "Pre-authorisation cycle times drive patient + clinician + scheme frustration in equal measure.",
            "Medical-scheme rule complexity: AI co-pilots for benefit reasoning are high-value, high-risk.",
            "Workforce capacity: nurse + allied-health productivity matters as much as physician productivity.",
        ],
        "regulators": [
            "HPCSA - Health Professions Council",
            "National Department of Health - NHI + facility licensing",
            "Council for Medical Schemes",
            "SAHPRA - if device-classified",
            "Information Regulator - POPIA (special-category data)",
            "Office of Health Standards Compliance",
        ],
        "frameworks": [
            "Microsoft RAI v2",
            "ISO/IEC 42001:2023",
            "NIST AI RMF 1.0",
            "ISO 27799 (health information security)",
            "HL7 FHIR (interoperability)",
            "Microsoft Cloud for Healthcare",
        ],
        "use_cases": [
            {
                "title": "Clinical documentation co-pilot",
                "surface": "M365 Copilot + Foundry",
                "value": "1-2 hr/clinician/day",
                "does": [
                    "Ambient encounter capture",
                    "Drafted SOAP note for clinician review",
                    "Coding suggestion (ICD-10 / CPT)",
                    "Patient-facing visit summary draft",
                ],
                "controls": ["Clinician-always-in-the-loop; HPCSA-aligned eval; POPIA special-category controls"],
            },
            {
                "title": "Pre-authorisation co-pilot",
                "surface": "Azure AI Foundry + DocIntel",
                "value": "Cycle time -60%",
                "does": [
                    "Submission completeness check",
                    "Medical-scheme rule reasoning with citation",
                    "Outcome draft with rationale for HITL",
                    "Appeals package assembly",
                ],
                "controls": ["HITL on adverse decisions; reasoning trace; CMS-aligned audit log"],
            },
            {
                "title": "Operations + scheduling co-pilot",
                "surface": "M365 Copilot + Copilot Studio",
                "value": "OT block utilisation +5-10%",
                "does": [
                    "Block-utilisation reasoning + reschedule suggestion",
                    "Staffing co-pilot",
                    "Supply demand forecasting",
                    "Quality metric synthesis",
                ],
                "controls": ["Purview labels; non-clinical scope; Copilot SOE adoption"],
            },
        ],
        "arch_lead": "Five-layer reference: clinical + admin surfaces over agents over FHIR + EMR + scheme-rule corpus, under POPIA special-category controls.",
        "arch": {
            "experience": "M365 Copilot for clinicians + admin; Copilot Studio for patient channels; Power Pages for HITL queues.",
            "orchestration": "Foundry orchestrators for clinical + pre-auth reasoning; Copilot Studio for patient intents.",
            "reasoning": "gpt-4o for clinical reasoning; gpt-4o-mini default; vector index over scheme rules + protocols.",
            "data": "Fabric + Synapse + Dataverse Healthcare; EMR via FHIR endpoints; CMK-encrypted clinical data.",
            "governance": "Purview AI Hub; Defender for Cloud AI; POPIA special-category controls; clinician HITL by default.",
        },
        "sov_lead": "POPIA special-category data + HPCSA clinician accountability define the governance perimeter; sovereignty is the operating constraint.",
        "sov_points": [
            "SA North + SA West regions; data-zone scoping for clinical data.",
            "Customer-Managed Keys in HSM; private endpoints; VNet integration.",
            "Clinician-always-in-the-loop on diagnostic suggestion; HPCSA-aligned eval slices.",
            "Purview AI Hub provides reasoning trace for HPCSA + Council for Medical Schemes review.",
            "Defender for Cloud AI surfaces shadow-AI in clinician toolchains.",
            "Quarterly attestation; clinician + DPO + Internal Audit sign-off.",
        ],
        "engagement": [
            ["Envision workshop", "Pre-sales ECIF", "50,000", "Clinical + admin shortlist"],
            ["Documentation pilot (10 wk)", "ATO + partner", "400,000-800,000", "Production-ready ambient + drafted notes"],
            ["Pre-auth pilot (12 wk)", "ATO + partner", "500,000-1,000,000", "Production-ready pre-auth agent"],
            ["Operations Copilot adoption", "ECIF + ACO", "200,000", "Non-clinical productivity"],
            ["Production + attestation", "MAICPP + partner", "by partner", "Scale + governance"],
        ],
        "reference": "RSA private hospital group - clinical documentation co-pilot pilot",
        "reference_note": "12-week pilot with 60 clinicians; self-reported 90 minutes/day recovered; clinician satisfaction +40 NPS points; HPCSA-aligned eval passed. Reference under NDA via account team.",
        "accelerators": [
            "ACC-3 M365 Copilot SOE Adoption - clinician + admin adoption path.",
            "ACC-2 POPIA Landing Zone - special-category data foundation.",
            "ACC-4 Regulated-Industry Pilot Kit - HPCSA + CMS scoping.",
            "ACC-5 DocIntel + Foundry Pattern - pre-auth + claims processing.",
            "AI-CoE-AI-Impact-Assessment.xlsx - per-use-case governance (special-category emphasis).",
            "AI-CoE-AI-TCO-Calculator.xlsx - per-token vs per-seat for clinician workloads.",
        ],
        "close_headline": "Clinical documentation first - clinician trust compounds every other use-case.",
        "close_actions": [
            "Book the Envision workshop ($50K ECIF).",
            "Anchor on documentation co-pilot - the clinician-trust win unlocks pre-auth.",
            "Sequence pre-auth pilot after documentation; reuse the reasoning + HITL patterns.",
            "Bring HPCSA-aligned clinical lead into Gate 2 - clinician sign-off is the moat.",
        ],
    },
]


def main() -> None:
    produced = []
    for sector in SECTORS:
        out = build_deck(sector)
        produced.append(out.name)
    print("Wrote:")
    for n in produced:
        print(f"  {n}")


if __name__ == "__main__":
    main()
