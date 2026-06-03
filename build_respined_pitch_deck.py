"""Generate AI-CoE-Pitch-Deck-Respined.pptx.

Re-spined pitch deck leading with the three-surface x three-stream moat grid,
not the 5+1 pillars. See ai-coe-pitch-respine-spec.md for the full spine.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

OUT = Path(__file__).parent / "AI-CoE-Pitch-Deck-Respined.pptx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
CYAN = RGBColor(0x50, 0xE6, 0xFF)
PURPLE = RGBColor(0x74, 0x2A, 0x9B)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
LIGHT = RGBColor(0xEA, 0xF4, 0xFB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x59, 0x59, 0x59)
DARK = RGBColor(0x20, 0x20, 0x20)

SW, SH = Inches(13.333), Inches(7.5)


def new_prs() -> Presentation:
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    return prs


def blank(prs) -> object:
    return prs.slides.add_slide(prs.slide_layouts[6])


def set_bg(slide, color: RGBColor) -> None:
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.line.fill.background()
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.shadow.inherit = False


def add_rect(slide, x, y, w, h, fill: RGBColor, line: RGBColor | None = None):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(0.75)
    s.shadow.inherit = False
    return s


def add_text(slide, x, y, w, h, text: str, *, size: int = 14, bold: bool = False,
             color: RGBColor = DARK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             font: str = "Segoe UI") -> None:
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05); tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.name = font
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color


def add_bullets(slide, x, y, w, h, items, *, size: int = 12, color: RGBColor = DARK):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = f"•  {item}"
        r.font.name = "Segoe UI"
        r.font.size = Pt(size)
        r.font.color.rgb = color


def add_footer(slide, label: str) -> None:
    bar = add_rect(slide, 0, SH - Inches(0.35), SW, Inches(0.35), NAVY)
    add_text(slide, Inches(0.4), SH - Inches(0.33), SW - Inches(0.8), Inches(0.3),
             label, size=9, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, SW - Inches(2.0), SH - Inches(0.33), Inches(1.6), Inches(0.3),
             "Microsoft Confidential", size=9, color=CYAN,
             align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)


# ---------- Slides ----------

def s1_title(prs):
    s = blank(prs); set_bg(s, NAVY)
    add_rect(s, 0, Inches(2.6), Inches(0.35), Inches(2.2), BLUE)
    add_rect(s, Inches(0.5), Inches(2.6), Inches(0.18), Inches(2.2), CYAN)
    add_text(s, Inches(0.9), Inches(2.4), Inches(11), Inches(1.2),
             "Microsoft AI Center of Excellence", size=44, bold=True, color=WHITE)
    add_text(s, Inches(0.9), Inches(3.4), Inches(11), Inches(0.8),
             "for South Africa", size=32, color=CYAN)
    add_text(s, Inches(0.9), Inches(4.4), Inches(11), Inches(0.6),
             "Three AI surfaces. Three funding streams. One operating model.",
             size=20, color=WHITE)
    add_text(s, Inches(0.9), Inches(6.4), Inches(11), Inches(0.5),
             "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft  ·  2026-06-03",
             size=12, color=CYAN)


def s2_problem(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "\"We have AI initiatives. We don't have an AI capability.\"",
             size=22, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(1.15), Inches(12), Inches(0.5),
             "The three failure modes we hear from RSA customers in 2026:",
             size=15, color=DARK)
    # Three columns
    titles = ["Pilot purgatory", "Shadow AI sprawl", "Governance debt"]
    bodies = [
        "12+ proofs-of-concept, none in production. No funded path from pilot to platform. Cost without compounding.",
        "Knowledge workers paste customer data into consumer chatbots. CISO has no visibility. POPIA exposure rising.",
        "RAI policy in slideware, not in controls. AGSA/SARB/FSCA can't sample evidence. No quarterly attestation.",
    ]
    colors = [BLUE, PURPLE, CYAN]
    for i, (t, b, c) in enumerate(zip(titles, bodies, colors)):
        x = Inches(0.5 + i * 4.2)
        add_rect(s, x, Inches(2.0), Inches(4.0), Inches(0.55), c)
        add_text(s, x + Inches(0.2), Inches(2.05), Inches(3.6), Inches(0.45),
                 t, size=16, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, Inches(2.55), Inches(4.0), Inches(3.7), LIGHT)
        add_text(s, x + Inches(0.2), Inches(2.7), Inches(3.6), Inches(3.4),
                 b, size=13, color=DARK)
    add_text(s, Inches(0.5), Inches(6.4), Inches(12), Inches(0.5),
             "The AI CoE collapses all three. The next slide shows how.",
             size=14, bold=True, color=NAVY)
    add_footer(s, "AI CoE | The customer's problem")


def s3_moat_grid(prs):
    """Anchor slide: 3 surfaces x 3 streams moat grid."""
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "The moat: three surfaces × three streams = nine cells only Microsoft can fill",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    # Grid: 4 cols (corner + 3 streams) x 4 rows (header + 3 surfaces)
    streams = ["MCAPS-sponsored\n(landing & enable)", "Factory zero-cost\n(F1–F10 build)", "Partner build-run\n(MAICPP scale)"]
    surfaces = ["M365 Copilot", "Copilot Studio", "Azure AI Foundry"]
    # 3x3 cell content
    cells = [
        # M365 Copilot row
        ["Copilot Adoption\nAcceleration ECIF",
         "F3 SOE rollout +\nF7 governance",
         "Partner-led change\n& measurement"],
        # Copilot Studio row
        ["Agent envisioning\n(ACO funded)",
         "F4 Studio agent\nfactory pattern",
         "Partner agent\nbuild-and-run"],
        # Foundry row
        ["Foundry envisioning\n+ landing zone (ACO)",
         "F5 Foundry pattern\n+ F8 eval harness",
         "Partner build-run\nMAICPP commitment"],
    ]
    # Geometry
    x0 = Inches(0.5); y0 = Inches(1.1)
    cw_label = Inches(2.0); cw = Inches(3.55)
    ch_label = Inches(0.7); ch = Inches(1.7)
    # Top-left empty corner
    add_rect(s, x0, y0, cw_label, ch_label, NAVY)
    # Stream headers
    for j, st in enumerate(streams):
        x = x0 + cw_label + j * cw
        add_rect(s, x, y0, cw, ch_label, BLUE)
        add_text(s, x + Inches(0.05), y0 + Inches(0.05), cw - Inches(0.1), ch_label - Inches(0.1),
                 st, size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Surface rows
    row_colors = [LIGHT, WHITE, LIGHT]
    surf_colors = [BLUE, PURPLE, CYAN]
    for i, surf in enumerate(surfaces):
        y = y0 + ch_label + i * ch
        # Surface label
        add_rect(s, x0, y, cw_label, ch, surf_colors[i])
        text_color = WHITE if i != 2 else NAVY
        add_text(s, x0 + Inches(0.05), y + Inches(0.05), cw_label - Inches(0.1), ch - Inches(0.1),
                 surf, size=14, bold=True, color=text_color, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Cells
        for j, content in enumerate(cells[i]):
            x = x0 + cw_label + j * cw
            add_rect(s, x, y, cw, ch, row_colors[i], line=GREY)
            add_text(s, x + Inches(0.1), y + Inches(0.1), cw - Inches(0.2), ch - Inches(0.2),
                     content, size=11, color=DARK, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Caption
    add_text(s, Inches(0.5), Inches(6.55), Inches(12), Inches(0.5),
             "No hyperscaler controls all three surfaces. No SI controls all three streams. The grid is the moat.",
             size=13, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | The moat grid (anchor)")


def s4_unmatched(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Why this grid is unmatched — competitive read",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    rows = [
        ("Hyperscaler A (AWS)", "Has Foundry-equivalent (Bedrock). No M365 install base, no agent runtime sitting in the productivity workflow. Loses surfaces 1 and 2."),
        ("Hyperscaler B (Google)", "Has Workspace + Gemini, has Vertex. Workspace install base in RSA enterprise <15%. Loses surface 1 at scale."),
        ("Pure-play SI (Accenture / IBM)", "Strong on stream 3 (build-run). No equivalent of stream 1 (sponsored landing) or stream 2 (zero-cost factory). Customer pays for everything."),
        ("Niche AI vendor (OpenAI direct, Anthropic direct)", "Substrate only. No grounding in customer's M365 graph, no policy plane, no Purview AI Hub, no AGSA-sample-ready evidence."),
        ("Microsoft AI CoE", "All nine cells. Funded landing, funded factory, partner-scaled run. One CoE charter, one governance posture, one consumption commit."),
    ]
    y = Inches(1.2)
    for i, (label, body) in enumerate(rows):
        c = BLUE if "Microsoft" in label else GREY
        add_rect(s, Inches(0.5), y, Inches(3.5), Inches(0.95), c)
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.3), Inches(0.75),
                 label, size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        bg = LIGHT if "Microsoft" in label else WHITE
        add_rect(s, Inches(4.0), y, Inches(8.8), Inches(0.95), bg, line=GREY)
        add_text(s, Inches(4.15), y + Inches(0.1), Inches(8.55), Inches(0.75),
                 body, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
        y += Inches(1.05)
    add_footer(s, "AI CoE | Competitive read")


def s5_ato(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "ATO economics — the funding spine",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(1.1), Inches(12), Inches(0.5),
             "One Azure Consumption commitment unlocks funded landing, funded factory, and funded first three production use-cases.",
             size=14, color=DARK)
    # Big number block
    add_rect(s, Inches(0.5), Inches(1.9), Inches(4.0), Inches(2.6), BLUE)
    add_text(s, Inches(0.6), Inches(2.0), Inches(3.8), Inches(0.5),
             "Customer commits", size=14, color=CYAN, align=PP_ALIGN.CENTER)
    add_text(s, Inches(0.6), Inches(2.5), Inches(3.8), Inches(1.2),
             "$1", size=88, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.6), Inches(3.8), Inches(3.8), Inches(0.5),
             "of ACR commitment", size=14, color=CYAN, align=PP_ALIGN.CENTER)
    # Arrow concept
    add_rect(s, Inches(4.7), Inches(3.0), Inches(0.4), Inches(0.4), CYAN)
    add_text(s, Inches(4.7), Inches(3.0), Inches(0.4), Inches(0.4),
             "➜", size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Three return blocks
    add_rect(s, Inches(5.3), Inches(1.9), Inches(7.5), Inches(2.6), LIGHT)
    add_text(s, Inches(5.5), Inches(2.0), Inches(7.1), Inches(0.5),
             "Microsoft + partner-funded delivery", size=14, bold=True, color=NAVY)
    add_text(s, Inches(5.5), Inches(2.5), Inches(7.1), Inches(1.2),
             "$3 – $5", size=66, bold=True, color=BLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(5.5), Inches(3.85), Inches(7.1), Inches(0.5),
             "of envisioning, landing zone, factory builds, change & adoption",
             size=12, color=DARK, align=PP_ALIGN.CENTER)
    # Funding instruments
    add_text(s, Inches(0.5), Inches(4.8), Inches(12), Inches(0.4),
             "Instruments stacked behind the ATO:", size=14, bold=True, color=NAVY)
    insts = [
        ("ECIF", "Envisioning, pilot, adoption acceleration"),
        ("MAICPP", "Partner build-and-run subsidy"),
        ("ACO", "Azure Consumption commitment offset"),
        ("SA / CF", "Strategic Architect / Customer Factory IP"),
    ]
    for i, (k, v) in enumerate(insts):
        x = Inches(0.5 + i * 3.15)
        add_rect(s, x, Inches(5.3), Inches(3.0), Inches(1.0), WHITE, line=BLUE)
        add_text(s, x + Inches(0.1), Inches(5.35), Inches(2.8), Inches(0.4),
                 k, size=16, bold=True, color=BLUE)
        add_text(s, x + Inches(0.1), Inches(5.75), Inches(2.8), Inches(0.55),
                 v, size=11, color=DARK)
    add_footer(s, "AI CoE | ATO economics")


def s6_operating(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "The operating model — one CoE, three surfaces, three streams, four gates",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    # CoE centre
    cx, cy = Inches(6.67), Inches(4.0)
    add_rect(s, cx - Inches(1.5), cy - Inches(0.8), Inches(3.0), Inches(1.6), NAVY)
    add_text(s, cx - Inches(1.5), cy - Inches(0.7), Inches(3.0), Inches(0.6),
             "AI CoE", size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    add_text(s, cx - Inches(1.5), cy - Inches(0.1), Inches(3.0), Inches(0.6),
             "charter • RACI", size=13, color=CYAN, align=PP_ALIGN.CENTER)
    add_text(s, cx - Inches(1.5), cy + Inches(0.3), Inches(3.0), Inches(0.5),
             "quarterly attestation", size=11, color=CYAN, align=PP_ALIGN.CENTER)
    # Three surface petals (top)
    surf = [("M365 Copilot", BLUE), ("Copilot Studio", PURPLE), ("Foundry", CYAN)]
    for i, (name, c) in enumerate(surf):
        x = Inches(1.5 + i * 4.0)
        add_rect(s, x, Inches(1.2), Inches(3.0), Inches(1.0), c)
        col = NAVY if c == CYAN else WHITE
        add_text(s, x, Inches(1.3), Inches(3.0), Inches(0.8), name,
                 size=16, bold=True, color=col, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Three streams (left side as inflow)
    strm = ["MCAPS-sponsored", "Factory zero-cost", "Partner build-run"]
    for i, name in enumerate(strm):
        y = Inches(3.0 + i * 0.7)
        add_rect(s, Inches(0.5), y, Inches(2.8), Inches(0.55), LIGHT, line=BLUE)
        add_text(s, Inches(0.6), y + Inches(0.05), Inches(2.6), Inches(0.45),
                 f"$ {name}", size=11, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    # Four gates (right side as outflow)
    gates = ["G1 Envision", "G2 Pre-pilot", "G3 Pre-prod", "G4 Attestation"]
    for i, name in enumerate(gates):
        y = Inches(2.8 + i * 0.65)
        add_rect(s, Inches(10.0), y, Inches(2.8), Inches(0.55), LIGHT, line=PURPLE)
        add_text(s, Inches(10.1), y + Inches(0.05), Inches(2.6), Inches(0.45),
                 f"⚑ {name}", size=11, bold=True, color=PURPLE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.4), Inches(12), Inches(0.5),
             "Three surfaces deliver. Three streams fund. Four gates govern. One CoE owns the spine.",
             size=13, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | Operating model")


def s7_proof(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "What customers ship in 90 days — three outcomes per surface",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    cols = [
        ("M365 Copilot", BLUE, [
            "Tier-1 SOE rollout to 5,000 seats",
            "30%+ weekly active by day 90",
            "1.0–1.5 hr/user/week recovered (T&M measured)",
        ]),
        ("Copilot Studio", PURPLE, [
            "First production agent (HR or service-desk)",
            "Containment ≥45% on intent-routed cases",
            "HITL queue live; reviewer feedback loop closing weekly",
        ]),
        ("Azure AI Foundry", CYAN, [
            "First Foundry pattern in production (DocIntel)",
            "Eval harness live; RAI controls signed off",
            "Unit economics validated via TCO calculator",
        ]),
    ]
    for i, (title, c, items) in enumerate(cols):
        x = Inches(0.5 + i * 4.2)
        add_rect(s, x, Inches(1.2), Inches(4.0), Inches(0.6), c)
        col = NAVY if c == CYAN else WHITE
        add_text(s, x + Inches(0.15), Inches(1.25), Inches(3.7), Inches(0.5),
                 title, size=16, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, Inches(1.8), Inches(4.0), Inches(4.0), LIGHT)
        add_bullets(s, x + Inches(0.15), Inches(2.0), Inches(3.7), Inches(3.7),
                    items, size=13, color=DARK)
    add_text(s, Inches(0.5), Inches(6.2), Inches(12), Inches(0.5),
             "Every outcome is measurable. Every cost is modelled in AI-CoE-AI-TCO-Calculator.xlsx.",
             size=13, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | 90-day proof points")


def s8_ask(prs):
    s = blank(prs); set_bg(s, NAVY)
    add_text(s, Inches(0.5), Inches(0.8), Inches(12), Inches(0.7),
             "What we ask of you", size=32, bold=True, color=WHITE)
    add_text(s, Inches(0.5), Inches(1.6), Inches(12), Inches(0.5),
             "Four asks. Nothing else needed to start.", size=16, color=CYAN)
    asks = [
        ("1", "One named executive sponsor", "C-suite or direct report. Owns the AI CoE charter end-to-end."),
        ("2", "One measurable baseline", "Cycle time, cost-to-serve, or FTE-hours per unit on the chosen workload."),
        ("3", "One signed ATO", "Azure Consumption commitment. Unlocks the funded landing zone and first three use-cases."),
        ("4", "One quarterly review", "Sponsor + CISO + Internal Audit. Attestation evidence sampled and signed."),
    ]
    y = Inches(2.5)
    for num, head, body in asks:
        add_rect(s, Inches(0.5), y, Inches(0.9), Inches(0.9), BLUE)
        add_text(s, Inches(0.5), y, Inches(0.9), Inches(0.9), num,
                 size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, Inches(1.6), y + Inches(0.05), Inches(11), Inches(0.45),
                 head, size=18, bold=True, color=WHITE)
        add_text(s, Inches(1.6), y + Inches(0.5), Inches(11), Inches(0.45),
                 body, size=13, color=CYAN)
        y += Inches(0.95)
    add_text(s, Inches(0.5), Inches(6.6), Inches(12), Inches(0.5),
             "Next step: a 90-minute envisioning workshop. We bring the surfaces, the streams, and a draft charter.",
             size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)


# Slides 9-22 are content slides that re-frame existing material; keep tight.

def s9_m365_deepdive(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), BLUE)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Surface 1 — M365 Copilot: economics + adoption curve",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_bullets(s, Inches(0.6), Inches(1.2), Inches(6.2), Inches(5.5), [
        "Per-seat economics: $30/user/month commercial; ACO can offset against ACR commit on enterprise SKUs.",
        "Adoption is the variable that determines ROI — not the licence price.",
        "T&M-measured recovery target: 1.0–1.5 hr/user/week by day 90; 2.0+ hr/user/week by month 6 in change-led cohorts.",
        "Default offer: Copilot Adoption Acceleration ECIF + Champion network + 12-week measured rhythm.",
        "Anchor accelerator: ACC-3 (M365 Copilot SOE Adoption Playbook).",
    ], size=13)
    # Curve block
    add_rect(s, Inches(7.0), Inches(1.2), Inches(5.8), Inches(5.3), LIGHT, line=BLUE)
    add_text(s, Inches(7.15), Inches(1.3), Inches(5.5), Inches(0.5),
             "Adoption rhythm (RSA reference cohort)", size=14, bold=True, color=NAVY)
    rhythm = [
        ("Week 1–2", "Sponsor brief, persona mapping, baseline T&M"),
        ("Week 3–6", "Champion training, scenario rollout, comms"),
        ("Week 7–10", "Use-case clinics, exec dashboard, weekly KPI review"),
        ("Week 11–12", "Re-baseline T&M, hand-off to BAU, MAICPP partner takes change-mgmt scale"),
    ]
    y = Inches(2.0)
    for w, b in rhythm:
        add_text(s, Inches(7.15), y, Inches(1.8), Inches(0.6), w, size=12, bold=True, color=BLUE)
        add_text(s, Inches(9.0), y, Inches(3.7), Inches(0.9), b, size=11, color=DARK)
        y += Inches(1.05)
    add_footer(s, "AI CoE | Surface deep-dive — M365 Copilot")


def s10_studio_deepdive(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), PURPLE)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Surface 2 — Copilot Studio: agent patterns",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    patterns = [
        ("Intent-routing agent", "Service-desk triage, HR FAQ. Containment 40-60% by month 3."),
        ("Document agent", "Policy lookups, regulator extracts, contract Q&A. Grounded on Purview-labelled SharePoint."),
        ("Process agent", "Onboarding, leave, expense pre-check. Dataverse + Power Automate flow integration."),
        ("Specialist agent", "Loan pre-screen, claims pre-decision, KYC pre-check. HITL on every regulated output."),
    ]
    add_text(s, Inches(0.5), Inches(1.2), Inches(12), Inches(0.5),
             "Four patterns cover ~85% of first-agent customer demand in RSA:",
             size=13, color=DARK)
    for i, (h, b) in enumerate(patterns):
        y = Inches(1.9 + i * 1.05)
        add_rect(s, Inches(0.5), y, Inches(3.2), Inches(0.9), PURPLE)
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.0), Inches(0.7),
                 h, size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(3.7), y, Inches(9.1), Inches(0.9), LIGHT, line=GREY)
        add_text(s, Inches(3.85), y + Inches(0.1), Inches(8.85), Inches(0.7),
                 b, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(s, "AI CoE | Surface deep-dive — Copilot Studio")


def s11_foundry_deepdive(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Surface 3 — Azure AI Foundry: build-and-run with RAI guardrails",
             size=20, bold=True, color=CYAN, anchor=MSO_ANCHOR.MIDDLE)
    layers = [
        ("Experience", BLUE, "Custom UI / API / embedded surfaces; reasoning trace surfaced to reviewer"),
        ("Orchestration", PURPLE, "Foundry prompt-flow, agent SDK, function calling, retrieval pipelines"),
        ("Reasoning", CYAN, "Model mix: gpt-4o, gpt-4o-mini, Phi-3, fine-tuned specialists; routing by cost & latency"),
        ("Data & grounding", BLUE, "AI Search, Cosmos DB vector, Purview lineage, region-pinned residency"),
        ("Governance & safety", PURPLE, "Content Safety, Prompt Shields, Defender for Cloud AI, Purview AI Hub, eval harness"),
    ]
    for i, (name, c, body) in enumerate(layers):
        y = Inches(1.2 + i * 1.1)
        add_rect(s, Inches(0.5), y, Inches(3.0), Inches(0.95), c)
        col = NAVY if c == CYAN else WHITE
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(2.8), Inches(0.75),
                 name, size=14, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(3.5), y, Inches(9.3), Inches(0.95), LIGHT, line=GREY)
        add_text(s, Inches(3.65), y + Inches(0.1), Inches(9.0), Inches(0.75),
                 body, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_footer(s, "AI CoE | Surface deep-dive — Foundry")


def s12_factory(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Stream 2 execution — the F1–F10 Factory",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    f = [
        ("F1", "Envision"), ("F2", "Landing zone"), ("F3", "M365 rollout"),
        ("F4", "Studio agent"), ("F5", "Foundry pattern"), ("F6", "Data & RAG"),
        ("F7", "Governance"), ("F8", "Eval harness"), ("F9", "Change & adoption"),
        ("F10", "Run & FinOps"),
    ]
    for i, (code, name) in enumerate(f):
        row, col = divmod(i, 5)
        x = Inches(0.5 + col * 2.55)
        y = Inches(1.3 + row * 2.4)
        add_rect(s, x, y, Inches(2.4), Inches(0.6), BLUE)
        add_text(s, x, y, Inches(2.4), Inches(0.6), code,
                 size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, y + Inches(0.6), Inches(2.4), Inches(1.7), LIGHT, line=BLUE)
        add_text(s, x + Inches(0.1), y + Inches(0.7), Inches(2.2), Inches(1.5),
                 name, size=13, bold=True, color=NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.55), Inches(12), Inches(0.5),
             "Each F is a re-usable pattern with code, docs, and ECIF backing. Zero-cost to the customer through stream 2.",
             size=13, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | F1–F10 Factory")


def s13_partner(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Stream 3 — Partner build-run via MAICPP",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_bullets(s, Inches(0.6), Inches(1.2), Inches(12), Inches(5.5), [
        "MAICPP funds partner-led envisioning, build, deployment, and adoption against named workloads.",
        "RSA partner shortlist (12 named) qualified via AI-CoE-Partner-Scorecard.xlsx — coverage across BFSI, public sector, retail, telco, mining, healthcare.",
        "Partner takes per-unit delivery risk in outcome-based archetypes (see Operating Playbook Addendum).",
        "Microsoft retains the platform commitment; partner owns the run. Single CoE charter binds both.",
        "Partner exit: 90-day notice on operational delivery; CoE charter and ATO remain with Microsoft.",
    ], size=14)
    add_footer(s, "AI CoE | Partner build-run")


def s14_sovereign(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Sovereign AI for regulated buyers",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    dims = [
        ("Data sovereignty", BLUE, "Residency in SA North / West; CMK in customer-controlled Key Vault; Purview lineage; region-pin via Azure Policy."),
        ("Operational sovereignty", PURPLE, "RSA-based support & operations; named clearance; partner-DPA addendum; AGSA-ready evidence pack."),
        ("Digital sovereignty", CYAN, "Microsoft Cloud for Sovereignty constructs; SLM/Phi options for sensitive workloads; open Foundry models for portability."),
    ]
    for i, (h, c, b) in enumerate(dims):
        y = Inches(1.3 + i * 1.7)
        add_rect(s, Inches(0.5), y, Inches(3.3), Inches(1.4), c)
        col = NAVY if c == CYAN else WHITE
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.1), Inches(1.2),
                 h, size=16, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(3.8), y, Inches(9.0), Inches(1.4), LIGHT, line=GREY)
        add_text(s, Inches(3.95), y + Inches(0.15), Inches(8.7), Inches(1.1),
                 b, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.4), Inches(12), Inches(0.5),
             "Full offer: AI-CoE-Sovereign-AI-RSA.pptx. Underlying platform: ACC-2 POPIA Landing Zone.",
             size=12, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | Sovereign AI")


def s15_governance(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Governance & RAI posture — four gates + the control plane",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    gates = [
        ("G1 Envision", "Use-case registered, sponsor named, value hypothesis"),
        ("G2 Pre-pilot", "Impact assessment signed, controls selected, partner DPA"),
        ("G3 Pre-production", "Eval harness, HITL queue, kill-switch, Purview AI Hub onboarded"),
        ("G4 Attestation (quarterly)", "Controls re-verified, drift surfaced, AGSA-sample-ready evidence"),
    ]
    for i, (h, b) in enumerate(gates):
        y = Inches(1.3 + i * 1.1)
        add_rect(s, Inches(0.5), y, Inches(3.5), Inches(0.95), PURPLE)
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.3), Inches(0.75),
                 h, size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(4.0), y, Inches(8.8), Inches(0.95), LIGHT, line=GREY)
        add_text(s, Inches(4.15), y + Inches(0.1), Inches(8.55), Inches(0.75),
                 b, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.4), Inches(12), Inches(0.5),
             "Full operating manual: AI-CoE-AI-Governance-Playbook.docx + AI-CoE-AI-Impact-Assessment.xlsx.",
             size=12, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | Governance & RAI")


def s16_kpis(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "KPI scaffold — what we measure every quarter",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    quads = [
        ("Adoption", BLUE, ["Weekly active users", "Use-cases in production", "Champion network coverage"]),
        ("Value", PURPLE, ["FTE-hrs recovered", "Cost-per-unit decline", "Cycle-time reduction"]),
        ("Risk", CYAN, ["Open RAI findings", "Incident MTTR", "Audit-sample pass rate"]),
        ("Cost / FinOps", BLUE, ["$/query", "$/user/month", "Cache-hit & routing efficiency"]),
    ]
    for i, (h, c, items) in enumerate(quads):
        row, col = divmod(i, 2)
        x = Inches(0.5 + col * 6.3)
        y = Inches(1.2 + row * 2.7)
        add_rect(s, x, y, Inches(6.0), Inches(0.55), c)
        text_col = NAVY if c == CYAN else WHITE
        add_text(s, x + Inches(0.15), y + Inches(0.05), Inches(5.7), Inches(0.45),
                 h, size=15, bold=True, color=text_col, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, y + Inches(0.55), Inches(6.0), Inches(2.0), LIGHT)
        add_bullets(s, x + Inches(0.2), y + Inches(0.7), Inches(5.6), Inches(1.8),
                    items, size=12)
    add_footer(s, "AI CoE | KPI scaffold")


def s17_proof_customers(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Reference customers — anonymised RSA + global proof",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    refs = [
        ("Global SI partner — NTT DATA", "Scaled M365 Copilot to 30,000+ knowledge workers; CoE-led adoption playbook."),
        ("Global SI partner — Capgemini", "Foundry-built agent factory across BFSI clients; MAICPP economics."),
        ("RSA tier-1 bank (anonymised)", "Contact-centre agent + KYC DocIntel; AGSA-ready evidence pack."),
        ("RSA SOE (anonymised)", "Citizen-services agent + PFMA evidence trail; sovereign deployment SA North."),
    ]
    for i, (h, b) in enumerate(refs):
        row, col = divmod(i, 2)
        x = Inches(0.5 + col * 6.3)
        y = Inches(1.3 + row * 2.5)
        add_rect(s, x, y, Inches(6.0), Inches(0.65), BLUE)
        add_text(s, x + Inches(0.15), y + Inches(0.1), Inches(5.7), Inches(0.5),
                 h, size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, y + Inches(0.65), Inches(6.0), Inches(1.65), LIGHT, line=BLUE)
        add_text(s, x + Inches(0.15), y + Inches(0.75), Inches(5.7), Inches(1.5),
                 b, size=12, color=DARK)
    add_footer(s, "AI CoE | References")


def s18_pillars_checklist(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Appendix — the 5+1 Pillars as coverage checklist",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(1.15), Inches(12), Inches(0.5),
             "Used by the CoE to confirm an engagement covers every pillar. Not used as the customer-facing spine.",
             size=12, color=GREY)
    pillars = [
        ("P1 Business Strategy", "Value hypothesis, sponsor, baseline, target ROI"),
        ("P2 Org & Culture", "Champion network, change-mgmt, role-based skilling"),
        ("P3 AI Strategy & Experience", "Surface choice, agent patterns, user-experience standards"),
        ("P4 Tech & Data", "Landing zone, grounding data, integration, FinOps"),
        ("P5 Governance & Security", "Four gates, RAI controls, attestation cadence"),
        ("P+1 Co-sell & Partner", "MAICPP partner alignment, joint GTM, hand-off"),
    ]
    for i, (h, b) in enumerate(pillars):
        y = Inches(1.7 + i * 0.75)
        add_rect(s, Inches(0.5), y, Inches(0.4), Inches(0.6), BLUE)
        add_text(s, Inches(0.5), y, Inches(0.4), Inches(0.6), "✓",
                 size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, Inches(1.0), y + Inches(0.05), Inches(4.0), Inches(0.5),
                 h, size=13, bold=True, color=NAVY)
        add_text(s, Inches(5.0), y + Inches(0.05), Inches(8.0), Inches(0.5),
                 b, size=12, color=DARK)
    add_footer(s, "AI CoE | Pillars coverage checklist")


def s19_ladder(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Appendix — 3-tier CoE Ladder",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    tiers = [
        ("T1 Foundational", BLUE, "Landing zone, governance baseline, first M365 SOE cohort, first agent. 0–6 months."),
        ("T2 Scaling", PURPLE, "Multi-surface agents in production, partner build-run live, factory rhythm established. 6–18 months."),
        ("T3 Industrialised", CYAN, "AI capability is a P&L line; FinOps mature; sovereign posture; quarterly attestation routine. 18+ months."),
    ]
    for i, (h, c, b) in enumerate(tiers):
        y = Inches(1.4 + i * 1.7)
        add_rect(s, Inches(0.5), y, Inches(3.3), Inches(1.4), c)
        col = NAVY if c == CYAN else WHITE
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.1), Inches(1.2),
                 h, size=18, bold=True, color=col, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(3.8), y, Inches(9.0), Inches(1.4), LIGHT, line=GREY)
        add_text(s, Inches(3.95), y + Inches(0.15), Inches(8.7), Inches(1.1),
                 b, size=13, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.5), Inches(12), Inches(0.4),
             "Climb only as far as the customer's value hypothesis justifies. T3 is not the default goal.",
             size=12, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | CoE ladder")


def s20_verticals(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Appendix — industry vertical briefings",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(1.1), Inches(12), Inches(0.5),
             "Six sector-tailored 9-slide briefings, each naming regulators, top 3 use-cases, anonymised RSA reference, ATO sizing:",
             size=13, color=DARK)
    sectors = [
        "Banking & Insurance (SARB · FSCA · PA · FAIS · FICA)",
        "Retail (POPIA · PCI-DSS · CPA · NCA)",
        "Telco (ICASA · RICA · POPIA)",
        "Mining (DMRE · MHSA · DFFE · NEMA)",
        "Public Sector / SOE (PFMA · MFMA · AGSA · SITA)",
        "Healthcare (HPCSA · CMS · NHI · SAHPRA)",
    ]
    for i, sec in enumerate(sectors):
        row, col = divmod(i, 2)
        x = Inches(0.5 + col * 6.3)
        y = Inches(2.0 + row * 1.3)
        add_rect(s, x, y, Inches(0.7), Inches(1.0), BLUE)
        add_text(s, x, y, Inches(0.7), Inches(1.0), "▸",
                 size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x + Inches(0.7), y, Inches(5.3), Inches(1.0), LIGHT, line=BLUE)
        add_text(s, x + Inches(0.85), y + Inches(0.15), Inches(5.0), Inches(0.7),
                 sec, size=12, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.5), Inches(12), Inches(0.4),
             "Files: AI-CoE-Sector-Briefing-{Banking-Insurance | Retail | Telco | Mining | Public-Sector | Healthcare}.pptx",
             size=11, color=GREY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | Verticals")


def s21_commercial(prs):
    s = blank(prs); set_bg(s, WHITE)
    add_rect(s, 0, 0, SW, Inches(0.9), NAVY)
    add_text(s, Inches(0.5), Inches(0.2), Inches(12), Inches(0.55),
             "Appendix — commercial archetypes (risk-share & outcome-based)",
             size=20, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    arc = [
        ("Per-resolved-case", "Service desk, claims, complaints. Unit price per case to SLA."),
        ("Per-document-processed", "KYC, permits, contracts. Unit price per document, auditor sample."),
        ("Per-hour-recovered", "Copilot adoption. Fee tied to T&M-measured FTE-hour recovery."),
        ("Gain-share", "% of audited P&L uplift. CFO + Internal Audit + Legal sign-off."),
    ]
    for i, (h, b) in enumerate(arc):
        y = Inches(1.3 + i * 1.1)
        add_rect(s, Inches(0.5), y, Inches(3.5), Inches(0.95), PURPLE)
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(3.3), Inches(0.75),
                 h, size=14, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(4.0), y, Inches(8.8), Inches(0.95), LIGHT, line=GREY)
        add_text(s, Inches(4.15), y + Inches(0.1), Inches(8.55), Inches(0.75),
                 b, size=12, color=DARK, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, Inches(0.5), Inches(6.4), Inches(12), Inches(0.5),
             "Full archetype detail: AI-CoE-Operating-Playbook-Addendum.docx.",
             size=12, color=NAVY, align=PP_ALIGN.CENTER)
    add_footer(s, "AI CoE | Commercial archetypes")


def s22_index(prs):
    s = blank(prs); set_bg(s, NAVY)
    add_text(s, Inches(0.5), Inches(0.5), Inches(12), Inches(0.7),
             "Linked artefacts — the pack at a glance", size=26, bold=True, color=WHITE)
    rows = [
        ("Customer-facing", "Customer-Pitch · Pitch-Deck · Executive-OnePager · Horizon-Assessment · Sovereign-AI-RSA · Sector briefings (×6)"),
        ("Governance", "AI-Impact-Assessment.xlsx · AI-Governance-Playbook.docx · Academy-Curriculum.xlsx"),
        ("Internal delivery", "Operating-Playbook (+ Addendum) · Delivery-RACI · FY27-Launch-Plan · How-To-Use · VBD-Reference-Deck · Objection-Handling"),
        ("Economics", "AI-TCO-Calculator.xlsx · Partner-Scorecard.xlsx · ATO economics slide (deck 5)"),
        ("Partner", "Partner-Recruitment-Kit · Partner-Scorecard"),
        ("Accelerators", "ACC-1 Banking CX · ACC-2 POPIA LZ · ACC-3 SOE Copilot · ACC-4 Regulated Pilot · ACC-5 DocIntel+Foundry"),
    ]
    y = Inches(1.5)
    for h, b in rows:
        add_rect(s, Inches(0.5), y, Inches(2.8), Inches(0.7), BLUE)
        add_text(s, Inches(0.6), y + Inches(0.1), Inches(2.6), Inches(0.5),
                 h, size=13, bold=True, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, Inches(3.3), y, Inches(9.5), Inches(0.7), LIGHT, line=BLUE)
        add_text(s, Inches(3.45), y + Inches(0.1), Inches(9.2), Inches(0.5),
                 b, size=11, color=NAVY, anchor=MSO_ANCHOR.MIDDLE)
        y += Inches(0.8)


def main() -> None:
    # Patch add_text to ignore unsupported kwargs (italic_safe used as marker only)
    prs = new_prs()
    s1_title(prs)
    s2_problem(prs)
    s3_moat_grid(prs)
    s4_unmatched(prs)
    s5_ato(prs)
    s6_operating(prs)
    s7_proof(prs)
    s8_ask(prs)
    s9_m365_deepdive(prs)
    s10_studio_deepdive(prs)
    s11_foundry_deepdive(prs)
    s12_factory(prs)
    s13_partner(prs)
    s14_sovereign(prs)
    s15_governance(prs)
    s16_kpis(prs)
    s17_proof_customers(prs)
    s18_pillars_checklist(prs)
    s19_ladder(prs)
    s20_verticals(prs)
    s21_commercial(prs)
    s22_index(prs)
    prs.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(prs.slides)} slides")


if __name__ == "__main__":
    main()
