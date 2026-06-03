"""Generate AI-CoE-AI-Governance-Playbook.docx.

The operating playbook for RAI/governance in RSA CoE engagements.
Companion to ai-coe-responsible-ai-governance.md and the Impact Assessment workbook.
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).parent / "AI-CoE-AI-Governance-Playbook.docx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
GREY = RGBColor(0x59, 0x59, 0x59)


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
            run.font.size = Pt(28)
        elif level == 1:
            run.font.color.rgb = BLUE
            run.font.size = Pt(18)
        else:
            run.font.color.rgb = NAVY
            run.font.size = Pt(13)


def add_paragraph(doc, text: str, bold: bool = False, italic: bool = False) -> None:
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(11)
    run.bold = bold
    run.italic = italic


def add_bullet(doc, text: str) -> None:
    p = doc.add_paragraph(style="List Bullet")
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(11)


def add_table(doc, headers: list[str], rows: list[list[str]]) -> None:
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
                run.font.bold = True
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

    # Page margins
    for section in doc.sections:
        section.left_margin = Cm(2)
        section.right_margin = Cm(2)
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)

    # Title
    add_heading(doc, "AI CoE — Responsible AI & Governance Playbook (RSA)", level=0)
    add_paragraph(doc, "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft", italic=True)
    add_paragraph(doc, "Version 1.0 · Last updated 2026-06-03", italic=True)
    add_paragraph(
        doc,
        "Companion artefacts: ai-coe-responsible-ai-governance.md, AI-CoE-AI-Impact-Assessment.xlsx",
        italic=True,
    )

    # 1. Purpose
    add_heading(doc, "1. Purpose", level=1)
    add_paragraph(
        doc,
        "This playbook is the operating manual for the AI CoE governance posture in RSA customer engagements. "
        "It names the gates, the roles, the cadences, and the evidence each customer must produce. It is the "
        "artefact AGSA, SARB, FSCA, or the Information Regulator should be able to sample at any point.",
    )

    # 2. The four-gate model
    add_heading(doc, "2. The four-gate model", level=1)
    add_paragraph(
        doc,
        "Every AI use-case in the CoE passes four governance gates before reaching production, and a recurring "
        "fifth attestation thereafter. No gate is skipped; gate evidence is captured in the Impact Assessment workbook.",
    )
    add_table(
        doc,
        ["Gate", "Stage", "Required evidence", "Sign-off"],
        [
            ["1. Envision", "MCEM 1–2", "Use-case registered; sponsor named; value hypothesis; sector mapped", "Sponsor + Microsoft CSA"],
            ["2. Pre-pilot", "MCEM 2–3", "Impact assessment signed; controls selected; risk register reviewed; partner DPA addendum", "CISO + DPO + Legal"],
            ["3. Pre-production", "MCEM 3", "Eval harness live; HITL queue live; kill-switch tested; Purview AI Hub onboarded; Defender for Cloud AI clean", "CISO"],
            ["4. Quarterly attestation", "MCEM 4–5", "Re-verify controls; refresh evidence; surface drift; record in attestation sheet", "CISO + DPO + Internal Audit"],
        ],
    )

    # 3. Operating model
    add_heading(doc, "3. Operating model — RACI by gate", level=1)
    add_paragraph(doc, "R = Responsible · A = Accountable · C = Consulted · I = Informed", italic=True)
    add_table(
        doc,
        ["Role", "Gate 1", "Gate 2", "Gate 3", "Gate 4"],
        [
            ["Business sponsor", "A", "C", "C", "I"],
            ["Microsoft CSA", "R", "R", "R", "R"],
            ["Partner CSA / build lead", "I", "R", "R", "R"],
            ["Customer CISO", "I", "A", "A", "A"],
            ["Customer DPO", "I", "A", "I", "A"],
            ["Customer Internal Audit", "I", "C", "C", "A"],
            ["Customer Legal", "I", "A", "I", "C"],
        ],
    )

    # 4. Cadences
    add_heading(doc, "4. Cadences", level=1)
    add_bullet(doc, "Weekly during pilot — Microsoft CSA + partner lead review eval results, override patterns, and incident log.")
    add_bullet(doc, "Monthly — risk register review with customer CISO; reviewer-feedback ingestion into eval set; cost/FinOps review.")
    add_bullet(doc, "Quarterly — full attestation refresh; AGSA-ready evidence pack export; region-availability re-verification on aka.ms/AzureRegions.")
    add_bullet(doc, "Annually — control crosswalk refresh; ISO 42001 / NIST AI RMF / EU AI Act version check.")

    # 5. Control library
    add_heading(doc, "5. Control library (operational reference)", level=1)
    add_paragraph(
        doc,
        "Full library lives in AI-CoE-AI-Impact-Assessment.xlsx, sheet 2 (Crosswalk) and sheet 5 (Control selection). "
        "Excerpt below names the 18 control families the playbook defaults ON; downgrade requires written justification "
        "captured in the workbook.",
    )
    add_table(
        doc,
        ["ID", "Control family", "Default", "Implementation surface"],
        [
            ["C-01", "Accountability & governance", "ON", "Azure Policy initiative + CoE charter"],
            ["C-02", "Data governance & residency", "ON", "Azure Policy data-residency + Purview lineage"],
            ["C-03", "Impact assessment", "ON", "Impact Assessment workbook"],
            ["C-04", "Risk identification", "ON", "Risk register (workbook sheet 4)"],
            ["C-05", "System-prompt versioning", "ON", "Foundry prompt-flow + GitHub"],
            ["C-06", "Content Safety / Prompt Shields", "ON", "Azure AI Content Safety + Prompt Shields"],
            ["C-07", "HITL gate on regulated outputs", "ON", "Power Pages HITL queue + Dataverse routing"],
            ["C-08", "Kill-switch + tested run-book", "ON", "Azure Policy disable + Foundry deployment flag"],
            ["C-09", "Audit trail (Purview AI Hub)", "ON", "Microsoft Purview AI Hub"],
            ["C-10", "Defender for Cloud AI posture", "ON", "Defender for Cloud AI"],
            ["C-11", "Reviewer override feedback loop", "ON", "PromptFlow eval pipeline"],
            ["C-12", "Encryption at rest (CMK)", "ON", "Azure Key Vault HSM"],
            ["C-13", "Network isolation", "ON", "Private endpoints + VNet integration"],
            ["C-14", "Quarterly attestation", "ON", "Attestation sheet (workbook sheet 8)"],
            ["C-15", "Third-party / partner controls", "ON", "Partner DPA addendum + MAICPP terms"],
            ["C-16", "Incident response & notification", "ON", "Sentinel + Defender + customer IR run-book"],
            ["C-17", "Demographic fairness assessment", "ON", "Fairness toolkit + PromptFlow eval slices"],
            ["C-18", "Explainability / reasoning trace", "ON", "Foundry reasoning trace + Purview log"],
        ],
    )

    # 6. Incident response
    add_heading(doc, "6. Incident response", level=1)
    add_paragraph(doc, "Three named incident classes:", bold=True)
    add_bullet(doc, "Class 1 — model behaviour incident (hallucination produces material harm; demographic bias surfaced; output regulator-actionable). Owner: CISO. Microsoft L3 on call.")
    add_bullet(doc, "Class 2 — data incident (personal data leakage; cross-border breach; oversharing surfaced). Owner: DPO. POPIA 72-hour notification clock starts.")
    add_bullet(doc, "Class 3 — service incident (region outage; service degradation). Owner: partner ops / Microsoft. Standard Azure incident channel.")
    add_paragraph(doc, "Run-book template: AI-CoE-Incident-Response-RunBook.md (to be added).")

    # 7. Kill-switch
    add_heading(doc, "7. Kill-switch", level=1)
    add_paragraph(
        doc,
        "Every production AI use-case has a tested kill-switch. The kill-switch is owned by the customer CISO, not by Microsoft. "
        "Tested quarterly; post-test report filed in the attestation sheet. Surfaces: Azure Policy disable on the deployment; "
        "Foundry endpoint disable; circuit-breaker in calling application.",
    )

    # 8. What to do when a gate fails
    add_heading(doc, "8. When a gate fails", level=1)
    add_bullet(doc, "Gate 1 fail — re-scope the use-case; usually the value hypothesis is too thin. Don't escalate; iterate.")
    add_bullet(doc, "Gate 2 fail — almost always a missing control or unaddressed risk. Block pilot; assign owner; revisit in two weeks.")
    add_bullet(doc, "Gate 3 fail — production launch blocked. Defects logged; eval threshold or HITL coverage usually the issue.")
    add_bullet(doc, "Gate 4 attestation gap — drift surfaced. Either re-establish the control or formally accept the residual risk with sign-off.")

    # 9. Linkages
    add_heading(doc, "9. Linked artefacts", level=1)
    add_bullet(doc, "ai-coe-responsible-ai-governance.md — strategic narrative behind this playbook.")
    add_bullet(doc, "AI-CoE-AI-Impact-Assessment.xlsx — the per-use-case working tool.")
    add_bullet(doc, "AI-CoE-Sovereign-AI-RSA.pptx — sovereignty offer that consumes this playbook.")
    add_bullet(doc, "ACC-2 (POPIA Landing Zone) — platform foundation under all of this.")
    add_bullet(doc, "ACC-4 (Regulated-Industry Pilot Kit) — pre-pilot workshop that completes Gate 2.")
    add_bullet(doc, "AI-CoE-Objection-Handling.pptx — pillar 5 responses for sellers.")

    # 10. Sources
    add_heading(doc, "10. Sources", level=1)
    add_bullet(doc, "Microsoft Responsible AI Standard v2 (public).")
    add_bullet(doc, "ISO/IEC 42001:2023 — AI Management System.")
    add_bullet(doc, "NIST AI Risk Management Framework 1.0.")
    add_bullet(doc, "EU AI Act (Regulation (EU) 2024/1689).")
    add_bullet(doc, "POPI Act; PFMA; NERSA Act; SARB Directive 7; FSCA Conduct Standards.")
    add_bullet(doc, "Microsoft Trust Center; Purview AI Hub documentation; Defender for Cloud AI documentation.")

    doc.save(str(OUT))
    print(f"Wrote {OUT.name}")


if __name__ == "__main__":
    main()
