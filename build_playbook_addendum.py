"""Generate AI-CoE-Operating-Playbook-Addendum.docx.

Addendum to AI-CoE-Operating-Playbook.docx covering outcome-based / risk-share
commercial archetypes. Standalone because the parent playbook is MIP-protected.
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).parent / "AI-CoE-Operating-Playbook-Addendum.docx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)


def set_cell_shading(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def add_heading(doc, text: str, level: int) -> None:
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.name = "Segoe UI"
        if level == 0:
            run.font.color.rgb = NAVY
            run.font.size = Pt(26)
        elif level == 1:
            run.font.color.rgb = BLUE
            run.font.size = Pt(16)
        else:
            run.font.color.rgb = NAVY
            run.font.size = Pt(12)


def add_paragraph(doc, text: str, italic: bool = False, bold: bool = False) -> None:
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(11)
    run.italic = italic
    run.bold = bold


def add_bullet(doc, text: str) -> None:
    p = doc.add_paragraph(style="List Bullet")
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(11)


def add_table(doc, headers, rows) -> None:
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        set_cell_shading(hdr[i], "0067B8")
        for p in hdr[i].paragraphs:
            for run in p.runs:
                run.font.name = "Segoe UI"
                run.font.size = Pt(10)
                run.bold = True
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for r, row in enumerate(rows, start=1):
        for c, val in enumerate(row):
            cell = table.rows[r].cells[c]
            cell.text = str(val)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.name = "Segoe UI"
                    run.font.size = Pt(10)


def main() -> None:
    doc = Document()
    for section in doc.sections:
        section.left_margin = Cm(2); section.right_margin = Cm(2)
        section.top_margin = Cm(2); section.bottom_margin = Cm(2)

    add_heading(doc, "AI CoE Operating Playbook — Addendum: Outcome-Based & Risk-Share Commercial Archetypes", level=0)
    add_paragraph(doc, "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft", italic=True)
    add_paragraph(doc, "Version 1.0 · 2026-06-03 · Companion to AI-CoE-Operating-Playbook.docx", italic=True)

    add_heading(doc, "1. Why this addendum exists", level=1)
    add_paragraph(
        doc,
        "Microsoft's AI CoE pack today defaults to T&M + ECIF subsidy. Accenture and IBM Consulting routinely pitch "
        "outcome-based commercials (per-resolved-ticket, per-document-processed); Genpact and Cognizant publish gain-share "
        "AI deals. CFOs increasingly anchor RFP responses on risk-share. Microsoft fielding only T&M loses the conversation "
        "at the CFO desk. This addendum codifies four risk-share archetypes RSA CoE can land alongside the ATO + partner stack.",
    )

    add_heading(doc, "2. When to propose a risk-share archetype", level=1)
    add_bullet(doc, "The customer has a measurable baseline (cycle time, cost-to-serve, FTE-hours per unit). Without a baseline, do not propose a risk-share — you will lose the measurement argument inside 90 days.")
    add_bullet(doc, "The customer's CFO is the decision-maker, not the CIO. Risk-share is a CFO-pleasing artefact.")
    add_bullet(doc, "There is a credible partner who can carry the operational delivery risk. Microsoft does not carry per-unit delivery risk directly.")
    add_bullet(doc, "Volumes are predictable enough to underwrite a unit price. Below ~10k units/month per archetype the unit economics are unstable.")
    add_bullet(doc, "Do NOT propose risk-share for first-pilots, exploratory use-cases, or non-repeatable workflows.")

    add_heading(doc, "3. Four named archetypes", level=1)

    # 3.1
    add_heading(doc, "3.1 Per-resolved-case (service desk, claims, complaints)", level=2)
    add_paragraph(doc, "Customer pays a unit price per case auto-resolved or HITL-resolved to a measurable SLA.", bold=True)
    add_table(doc, ["Element", "Detail"], [
        ["Baseline definition", "12-month rolling average cases/month and current cost-per-case (FTE + tooling)"],
        ["Measurement", "Case closed within SLA + customer-satisfaction floor; both metered in Dataverse/ServiceNow"],
        ["Partner role", "Prime delivery + per-unit price; partner carries the OPEX risk"],
        ["MAICPP / ECIF treatment", "Microsoft funds the pilot to baseline-establishment via ECIF; partner takes over at unit-economics gate"],
        ["Exit terms", "Either party may exit on 90-day notice; baseline floor must hold for unit-price guarantee to remain"],
        ["Typical price floor", "30-45% of incumbent cost-per-case"],
    ])

    # 3.2
    add_heading(doc, "3.2 Per-document-processed (KYC, permits, contracts, claims)", level=2)
    add_paragraph(doc, "Customer pays a unit price per document processed end-to-end (extract + reason + decide + audit trail).", bold=True)
    add_table(doc, ["Element", "Detail"], [
        ["Baseline definition", "12-month rolling document volume + cost-per-document including reviewer FTE"],
        ["Measurement", "Document closed (auto-decided + HITL-decided) with reasoning trace + auditor-sample pass-rate"],
        ["Partner role", "Prime delivery; partner owns the HITL UI and reviewer operations"],
        ["MAICPP / ECIF treatment", "Microsoft funds Document Intelligence + Foundry envisioning + landing-zone via ACO; partner takes per-unit risk from production go-live"],
        ["Exit terms", "12-month minimum commit; auditor-sample failure rate > 5% triggers re-baseline"],
        ["Typical price floor", "25-40% of incumbent cost-per-document"],
    ])
    add_paragraph(doc, "Anchor accelerator: ACC-5 (Document Intelligence + Foundry pattern).", italic=True)

    # 3.3
    add_heading(doc, "3.3 Per-hour-recovered (knowledge worker time studies)", level=2)
    add_paragraph(doc, "Customer pays a fee tied to time-and-motion measured FTE-hour recovery from Copilot adoption.", bold=True)
    add_table(doc, ["Element", "Detail"], [
        ["Baseline definition", "Time-and-motion study before deployment; 3 personas minimum, 30-day window"],
        ["Measurement", "Repeated time-and-motion at month 6 and month 12; self-report cross-validated with telemetry"],
        ["Partner role", "Change-management partner runs the study; payment tied to verified recovery"],
        ["MAICPP / ECIF treatment", "Copilot Adoption Acceleration ECIF funds the baseline; partner-funded thereafter under MAICPP"],
        ["Exit terms", "Walk-away if month-6 recovery < 1 hr/user/week"],
        ["Typical fee shape", "Loaded-cost equivalent of 0.5 recovered hours/user/month, capped"],
    ])
    add_paragraph(doc, "Anchor accelerator: ACC-3 (M365 Copilot SOE Adoption Playbook).", italic=True)

    # 3.4
    add_heading(doc, "3.4 Gain-share (% of measured uplift over baseline)", level=2)
    add_paragraph(doc, "Customer pays Microsoft + partner a percentage of the measured P&L uplift over a 12-24 month period.", bold=True)
    add_table(doc, ["Element", "Detail"], [
        ["Baseline definition", "Audited financial baseline at workload level; sign-off by customer CFO + Internal Audit before pilot"],
        ["Measurement", "Annual audited financial uplift; methodology pre-agreed; tracked monthly"],
        ["Partner role", "Co-prime with Microsoft; both share the upside and the underwriting risk"],
        ["MAICPP / ECIF treatment", "ECIF funds the baseline establishment + pilot; gain-share kicks in at production go-live"],
        ["Exit terms", "24-month minimum measurement window; either party can exit at month 12 with pro-rata true-up"],
        ["Typical share", "15-25% of audited uplift to Microsoft + partner combined; partner split case-by-case"],
    ])
    add_paragraph(doc, "Use sparingly. Gain-share requires CFO + Internal Audit + Legal alignment up-front; in RSA expect 8-12 weeks of negotiation.", italic=True)

    add_heading(doc, "4. RACI for risk-share deals", level=1)
    add_table(doc, ["Role", "Baseline establishment", "Unit-price underwriting", "Measurement", "Disputes"], [
        ["Microsoft CSA", "R", "C", "C", "C"],
        ["Microsoft commercial lead", "A", "A", "I", "A"],
        ["Partner prime", "R", "R", "R", "R"],
        ["Customer CFO", "A", "A", "A", "A"],
        ["Customer Internal Audit", "C", "I", "C", "C"],
        ["Customer business sponsor", "C", "I", "C", "C"],
    ])

    add_heading(doc, "5. Cross-references", level=1)
    add_bullet(doc, "Objection 1.1 (ROI unproven) — AI-CoE-Objection-Handling.pptx Pillar 1; this addendum is the long-form rebuttal artefact.")
    add_bullet(doc, "ACC-1 Banking CX Agent — per-resolved-case archetype applies to tier-1 contact-centre.")
    add_bullet(doc, "ACC-3 SOE Copilot Adoption — per-hour-recovered archetype.")
    add_bullet(doc, "ACC-5 DocIntel + Foundry pattern — per-document-processed archetype.")
    add_bullet(doc, "AI-CoE-AI-TCO-Calculator.xlsx — unit economics underwriting input.")

    add_heading(doc, "6. What this addendum is NOT", level=1)
    add_bullet(doc, "Not a substitute for the standard ATO + ECIF + MAICPP commercial path. Use risk-share where it fits; default to ATO where it doesn't.")
    add_bullet(doc, "Not pre-approved pricing. Every risk-share deal requires Microsoft commercial-lead and legal approval; the unit prices above are typical floors, not guarantees.")
    add_bullet(doc, "Not a partner exit strategy. Microsoft remains the AI platform commitment; risk-share lives on top of the consumption commitment.")

    doc.save(str(OUT))
    print(f"Wrote {OUT.name}")


if __name__ == "__main__":
    main()
