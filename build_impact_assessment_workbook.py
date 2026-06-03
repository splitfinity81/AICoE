"""Generate AI-CoE-AI-Impact-Assessment.xlsx.

Eight sheets per the responsible-AI governance pack:
  1. Use-case register
  2. Crosswalk (RAI v2 -> ISO 42001 / NIST AI RMF / EU AI Act / POPIA / PFMA)
  3. Impact assessment (per use-case template)
  4. Risk register (18 pre-populated GenAI risks)
  5. Control selection
  6. Evidence log
  7. Sign-off
  8. Quarterly attestation log
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side

OUT = Path(__file__).parent / "AI-CoE-AI-Impact-Assessment.xlsx"

BLUE = "0067B8"
NAVY = "0B1F3A"
LIGHT = "EAF4FB"
AMBER = "FFE69C"
RED = "F8CBAD"
GREEN = "C6E0B4"

HEADER_FILL = PatternFill("solid", fgColor=BLUE)
HEADER_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=14)
TITLE_FILL = PatternFill("solid", fgColor=NAVY)
BODY_FONT = Font(name="Segoe UI", size=10)
BAND_FILL = PatternFill("solid", fgColor=LIGHT)

THIN = Side(border_style="thin", color="C0C0C0")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def add_title(ws, text: str, ncols: int) -> None:
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    cell = ws.cell(row=1, column=1, value=text)
    cell.fill = TITLE_FILL
    cell.font = TITLE_FONT
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 28


def style_header(ws, row: int, ncols: int) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = BORDER


def write_rows(ws, start_row: int, rows: list[list], ncols: int, band: bool = True) -> None:
    for r, row in enumerate(rows, start=start_row):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.font = BODY_FONT
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.border = BORDER
            if band and (r - start_row) % 2 == 1:
                cell.fill = BAND_FILL


def set_widths(ws, widths: list[int]) -> None:
    for i, w in enumerate(widths, start=1):
        col = chr(64 + i)
        ws.column_dimensions[col].width = w


def build_register(wb: Workbook) -> None:
    ws = wb.active
    ws.title = "1. Use-case register"
    headers = ["Use-case ID", "Name", "Business sponsor", "Business problem", "Expected value (annualised)", "MCEM stage", "Status", "Sector", "Pilot start", "Production target"]
    rows = [
        ["UC-001", "Claims triage agent (sample)", "Head of Claims, BU1", "Cycle time 4d; backlog 2k; reviewer FTE pressure", "ZAR 8m FTE-recovery + 30% cycle reduction", "3", "Pilot", "Insurance", "2026-07-15", "2026-11-01"],
        ["UC-002", "(add use-case)", "", "", "", "", "", "", "", ""],
        ["UC-003", "(add use-case)", "", "", "", "", "", "", "", ""],
    ]
    add_title(ws, "Use-case register — one row per AI workload", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [12, 32, 24, 38, 32, 12, 14, 18, 14, 16])


def build_crosswalk(wb: Workbook) -> None:
    ws = wb.create_sheet("2. Crosswalk")
    headers = ["Control family", "RAI v2", "ISO/IEC 42001", "NIST AI RMF", "EU AI Act", "POPIA", "PFMA", "Microsoft control surface"]
    rows = [
        ["Accountability & governance", "G1, G2", "A.5.1, A.5.2", "GOVERN-1", "Art. 9, 17", "§22", "s.38", "Azure Policy initiative; CoE charter"],
        ["Data governance & residency", "F1, T3", "A.6.2, A.8.24", "GOVERN-1.3, PROTECT", "Art. 10, 15", "§19, §72", "s.45", "Azure Policy data residency; Purview lineage"],
        ["Impact assessment", "T1", "A.6.4", "MAP-1, MAP-2", "Art. 9, 27", "§11, §22", "n/a", "This workbook; Microsoft RAI Impact Assessment template"],
        ["Risk identification", "T2", "A.6.1.4", "MAP-3, MAP-5", "Art. 9", "§19", "n/a", "Risk register sheet (sheet 4)"],
        ["System-prompt versioning", "T2", "A.5.37", "GOVERN-1.5", "Art. 11", "§22", "n/a", "Foundry prompt-flow versioning; GitHub"],
        ["Content Safety / Prompt Shields", "S1", "A.5.34", "MANAGE-2.3", "Art. 15", "n/a", "n/a", "Azure AI Content Safety; Prompt Shields"],
        ["HITL gate on regulated outputs", "A1", "A.6.4", "MANAGE-2.4", "Art. 14", "§11", "n/a", "Power Pages HITL queue; Dataverse routing"],
        ["Kill-switch + tested run-book", "S3", "A.5.30", "MANAGE-3", "Art. 9", "n/a", "s.45", "Azure Policy disable; Foundry deployment flag"],
        ["Audit trail (Purview AI Hub)", "G3", "A.5.10", "MEASURE-2.5", "Art. 12", "§17, §22", "s.38", "Microsoft Purview AI Hub"],
        ["Defender for Cloud AI posture", "S2", "A.8.16", "MANAGE-3", "Art. 9", "§19", "n/a", "Defender for Cloud AI"],
        ["Reviewer override feedback loop", "T4", "A.6.4", "MEASURE-3", "Art. 14", "n/a", "n/a", "PromptFlow eval; override-to-eval pipeline"],
        ["Encryption at rest (CMK)", "F2", "A.8.24", "PROTECT", "Art. 15", "§19", "s.45", "Azure Key Vault HSM CMK"],
        ["Network isolation", "F2", "A.8.20", "PROTECT", "Art. 15", "§19", "n/a", "Private endpoints; VNet integration"],
        ["Quarterly attestation", "G2", "A.5.36", "GOVERN-1.6", "Art. 17", "§22", "s.38", "Quarterly attestation sheet (sheet 8)"],
        ["Third-party / partner controls", "F3", "A.5.19", "GOVERN-6", "Art. 25", "§20", "s.38", "Partner DPA addendum; MAICPP terms"],
        ["Incident response & notification", "S3", "A.5.24", "MANAGE-3", "Art. 73", "§22(4)", "n/a", "Sentinel; Defender; customer IR run-book"],
        ["Demographic fairness assessment", "T1, A2", "A.6.1.4", "MEASURE-2.11", "Art. 10(2)", "n/a", "n/a", "Fairness toolkit; PromptFlow eval slices"],
        ["Explainability / reasoning trace", "T2", "A.6.1.4", "MEASURE-2.9", "Art. 13", "§22", "n/a", "Foundry reasoning trace; Purview log"],
    ]
    add_title(ws, "Master crosswalk — Microsoft control family x external frameworks", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [32, 14, 18, 22, 18, 14, 12, 38])
    for r in range(3, 3 + len(rows)):
        ws.row_dimensions[r].height = 32


def build_impact(wb: Workbook) -> None:
    ws = wb.create_sheet("3. Impact assessment")
    headers = ["Question", "Use-case answer", "Severity (1-5)", "Reversibility (1-5)", "Scale (1-5)", "Notes"]
    questions = [
        "Who is affected (employees / customers / third parties)?",
        "What decision does the AI make or influence?",
        "What is the worst-case bad outcome for an affected person?",
        "How reversible is that outcome?",
        "How many people are affected per month at production scale?",
        "Can an affected person contest the outcome? How?",
        "Are there demographic groups disproportionately affected?",
        "Does the use-case touch sensitive data per POPIA s.26?",
        "Is the use-case subject to sector-specific regulation? Which?",
        "Does the use-case meet EU AI Act high-risk criteria? Which annex?",
        "What is the kill-switch? Who can invoke it? Tested when?",
        "What is the HITL gate? On which decisions?",
        "What evidence does Internal Audit need to sample quarterly?",
        "What changes would trigger a re-assessment?",
    ]
    rows = [[q, "", "", "", "", ""] for q in questions]
    add_title(ws, "Per-use-case impact assessment (RAI v2 T1 adapted)", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [50, 40, 12, 14, 10, 30])
    for r in range(3, 3 + len(rows)):
        ws.row_dimensions[r].height = 30


def build_risk(wb: Workbook) -> None:
    ws = wb.create_sheet("4. Risk register")
    headers = ["Risk ID", "Risk", "Category", "Severity (1-5)", "Likelihood (1-5)", "Mitigation control", "Residual (1-5)", "Owner"]
    risks = [
        ("R-01", "Hallucination produces incorrect output cited as fact", "Model", 4, 4, "Content Safety + Prompt Shields + HITL gate + citation enforcement", 2, "Engineering lead"),
        ("R-02", "Prompt injection from untrusted user input", "Model", 4, 4, "Prompt Shields; input sanitisation; tool call allow-list", 2, "Engineering lead"),
        ("R-03", "Data leakage via vector index oversharing", "Data", 5, 3, "Purview sensitivity labels; row-level security; grounding-scope filter", 2, "Data engineering lead"),
        ("R-04", "Model drift on monthly refresh", "Model", 3, 4, "Eval harness with promotion gate; reviewer-override feedback", 2, "MLOps lead"),
        ("R-05", "Personal data processed outside SA without lawful basis", "Data / Compliance", 5, 2, "Foundry data-zone scoping; Azure Policy region lock; POPIA s72 check", 1, "DPO"),
        ("R-06", "M365 Copilot oversharing pre-existing SharePoint exposure", "Data / Adoption", 4, 4, "SharePoint Advanced Management; Purview classification sweep pre-go-live", 2, "M365 lead"),
        ("R-07", "Reviewer fatigue degrades HITL quality", "Process", 3, 4, "Reviewer workload monitoring; QA sample; UI investment", 2, "Operations lead"),
        ("R-08", "Bias against demographic group in claim / credit decisions", "Fairness", 5, 3, "Fairness eval slices; pre-production audit; ongoing monitoring", 2, "Risk lead"),
        ("R-09", "IP / copyright infringement in generated output", "Legal", 4, 2, "Customer Copyright Commitment; content filters; usage policy", 2, "Legal lead"),
        ("R-10", "Shadow AI use bypasses governance", "Governance", 4, 5, "Defender for Cloud AI discovery; approved-catalog policy; comms", 2, "CISO"),
        ("R-11", "Cost overrun (token/compute) at scale", "FinOps", 3, 4, "Budget alerts; model routing (small first); usage caps per tenant", 2, "FinOps lead"),
        ("R-12", "Third-party / partner control gap", "Vendor", 4, 3, "Partner DPA addendum; MAICPP terms; partner audit", 2, "Procurement lead"),
        ("R-13", "Incident: prompt logs contain personal data, not retention-managed", "Data", 4, 3, "Retention policy on prompt logs; Purview classification; quarterly purge audit", 2, "DPO"),
        ("R-14", "Eval harness becomes stale", "Quality", 3, 4, "Monthly eval-set refresh from reviewer overrides; quarterly review", 2, "MLOps lead"),
        ("R-15", "Kill-switch fails when invoked under stress", "Resilience", 5, 2, "Quarterly kill-switch test; documented run-book; post-test report", 1, "CISO"),
        ("R-16", "Sensitive output emailed externally", "Data Loss", 4, 3, "Purview DLP on outbound channels; output classification", 2, "CISO"),
        ("R-17", "Regulator request for explanation cannot be met", "Compliance", 4, 3, "Reasoning trace; Purview AI Hub log; evidence pack template", 2, "Internal Audit"),
        ("R-18", "Adoption stalls, value not realised", "Adoption", 3, 4, "Champion network; value-capture survey; quarterly Exco review", 2, "Change lead"),
    ]
    add_title(ws, "Pre-populated GenAI risk register (extend as needed)", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    rows = [list(r) for r in risks]
    write_rows(ws, 3, rows, len(headers))
    # Colour residual cell
    for i, r in enumerate(risks, start=3):
        residual = r[6]
        col = 7
        cell = ws.cell(row=i, column=col)
        if residual >= 4:
            cell.fill = PatternFill("solid", fgColor=RED)
        elif residual == 3:
            cell.fill = PatternFill("solid", fgColor=AMBER)
        else:
            cell.fill = PatternFill("solid", fgColor=GREEN)
    set_widths(ws, [8, 50, 18, 14, 16, 50, 14, 22])
    for r in range(3, 3 + len(rows)):
        ws.row_dimensions[r].height = 36


def build_controls(wb: Workbook) -> None:
    ws = wb.create_sheet("5. Control selection")
    headers = ["Control ID", "Control family (from crosswalk)", "Selected (Y/N)", "Implementation owner", "Evidence reference", "Notes"]
    families = [
        "Accountability & governance", "Data governance & residency", "Impact assessment", "Risk identification",
        "System-prompt versioning", "Content Safety / Prompt Shields", "HITL gate on regulated outputs",
        "Kill-switch + tested run-book", "Audit trail (Purview AI Hub)", "Defender for Cloud AI posture",
        "Reviewer override feedback loop", "Encryption at rest (CMK)", "Network isolation", "Quarterly attestation",
        "Third-party / partner controls", "Incident response & notification", "Demographic fairness assessment",
        "Explainability / reasoning trace",
    ]
    rows = [[f"C-{i:02d}", f, "Y", "", "", ""] for i, f in enumerate(families, start=1)]
    add_title(ws, "Control selection per use-case (defaults to Y; downgrade with justification)", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [10, 36, 14, 24, 28, 28])


def build_evidence(wb: Workbook) -> None:
    ws = wb.create_sheet("6. Evidence log")
    headers = ["Evidence ID", "Control ID", "Evidence type", "Storage location", "Cadence", "Reviewer", "Last collected", "Next due"]
    rows = [[f"E-{i:02d}", "", "", "", "", "", "", ""] for i in range(1, 11)]
    add_title(ws, "Evidence collection log", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [10, 10, 30, 30, 14, 22, 14, 14])


def build_signoff(wb: Workbook) -> None:
    ws = wb.create_sheet("7. Sign-off")
    headers = ["Role", "Name", "Signature (initials / DocuSign id)", "Date", "Gate signed"]
    rows = [
        ["Business sponsor", "", "", "", "Gate 1 / Gate 2 / Gate 3"],
        ["Microsoft CSA", "", "", "", "Gate 1 / Gate 2 / Gate 3"],
        ["Partner CSA / build lead", "", "", "", "Gate 2 / Gate 3"],
        ["Customer CISO", "", "", "", "Gate 2 / Gate 3 / Gate 4"],
        ["Customer DPO", "", "", "", "Gate 2 / Gate 4"],
        ["Customer Internal Audit", "", "", "", "Gate 4"],
        ["Customer Legal", "", "", "", "Gate 2"],
    ]
    add_title(ws, "Sign-off block per use-case", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [26, 26, 28, 14, 30])


def build_attestation(wb: Workbook) -> None:
    ws = wb.create_sheet("8. Quarterly attestation")
    headers = ["Quarter", "Use-case ID", "Controls re-verified", "Evidence refreshed", "Drift observed", "Action taken", "Signed by", "Date"]
    rows = [[q, "", "", "", "", "", "", ""] for q in ["FY26 Q3", "FY26 Q4", "FY27 Q1", "FY27 Q2", "FY27 Q3", "FY27 Q4"]]
    add_title(ws, "Quarterly attestation log (rolling)", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [12, 10, 26, 24, 24, 26, 18, 12])


def main() -> None:
    wb = Workbook()
    build_register(wb)
    build_crosswalk(wb)
    build_impact(wb)
    build_risk(wb)
    build_controls(wb)
    build_evidence(wb)
    build_signoff(wb)
    build_attestation(wb)
    wb.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(wb.sheetnames)} sheets: {wb.sheetnames}")


if __name__ == "__main__":
    main()
