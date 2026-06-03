"""Build the AI CoE Sovereign AI for RSA deck.

Generates AI-CoE-Sovereign-AI-RSA.pptx from ai-coe-sovereign-ai-rsa-report.md.
Mirrors the visual canon of build_objection_deck.py / build_vbd_deck.py.

Author: Yuri Baijnath - CSU Cloud & AI Lead (South Africa)
"""

from __future__ import annotations

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt, Emu

# Theme - matches build_objection_deck.py
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

C_BG       = RGBColor(0xFF, 0xFF, 0xFF)
C_INK      = RGBColor(0x1A, 0x1A, 0x1A)
C_MUTED    = RGBColor(0x55, 0x55, 0x55)
C_RULE     = RGBColor(0xD0, 0xD0, 0xD0)
C_ACCENT   = RGBColor(0x00, 0x67, 0xB8)
C_ACCENT2  = RGBColor(0x50, 0xE6, 0xFF)
C_HIGHLIGHT= RGBColor(0x74, 0x2A, 0x9B)
C_GOOD     = RGBColor(0x10, 0x7C, 0x10)
C_WARN     = RGBColor(0xB7, 0x6E, 0x00)
C_BAND     = RGBColor(0xF3, 0xF6, 0xFA)
C_DARK     = RGBColor(0x0B, 0x1F, 0x3A)

TOTAL_SLIDES = 14


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
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, font="Segoe UI"):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.margin_left = Inches(0.0); tf.margin_right = Inches(0.0)
    tf.margin_top = Inches(0.0); tf.margin_bottom = Inches(0.0)
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, line in enumerate(text.split("\n")):
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
                bullet_color=C_ACCENT, line_spacing=1.2):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.0); tf.margin_top = Inches(0.0)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = line_spacing
        r1 = p.add_run(); r1.text = "\u2022  "
        r1.font.name = "Segoe UI"; r1.font.size = Pt(size); r1.font.bold = True
        r1.font.color.rgb = bullet_color
        r2 = p.add_run(); r2.text = item
        r2.font.name = "Segoe UI"; r2.font.size = Pt(size); r2.font.color.rgb = color
    return tb


def add_section_tag(slide, text, color=C_ACCENT):
    add_text(slide, Inches(0.6), Inches(0.35), Inches(10), Inches(0.3),
             text.upper(), size=11, bold=True, color=color)


def add_title(slide, title, subtitle=None):
    add_text(slide, Inches(0.6), Inches(0.65), Inches(12.2), Inches(0.8),
             title, size=28, bold=True, color=C_INK)
    if subtitle:
        add_text(slide, Inches(0.6), Inches(1.4), Inches(12.2), Inches(0.55),
                 subtitle, size=14, color=C_MUTED)


def add_footer(slide, slide_no):
    add_rect(slide, Inches(0.6), Inches(0.28), Inches(12.13), Emu(9000), C_RULE)
    add_rect(slide, Inches(0.6), Inches(7.05), Inches(12.13), Emu(9000), C_RULE)
    add_text(slide, Inches(0.6), Inches(7.12), Inches(8), Inches(0.3),
             "Microsoft \u00b7 Confidential \u00b7 \u00a9 2026 Microsoft Corporation",
             size=9, color=C_MUTED)
    add_text(slide, Inches(10.7), Inches(7.12), Inches(2.0), Inches(0.3),
             f"{slide_no} / {TOTAL_SLIDES}",
             size=9, color=C_MUTED, align=PP_ALIGN.RIGHT)


def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def add_table(slide, x, y, w, h, headers, rows, *,
              header_fill=C_DARK, header_color=C_BG,
              header_size=11, body_size=10, col_widths=None,
              first_col_bold=True, alt_band=True):
    n_cols = len(headers); n_rows = len(rows) + 1
    tbl_shape = slide.shapes.add_table(n_rows, n_cols, x, y, w, h)
    tbl = tbl_shape.table
    if col_widths:
        total = sum(col_widths)
        for i, cw in enumerate(col_widths):
            tbl.columns[i].width = int(w * cw / total)
    for j, htext in enumerate(headers):
        cell = tbl.cell(0, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = header_fill
        cell.margin_left = Inches(0.08); cell.margin_right = Inches(0.08)
        cell.margin_top = Inches(0.04); cell.margin_bottom = Inches(0.04)
        tf = cell.text_frame; tf.word_wrap = True; tf.clear()
        p = tf.paragraphs[0]; r = p.add_run()
        r.text = htext; r.font.name = "Segoe UI"; r.font.size = Pt(header_size)
        r.font.bold = True; r.font.color.rgb = header_color
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_BAND if (alt_band and i % 2 == 0) else C_BG
            cell.margin_left = Inches(0.08); cell.margin_right = Inches(0.08)
            cell.margin_top = Inches(0.03); cell.margin_bottom = Inches(0.03)
            tf = cell.text_frame; tf.word_wrap = True; tf.clear()
            p = tf.paragraphs[0]; r = p.add_run()
            r.text = str(val); r.font.name = "Segoe UI"; r.font.size = Pt(body_size)
            r.font.color.rgb = C_INK; r.font.bold = first_col_bold and (j == 0)
    return tbl


# ---------- Slide builders ----------

def build_title(prs):
    s = new_slide(prs)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, C_DARK)
    add_rect(s, 0, Inches(5.1), SLIDE_W, Inches(0.06), C_ACCENT2)
    add_text(s, Inches(0.6), Inches(0.6), Inches(8), Inches(0.4),
             "AI CENTER OF EXCELLENCE", size=12, bold=True, color=C_ACCENT2)
    add_text(s, Inches(0.6), Inches(2.6), Inches(12.2), Inches(1.4),
             "Sovereign AI for South Africa",
             size=44, bold=True, color=C_BG)
    add_text(s, Inches(0.6), Inches(3.8), Inches(12.2), Inches(0.6),
             "A named offer for POPIA-, PFMA-, and sector-regulated AI workloads",
             size=18, color=C_ACCENT2)
    add_text(s, Inches(0.6), Inches(5.4), Inches(12.2), Inches(0.4),
             "RSA CSU \u00b7 v1.0 \u00b7 June 2026",
             size=12, color=C_BG, italic=True)
    add_text(s, Inches(0.6), Inches(6.6), Inches(6), Inches(0.4),
             "Yuri Baijnath", size=18, bold=True, color=C_BG)
    add_text(s, Inches(0.6), Inches(6.95), Inches(10), Inches(0.4),
             "CSU Cloud & AI Lead (South Africa)  \u00b7  Yuri.Baijnath@microsoft.com  \u00b7  Microsoft",
             size=11, color=C_ACCENT2)


def build_why(prs):
    s = new_slide(prs)
    add_section_tag(s, "Why this offer exists")
    add_title(s, "Sovereignty is now a deal qualifier in RSA",
              "What used to be a checkbox is now the architecture review.")
    add_bullets(s, Inches(0.6), Inches(2.2), Inches(12.2), Inches(4.5), [
        "SOEs, banks, insurers, and large public-sector buyers no longer accept \"the data stays in Azure\" as an answer.",
        "Buyers want a named offer, named controls, a named operating model, and named regions.",
        "Capgemini (Sovereign Cloud for AI), Atos/Eviden, Thales, Orange Business have productised this. Microsoft RSA fielding only caveats loses the deal at the CISO / DPO review.",
        "This offer packages our existing capability into a single SKU a CSA can take to a CISO + DPO + Internal Audit triad and walk out with a signed pilot gate.",
        "Backed by SA North + SA West regions, Purview AI Hub, Defender for Cloud AI, Foundry data-zone scoping, and a control crosswalk to every framework an RSA buyer will ask about.",
    ], size=14)
    add_footer(s, 2)


def build_what_we_sell(prs):
    s = new_slide(prs)
    add_section_tag(s, "What we sell")
    add_title(s, "Five components in one SKU")
    cards = [
        ("1. Residency commitment", "Workload + data confined to SA North / SA West. Foundry data-zone scoping. Azure Policy + Purview lineage as evidence."),
        ("2. Governance posture", "Purview AI Hub, Defender for Cloud AI, Sentinel connector, Azure Policy initiative \u2014 all wired day 1, not day 90."),
        ("3. Control crosswalk", "Single matrix: our controls \u2192 POPIA, PFMA, NERSA, SARB Dir 7, FSCA, AGSA, ISO 42001, NIST AI RMF, EU AI Act."),
        ("4. Operating model", "Two-page RACI: CISO + DPO + Internal Audit + Microsoft + partner. Run-time, incident, audit, quarterly attestation."),
        ("5. Artefact pack", "Board summary, regulator brief, audit evidence template, kill-switch run-book \u2014 all customer-deliverable."),
    ]
    y = Inches(2.2); h = Inches(0.85); gap = Inches(0.12)
    for title, body in cards:
        add_rect(s, Inches(0.6), y, Inches(12.2), h, C_BAND)
        add_rect(s, Inches(0.6), y, Inches(0.1), h, C_ACCENT)
        add_text(s, Inches(0.85), y + Inches(0.1), Inches(3.4), Inches(0.45),
                 title, size=14, bold=True, color=C_ACCENT)
        add_text(s, Inches(4.4), y + Inches(0.1), Inches(8.2), Inches(0.7),
                 body, size=12, color=C_INK)
        y += h + gap
    add_footer(s, 3)


def build_three_dimensions(prs):
    s = new_slide(prs)
    add_section_tag(s, "Three sovereignty dimensions", color=C_HIGHLIGHT)
    add_title(s, "Customers conflate three different sovereignties",
              "Separating them is half the conversation.")
    cols = [
        ("Data sovereignty", C_ACCENT,
         "Data \u2014 at rest, in flight, in vector indexes, in logs \u2014 stays in SA North / SA West.",
         ["Foundry data-zone scoping", "Vector + eval datasets in-region",
          "Cross-border per POPIA \u00a772 list only", "Prompt + completion logs in-region"]),
        ("Operational sovereignty", C_HIGHLIGHT,
         "SA-based operations, customer-controlled keys, customer-controlled break-glass.",
         ["CMK via Key Vault HSM", "In-region business-hours support",
          "Customer-owned break-glass run-book", "Global support routed only on consent"]),
        ("Decision sovereignty", C_DARK,
         "Customer retains decision authority on what the AI does.",
         ["Customer owns system prompts", "Customer-approved model catalogue",
          "Reasoning trace exposed to IA", "Kill-switch under customer control"]),
    ]
    col_w = Inches(4.0); col_gap = Inches(0.1); x0 = Inches(0.6); y0 = Inches(2.3)
    for i, (head, color, sub, bullets) in enumerate(cols):
        x = x0 + (col_w + col_gap) * i
        add_rect(s, x, y0, col_w, Inches(0.7), color)
        add_text(s, x + Inches(0.15), y0 + Inches(0.18), col_w, Inches(0.5),
                 head, size=15, bold=True, color=C_BG)
        add_rect(s, x, y0 + Inches(0.7), col_w, Inches(3.8), C_BAND)
        add_text(s, x + Inches(0.15), y0 + Inches(0.85), col_w - Inches(0.3),
                 Inches(0.9), sub, size=11, italic=True, color=C_MUTED)
        add_bullets(s, x + Inches(0.15), y0 + Inches(1.8),
                    col_w - Inches(0.3), Inches(2.8), bullets,
                    size=11, bullet_color=color)
    add_footer(s, 4)


def build_region_posture(prs):
    s = new_slide(prs)
    add_section_tag(s, "Region posture")
    add_title(s, "What is in-region today",
              "Verify quarterly against aka.ms/AzureRegions and Foundry data-zone docs.")
    rows = [
        ["Azure AI Foundry", "Available", "Partial", "Service GA progression \u2014 verify quarterly"],
        ["Azure OpenAI models", "Available", "Partial", "Model rollout differs by region"],
        ["M365 Copilot processing", "EU / US", "EU / US", "Tenant-region determined; not in-SA today"],
        ["Purview AI Hub", "Available", "Available", "Tenant-region service"],
        ["Defender for Cloud AI", "Available", "Available", ""],
        ["Document Intelligence", "Available", "Available", ""],
        ["Communication Services", "Available", "Partial", "WhatsApp / SMS channels"],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(4.2),
              ["Capability", "SA North", "SA West", "Notes"], rows,
              col_widths=[3.0, 1.5, 1.5, 6.0], body_size=11)
    add_text(s, Inches(0.6), Inches(6.6), Inches(12.2), Inches(0.35),
             "Source: aka.ms/AzureRegions \u00b7 Foundry data-zone documentation. "
             "Re-verify quarterly before any customer commit.",
             size=10, italic=True, color=C_MUTED)
    add_footer(s, 5)


def build_m365_honest(prs):
    s = new_slide(prs)
    add_section_tag(s, "M365 Copilot \u2014 honest answer", color=C_WARN)
    add_title(s, "Don't over-promise where the service does not deliver",
              "Walking into this conversation badly is a deal-killer.")
    add_text(s, Inches(0.6), Inches(2.2), Inches(12.2), Inches(0.5),
             "The truth", size=13, bold=True, color=C_WARN)
    add_bullets(s, Inches(0.6), Inches(2.6), Inches(12.2), Inches(1.8), [
        "M365 Copilot tenant-region determines processing region. SA-tenanted customers typically process in EU today.",
        "Prompts + responses are not stored long-term; transit encrypted; tenant data not used to train models.",
        "EU Data Boundary commitments apply where workload routes via EU.",
    ], size=12)
    add_text(s, Inches(0.6), Inches(4.4), Inches(12.2), Inches(0.5),
             "What this offer recommends", size=13, bold=True, color=C_GOOD)
    add_bullets(s, Inches(0.6), Inches(4.8), Inches(12.2), Inches(1.8), [
        "For deepest sovereignty, route sensitive AI workloads via Azure AI Foundry in SA regions \u2014 use Copilot Studio agents to surface them in M365 surfaces.",
        "Position M365 Copilot for productivity scenarios where the regulatory posture is acceptable.",
        "Document the gap explicitly in the offer; never paper over it in the pitch.",
    ], size=12, bullet_color=C_GOOD)
    add_footer(s, 6)


def build_crosswalk(prs):
    s = new_slide(prs)
    add_section_tag(s, "Control crosswalk")
    add_title(s, "One control \u2192 every framework an RSA buyer asks about",
              "Excerpt from the master matrix. Full version in AI-CoE-AI-Impact-Assessment.xlsx.")
    rows = [
        ["Data residency to SA regions", "\u00a772", "n/a", "n/a", "A.6.2", "GOVERN-1.3", "Art. 10"],
        ["CMK encryption at rest", "\u00a719", "s.45", "n/a", "A.8.24", "PROTECT", "Art. 15"],
        ["Purview AI Hub audit trail", "\u00a717, \u00a722", "s.38", "RAI-G3", "A.5.10", "MEASURE-2.5", "Art. 12"],
        ["Defender for Cloud AI posture", "\u00a719", "n/a", "RAI-S2", "A.8.16", "MANAGE-3", "Art. 9"],
        ["Content Safety + Prompt Shields", "n/a", "n/a", "RAI-S1", "A.5.34", "MANAGE-2.3", "Art. 15"],
        ["System-prompt versioning", "\u00a722", "n/a", "RAI-T2", "A.5.37", "GOVERN-1.5", "Art. 11"],
        ["HITL gate on regulated outputs", "\u00a711", "n/a", "RAI-A1", "A.6.4", "MANAGE-2.4", "Art. 14"],
        ["Kill-switch run-book + test", "n/a", "s.45", "RAI-S3", "A.5.30", "MANAGE-3", "Art. 9"],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(4.4),
              ["Microsoft control", "POPIA", "PFMA", "RAI v2", "ISO 42001", "NIST AI RMF", "EU AI Act"],
              rows,
              col_widths=[3.5, 1.2, 1.0, 1.2, 1.4, 1.8, 1.5],
              body_size=10, header_size=10)
    add_footer(s, 7)


def build_operating_model(prs):
    s = new_slide(prs)
    add_section_tag(s, "Operating model")
    add_title(s, "Who owns what",
              "RACI customised per customer; this is the spine.")
    rows = [
        ["Architecture authority", "A / R", "C", "I", "I", "C"],
        ["Region availability change", "R", "I", "I", "I", "I"],
        ["Policy ownership + attestation", "C", "A / R", "C", "C", "I"],
        ["POPIA DPIA + cross-border approval", "I", "C", "A / R", "I", "I"],
        ["Quarterly evidence + AGSA liaison", "C", "C", "C", "A / R", "I"],
        ["Day-to-day operations + L1/L2 incident", "C", "I", "I", "I", "A / R"],
        ["Kill-switch authority", "I", "A / R", "I", "I", "C"],
        ["L3 incident escalation", "A / R", "I", "I", "I", "C"],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(4.4),
              ["Activity", "Microsoft", "Customer CISO", "Customer DPO", "Internal Audit", "Partner"],
              rows,
              col_widths=[4.0, 1.6, 1.7, 1.6, 1.7, 1.6],
              body_size=10, header_size=10)
    add_footer(s, 8)


def build_engagement_shape(prs):
    s = new_slide(prs)
    add_section_tag(s, "Engagement shape")
    add_title(s, "From envision to attestation",
              "Phased commercial \u2014 every phase has a funding instrument.")
    rows = [
        ["Sovereign-AI Envision Workshop", "4 wk", "Pre-sales ECIF $50K",
         "Crosswalk tailored, gap analysis, regulator-correspondence pack"],
        ["Landing-Zone deploy (ACC-2)", "2 wk", "Cloud Accelerate Factory $0",
         "Production landing-zone in SA North"],
        ["Pilot (use-case dependent)", "8\u201312 wk", "ATO $250\u2013500K + partner",
         "First production workload + audit evidence pack"],
        ["Quarterly attestation", "Ongoing", "Customer",
         "Re-verify controls, region availability, model catalogue"],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(3.5),
              ["Phase", "Duration", "Funded by", "Deliverables"], rows,
              col_widths=[3.5, 1.4, 3.3, 5.0], body_size=11)
    add_footer(s, 9)


def build_what_this_is_not(prs):
    s = new_slide(prs)
    add_section_tag(s, "What this is NOT", color=C_WARN)
    add_title(s, "Boundaries of the offer",
              "Setting these in the first meeting prevents the deal slipping later.")
    items = [
        ("Not an air-gapped offer",
         "We do not operate Azure Stack Edge / disconnected scenarios under this SKU."),
        ("Not a workaround for not-yet-in-region services",
         "Where a service is not in SA, this offer documents the gap and customer risk acceptance \u2014 it does not pretend coverage."),
        ("Not a substitute for the customer's POPIA programme",
         "We provide the controls; the customer remains the responsible party under POPIA \u00a78."),
    ]
    y = Inches(2.3); h = Inches(1.2); gap = Inches(0.2)
    for head, body in items:
        add_rect(s, Inches(0.6), y, Inches(12.2), h, C_BAND)
        add_rect(s, Inches(0.6), y, Inches(0.1), h, C_WARN)
        add_text(s, Inches(0.85), y + Inches(0.18), Inches(11.5), Inches(0.45),
                 head, size=15, bold=True, color=C_WARN)
        add_text(s, Inches(0.85), y + Inches(0.6), Inches(11.5), Inches(0.55),
                 body, size=12, color=C_INK)
        y += h + gap
    add_footer(s, 10)


def build_counter_objections(prs):
    s = new_slide(prs)
    add_section_tag(s, "Counter-objections")
    add_title(s, "What you will be asked, and what to say")
    rows = [
        ["\"M365 Copilot processes in EU \u2014 you're not sovereign.\"",
         "Correct for M365 Copilot today. For deep-sovereignty workloads, route via Foundry in SA. This offer makes that explicit."],
        ["\"You can't promise in-region forever.\"",
         "Correct. We commit to quarterly attestation and 12-month notice on region changes via the operating model."],
        ["\"AGSA will reject this.\"",
         "AGSA reviews evidence, not vendor promises. The evidence template in this pack is what an AGSA reviewer wants to see."],
        ["\"What about EU AI Act for our multinational parent?\"",
         "Crosswalk includes EU AI Act categories; co-deployable with EU Data Boundary if needed."],
        ["\"How do we exit?\"",
         "Customer-owned keys + customer tenant + Foundry multi-model = portability. Exit returns customer-owned assets."],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(4.4),
              ["Objection", "Response"], rows,
              col_widths=[5.0, 7.2], body_size=11, first_col_bold=True)
    add_footer(s, 11)


def build_linked_artefacts(prs):
    s = new_slide(prs)
    add_section_tag(s, "Linked artefacts")
    add_title(s, "Where the rest of the answer lives")
    rows = [
        ["ai-coe-sovereign-ai-rsa-report.md", "Long-form source of truth for this deck"],
        ["AI-CoE-AI-Impact-Assessment.xlsx", "Per-use-case impact assessment with full control crosswalk"],
        ["AI-CoE-AI-Governance-Playbook.docx", "Operating model, gates, control library"],
        ["accelerators/acc-2-popia-landing-zone.md", "Bicep landing-zone blueprint"],
        ["accelerators/acc-4-regulated-pilot-kit.md", "4-week workshop kit + risk register"],
        ["AI-CoE-Eskom-Executive-Briefing.pptx", "Reference customer narrative"],
        ["AI-CoE-Objection-Handling.pptx", "Pillar 5 objections \u2014 governance & security"],
    ]
    add_table(s, Inches(0.6), Inches(2.3), Inches(12.2), Inches(4.2),
              ["Artefact", "Use it for"], rows,
              col_widths=[5.5, 6.7], body_size=11)
    add_footer(s, 12)


def build_sources(prs):
    s = new_slide(prs)
    add_section_tag(s, "Sources & verification")
    add_title(s, "Where these claims come from")
    add_bullets(s, Inches(0.6), Inches(2.2), Inches(12.2), Inches(4.5), [
        "aka.ms/AzureRegions \u2014 region availability (verify quarterly)",
        "Microsoft Trust Center \u2014 Data Residency and Sovereignty",
        "Azure AI Foundry Data Zone documentation",
        "Microsoft Responsible AI Standard v2 (RAI v2)",
        "POPI Act, PFMA, NERSA Act, SARB Directive 7 \u2014 publicly available statute",
        "ISO/IEC 42001:2023, NIST AI RMF 1.0, EU AI Act (Regulation 2024/1689)",
        "HIGH trust \u2014 ai-coe-sovereign-ai-rsa-report.md (Yuri Baijnath, author)",
    ], size=13)
    add_footer(s, 13)


def build_close(prs):
    s = new_slide(prs)
    add_rect(s, 0, 0, SLIDE_W, SLIDE_H, C_DARK)
    add_rect(s, 0, Inches(5.1), SLIDE_W, Inches(0.06), C_ACCENT2)
    add_text(s, Inches(0.6), Inches(0.6), Inches(10), Inches(0.4),
             "AI CENTER OF EXCELLENCE \u00b7 SOVEREIGN AI", size=12, bold=True, color=C_ACCENT2)
    add_text(s, Inches(0.6), Inches(2.8), Inches(12.2), Inches(1.2),
             "Sell it as one offer.", size=42, bold=True, color=C_BG)
    add_text(s, Inches(0.6), Inches(4.0), Inches(12.2), Inches(0.6),
             "Five components. One signed gate. Every framework an RSA buyer asks about.",
             size=18, color=C_ACCENT2)
    add_text(s, Inches(0.6), Inches(6.6), Inches(6), Inches(0.4),
             "Yuri Baijnath", size=18, bold=True, color=C_BG)
    add_text(s, Inches(0.6), Inches(6.95), Inches(10), Inches(0.4),
             "CSU Cloud & AI Lead (South Africa)  \u00b7  Yuri.Baijnath@microsoft.com  \u00b7  Microsoft",
             size=11, color=C_ACCENT2)


def main():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    build_title(prs)
    build_why(prs)
    build_what_we_sell(prs)
    build_three_dimensions(prs)
    build_region_posture(prs)
    build_m365_honest(prs)
    build_crosswalk(prs)
    build_operating_model(prs)
    build_engagement_shape(prs)
    build_what_this_is_not(prs)
    build_counter_objections(prs)
    build_linked_artefacts(prs)
    build_sources(prs)
    build_close(prs)

    out = "AI-CoE-Sovereign-AI-RSA.pptx"
    prs.save(out)
    print(f"Wrote {out} with {len(prs.slides)} slides.")


if __name__ == "__main__":
    main()
