"""Generate AI-CoE-Three-Surface-Offers.pptx.

Three packaged, simple offers — one per AI surface (M365 Copilot, Copilot Studio,
Azure AI Foundry) — drawn from the VBD Reference Deck. Each offer bundles 3-5
VBDs in a clear envision -> build -> realise sequence with named funding,
duration, and exec sponsor ask. The deck is the customer-facing menu the CSA
runs against; the VBD Reference Deck remains the internal catalogue.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

OUT = Path(__file__).parent / "AI-CoE-Three-Surface-Offers.pptx"

NAVY = RGBColor(0x0B, 0x1F, 0x3A)
BLUE = RGBColor(0x00, 0x67, 0xB8)
CYAN = RGBColor(0x50, 0xE6, 0xFF)
LIGHT = RGBColor(0xEA, 0xF4, 0xFB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREY = RGBColor(0x59, 0x59, 0x59)
DARK = RGBColor(0x20, 0x20, 0x20)

SW, SH = Inches(13.333), Inches(7.5)


# --------------------------------------------------------------------------- #
# Drawing helpers
# --------------------------------------------------------------------------- #

def blank(prs: Presentation):
    return prs.slides.add_slide(prs.slide_layouts[6])


def set_bg(slide, color: RGBColor) -> None:
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
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


def add_bullets(slide, x, y, w, h, items, *, size: int = 11,
                color: RGBColor = DARK, bold_first: bool = False) -> None:
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
        r.font.bold = bold_first and i == 0


def add_footer(slide, label: str, page: str) -> None:
    bar = add_rect(slide, 0, SH - Inches(0.35), SW, Inches(0.35), NAVY)
    add_text(slide, Inches(0.4), SH - Inches(0.33), SW - Inches(2.0), Inches(0.3),
             label, size=9, color=WHITE, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, SW - Inches(1.8), SH - Inches(0.33), Inches(1.4), Inches(0.3),
             page, size=9, color=WHITE, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)


def slide_title(slide, eyebrow: str, title: str) -> None:
    """Standard header: navy band with eyebrow + title."""
    add_rect(slide, 0, 0, SW, Inches(1.25), NAVY)
    add_text(slide, Inches(0.5), Inches(0.18), SW - Inches(1.0), Inches(0.35),
             eyebrow.upper(), size=11, bold=True, color=CYAN)
    add_text(slide, Inches(0.5), Inches(0.5), SW - Inches(1.0), Inches(0.7),
             title, size=22, bold=True, color=WHITE)


# --------------------------------------------------------------------------- #
# Offer data
# --------------------------------------------------------------------------- #

class VBD:
    def __init__(self, code, name, mcem, funding, note):
        self.code = code
        self.name = name
        self.mcem = mcem
        self.funding = funding
        self.note = note


class Offer:
    def __init__(self, surface, name, outcome, buyer, duration, envelope,
                 commitment, vbds, why):
        self.surface = surface
        self.name = name
        self.outcome = outcome
        self.buyer = buyer
        self.duration = duration
        self.envelope = envelope
        self.commitment = commitment
        self.vbds = vbds
        self.why = why


OFFERS = [
    Offer(
        surface="M365 Copilot",
        name="Copilot Productivity Sprint",
        outcome="Measurable Copilot adoption and recovered FTE-hours across the "
                "top five business functions within 90 days.",
        buyer="COO + CHRO (sponsor) · CIO (delivery)",
        duration="12–16 weeks",
        envelope="ECIF + SA-funded; ACO offsets seat economics",
        commitment="Named exec sponsor · baseline T&M measurement · 5,000-seat tier-1 SOE",
        why="Adoption is the variable that determines Copilot ROI. This bundle "
            "compresses inspire → secure → adopt → measure into one 90-day motion.",
        vbds=[
            VBD("A1", "Art of the Possible",
                "MCEM 2 · Inspire & Design", "ECIF",
                "Half-day exec workshop; persona-mapped scenarios; sponsor sign-off on top 5 use-cases."),
            VBD("A6", "Data Security Assessment",
                "MCEM 2 · Governance overlay", "SA-funded",
                "Purview readiness, oversharing scan, sensitivity-label posture before Copilot rollout."),
            VBD("A3", "Copilot Adoption Accelerator",
                "MCEM 3 · Empower & Achieve", "ECIF / MAICPP",
                "Champion network, comms cadence, prompt library, training rhythm — the engine that converts pilot to value."),
            VBD("A4", "Optimization & Value Realization",
                "MCEM 4–5 · Realize", "ACO / Customer-funded",
                "Active-Use telemetry, sentiment + habit scoring, T&M-measured FTE-hour recovery; quarterly attestation."),
        ],
    ),
    Offer(
        surface="Copilot Studio + Power Platform",
        name="First Production Agent",
        outcome="One named production agent — built, governed, and live in a "
                "business process — with a Power Platform CoE wrap to scale "
                "the next four.",
        buyer="Business-unit head (sponsor) · IT / Power Platform lead",
        duration="8–12 weeks",
        envelope="MAICPP partner-funded build; SA for readiness; CF for CoE",
        commitment="One workload (service-desk, HR, or process) · DPA in place · HITL reviewer named",
        why="Every customer asks for 'an agent'. This bundle moves from "
            "envisioning to a single production agent with the governance "
            "rails the audit team requires.",
        vbds=[
            VBD("B1", "Agent in a Day",
                "MCEM 2 · Inspire & Design", "ECIF",
                "Hands-on day; first low-code agent built; workload candidate selected for production build."),
            VBD("B7", "Copilot Studio Solution Assessment",
                "MCEM 2 · Readiness", "SA-funded",
                "Environment + data + integration readiness scored; risks and controls catalogued before build."),
            VBD("B2", "Copilot Studio Co-build",
                "MCEM 3 · Empower & Achieve", "MAICPP",
                "Partner-led co-build of the named agent with HITL queue, eval harness, Purview labelling."),
            VBD("B6", "Power Platform CoE Starter Kit",
                "MCEM 3–4 · Govern at scale", "Customer-funded",
                "Environment strategy, DLP policies, maker enablement; the rails that let agents 2–5 ship faster."),
        ],
    ),
    Offer(
        surface="Azure AI Foundry",
        name="Foundry ATO Bundle — Foundation + First Agent",
        outcome="A production-grade Foundry foundation (ALZ + RAI + GenAIOps) "
                "and the first Foundry-built agent in production — with the "
                "$1M ATO envelope wrapped around it.",
        buyer="CIO / CTO (sponsor) · Head of Data & AI · CISO",
        duration="16–24 weeks",
        envelope="Up to $1M (ATO C1 ECIF + ATO C2 ECIF + ATO C2 ACO uplift + ATO C3 stack)",
        commitment="Azure Consumption commitment · cleared engineer pool or partner · first workload named",
        why="The keystone bundle. One contract traverses pillars 1–5, tiers "
            "T1→T2+T3, MCEM 2→3. Funding multiplier: $1 ECIF unlocks $3–$5 ACR.",
        vbds=[
            VBD("C16", "ATO C1 — CoE & Envisioning",
                "MCEM 2 · Inspire & Design", "ECIF (up to $50K pre-sales)",
                "AI CoE charter, sponsor named, use-case backlog, value hypothesis registered at G1 gate."),
            VBD("C17", "ATO C2 — Foundation Architecture",
                "MCEM 3 · Empower & Achieve",
                "ECIF (up to $500K) + ACO uplift (up to $500K)",
                "ALZ + Foundry foundation; private endpoints; CMK; Purview; eval-harness scaffolding."),
            VBD("C18", "ATO C3 — Agent Factory",
                "MCEM 3 · Empower & Achieve", "ECIF + ACO + MAICPP",
                "First Foundry agent in production; factory pattern; RAI controls signed off; G3 gate passed."),
            VBD("C13", "GenAIOps Maturity (ATO 3.1)",
                "MCEM 4–5 · Realize & Operate", "ECIF / ACO",
                "Eval pipelines, drift + cost telemetry, HITL queue ops, quarterly G4 attestation."),
        ],
    ),
]


# --------------------------------------------------------------------------- #
# Speaker notes per slide
# --------------------------------------------------------------------------- #

NOTES = [
    # 1 title
    "Opening. Three offers, three surfaces — the customer-facing menu we run "
    "against the 40+ VBDs in the AI-CoE-VBD-Reference-Deck. Each offer is 3-5 "
    "VBDs, named funding, named buyer, named outcome. Pick one or sequence them.",
    # 2 overview
    "The one-slide comparison. Walk left to right. Customers usually start with "
    "the M365 Sprint (fastest to value) and add the Foundry ATO Bundle once an "
    "Azure commit is signed. Studio's First Production Agent is the cross-sell "
    "for business-unit sponsors who want their own agent.",
    # 3 offer 1
    "Copilot Productivity Sprint. The default offer when the buyer is COO or "
    "CHRO. Inspire (A1), secure (A6), adopt (A3 - the engine), measure (A4). "
    "90-day window. Adoption is the variable; A3 is the line item that "
    "determines whether the Copilot programme returns value.",
    # 4 offer 2
    "First Production Agent. The default offer when a business-unit head wants "
    "their own agent. Hands-on inspire (B1), readiness (B7), partner co-build "
    "(B2 - MAICPP-funded), then CoE wrap (B6) to scale the next four. Outcome "
    "is one production agent live with HITL and Purview labelling.",
    # 5 offer 3
    "Foundry ATO Bundle. The keystone. CIO/CTO sponsor. One contract, $1M "
    "envelope, traverses pillars 1-5 and MCEM 2-3 in a single motion. C16 "
    "envisions and registers the CoE; C17 builds the ALZ + Foundry foundation; "
    "C18 ships the first production agent; C13 operates it. Anchor every "
    "Foundry conversation here.",
    # 6 next steps
    "Close. Two rules: lead with the surface the buyer's pain maps to; never "
    "pitch all three at once. The VBD Reference Deck remains the internal "
    "catalogue. This deck is the menu — three offers, named outcomes, named "
    "funding, named asks. Pre-flight every commit on MCAPS Catalog.",
]


# --------------------------------------------------------------------------- #
# Slide builders
# --------------------------------------------------------------------------- #

def add_notes(slide, text: str) -> None:
    tf = slide.notes_slide.notes_text_frame
    tf.clear()
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = text
    r.font.size = Pt(11)


def cover_slide(prs):
    s = blank(prs)
    set_bg(s, WHITE)
    add_rect(s, 0, 0, Inches(8.0), SH, NAVY)
    add_text(s, Inches(0.6), Inches(0.55), Inches(7.0), Inches(0.45),
             "AI CENTER OF EXCELLENCE · THREE-SURFACE OFFER MENU",
             size=12, bold=True, color=CYAN)
    add_text(s, Inches(0.6), Inches(1.6), Inches(7.0), Inches(1.4),
             "Three Offers, One per Surface", size=38, bold=True, color=WHITE)
    add_text(s, Inches(0.6), Inches(3.05), Inches(7.0), Inches(1.5),
             "Simple bundles drawn from the 40+ CSU AI VBDs — "
             "one for M365 Copilot, one for Copilot Studio, one for Azure AI Foundry. "
             "Each bundle carries 3–5 VBDs in a clear envision → build → realise sequence.",
             size=15, color=LIGHT)
    add_text(s, Inches(0.6), Inches(5.3), Inches(7.0), Inches(0.5),
             "Yuri Baijnath", size=15, bold=True, color=WHITE)
    add_text(s, Inches(0.6), Inches(5.75), Inches(7.0), Inches(0.4),
             "CSU Cloud & AI Lead (South Africa) · Microsoft",
             size=12, color=LIGHT)
    add_text(s, Inches(0.6), Inches(6.6), Inches(7.0), Inches(0.4),
             "Pairs with AI-CoE-VBD-Reference-Deck.pptx (internal catalogue)",
             size=10, color=CYAN)
    # right-hand accent column with stacked triangles
    add_rect(s, Inches(8.0), 0, Inches(0.08), SH, CYAN)
    palette = [(CYAN, 0.0), (BLUE, 180.0), (NAVY, 0.0), (CYAN, 90.0)]
    band = SH / 4
    for i, (color, rot) in enumerate(palette):
        sz = min(Inches(2.2), Inches(1.6))
        cy = int(i * band + (band - sz) / 2)
        cx = Inches(8.0) + Inches(0.4)
        tri = s.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, cx, cy, sz, sz)
        tri.fill.solid(); tri.fill.fore_color.rgb = color
        tri.line.fill.background(); tri.shadow.inherit = False
        tri.rotation = rot
    add_notes(s, NOTES[0])


def overview_slide(prs):
    s = blank(prs)
    set_bg(s, WHITE)
    slide_title(s, "Overview", "Three offers — pick by buyer and by surface")
    add_text(s, Inches(0.5), Inches(1.35), SW - Inches(1.0), Inches(0.5),
             "Each offer bundles 3–5 VBDs in a clear envision → build → realise sequence.",
             size=13, color=GREY)

    col_w = Inches(4.15)
    col_h = Inches(5.0)
    gap = Inches(0.15)
    x0 = Inches(0.5)
    y0 = Inches(2.0)
    for i, o in enumerate(OFFERS):
        x = x0 + (col_w + gap) * i
        # header band
        add_rect(s, x, y0, col_w, Inches(0.7), BLUE)
        add_text(s, x + Inches(0.2), y0 + Inches(0.1), col_w - Inches(0.4),
                 Inches(0.3), o.surface.upper(), size=10, bold=True, color=CYAN)
        add_text(s, x + Inches(0.2), y0 + Inches(0.32), col_w - Inches(0.4),
                 Inches(0.35), o.name, size=14, bold=True, color=WHITE)
        # body
        add_rect(s, x, y0 + Inches(0.7), col_w, col_h - Inches(0.7), LIGHT)
        ty = y0 + Inches(0.85)
        add_text(s, x + Inches(0.2), ty, col_w - Inches(0.4), Inches(0.4),
                 "OUTCOME", size=9, bold=True, color=BLUE)
        add_text(s, x + Inches(0.2), ty + Inches(0.3), col_w - Inches(0.4),
                 Inches(1.2), o.outcome, size=10, color=DARK)
        add_text(s, x + Inches(0.2), ty + Inches(1.55), col_w - Inches(0.4),
                 Inches(0.3), "VBDs", size=9, bold=True, color=BLUE)
        vbd_list = [f"{v.code} {v.name}" for v in o.vbds]
        add_bullets(s, x + Inches(0.2), ty + Inches(1.85), col_w - Inches(0.4),
                    Inches(1.7), vbd_list, size=10)
        add_text(s, x + Inches(0.2), ty + Inches(3.4), col_w - Inches(0.4),
                 Inches(0.3), "DURATION · ENVELOPE", size=9, bold=True, color=BLUE)
        add_text(s, x + Inches(0.2), ty + Inches(3.7), col_w - Inches(0.4),
                 Inches(0.5), f"{o.duration}  ·  {o.envelope}", size=10, color=DARK)
    add_footer(s, "AI CoE · Three-Surface Offers · Customer Menu", "2 / 6")
    add_notes(s, NOTES[1])


def offer_slide(prs, offer: Offer, page_num: int, note: str):
    s = blank(prs)
    set_bg(s, WHITE)
    slide_title(s, f"Offer · {offer.surface}", offer.name)

    # Left summary panel
    panel_x = Inches(0.5)
    panel_y = Inches(1.5)
    panel_w = Inches(4.4)
    panel_h = Inches(5.4)
    add_rect(s, panel_x, panel_y, panel_w, panel_h, NAVY)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(0.2),
             panel_w - Inches(0.5), Inches(0.35),
             "OUTCOME", size=10, bold=True, color=CYAN)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(0.55),
             panel_w - Inches(0.5), Inches(1.5), offer.outcome,
             size=12, color=WHITE)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(2.1),
             panel_w - Inches(0.5), Inches(0.3),
             "TARGET BUYER", size=10, bold=True, color=CYAN)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(2.4),
             panel_w - Inches(0.5), Inches(0.5), offer.buyer,
             size=11, color=WHITE)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(3.0),
             panel_w - Inches(0.5), Inches(0.3),
             "DURATION", size=10, bold=True, color=CYAN)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(3.3),
             panel_w - Inches(0.5), Inches(0.4), offer.duration,
             size=11, color=WHITE)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(3.75),
             panel_w - Inches(0.5), Inches(0.3),
             "FUNDING ENVELOPE", size=10, bold=True, color=CYAN)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(4.05),
             panel_w - Inches(0.5), Inches(0.65), offer.envelope,
             size=11, color=WHITE)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(4.75),
             panel_w - Inches(0.5), Inches(0.3),
             "CUSTOMER COMMITS", size=10, bold=True, color=CYAN)
    add_text(s, panel_x + Inches(0.25), panel_y + Inches(5.05),
             panel_w - Inches(0.5), Inches(0.35), offer.commitment,
             size=10, color=WHITE)

    # Right: VBD sequence cards
    rx = Inches(5.1)
    ry = Inches(1.5)
    rw = SW - rx - Inches(0.5)
    add_text(s, rx, ry, rw, Inches(0.35),
             f"{len(offer.vbds)} VBDS · ENVISION → BUILD → REALISE",
             size=10, bold=True, color=BLUE)
    card_h = (Inches(5.4) - Inches(0.4)) / len(offer.vbds)
    for i, v in enumerate(offer.vbds):
        cy = ry + Inches(0.4) + card_h * i + Inches(0.05)
        ch = card_h - Inches(0.1)
        # accent stripe
        add_rect(s, rx, cy, Inches(0.15), ch, CYAN if i % 2 == 0 else BLUE)
        # card body
        add_rect(s, rx + Inches(0.15), cy, rw - Inches(0.15), ch, LIGHT)
        # code + name
        add_text(s, rx + Inches(0.35), cy + Inches(0.08),
                 Inches(0.8), Inches(0.4),
                 v.code, size=14, bold=True, color=BLUE)
        add_text(s, rx + Inches(1.15), cy + Inches(0.08),
                 rw - Inches(1.4), Inches(0.4),
                 v.name, size=13, bold=True, color=DARK)
        # mcem + funding tags
        add_text(s, rx + Inches(0.35), cy + Inches(0.45),
                 rw - Inches(0.5), Inches(0.3),
                 f"{v.mcem}  ·  {v.funding}",
                 size=9, bold=True, color=GREY)
        # note
        add_text(s, rx + Inches(0.35), cy + Inches(0.75),
                 rw - Inches(0.5), ch - Inches(0.8),
                 v.note, size=10, color=DARK)

    # Why-this-bundle ribbon (bottom)
    add_rect(s, Inches(0.5), Inches(6.95), SW - Inches(1.0), Inches(0.18), CYAN)
    add_footer(s, f"AI CoE · {offer.surface} · {offer.name}", f"{page_num} / 6")
    add_notes(s, note)


def closing_slide(prs):
    s = blank(prs)
    set_bg(s, WHITE)
    slide_title(s, "How to choose", "Two rules — and pre-flight every commit")

    # Three rule cards
    rules = [
        ("LEAD WITH THE BUYER'S PAIN",
         "COO/CHRO → Copilot Productivity Sprint. BU head → First Production Agent. "
         "CIO/CTO + Azure commit → Foundry ATO Bundle. Surface follows pain, not the other way around."),
        ("NEVER PITCH ALL THREE",
         "Pick one. Land it. Earn the right to sequence the next. A sequenced "
         "second offer always lands harder than two pitched at once."),
        ("PRE-FLIGHT EVERY COMMIT",
         "Re-verify VERIFY-flagged VBDs on MCAPS Catalog before customer-facing commit. "
         "Re-check Azure Accelerate envelope on aka.ms/AzureAccelerate. ATO numbers are HIGH-trust."),
    ]
    col_w = Inches(4.15)
    gap = Inches(0.15)
    x0 = Inches(0.5)
    y0 = Inches(1.7)
    h = Inches(3.0)
    for i, (head, body) in enumerate(rules):
        x = x0 + (col_w + gap) * i
        add_rect(s, x, y0, col_w, Inches(0.6), NAVY)
        add_text(s, x + Inches(0.2), y0 + Inches(0.12), col_w - Inches(0.4),
                 Inches(0.4), head, size=12, bold=True, color=CYAN,
                 anchor=MSO_ANCHOR.MIDDLE)
        add_rect(s, x, y0 + Inches(0.6), col_w, h - Inches(0.6), LIGHT)
        add_text(s, x + Inches(0.2), y0 + Inches(0.8), col_w - Inches(0.4),
                 h - Inches(0.95), body, size=12, color=DARK)

    # Pairing ribbon
    add_rect(s, Inches(0.5), Inches(5.1), SW - Inches(1.0), Inches(1.5), LIGHT)
    add_text(s, Inches(0.75), Inches(5.25), SW - Inches(1.5), Inches(0.4),
             "PAIRING & PROOF", size=11, bold=True, color=BLUE)
    add_bullets(s, Inches(0.75), Inches(5.55), SW - Inches(1.5), Inches(1.0),
                ["Customer-facing pack: AI-CoE-Customer-Pitch · AI-CoE-Sector-Briefing-* · this offer menu.",
                 "Internal pack: AI-CoE-VBD-Reference-Deck (full catalogue, 25 slides) · AI-CoE-Objection-Handling · AI-CoE-How-To-Use.",
                 "Economics: AI-CoE-AI-TCO-Calculator.xlsx · AI-CoE-Change-Readiness-Instrument.xlsx."],
                size=11)
    add_footer(s, "AI CoE · Three-Surface Offers · Closing", "6 / 6")
    add_notes(s, NOTES[5])


# --------------------------------------------------------------------------- #
# Assemble
# --------------------------------------------------------------------------- #

def main() -> int:
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    cover_slide(prs)
    overview_slide(prs)
    for i, o in enumerate(OFFERS):
        offer_slide(prs, o, page_num=3 + i, note=NOTES[2 + i])
    closing_slide(prs)
    prs.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(prs.slides)} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
