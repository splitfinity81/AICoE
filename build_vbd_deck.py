"""Build the AI CoE VBD Reference Deck.

Generates AI-CoE-VBD-Reference-Deck.pptx from csu-ai-vbd-reference-report.md.
Each VBD is articulated with Key Outcomes and Contribution to the AI CoE
(5+1 pillars x 3-tier ladder x MCEM 1-5).

Author: Yuri Baijnath - CSU Cloud & AI Lead (South Africa)
"""

from __future__ import annotations

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

# ---------------------------------------------------------------------------
# Theme - aligned to AI-CoE-Pitch-Deck style canon
# ---------------------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

C_BG       = RGBColor(0xFF, 0xFF, 0xFF)
C_INK      = RGBColor(0x1A, 0x1A, 0x1A)
C_MUTED    = RGBColor(0x55, 0x55, 0x55)
C_RULE     = RGBColor(0xD0, 0xD0, 0xD0)
C_ACCENT   = RGBColor(0x00, 0x67, 0xB8)   # Microsoft blue
C_ACCENT2  = RGBColor(0x50, 0xE6, 0xFF)   # Azure cyan
C_HIGHLIGHT= RGBColor(0x74, 0x2A, 0x9B)   # Copilot purple
C_GOOD     = RGBColor(0x10, 0x7C, 0x10)
C_WARN     = RGBColor(0xB7, 0x6E, 0x00)
C_BAND     = RGBColor(0xF3, 0xF6, 0xFA)
C_BAND2    = RGBColor(0xE8, 0xEE, 0xF7)
C_DARK     = RGBColor(0x0B, 0x1F, 0x3A)

TOTAL_SLIDES = 25  # used in footer N / 25; updated after build if drift

# ---------------------------------------------------------------------------
# Primitives
# ---------------------------------------------------------------------------

def add_rect(slide, x, y, w, h, fill, line=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
    shape.shadow.inherit = False
    return shape


def add_text(slide, x, y, w, h, text, *, size=14, bold=False, color=C_INK,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False,
             font="Segoe UI"):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.margin_left = Inches(0.0)
    tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0)
    tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run()
        r.text = line
        r.font.name = font
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def add_bullets(slide, x, y, w, h, items, *, size=14, color=C_INK,
                bullet_color=C_ACCENT, line_spacing=1.15):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.0)
    tf.margin_top = Inches(0.0)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = line_spacing
        r1 = p.add_run()
        r1.text = "\u2022  "
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(size)
        r1.font.bold = True
        r1.font.color.rgb = bullet_color
        r2 = p.add_run()
        r2.text = item
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(size)
        r2.font.color.rgb = color
    return tb


def add_section_tag(slide, text, color=C_ACCENT):
    add_text(slide, Inches(0.6), Inches(0.35), Inches(8), Inches(0.3),
             text.upper(), size=11, bold=True, color=color)


def add_title(slide, title, subtitle=None):
    add_text(slide, Inches(0.6), Inches(0.65), Inches(12.2), Inches(0.8),
             title, size=30, bold=True, color=C_INK)
    if subtitle:
        add_text(slide, Inches(0.6), Inches(1.45), Inches(12.2), Inches(0.5),
                 subtitle, size=14, color=C_MUTED)


def add_footer(slide, slide_no):
    # Top rule
    add_rect(slide, Inches(0.6), Inches(0.28), Inches(12.13), Emu(9000),
             C_RULE)
    # Bottom rule + footer text
    add_rect(slide, Inches(0.6), Inches(7.05), Inches(12.13), Emu(9000),
             C_RULE)
    add_text(slide, Inches(0.6), Inches(7.12), Inches(8), Inches(0.3),
             f"Microsoft \u00b7 Confidential \u00b7 \u00a9 2026 Microsoft Corporation",
             size=9, color=C_MUTED)
    add_text(slide, Inches(10.7), Inches(7.12), Inches(2.0), Inches(0.3),
             f"{slide_no} / {TOTAL_SLIDES}",
             size=9, color=C_MUTED, align=PP_ALIGN.RIGHT)


def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])  # blank


def add_table(slide, x, y, w, h, headers, rows, *,
              header_fill=C_DARK, header_color=C_BG,
              header_size=11, body_size=10,
              col_widths=None, row_height=None,
              first_col_bold=True, alt_band=True):
    """Build a styled table. headers: list[str]; rows: list[list[str]]."""
    n_cols = len(headers)
    n_rows = len(rows) + 1
    tbl_shape = slide.shapes.add_table(n_rows, n_cols, x, y, w, h)
    tbl = tbl_shape.table
    if col_widths:
        total = sum(col_widths)
        for i, cw in enumerate(col_widths):
            tbl.columns[i].width = int(w * cw / total)
    if row_height:
        for r in tbl.rows:
            r.height = row_height
    # header
    for j, htext in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = header_fill
        cell.margin_left = Inches(0.08)
        cell.margin_right = Inches(0.08)
        cell.margin_top = Inches(0.04)
        cell.margin_bottom = Inches(0.04)
        tf = cell.text_frame
        tf.word_wrap = True
        tf.clear()
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = htext
        r.font.name = "Segoe UI"
        r.font.size = Pt(header_size)
        r.font.bold = True
        r.font.color.rgb = header_color
    # body
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_BAND if (alt_band and i % 2 == 0) else C_BG
            cell.margin_left = Inches(0.08)
            cell.margin_right = Inches(0.08)
            cell.margin_top = Inches(0.03)
            cell.margin_bottom = Inches(0.03)
            tf = cell.text_frame
            tf.word_wrap = True
            tf.clear()
            p = tf.paragraphs[0]
            r = p.add_run()
            r.text = str(val)
            r.font.name = "Segoe UI"
            r.font.size = Pt(body_size)
            r.font.color.rgb = C_INK
            r.font.bold = first_col_bold and (j == 0)
    return tbl


# ---------------------------------------------------------------------------
# Slide builders
# ---------------------------------------------------------------------------

def build_title(prs):
    s = new_slide(prs)
    # Background band
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, C_BG)
    add_rect(s, 0, Inches(5.6), SLIDE_W, Inches(1.9), C_DARK)
    # Eyebrow
    add_text(s, Inches(0.7), Inches(0.7), Inches(10), Inches(0.4),
             "AI CENTER OF EXCELLENCE \u00b7 VBD REFERENCE",
             size=12, bold=True, color=C_ACCENT)
    # Title
    add_text(s, Inches(0.7), Inches(1.3), Inches(12), Inches(1.4),
             "The AI VBD Playbook",
             size=54, bold=True, color=C_INK)
    add_text(s, Inches(0.7), Inches(2.7), Inches(12), Inches(1.4),
             "Outcomes of every CSU-deliverable AI VBD and how each\nadvances the AI Centre of Excellence",
             size=22, color=C_MUTED)
    # Pull-quote
    add_text(s, Inches(0.7), Inches(4.6), Inches(12), Inches(0.8),
             "5+1 pillars \u00b7 3-tier ladder \u00b7 MCEM 1\u20135 \u00b7 FY26 H2 RSA CSU",
             size=14, italic=True, color=C_HIGHLIGHT)
    # Signature band
    add_text(s, Inches(0.7), Inches(5.85), Inches(12), Inches(0.4),
             "Yuri Baijnath", size=18, bold=True, color=C_BG)
    add_text(s, Inches(0.7), Inches(6.25), Inches(12), Inches(0.4),
             "CSU Cloud & AI Lead (South Africa)  \u00b7  Yuri.Baijnath@microsoft.com  \u00b7  Microsoft",
             size=12, color=C_ACCENT2)
    add_text(s, Inches(0.7), Inches(6.7), Inches(12), Inches(0.4),
             "Source: csu-ai-vbd-reference-report.md  \u00b7  Re-verify VERIFY-flagged items on MCAPS Catalog before customer commit",
             size=10, italic=True, color=C_RULE)


def build_agenda(prs):
    s = new_slide(prs)
    add_section_tag(s, "Agenda")
    add_title(s, "What you will leave with",
              "A working menu of AI VBDs mapped to outcomes and to the AI CoE")
    items = [
        ("01", "Why this deck", "Articulating outcomes \u00b7 mapping every VBD to the AI CoE"),
        ("02", "The framing", "5+1 pillars \u00d7 3-tier ladder \u00d7 MCEM 1\u20135"),
        ("03", "Family A \u2014 M365 Copilot (MW)", "8 VBDs \u00b7 envisioning, adoption, optimisation, security"),
        ("04", "Family B \u2014 Copilot Studio (BA)", "7 VBDs \u00b7 agents, AI Builder, D365, CoE Starter Kit"),
        ("05", "Family C \u2014 Foundry & Azure (CAI)", "19 VBDs \u00b7 Azure Accelerate, ATO, GenAIOps, RAI"),
        ("06", "Factory engine", "10 zero-cost Cloud Accelerate Factory plays (F1\u2013F10)"),
        ("07", "Cross-CSU", "Frontier AI CoE stand-up, Skilling, Value Realization"),
        ("08", "Synthesis", "Tier x Pillar coverage \u00b7 MCEM sequencing \u00b7 next steps"),
    ]
    y = Inches(2.1)
    for n, t, sub in items:
        add_text(s, Inches(0.7), y, Inches(0.7), Inches(0.5),
                 n, size=20, bold=True, color=C_ACCENT)
        add_text(s, Inches(1.5), y, Inches(4.5), Inches(0.5),
                 t, size=16, bold=True, color=C_INK)
        add_text(s, Inches(6.0), y, Inches(6.8), Inches(0.5),
                 sub, size=13, color=C_MUTED)
        y += Inches(0.55)
    add_footer(s, 2)


def build_why(prs):
    s = new_slide(prs)
    add_section_tag(s, "Why this deck")
    add_title(s, "AI demand is loud. Delivery clarity is the bottleneck.",
              "The CSU has 40+ AI VBDs. Customers do not need a catalogue \u2014 they need outcomes.")
    # Two columns
    add_rect(s, Inches(0.6), Inches(2.1), Inches(5.95), Inches(4.4), C_BAND)
    add_text(s, Inches(0.85), Inches(2.25), Inches(5.5), Inches(0.4),
             "THE PROBLEM", size=11, bold=True, color=C_WARN)
    add_bullets(s, Inches(0.85), Inches(2.65), Inches(5.6), Inches(3.6), [
        "88% of organisations use AI; 2/3 have not scaled \u2014 McKinsey 2025.",
        "60% reap little measurable value \u2014 BCG 2024.",
        "Only 1/3 of workforce trained on AI \u2014 BCG 2024.",
        "AI VBD names alone do not articulate outcomes or CoE fit.",
        "CSAs need a single menu mapping VBD \u2192 outcome \u2192 pillar \u2192 tier \u2192 MCEM.",
    ], size=13, bullet_color=C_WARN)

    add_rect(s, Inches(6.78), Inches(2.1), Inches(5.95), Inches(4.4), C_BAND2)
    add_text(s, Inches(7.03), Inches(2.25), Inches(5.5), Inches(0.4),
             "WHAT THIS DECK DOES", size=11, bold=True, color=C_GOOD)
    add_bullets(s, Inches(7.03), Inches(2.65), Inches(5.6), Inches(3.6), [
        "Lists every CSU-deliverable AI VBD in one place.",
        "For each VBD: Key Outcomes + Contribution to the AI CoE.",
        "Maps each VBD to the 5+1 pillars and the 3-tier ladder.",
        "Sequences VBDs to MCEM 1\u20132, MCEM 3, MCEM 4\u20135.",
        "Flags FY26 H2 VERIFY items for re-check before customer commit.",
    ], size=13, bullet_color=C_GOOD)
    add_footer(s, 3)


def build_framing(prs):
    s = new_slide(prs)
    add_section_tag(s, "The framing")
    add_title(s, "5+1 pillars \u00d7 3-tier ladder \u00d7 MCEM 1\u20135",
              "Every VBD in this deck slots into this grid \u2014 that is what makes it a CoE asset.")
    # Pillars row
    pillars = [
        ("1", "Business Strategy",   "Value cases, P&L, KPIs"),
        ("2", "Org & Culture",       "Skilling, change, comms"),
        ("3", "AI Strategy & XP",    "Use-case design, scenarios"),
        ("4", "Tech & Data",         "Platform, data, agents"),
        ("5", "Governance & Sec",    "Responsible AI, posture"),
        ("+1", "Co-sell & Partner",  "MAICPP, ACO, archetypes"),
    ]
    add_text(s, Inches(0.6), Inches(2.05), Inches(12), Inches(0.3),
             "THE 5+1 PILLARS", size=11, bold=True, color=C_ACCENT)
    px = Inches(0.6); py = Inches(2.4); pw = Inches(2.02); ph = Inches(1.35)
    for i, (n, name, sub) in enumerate(pillars):
        add_rect(s, px, py, pw, ph, C_BAND, line=C_RULE)
        add_text(s, px + Inches(0.12), py + Inches(0.08), pw - Inches(0.2), Inches(0.35),
                 f"Pillar {n}", size=10, bold=True, color=C_HIGHLIGHT)
        add_text(s, px + Inches(0.12), py + Inches(0.4), pw - Inches(0.2), Inches(0.4),
                 name, size=12, bold=True, color=C_INK)
        add_text(s, px + Inches(0.12), py + Inches(0.8), pw - Inches(0.2), Inches(0.5),
                 sub, size=10, color=C_MUTED)
        px += pw + Inches(0.01)

    # Tier ladder
    add_text(s, Inches(0.6), Inches(4.0), Inches(12), Inches(0.3),
             "THE 3-TIER LADDER", size=11, bold=True, color=C_ACCENT)
    tiers = [
        ("T1 Envisioning",  "Inspire, design, pilot. Workshops, assessments, ATO C1.", C_ACCENT2),
        ("T2 Build",        "Foundation + first scaled workload. Azure Accelerate, ATO C2/C3.", C_ACCENT),
        ("T3 Managed Run",  "Operate, optimise, scale. Value realisation, GenAIOps, MSP relay.", C_HIGHLIGHT),
    ]
    tx = Inches(0.6)
    for label, body, col in tiers:
        add_rect(s, tx, Inches(4.35), Inches(4.05), Inches(1.3), C_BG, line=col)
        add_rect(s, tx, Inches(4.35), Inches(4.05), Inches(0.05), col)
        add_text(s, tx + Inches(0.15), Inches(4.5), Inches(3.7), Inches(0.4),
                 label, size=14, bold=True, color=col)
        add_text(s, tx + Inches(0.15), Inches(4.9), Inches(3.7), Inches(0.7),
                 body, size=11, color=C_INK)
        tx += Inches(4.1)

    # MCEM
    add_text(s, Inches(0.6), Inches(5.9), Inches(12), Inches(0.3),
             "MCEM STAGES", size=11, bold=True, color=C_ACCENT)
    add_text(s, Inches(0.6), Inches(6.2), Inches(12.13), Inches(0.6),
             "1 Listen & Consult   \u2192   2 Inspire & Design   \u2192   3 Empower & Achieve   \u2192   4 Realize Value   \u2192   5 Manage & Optimize",
             size=14, bold=True, color=C_INK, align=PP_ALIGN.CENTER)
    add_footer(s, 4)


def build_landscape(prs):
    s = new_slide(prs)
    add_section_tag(s, "The VBD landscape")
    add_title(s, "Three AI surfaces \u00b7 three CSU sub-teams \u00b7 one engine + a cross-CSU spine",
              "40+ VBDs aligned to the three AI surfaces customers actually buy.")
    cols = [
        ("FAMILY A", "M365 Copilot", "Modern Work CSU", "A1\u2013A8 \u00b7 8 VBDs",
         "Envisioning, adoption, optimisation, security \u2014 the seat-licensed Copilot surface.",
         C_ACCENT),
        ("FAMILY B", "Copilot Studio + Power Platform", "Business Apps CSU", "B1\u2013B7 \u00b7 7 VBDs",
         "Custom agents, AI Builder, D365 Copilot envisioning, Power Platform CoE.",
         C_HIGHLIGHT),
        ("FAMILY C", "Azure AI Foundry + Data + Apps", "Cloud & AI CSU", "C1\u2013C19 \u00b7 19 VBDs",
         "Azure Accelerate, AI Transformation Offer, GenAIOps, Responsible AI.",
         C_DARK),
    ]
    cx = Inches(0.6); cw = Inches(4.05); cy = Inches(2.1); ch = Inches(2.4)
    for tag, t, sub, count, body, col in cols:
        add_rect(s, cx, cy, cw, ch, C_BG, line=col)
        add_rect(s, cx, cy, cw, Inches(0.05), col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.15), cw - Inches(0.3), Inches(0.3),
                 tag, size=10, bold=True, color=col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.45), cw - Inches(0.3), Inches(0.45),
                 t, size=16, bold=True, color=C_INK)
        add_text(s, cx + Inches(0.15), cy + Inches(0.9), cw - Inches(0.3), Inches(0.3),
                 sub, size=11, italic=True, color=C_MUTED)
        add_text(s, cx + Inches(0.15), cy + Inches(1.2), cw - Inches(0.3), Inches(0.3),
                 count, size=12, bold=True, color=col)
        add_text(s, cx + Inches(0.15), cy + Inches(1.55), cw - Inches(0.3), Inches(0.85),
                 body, size=11, color=C_INK)
        cx += cw + Inches(0.08)

    # Bottom two bands: Factory + Cross-CSU
    add_rect(s, Inches(0.6), Inches(4.7), Inches(8.2), Inches(1.9), C_BAND)
    add_text(s, Inches(0.8), Inches(4.85), Inches(7.8), Inches(0.4),
             "D-BIS \u00b7 CLOUD ACCELERATE FACTORY", size=11, bold=True, color=C_WARN)
    add_text(s, Inches(0.8), Inches(5.18), Inches(7.8), Inches(0.4),
             "10 zero-cost plays (F1\u2013F10)", size=15, bold=True, color=C_INK)
    add_text(s, Inches(0.8), Inches(5.6), Inches(7.8), Inches(1.0),
             "Microsoft remote workforce delivers ALZ, GenAI Assistant MVP, data, app and security migrations \u2014 the foundation under every Family-C AI workload. Unified Support OR 2-page Factory agreement required.",
             size=11, color=C_INK)

    add_rect(s, Inches(8.92), Inches(4.7), Inches(3.81), Inches(1.9), C_DARK)
    add_text(s, Inches(9.07), Inches(4.85), Inches(3.6), Inches(0.4),
             "FAMILY D \u00b7 CROSS-CSU", size=11, bold=True, color=C_ACCENT2)
    add_text(s, Inches(9.07), Inches(5.18), Inches(3.6), Inches(0.4),
             "D1\u2013D3 \u00b7 3 VBDs", size=15, bold=True, color=C_BG)
    add_text(s, Inches(9.07), Inches(5.6), Inches(3.6), Inches(1.0),
             "Frontier AI CoE stand-up, Skilling Navigator, Value Realization \u2014 the operating-model spine.",
             size=11, color=C_BG)
    add_footer(s, 5)


def build_legend(prs):
    s = new_slide(prs)
    add_section_tag(s, "How to read the VBD slides")
    add_title(s, "Every VBD on the next slides is articulated the same way",
              "VBD name \u00b7 Key Outcomes \u00b7 Contribution to the AI CoE (pillar + tier + MCEM)")
    add_bullets(s, Inches(0.7), Inches(2.15), Inches(12), Inches(4),
                [
        "Key Outcomes \u2014 what the customer walks away with (artefact, capability, or decision).",
        "Contribution to AI CoE \u2014 which of the 5+1 pillars and which tier the VBD advances.",
        "MCEM stage \u2014 where in the customer journey the VBD belongs (1\u20132 inspire, 3 build, 4\u20135 realise).",
        "Funding instrument \u2014 ECIF, AMM, MAICPP, ACO, SA, customer-funded \u2014 stamped on every row.",
        "Owner \u2014 which CSU team carries MCEM-stage accountability (delivery may be partner-led).",
        "VERIFY flag (\u002A) \u2014 catalogue churn risk; re-check on MCAPS Catalog before customer commit.",
    ], size=14)
    # Funding key
    add_rect(s, Inches(0.6), Inches(5.6), Inches(12.13), Inches(1.2), C_BAND)
    add_text(s, Inches(0.8), Inches(5.72), Inches(12), Inches(0.4),
             "FUNDING KEY", size=11, bold=True, color=C_ACCENT)
    add_text(s, Inches(0.8), Inches(6.05), Inches(12), Inches(0.7),
             "ECIF \u2014 End Customer Investment Funds  \u00b7  AMM \u2014 Azure Migrate & Modernize  \u00b7  MAICPP \u2014 MS AI Cloud Partner Program  \u00b7\nACO \u2014 Azure Consumption Offset  \u00b7  SA \u2014 Solution Assessment funding  \u00b7  CF \u2014 Customer-funded",
             size=11, color=C_INK)
    add_footer(s, 6)


# ---------------------------------------------------------------------------
# Family A
# ---------------------------------------------------------------------------

def build_family_a_overview(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family A \u00b7 M365 Copilot \u00b7 Modern Work CSU")
    add_title(s, "Drive seat-Copilot value from envisioning to realisation",
              "8 VBDs covering the full Copilot lifecycle plus the security overlay")
    add_bullets(s, Inches(0.7), Inches(2.05), Inches(12), Inches(3), [
        "Centre of gravity: pillars 1 Business Strategy, 2 Org & Culture, 3 AI Strategy & XP \u2014 with 5 Governance & Security as the safety overlay.",
        "Tier coverage: T1 dominant (envisioning); A3 + A8 extend into T2 (build); A4 lands in T3 (managed run).",
        "MCEM fit: A1/A2/A5/A6/A7 \u2014 Inspire & Design; A3/A8 \u2014 Empower & Achieve; A4 \u2014 Realize Value.",
        "Funding: ECIF and MAICPP dominate; A6/A7 are SA-funded; A4 is post-deployment ACO/CF.",
    ], size=14)
    # Funnel diagram
    add_rect(s, Inches(0.6), Inches(5.3), Inches(12.13), Inches(1.6), C_BAND)
    add_text(s, Inches(0.8), Inches(5.4), Inches(12), Inches(0.4),
             "LIFECYCLE FLOW", size=11, bold=True, color=C_ACCENT)
    add_text(s, Inches(0.8), Inches(5.75), Inches(12), Inches(0.5),
             "Envision  \u2192  Pilot & Adopt  \u2192  Scale  \u2192  Realise Value",
             size=18, bold=True, color=C_INK)
    add_text(s, Inches(0.8), Inches(6.25), Inches(12), Inches(0.5),
             "A1 / A2 / A5  \u2192  A3 \u00b7 A6 \u00b7 A7  \u2192  A8 (CoE)  \u2192  A4 Optimization & Value Realization",
             size=13, color=C_MUTED)
    add_footer(s, 7)


def build_family_a_table(prs, slide_no):
    s = new_slide(prs)
    add_section_tag(s, "Family A \u00b7 M365 Copilot \u00b7 VBD menu")
    add_title(s, "Every A-family VBD \u2014 outcomes and CoE contribution",
              "Owner: Modern Work CSU  \u00b7  Pillar shorthand: 1 BizStrat \u00b7 2 Org \u00b7 3 AIXP \u00b7 4 Tech \u00b7 5 GovSec")
    rows = [
        ["A1 \u00b7 Art of the Possible Workshop",
         "Copilot use-case shortlist, executive buy-in, scenario backlog seeded.",
         "Pillars 1, 2, 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["A2 \u00b7 Scenario Workshop \"Day in the Life\"",
         "Persona-mapped scenarios, ROI hypothesis per role, pilot cohort.",
         "Pillars 1, 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["A3 \u00b7 Copilot Adoption Accelerator (8\u201312 wk)",
         "Champions network, comms plan, measured adoption uplift, repeatable playbook.",
         "Pillars 2, 3  \u00b7  T1+T2  \u00b7  MCEM 3"],
        ["A4 \u00b7 Optimization & Value Realization\u002A",
         "Telemetry-driven tuning, CFO-grade value report, next-wave roadmap.",
         "Pillars 1, 2, 3  \u00b7  T3  \u00b7  MCEM 4\u20135"],
        ["A5 \u00b7 Copilot Chat & Agents Workshop\u002A",
         "Agentic use-case shortlist on the M365 surface, build-vs-buy decision.",
         "Pillars 2, 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["A6 \u00b7 Data Security Assessment",
         "Purview/M365 DS readiness report, oversharing remediation plan.",
         "Pillar 5  \u00b7  T1  \u00b7  MCEM 2"],
        ["A7 \u00b7 Copilot for Security Workshop",
         "SOC use cases for CfS, MDC/MDE integration plan.",
         "Pillars 3, 5  \u00b7  T1  \u00b7  MCEM 2"],
        ["A8 \u00b7 M365 Copilot CoE Engagement\u002A",
         "Customer-side CoE charter, governance model, scaled rollout cadence.",
         "Pillars 1, 2, 5  \u00b7  T2+T3  \u00b7  MCEM 3"],
    ]
    add_table(s, Inches(0.6), Inches(2.1), Inches(12.13), Inches(4.6),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows, body_size=11, col_widths=[3.2, 5.8, 3.13])
    add_text(s, Inches(0.6), Inches(6.78), Inches(12), Inches(0.25),
             "\u002A VERIFY on MCAPS Catalog \u2014 FY26 H2 catalogue churn risk.",
             size=9, italic=True, color=C_MUTED)
    add_footer(s, slide_no)


def build_family_a_spotlight(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family A \u00b7 Spotlight")
    add_title(s, "A3 Copilot Adoption Accelerator \u2014 the value-realisation engine",
              "Why most Copilot programs stall, and the VBD that fixes it")
    # Left: outcomes
    add_rect(s, Inches(0.6), Inches(2.1), Inches(5.95), Inches(4.6), C_BG, line=C_ACCENT)
    add_rect(s, Inches(0.6), Inches(2.1), Inches(5.95), Inches(0.05), C_ACCENT)
    add_text(s, Inches(0.8), Inches(2.25), Inches(5.6), Inches(0.4),
             "KEY OUTCOMES", size=11, bold=True, color=C_ACCENT)
    add_bullets(s, Inches(0.8), Inches(2.65), Inches(5.6), Inches(4),
                [
        "Champions network stood up across the top 5 business functions.",
        "Comms plan, training cadence, prompt library shipped.",
        "Measured adoption uplift \u2014 Active Use, Sentiment, Habit.",
        "Repeatable playbook the customer can run scope after scope.",
        "Backlog of next-wave scenarios groomed and prioritised.",
    ], size=13)
    # Right: AI CoE contribution
    add_rect(s, Inches(6.78), Inches(2.1), Inches(5.95), Inches(4.6), C_BG, line=C_HIGHLIGHT)
    add_rect(s, Inches(6.78), Inches(2.1), Inches(5.95), Inches(0.05), C_HIGHLIGHT)
    add_text(s, Inches(6.98), Inches(2.25), Inches(5.6), Inches(0.4),
             "CONTRIBUTION TO AI CoE", size=11, bold=True, color=C_HIGHLIGHT)
    add_bullets(s, Inches(6.98), Inches(2.65), Inches(5.6), Inches(4), [
        "Pillar 2 Org & Culture \u2014 trains the workforce we measured at only 1/3 today.",
        "Pillar 3 AI Strategy & XP \u2014 turns workshop hypotheses into lived use-cases.",
        "Tier T1\u2192T2 bridge \u2014 the play that converts envisioning into build.",
        "MCEM 3 \u2014 the Empower & Achieve stage where most Copilot money is lost or won.",
        "Feeds A4 Realization with the telemetry it needs to prove value.",
    ], size=13, bullet_color=C_HIGHLIGHT)
    # Stat strip
    add_rect(s, Inches(0.6), Inches(6.78), Inches(12.13), Inches(0.25), C_BAND2)
    add_text(s, Inches(0.7), Inches(6.78), Inches(12), Inches(0.25),
             "Why this VBD matters: BCG 2024 \u2014 60% of orgs reap little value from AI; only 1/3 of workers are trained on it.",
             size=10, italic=True, color=C_MUTED)
    add_footer(s, 9)


# ---------------------------------------------------------------------------
# Family B
# ---------------------------------------------------------------------------

def build_family_b_overview(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family B \u00b7 Copilot Studio + Power Platform \u00b7 Business Apps CSU")
    add_title(s, "Custom agents and AI inside D365 + Power Platform",
              "7 VBDs covering envisioning, co-build, governance and D365 Copilot scenarios")
    add_bullets(s, Inches(0.7), Inches(2.05), Inches(12), Inches(3.4), [
        "Centre of gravity: pillars 3 AI Strategy & XP and 4 Tech & Data \u2014 with 2 Org & 5 Governance as the wrap.",
        "Tier coverage: T1 entry (B1, B3, B4, B7); T2 build (B2, B5, B6).",
        "MCEM fit: B1/B3/B4/B7 \u2014 Inspire & Design; B2/B5/B6 \u2014 Empower & Achieve.",
        "Funding: MAICPP is the dominant lever (B2 Co-build); B6 CoE Starter Kit is largely customer-funded.",
        "Pairs with: A-family on the M365 surface and C-family when agents need Foundry-grade backends.",
    ], size=14)
    add_rect(s, Inches(0.6), Inches(5.5), Inches(12.13), Inches(1.4), C_BAND)
    add_text(s, Inches(0.8), Inches(5.6), Inches(12), Inches(0.4),
             "AGENT SURFACE FLOW", size=11, bold=True, color=C_ACCENT)
    add_text(s, Inches(0.8), Inches(5.95), Inches(12), Inches(0.5),
             "Inspire  \u2192  Build first agent  \u2192  Industrialise on Power Platform",
             size=18, bold=True, color=C_INK)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.5),
             "B1 AiaD \u00b7 B3 AI Builder \u00b7 B4 D365  \u2192  B2 Co-build \u00b7 B5 D365+CS Agentic  \u2192  B6 PP CoE \u00b7 B7 CS SA",
             size=12, color=C_MUTED)
    add_footer(s, 10)


def build_family_b_table(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family B \u00b7 Copilot Studio + Power Platform \u00b7 VBD menu")
    add_title(s, "Every B-family VBD \u2014 outcomes and CoE contribution",
              "Owner: Business Applications CSU  \u00b7  Pairs frequently with MAICPP partners")
    rows = [
        ["B1 \u00b7 Agent in a Day (AiaD)",
         "First custom agent shipped in a day; backlog of next agents identified.",
         "Pillar 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["B2 \u00b7 Copilot Studio Co-build\u002A",
         "Production-grade agent built with MAICPP partner; handover plan.",
         "Pillars 3, 4  \u00b7  T2  \u00b7  MCEM 3"],
        ["B3 \u00b7 AI Builder Workshop",
         "Low-code AI use-cases (forms, classification) costed and prioritised.",
         "Pillars 3, 4  \u00b7  T1  \u00b7  MCEM 2"],
        ["B4 \u00b7 D365 Copilot Envisioning",
         "Persona-mapped Copilot scenarios across Sales/Service/Finance/Ops.",
         "Pillars 1, 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["B5 \u00b7 D365 + Copilot Studio Agentic Workflow",
         "Cross-process agent (e.g. CSR-assist, AR-collections) on D365 data.",
         "Pillars 3, 4  \u00b7  T2  \u00b7  MCEM 3"],
        ["B6 \u00b7 Power Platform CoE Starter Kit",
         "Customer CoE for citizen-dev with governance, telemetry, ALM.",
         "Pillars 2, 5  \u00b7  T2  \u00b7  MCEM 3"],
        ["B7 \u00b7 Copilot Studio Solution Assessment\u002A",
         "Governance posture, DLP, environment strategy for agents at scale.",
         "Pillars 3, 5  \u00b7  T1  \u00b7  MCEM 2"],
    ]
    add_table(s, Inches(0.6), Inches(2.1), Inches(12.13), Inches(4.4),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows, body_size=11, col_widths=[3.2, 5.8, 3.13])
    add_text(s, Inches(0.6), Inches(6.6), Inches(12), Inches(0.25),
             "\u002A VERIFY on MCAPS Catalog \u2014 FY26 H2 catalogue churn risk.",
             size=9, italic=True, color=C_MUTED)
    add_footer(s, 11)


# ---------------------------------------------------------------------------
# Family C - 3 slides (overview, accelerate table, SA + workshops table)
# ---------------------------------------------------------------------------

def build_family_c_overview(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family C \u00b7 Azure AI Foundry + Data + Apps \u00b7 Cloud & AI CSU")
    add_title(s, "The deepest catalogue \u2014 19 VBDs across Azure Accelerate, ATO and RAI",
              "From plan to managed run, with the AI Transformation Offer as the keystone")
    # Three sub-bands
    bands = [
        ("C.1 Azure Accelerate (C1\u2013C5)",
         "Plan \u2192 Implement (with ACR uplift) \u2192 Build/Modernize \u2192 AI App & Agent Factory \u2192 Fabric Analytics & AI.",
         C_ACCENT),
        ("C.2 Solution Assessments (C6\u2013C8)",
         "AOAI/Foundry SA \u00b7 Fabric SA \u00b7 AI Migrate SA \u2014 SA-funded readiness with discoverable outputs.",
         C_HIGHLIGHT),
        ("C.3 Workshops, Hackathons, CoE (C9\u2013C19)",
         "GenAI/Foundry workshop \u00b7 AI Hackathon \u00b7 Landing Zone \u00b7 WAF-AI \u00b7 GenAIOps \u00b7 RAI \u00b7 ATO C16\u2013C18 \u00b7 5 AI Patterns.",
         C_DARK),
    ]
    y = Inches(2.1)
    for t, body, col in bands:
        add_rect(s, Inches(0.6), y, Inches(12.13), Inches(1.35), C_BG, line=col)
        add_rect(s, Inches(0.6), y, Inches(0.08), Inches(1.35), col)
        add_text(s, Inches(0.85), y + Inches(0.15), Inches(11.5), Inches(0.5),
                 t, size=16, bold=True, color=col)
        add_text(s, Inches(0.85), y + Inches(0.65), Inches(11.5), Inches(0.7),
                 body, size=13, color=C_INK)
        y += Inches(1.5)
    # Anchor stat
    add_rect(s, Inches(0.6), Inches(6.7), Inches(12.13), Inches(0.3), C_BAND2)
    add_text(s, Inches(0.8), Inches(6.7), Inches(12), Inches(0.3),
             "AI Transformation Offer (C16+C17+C18) = up to $1M envelope (pre-sales ECIF + post-sales ECIF + ACO) \u00b7 HIGH-trust source.",
             size=11, italic=True, color=C_MUTED)
    add_footer(s, 12)


def build_family_c_table_1(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family C \u00b7 Azure Accelerate \u00b7 VBD menu")
    add_title(s, "C1\u2013C5 \u2014 the Azure Accelerate stack",
              "Plan \u2192 Implement \u2192 Build/Modernize \u2192 Agent Factory \u2192 Fabric")
    rows = [
        ["C1 \u00b7 Azure Innovate Plan ($15K\u2013$50K)",
         "Architecture, roadmap, business case for first AI workload.",
         "Pillars 1, 3, 4  \u00b7  T1  \u00b7  MCEM 2"],
        ["C2 \u00b7 Azure Innovate Implement (XS\u2013L tiers)",
         "Production-grade AI workload delivered; +20% ACR uplift available.",
         "Pillars 3, 4, 5  \u00b7  T2  \u00b7  MCEM 3"],
        ["C3 \u00b7 Build & Modernize AI Apps",
         ".NET/Java app modernised on Azure with AI capabilities embedded.",
         "Pillars 3, 4  \u00b7  T2  \u00b7  MCEM 3"],
        ["C4 \u00b7 AI App & Agent Factory\u002A",
         "MVP agent factory pattern, repeatable Foundry-based pipeline.",
         "Pillars 3, 4  \u00b7  T2+T3  \u00b7  MCEM 3"],
        ["C5 \u00b7 Fabric Analytics & AI",
         "Fabric workload live; data substrate ready for AI grounding.",
         "Pillars 3, 4  \u00b7  T2  \u00b7  MCEM 3"],
    ]
    add_table(s, Inches(0.6), Inches(2.1), Inches(12.13), Inches(3.4),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows, body_size=11, col_widths=[3.2, 5.8, 3.13])

    # SA strip - C6-C8
    add_text(s, Inches(0.6), Inches(5.65), Inches(12), Inches(0.4),
             "C.2 SOLUTION ASSESSMENTS (SA-funded \u2014 discoverable readiness reports)",
             size=11, bold=True, color=C_HIGHLIGHT)
    rows2 = [
        ["C6 \u00b7 AOAI / Foundry SA\u002A",
         "Foundry adoption readiness; first use-case shortlist.",
         "Pillars 3, 4, 5  \u00b7  T1  \u00b7  MCEM 2"],
        ["C7 \u00b7 Fabric SA",
         "Lakehouse-readiness assessment for AI grounding.",
         "Pillar 4  \u00b7  T1  \u00b7  MCEM 2"],
        ["C8 \u00b7 AI Migrate SA\u002A",
         "Plan to migrate 3rd-party LLM workloads onto Azure.",
         "Pillar 4  \u00b7  T1  \u00b7  MCEM 2"],
    ]
    add_table(s, Inches(0.6), Inches(6.0), Inches(12.13), Inches(0.85),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows2, body_size=10, col_widths=[3.2, 5.8, 3.13], header_size=10)
    add_text(s, Inches(0.6), Inches(6.9), Inches(12), Inches(0.15),
             "\u002A VERIFY on MCAPS Catalog \u2014 FY26 H2 catalogue churn risk.",
             size=9, italic=True, color=C_MUTED)
    add_footer(s, 13)


def build_family_c_table_2(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family C \u00b7 Workshops, Hackathons, CoE \u00b7 VBD menu")
    add_title(s, "C9\u2013C19 \u2014 the envisioning and governance stack",
              "Where Foundry, RAI, GenAIOps and the AI Transformation Offer live")
    rows = [
        ["C9 \u00b7 GenAI / Foundry Workshop",
         "Foundry use-case shortlist, model selection guidance.",
         "Pillar 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["C10 \u00b7 AI Hackathon",
         "Hands-on Foundry prototypes from internal teams; backlog seeded.",
         "Pillar 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["C11 \u00b7 AI Landing Zone Implementation",
         "Hub-and-spoke ALZ for AI workloads, ready for Foundry/AOAI.",
         "Pillars 4, 5  \u00b7  T1+T2  \u00b7  MCEM 3"],
        ["C12 \u00b7 Well-Architected Framework for AI",
         "WAF review covering reliability, security, cost, ops for AI workloads.",
         "Pillars 4, 5  \u00b7  T3  \u00b7  MCEM 4"],
        ["C13 \u00b7 GenAIOps Maturity Assessment (ATO 3.1)",
         "AIOps posture, monitoring/eval gaps, remediation roadmap.",
         "Pillar 5  \u00b7  T3  \u00b7  MCEM 4"],
        ["C14 \u00b7 Azure Essentials AI Adoption",
         "Azure Essentials AI workload pattern adopted by the customer.",
         "Pillar 4  \u00b7  T1  \u00b7  MCEM 2"],
        ["C15 \u00b7 Responsible AI Workshop",
         "RAI v2 standard applied; Impact Assessment artefacts produced.",
         "Pillar 5  \u00b7  T1  \u00b7  MCEM 2"],
        ["C16 \u00b7 ATO C1 CoE & Envisioning (HIGH trust)",
         "AI CoE charter + first-wave use-case backlog; up to $50K pre-sales ECIF.",
         "Pillars 1, 2, 3  \u00b7  T1  \u00b7  MCEM 2"],
        ["C17 \u00b7 ATO C2 Foundation Architecture (HIGH)",
         "ALZ + Foundry foundation; up to $500K ECIF + $500K ACO.",
         "Pillars 4, 5  \u00b7  T2  \u00b7  MCEM 3"],
        ["C18 \u00b7 ATO C3 GenAI / Agent Factory (HIGH)",
         "First production agent + factory pattern; ECIF + ACO + MAICPP stack.",
         "Pillars 3, 4, 5  \u00b7  T2+T3  \u00b7  MCEM 3"],
        ["C19 \u00b7 AI Patterns Scorecard",
         "5 patterns (IDP \u00b7 Extraction/Summ \u00b7 Workflow \u00b7 Multimodal \u00b7 NBA) scored.",
         "Pillars 1, 3  \u00b7  T1  \u00b7  MCEM 2"],
    ]
    add_table(s, Inches(0.6), Inches(2.05), Inches(12.13), Inches(4.85),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows, body_size=10, col_widths=[3.4, 5.6, 3.13], header_size=10)
    add_footer(s, 14)


def build_ato_spotlight(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family C \u00b7 ATO Spotlight  \u00b7  HIGH-TRUST FLAGSHIP")
    add_title(s, "The AI Transformation Offer \u2014 C16 + C17 + C18",
              "One bundle, three motions, up to $1M of envelope to remove customer-side friction")
    # Three component cards
    comps = [
        ("ATO C1 (C16)", "CoE & Envisioning",
         ["Up to $50K pre-sales ECIF",
          "AI CoE charter + use-case backlog",
          "Pillars 1, 2, 3  \u00b7  T1",
          "MCEM 2"],
         C_ACCENT2),
        ("ATO C2 (C17)", "Foundation Architecture",
         ["Up to $500K ECIF post-sales",
          "+ up to $500K ACO uplift",
          "ALZ + Foundry foundation",
          "Pillars 4, 5  \u00b7  T2  \u00b7  MCEM 3"],
         C_ACCENT),
        ("ATO C3 (C18)", "GenAI / Agent Factory",
         ["ECIF + ACO + MAICPP stack",
          "First production agent + factory pattern",
          "Pillars 3, 4, 5  \u00b7  T2+T3",
          "MCEM 3"],
         C_HIGHLIGHT),
    ]
    cx = Inches(0.6); cw = Inches(4.05); cy = Inches(2.1); ch = Inches(3.2)
    for tag, title, items, col in comps:
        add_rect(s, cx, cy, cw, ch, C_BG, line=col)
        add_rect(s, cx, cy, cw, Inches(0.05), col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.15), cw - Inches(0.3), Inches(0.3),
                 tag, size=10, bold=True, color=col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.5), cw - Inches(0.3), Inches(0.5),
                 title, size=17, bold=True, color=C_INK)
        add_bullets(s, cx + Inches(0.15), cy + Inches(1.1), cw - Inches(0.3), Inches(2.0),
                    items, size=12, bullet_color=col)
        cx += cw + Inches(0.08)
    # Footer bar
    add_rect(s, Inches(0.6), Inches(5.45), Inches(12.13), Inches(1.45), C_DARK)
    add_text(s, Inches(0.85), Inches(5.55), Inches(12), Inches(0.4),
             "WHY THIS IS THE KEYSTONE", size=11, bold=True, color=C_ACCENT2)
    add_bullets(s, Inches(0.85), Inches(5.9), Inches(12), Inches(1.0), [
        "Single bundle that traverses pillars 1\u20135 \u00b7 tiers T1\u2192T2+T3 \u00b7 MCEM 2\u21923 in one motion.",
        "100+ ATO accounts running at 15% MoM ACR growth \u2014 the proof-point we lead with.",
        "Funding multiplier: $1 of ECIF unlocks $3\u2013$5 of Azure consumption.",
    ], size=12, color=C_BG, bullet_color=C_ACCENT2)
    add_footer(s, 15)


# ---------------------------------------------------------------------------
# Factory + Cross-CSU
# ---------------------------------------------------------------------------

def build_factory(prs):
    s = new_slide(prs)
    add_section_tag(s, "D-bis \u00b7 Cloud Accelerate Factory")
    add_title(s, "Ten zero-cost plays that put the foundation under every AI workload",
              "Microsoft remote workforce  \u00b7  Unified Support OR 2-page Factory agreement  \u00b7  2-week nomination")
    rows = [
        ["F1 \u00b7 AI \u2014 GenAI Assistant",
         "AOAI MVP: LZ + data migration + first use-case build + tuning.",
         "Pillars 3, 4  \u00b7  T2  \u00b7  pairs with ATO C18"],
        ["F2 \u00b7 Azure Landing Zone",
         "Enterprise-scale ALZ via Portal Accelerator; LZ validation.",
         "Pillars 4, 5  \u00b7  T2  \u00b7  pairs with ATO C17"],
        ["F3 \u00b7 Real-time intelligence MVP",
         "Lakehouse LZ (Databricks/Fabric) + data migration + first use case.",
         "Pillar 4  \u00b7  T2  \u00b7  Foundry grounding"],
        ["F4 \u00b7 Lakehouse + DW migration",
         "Synapse \u2192 Fabric, Databricks LH, DW modernisation.",
         "Pillar 4  \u00b7  T2  \u00b7  enables C5"],
        ["F5 \u00b7 Power BI \u2192 Fabric migration",
         "SSRS/SSAS/Premium \u2192 Fabric SKU; Copilot-in-Fabric ready.",
         "Pillar 4  \u00b7  T2  \u00b7  pairs with MW"],
        ["F6 \u00b7 Arc Enablement (Win + SQL)",
         "Arc agent deployment for hybrid/edge AI workloads.",
         "Pillars 4, 5  \u00b7  T2  \u00b7  sovereign-ready"],
        ["F7 \u00b7 App Migration (App Svc/AKS/ACA)",
         ".NET/Java/Spring on-prem \u2192 PaaS; AI embedding-ready.",
         "Pillar 4  \u00b7  T2  \u00b7  pairs with C3"],
        ["F8 \u00b7 Defender for Cloud deployment",
         "CSPM + CWP across servers, DBs, storage, containers, APIs.",
         "Pillar 5  \u00b7  T2  \u00b7  underpins RAI (C15)"],
        ["F9 \u00b7 Sentinel greenfield / Splunk\u2192Sentinel",
         "SIEM for AI workload observability + prompt-injection monitoring.",
         "Pillar 5  \u00b7  T2  \u00b7  AI governance"],
        ["F10 \u00b7 Infra & DB migration",
         "Win/Linux/AVS/SQL/OSS/NoSQL lift-and-shift.",
         "Pillar 4  \u00b7  T2  \u00b7  pairs with C8"],
    ]
    add_table(s, Inches(0.6), Inches(2.05), Inches(12.13), Inches(4.65),
              ["Factory offering", "Scope summary", "Contribution to the AI CoE"],
              rows, body_size=10, col_widths=[3.0, 6.0, 3.13], header_size=10,
              header_fill=C_WARN)
    add_text(s, Inches(0.6), Inches(6.78), Inches(12), Inches(0.25),
             "Out of Factory scope: M365 Copilot, Copilot Studio agent build, business-logic changes, custom rewrites, advisory/consulting, in-country cleared delivery.",
             size=9, italic=True, color=C_MUTED)
    add_footer(s, 16)


def build_delivery_stack(prs):
    s = new_slide(prs)
    add_section_tag(s, "Delivery stack")
    add_title(s, "Three streams \u2014 envision, foundation, build & run",
              "Where MCAPS leads, where Factory carries the load, where partners take the relay")
    streams = [
        ("STREAM 1 \u00b7 MCAPS-led envisioning",
         "CSA + ATU + STU + EPS",
         "MCEM 1\u20132  \u00b7  ATO C1  \u00b7  ECIF pre-sales",
         "Pillars 1\u20132  \u00b7  Tier 1",
         C_ACCENT),
        ("STREAM 2 \u00b7 Factory-delivered foundation",
         "Cloud Accelerate Factory \u2014 zero cost",
         "MCEM 3  \u00b7  ATO C2 + parts of C3 MVP",
         "Pillars 4\u20135  \u00b7  Tier 2  \u00b7  F1\u2013F10",
         C_WARN),
        ("STREAM 3 \u00b7 Partner-led build & managed run",
         "MAICPP partners + MSPs",
         "MCEM 3\u20135  \u00b7  ATO C3 + scale",
         "Pillars 1\u20135 + co-sell  \u00b7  Tiers 1\u20133",
         C_HIGHLIGHT),
    ]
    y = Inches(2.1)
    for title, who, mcem, pillars, col in streams:
        add_rect(s, Inches(0.6), y, Inches(12.13), Inches(1.45), C_BG, line=col)
        add_rect(s, Inches(0.6), y, Inches(0.1), Inches(1.45), col)
        add_text(s, Inches(0.85), y + Inches(0.1), Inches(11.5), Inches(0.45),
                 title, size=16, bold=True, color=col)
        add_text(s, Inches(0.85), y + Inches(0.55), Inches(11.5), Inches(0.4),
                 who, size=12, italic=True, color=C_INK)
        add_text(s, Inches(0.85), y + Inches(0.92), Inches(5.8), Inches(0.4),
                 mcem, size=11, color=C_MUTED)
        add_text(s, Inches(7.0), y + Inches(0.92), Inches(5.5), Inches(0.4),
                 pillars, size=11, color=C_MUTED)
        y += Inches(1.55)
    # Decision rule
    add_rect(s, Inches(0.6), Inches(6.78), Inches(12.13), Inches(0.25), C_BAND2)
    add_text(s, Inches(0.7), Inches(6.78), Inches(12), Inches(0.25),
             "Decision rule: on Factory catalogue + Unified Support/2-page \u00b7 standardised \u00b7 2-week lead OK \u2192 nominate. Else partner-deliver.",
             size=10, italic=True, color=C_MUTED)
    add_footer(s, 17)


def build_family_d(prs):
    s = new_slide(prs)
    add_section_tag(s, "Family D \u00b7 Cross-CSU \u00b7 Operating-model spine")
    add_title(s, "Three VBDs that stand up and sustain the AI CoE itself",
              "Owner: X (cross-CSU)  \u00b7  These are the engagements that turn a project into a programme")
    rows = [
        ["D1 \u00b7 Frontier AI CoE Stand-up (5+1 pillars)  \u2014  HIGH trust",
         "Customer-side AI CoE stood up across all 5 pillars + co-sell archetype mapping.",
         "Pillars 1, 2, 3, 4, 5, +1  \u00b7  T1+T2  \u00b7  MCEM 1\u20133"],
        ["D2 \u00b7 AI Skilling / Learn AI Skill Navigator",
         "Skilling plan against AI Engineer / Data Engineer / Copilot Champion paths.",
         "Pillar 2  \u00b7  T1+T2  \u00b7  MCEM 3"],
        ["D3 \u00b7 AI Value Realization (Stage-4) Engagement  \u2014  HIGH trust",
         "CFO-grade telemetry-driven value-tracking across Copilot, Foundry, Fabric usage.",
         "Pillar 1  \u00b7  T3  \u00b7  MCEM 4\u20135"],
    ]
    add_table(s, Inches(0.6), Inches(2.1), Inches(12.13), Inches(2.4),
              ["VBD", "Key Outcomes", "Contribution to the AI CoE"],
              rows, body_size=12, col_widths=[4.0, 5.0, 3.13])
    # Pull-quote
    add_rect(s, Inches(0.6), Inches(4.85), Inches(12.13), Inches(2.05), C_DARK)
    add_text(s, Inches(0.85), Inches(5.0), Inches(11.5), Inches(0.4),
             "WHY D1 IS THE ANCHOR", size=11, bold=True, color=C_ACCENT2)
    add_text(s, Inches(0.85), Inches(5.35), Inches(11.5), Inches(0.5),
             "It is the only VBD that explicitly delivers all 5+1 pillars.",
             size=16, bold=True, color=C_BG)
    add_bullets(s, Inches(0.85), Inches(5.85), Inches(11.5), Inches(1), [
        "Maps every other VBD in this deck onto the customer's own CoE pillars \u2014 turns the catalogue into a programme.",
        "Funding: ECIF + MAICPP \u00b7 Duration: 6\u201312 weeks \u00b7 Trust: HIGH (sourced from internal Frontier CoE pillar decks).",
    ], size=12, color=C_BG, bullet_color=C_ACCENT2)
    add_footer(s, 18)


# ---------------------------------------------------------------------------
# Synthesis
# ---------------------------------------------------------------------------

def build_tier_pillar_map(prs):
    s = new_slide(prs)
    add_section_tag(s, "Synthesis")
    add_title(s, "Tier \u00d7 Pillar coverage map",
              "Dense at T1+T2 across pillars 3\u20135; T3 Managed Run is intentionally thin \u2014 partner-MSP relay")
    headers = ["Pillar", "T1 \u00b7 Envisioning", "T2 \u00b7 Build", "T3 \u00b7 Managed Run"]
    rows = [
        ["1 \u00b7 Business Strategy",
         "A1, A2, B4, C16, C19, D1", "\u2014", "A4, D3"],
        ["2 \u00b7 Org & Culture",
         "A3, A8, B6", "A8, B6, D1", "A4"],
        ["3 \u00b7 AI Strategy & XP",
         "A1\u2013A7, B1, B3, B4, B7, C1, C9, C10, C16, C19",
         "A3, B2, B5, C2\u2013C5, C18", "A4, C18"],
        ["4 \u00b7 Tech & Data",
         "C6\u2013C8, C11, C14", "B5, C2\u2013C5, C11, C17, C18", "C12, C18"],
        ["5 \u00b7 Governance & Security",
         "A6, B7, C6, C13, C15", "A8, B6, C2, C17", "A4, C12, C13, D3"],
        ["+1 \u00b7 Co-sell & Partner",
         "D1 (archetype mapping)", "All MAICPP items \u2014 B2, B5, C2\u2013C5, D1", "\u2014"],
    ]
    add_table(s, Inches(0.6), Inches(2.1), Inches(12.13), Inches(4.5),
              headers, rows, body_size=11, col_widths=[2.5, 4.0, 3.5, 2.13])
    add_text(s, Inches(0.6), Inches(6.7), Inches(12), Inches(0.3),
             "Reading: column thickness shows where the AI CoE has menu depth today; T3 thinness is the right place for partner-MSP (Tier-3) handoff.",
             size=11, italic=True, color=C_MUTED)
    add_footer(s, 19)


def build_contribution_synthesis(prs):
    s = new_slide(prs)
    add_section_tag(s, "Synthesis")
    add_title(s, "How every family contributes to the AI CoE",
              "One sentence per family \u2014 the elevator answer to \"what does this VBD do for the CoE?\"")
    cards = [
        ("Family A \u00b7 M365 Copilot",
         "Makes the workforce productive on Copilot \u2014 lifting pillars 2 (Org), 3 (AI XP) and 5 (Governance via A6/A7).",
         C_ACCENT),
        ("Family B \u00b7 Copilot Studio + PP",
         "Operationalises agents inside business processes \u2014 lifting pillars 3 (XP), 4 (Tech) and 5 (Governance via B6/B7).",
         C_HIGHLIGHT),
        ("Family C \u00b7 Foundry + Azure",
         "Builds the AI platform and the production agents \u2014 lifting pillars 3, 4, 5 and anchoring the keystone ATO bundle.",
         C_DARK),
        ("D-bis \u00b7 Factory",
         "Puts the foundation under everything for free \u2014 pillars 4 + 5, T2 build, MCEM 3, zero customer cost.",
         C_WARN),
        ("Family D \u00b7 Cross-CSU",
         "Stands up the customer-side CoE itself \u2014 D1 spans all 5+1 pillars; D3 proves value at MCEM 4\u20135.",
         C_GOOD),
    ]
    y = Inches(2.1)
    for title, body, col in cards:
        add_rect(s, Inches(0.6), y, Inches(12.13), Inches(0.9), C_BG, line=col)
        add_rect(s, Inches(0.6), y, Inches(0.08), Inches(0.9), col)
        add_text(s, Inches(0.85), y + Inches(0.1), Inches(11.5), Inches(0.4),
                 title, size=14, bold=True, color=col)
        add_text(s, Inches(0.85), y + Inches(0.45), Inches(11.5), Inches(0.5),
                 body, size=12, color=C_INK)
        y += Inches(0.98)
    add_footer(s, 20)


def build_sequencing(prs):
    s = new_slide(prs)
    add_section_tag(s, "Synthesis")
    add_title(s, "VBD shortlist by MCEM stage",
              "The standard menu the CSA team should run inside the AI CoE artefact pack")
    cols = [
        ("INSPIRE & DESIGN", "MCEM 1\u20132",
         ["A1 \u00b7 Art of the Possible",
          "A2 \u00b7 Day in the Life",
          "A6 \u00b7 Data Security Assessment",
          "B1 \u00b7 Agent in a Day",
          "B4 \u00b7 D365 Copilot Envisioning",
          "C9 \u00b7 GenAI / Foundry Workshop",
          "C16 \u00b7 ATO C1 \u2014 CoE & Envisioning"],
         C_ACCENT2),
        ("EMPOWER & ACHIEVE", "MCEM 3",
         ["A3 \u00b7 Adoption Accelerator",
          "A8 \u00b7 M365 Copilot CoE",
          "B2 \u00b7 Copilot Studio Co-build",
          "C2 / C3 / C5 \u00b7 Azure Accelerate",
          "C11 \u00b7 AI Landing Zone",
          "C17 \u00b7 ATO C2 \u2014 Foundation",
          "C18 \u00b7 ATO C3 \u2014 Agent Factory"],
         C_ACCENT),
        ("REALIZE & OPTIMIZE", "MCEM 4\u20135",
         ["A4 \u00b7 Optimization & Value Realization",
          "C12 \u00b7 WAF for AI",
          "C13 \u00b7 GenAIOps Maturity (ATO 3.1)",
          "D3 \u00b7 AI Value Realization (Stage-4)"],
         C_HIGHLIGHT),
    ]
    cx = Inches(0.6); cw = Inches(4.05); cy = Inches(2.1); ch = Inches(4.7)
    for title, sub, items, col in cols:
        add_rect(s, cx, cy, cw, ch, C_BG, line=col)
        add_rect(s, cx, cy, cw, Inches(0.05), col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.15), cw - Inches(0.3), Inches(0.3),
                 title, size=11, bold=True, color=col)
        add_text(s, cx + Inches(0.15), cy + Inches(0.45), cw - Inches(0.3), Inches(0.3),
                 sub, size=12, italic=True, color=C_MUTED)
        add_bullets(s, cx + Inches(0.15), cy + Inches(0.85), cw - Inches(0.3), Inches(3.7),
                    items, size=12, bullet_color=col)
        cx += cw + Inches(0.08)
    add_footer(s, 21)


def build_premortem(prs):
    s = new_slide(prs)
    add_section_tag(s, "Pre-mortem")
    add_title(s, "What could be wrong with this list six months out",
              "The honest disclosure \u2014 re-verify before any customer commit")
    items = [
        ("1 \u00b7 Catalogue churn",
         "FY26 H2 \u2192 FY27 will rename or retire 3\u20136 SKUs. VERIFY: A4, A5, A8, B2, B7, C4, C6, C8."),
        ("2 \u00b7 Funding-instrument substitution",
         "Azure Accelerate FY26 H2 rates and T-shirt sizes are the highest-volatility numbers \u2014 verify on aka.ms/AzureAccelerate."),
        ("3 \u00b7 Owner vs delivery labour",
         "C18, B2, B5, D1 listed as CSU-owned for MCEM-stage accountability; hands-on-keyboard is regularly MAICPP partner."),
        ("4 \u00b7 Sandbox limitation",
         "A1\u2013A8, B1\u2013B7, C6\u2013C15, D2 reflect 2025-05 training-data knowledge. ATO (C16\u2013C19) and D1 are HIGH trust from internal sources."),
    ]
    y = Inches(2.1)
    for title, body in items:
        add_rect(s, Inches(0.6), y, Inches(12.13), Inches(1.05), C_BAND)
        add_text(s, Inches(0.85), y + Inches(0.15), Inches(11.5), Inches(0.4),
                 title, size=14, bold=True, color=C_WARN)
        add_text(s, Inches(0.85), y + Inches(0.5), Inches(11.5), Inches(0.55),
                 body, size=12, color=C_INK)
        y += Inches(1.15)
    add_footer(s, 22)


def build_next_steps(prs):
    s = new_slide(prs)
    add_section_tag(s, "Next steps")
    add_title(s, "How RSA CSU should use this deck",
              "Run it as the AI CoE VBD menu \u2014 with verification gates at three points")
    items = [
        ("\u2460 Adopt as the standard CSA menu",
          "Embed this deck in the AI CoE artefact pack; CSAs lead with the 3-MCEM shortlist."),
        ("\u2461 Lead every customer with the right tier",
          "T1 \u2192 envision/SA; T2 \u2192 Factory + Accelerate + ATO; T3 \u2192 hand to MSP/partner via +1 pillar."),
        ("\u2462 Stand up the customer's own CoE with D1",
          "Use D1 Frontier CoE as the contract that turns one engagement into a programme."),
        ("\u2463 Pre-flight every commit",
          "Re-verify VERIFY-flagged items on MCAPS Catalog; re-check Accelerate $$ on aka.ms/AzureAccelerate."),
        ("\u2464 Close the loop with D3",
          "Stage-4 Value Realization quarterly cadence \u2014 the CFO-grade evidence that keeps the CoE funded."),
    ]
    y = Inches(2.1)
    for title, body in items:
        add_rect(s, Inches(0.6), y, Inches(12.13), Inches(0.85), C_BG, line=C_RULE)
        add_text(s, Inches(0.85), y + Inches(0.12), Inches(11.5), Inches(0.4),
                 title, size=14, bold=True, color=C_ACCENT)
        add_text(s, Inches(0.85), y + Inches(0.45), Inches(11.5), Inches(0.4),
                 body, size=12, color=C_INK)
        y += Inches(0.93)
    add_footer(s, 23)


def build_sources(prs):
    s = new_slide(prs)
    add_section_tag(s, "Sources & verification")
    add_title(s, "Where every VBD on this menu came from",
              "Trust grades applied; methodology disclosed")
    add_bullets(s, Inches(0.7), Inches(2.1), Inches(12), Inches(4.4), [
        "HIGH trust \u2014 content-brief.md (Yuri Baijnath, author).",
        "HIGH trust \u2014 ato-content.md (Microsoft internal ATO slide deck; ATO C1\u2013C3 funding cross-checked between slides 11 and 12).",
        "HIGH trust \u2014 Frontier CoE pillar decks (Business Strategy, Org & Culture, AI Strategy, Tech & Data, Governance & Security \u2014 source for D1 and pillar definitions).",
        "MODERATE trust (2025-05 cutoff, re-verify on MCAPS Catalog) \u2014 Azure Accelerate (aka.ms/AzureAccelerate), Microsoft Learn (CAF for AI, Foundry, Fabric, PP CoE), M365 Copilot Adoption Hub, Copilot Studio Workshop, RAI Standard v2, MAICPP program.",
        "Cloud Accelerate Factory \u2014 aka.ms/CloudAccelerateFactory; OpenAI scripts at github.com/Azure/cloud-accelerate-factory.",
        "Methodology \u2014 SIFT on grounding files (recent date, internal authorship, cross-corroboration); Chain-of-Verification on ATO funding numbers; adversarial pass produced the 4 pre-mortem risks.",
    ], size=12, line_spacing=1.25)
    add_rect(s, Inches(0.6), Inches(6.6), Inches(12.13), Inches(0.4), C_BAND2)
    add_text(s, Inches(0.7), Inches(6.62), Inches(12), Inches(0.35),
             "Limitations disclosure: compiled in a sandboxed environment without live partner-portal access. Re-verify FY26 H2 VERIFY entries before any customer commit.",
             size=10, italic=True, color=C_MUTED)
    add_footer(s, 24)


def build_close(prs):
    s = new_slide(prs)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, C_DARK)
    add_text(s, Inches(0.7), Inches(0.7), Inches(12), Inches(0.4),
             "AI CENTER OF EXCELLENCE  \u00b7  CLOSING",
             size=12, bold=True, color=C_ACCENT2)
    add_text(s, Inches(0.7), Inches(1.3), Inches(12), Inches(1.4),
             "Outcomes over offerings.",
             size=54, bold=True, color=C_BG)
    add_text(s, Inches(0.7), Inches(2.6), Inches(12), Inches(0.7),
             "Every VBD in this deck names what the customer walks away with \u2014\nand which AI CoE pillar and tier it advances.",
             size=22, color=C_ACCENT2)
    # Pull number strip
    nums = [
        ("40+", "VBDs articulated"),
        ("5+1", "Pillars covered"),
        ("3", "Tiers \u2014 envision, build, run"),
        ("$1M", "ATO envelope per customer"),
    ]
    nx = Inches(0.7)
    for n, lbl in nums:
        add_text(s, nx, Inches(4.4), Inches(3.0), Inches(0.7),
                 n, size=44, bold=True, color=C_HIGHLIGHT)
        add_text(s, nx, Inches(5.1), Inches(3.0), Inches(0.4),
                 lbl, size=12, color=C_ACCENT2)
        nx += Inches(3.0)
    # Signature
    add_rect(s, Inches(0.7), Inches(6.05), Inches(11.9), Emu(9000), C_ACCENT2)
    add_text(s, Inches(0.7), Inches(6.2), Inches(12), Inches(0.4),
             "Yuri Baijnath", size=18, bold=True, color=C_BG)
    add_text(s, Inches(0.7), Inches(6.6), Inches(12), Inches(0.4),
             "CSU Cloud & AI Lead (South Africa)  \u00b7  Yuri.Baijnath@microsoft.com  \u00b7  Microsoft",
             size=12, color=C_ACCENT2)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def main():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    build_title(prs)                       # 1
    build_agenda(prs)                      # 2
    build_why(prs)                         # 3
    build_framing(prs)                     # 4
    build_landscape(prs)                   # 5
    build_legend(prs)                      # 6
    build_family_a_overview(prs)           # 7
    build_family_a_table(prs, 8)           # 8
    build_family_a_spotlight(prs)          # 9
    build_family_b_overview(prs)           # 10
    build_family_b_table(prs)              # 11
    build_family_c_overview(prs)           # 12
    build_family_c_table_1(prs)            # 13
    build_family_c_table_2(prs)            # 14
    build_ato_spotlight(prs)               # 15
    build_factory(prs)                     # 16
    build_delivery_stack(prs)              # 17
    build_family_d(prs)                    # 18
    build_tier_pillar_map(prs)             # 19
    build_contribution_synthesis(prs)      # 20
    build_sequencing(prs)                  # 21
    build_premortem(prs)                   # 22
    build_next_steps(prs)                  # 23
    build_sources(prs)                     # 24
    build_close(prs)                       # 25

    out = "AI-CoE-VBD-Reference-Deck.pptx"
    prs.save(out)
    print(f"Wrote {out} with {len(prs.slides)} slides.")


if __name__ == "__main__":
    main()
