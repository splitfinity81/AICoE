"""Generate AI-CoE-Change-Readiness-Instrument.xlsx.

Companion workbook for issue #13: change-management methodology.
Five-dimension readiness scoring (Sponsorship, Workforce, Use-case, Enablement, Measurement)
with auto-computed band (Green / Amber / Red).
"""

from __future__ import annotations
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

OUT = Path(__file__).parent / "AI-CoE-Change-Readiness-Instrument.xlsx"

BLUE = "0067B8"
CYAN = "50E6FF"
PURPLE = "742A9B"
NAVY = "0B1F3A"
LIGHT = "EAF4FB"
WHITE = "FFFFFF"
GREEN = "C6EFCE"
AMBER = "FFEB9C"
RED = "FFC7CE"

THIN = Side(border_style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def style_header(cell, fill=BLUE, color=WHITE, size=11):
    cell.font = Font(name="Segoe UI", bold=True, color=color, size=size)
    cell.fill = PatternFill("solid", fgColor=fill)
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell.border = BORDER


def style_cell(cell, bold=False, size=10, color="000000", fill=None, wrap=True, align="left"):
    cell.font = Font(name="Segoe UI", bold=bold, color=color, size=size)
    if fill:
        cell.fill = PatternFill("solid", fgColor=fill)
    cell.alignment = Alignment(horizontal=align, vertical="top", wrap_text=wrap)
    cell.border = BORDER


def widths(ws, cols):
    for i, w in enumerate(cols, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def sheet_readme(wb):
    ws = wb.create_sheet("README")
    ws.sheet_view.showGridLines = False
    widths(ws, [110])
    rows = [
        ("AI CoE — Change Readiness Instrument", True, 18, NAVY),
        ("Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft · v1.0 · 2026-06-03", False, 11, NAVY),
        ("", False, 11, NAVY),
        ("Companion to: ai-coe-change-management-methodology.md", False, 11, NAVY),
        ("Closes issue #13 (deepen change-management methodology — replace one-bullet VBD A3).", False, 11, NAVY),
        ("", False, 11, NAVY),
        ("How to use", True, 14, BLUE),
        ("1. Open the 'Assessment' sheet. For each of the 5 dimensions, score 1-5 against the rubric.", False, 11, NAVY),
        ("2. The 'Score' sheet auto-computes the total and lights the readiness band:", False, 11, NAVY),
        ("    Green 20-25 = proceed at full pace", False, 11, NAVY),
        ("    Amber 14-19 = proceed with mitigations on weakest dimensions; 30-day pre-launch plan", False, 11, NAVY),
        ("    Red <14 = do not launch broadly; 90-day fixture programme on weakest dimensions", False, 11, NAVY),
        ("3. The 'Summary' sheet is a one-page output suitable for steering-committee distribution.", False, 11, NAVY),
        ("4. The 'Rubric' sheet documents the 1-5 scoring rubric per dimension.", False, 11, NAVY),
        ("5. Re-run quarterly; trend the score in the Adoption & Value dashboard.", False, 11, NAVY),
        ("", False, 11, NAVY),
        ("Linked artefacts", True, 14, BLUE),
        ("ai-coe-change-management-methodology.md — full methodology + ADKAR framing + 8-week plan", False, 11, NAVY),
        ("AI-CoE-Academy-Curriculum.xlsx — learning paths plug into Knowledge + Ability ADKAR stages", False, 11, NAVY),
        ("AI-CoE-Horizon-Assessment.xlsx — workforce-readiness dimension feeds into this instrument", False, 11, NAVY),
        ("AI-CoE-GenAIOps-Reference.docx §6 — Adoption & Value dashboard is the measurement surface", False, 11, NAVY),
        ("AI-CoE-Objection-Handling.pptx — objections 2.1 / 2.2 / 2.3 anchor here", False, 11, NAVY),
    ]
    for i, (text, bold, size, color) in enumerate(rows, start=1):
        c = ws.cell(row=i, column=1, value=text)
        c.font = Font(name="Segoe UI", bold=bold, size=size, color=color)
        c.alignment = Alignment(wrap_text=True, vertical="top")


def sheet_rubric(wb):
    ws = wb.create_sheet("Rubric")
    ws.sheet_view.showGridLines = False
    widths(ws, [22, 70, 22, 22, 22, 22, 22])
    headers = ["Dimension", "What it measures", "Score 1", "Score 2", "Score 3", "Score 4", "Score 5"]
    for i, h in enumerate(headers, start=1):
        style_header(ws.cell(row=1, column=i, value=h))
    rubric = [
        ["Sponsorship", "Visible C-suite ownership, named exec sponsor, public commitment",
         "No named sponsor", "Sponsor named but silent", "Sponsor visible internally", "Sponsor visible + tied to KPI", "C-suite drumbeat + own KPIs"],
        ["Workforce", "Digital fluency baseline, prior change fatigue, openness to AI",
         "Low fluency + high fatigue", "Mixed; recent failures", "Average baseline; neutral", "Generally fluent + curious", "High fluency + grass-roots demand"],
        ["Use-case clarity", "Top 3 use-cases defined with named LOB owners and measurable outcome",
         "No defined use-cases", "Use-cases listed, no owners", "Owners named, outcome vague", "Owners + measurable outcomes", "Owners + outcomes + baselines"],
        ["Enablement capacity", "Champions identified, learning paths assigned, trainer/partner contracted",
         "No Champions / training", "Champions named, not trained", "Champions + learning paths", "Champions trained + community live", "Community + office hours + mentoring"],
        ["Measurement", "Adoption KPIs agreed, baseline measured, dashboard owner named",
         "No KPIs agreed", "KPIs drafted, no baseline", "KPIs + baseline, no owner", "KPIs + baseline + owner", "All above + live dashboard"],
    ]
    for r, row in enumerate(rubric, start=2):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            style_cell(cell, bold=(c == 1), fill=LIGHT if c == 1 else None)


def sheet_assessment(wb):
    ws = wb.create_sheet("Assessment")
    ws.sheet_view.showGridLines = False
    widths(ws, [22, 60, 16, 50])
    for i, h in enumerate(["Dimension", "Question prompt", "Score (1-5)", "Mitigation note"], start=1):
        style_header(ws.cell(row=1, column=i, value=h))
    items = [
        ("Sponsorship", "How visible and committed is the executive sponsor?"),
        ("Workforce", "How ready is the workforce — digital fluency, openness, change fatigue?"),
        ("Use-case clarity", "How well-defined are the top 3 use-cases with named owners and outcomes?"),
        ("Enablement capacity", "Are Champions, learning paths, and trainers in place?"),
        ("Measurement", "Are KPIs, baselines and dashboards agreed with named owners?"),
    ]
    for r, (dim, q) in enumerate(items, start=2):
        style_cell(ws.cell(row=r, column=1, value=dim), bold=True, fill=LIGHT)
        style_cell(ws.cell(row=r, column=2, value=q))
        cell = ws.cell(row=r, column=3, value=3)
        style_cell(cell, bold=True, align="center", fill="FFF2CC")
        style_cell(ws.cell(row=r, column=4, value=""))
    ws.row_dimensions[1].height = 28
    for r in range(2, 7):
        ws.row_dimensions[r].height = 42


def sheet_score(wb):
    ws = wb.create_sheet("Score")
    ws.sheet_view.showGridLines = False
    widths(ws, [28, 18, 60])
    style_header(ws.cell(row=1, column=1, value="Output"))
    style_header(ws.cell(row=1, column=2, value="Value"))
    style_header(ws.cell(row=1, column=3, value="Interpretation"))
    rows = [
        ("Sponsorship score", "=Assessment!C2", ""),
        ("Workforce score", "=Assessment!C3", ""),
        ("Use-case clarity score", "=Assessment!C4", ""),
        ("Enablement capacity score", "=Assessment!C5", ""),
        ("Measurement score", "=Assessment!C6", ""),
        ("TOTAL / 25", "=SUM(B2:B6)", ""),
        ("Readiness band", '=IF(B7>=20,"GREEN — proceed at full pace",IF(B7>=14,"AMBER — proceed with mitigations; 30-day pre-launch plan","RED — do not broad-launch; 90-day fixture programme"))', ""),
    ]
    for r, (label, formula, interp) in enumerate(rows, start=2):
        style_cell(ws.cell(row=r, column=1, value=label), bold=True, fill=LIGHT)
        c = ws.cell(row=r, column=2, value=formula)
        style_cell(c, bold=True, align="center")
        style_cell(ws.cell(row=r, column=3, value=interp))
    ws.cell(row=8, column=1).font = Font(name="Segoe UI", bold=True, size=12, color=NAVY)
    band_cell = "B8"
    ws.conditional_formatting.add(band_cell,
        CellIsRule(operator="containsText", formula=['"GREEN"'], fill=PatternFill("solid", fgColor=GREEN)))
    # Simpler band coloring via formula text-search isn't trivial in openpyxl; do per-cell fill instruction in README.
    for r in range(2, 9):
        ws.row_dimensions[r].height = 22


def sheet_summary(wb):
    ws = wb.create_sheet("Summary")
    ws.sheet_view.showGridLines = False
    widths(ws, [40, 50])
    ws.cell(row=1, column=1, value="AI CoE — Change Readiness Summary").font = Font(name="Segoe UI", bold=True, size=18, color=NAVY)
    ws.cell(row=2, column=1, value="One-page output for steering committee").font = Font(name="Segoe UI", italic=True, size=11, color=NAVY)
    rows = [
        ("Sponsorship", "=Assessment!C2"),
        ("Workforce", "=Assessment!C3"),
        ("Use-case clarity", "=Assessment!C4"),
        ("Enablement capacity", "=Assessment!C5"),
        ("Measurement", "=Assessment!C6"),
        ("TOTAL / 25", "=Score!B7"),
        ("Readiness band", "=Score!B8"),
    ]
    for i, (label, formula) in enumerate(rows, start=4):
        style_cell(ws.cell(row=i, column=1, value=label), bold=True, fill=LIGHT)
        style_cell(ws.cell(row=i, column=2, value=formula), bold=True, align="center")
    ws.cell(row=12, column=1, value="Next actions").font = Font(name="Segoe UI", bold=True, size=14, color=BLUE)
    ws.cell(row=13, column=1, value="1. Review the lowest-scoring dimension(s) on the Assessment sheet.").font = Font(name="Segoe UI", size=11)
    ws.cell(row=14, column=1, value="2. Capture mitigations in the 'Mitigation note' column for any score <= 3.").font = Font(name="Segoe UI", size=11)
    ws.cell(row=15, column=1, value="3. Re-score after 30 / 90 days per band guidance in README.").font = Font(name="Segoe UI", size=11)
    ws.cell(row=16, column=1, value="4. Trend total score quarterly in Adoption & Value dashboard.").font = Font(name="Segoe UI", size=11)


def main():
    wb = Workbook()
    wb.remove(wb.active)
    sheet_readme(wb)
    sheet_rubric(wb)
    sheet_assessment(wb)
    sheet_score(wb)
    sheet_summary(wb)
    wb.save(str(OUT))
    print(f"Wrote {OUT.name}")


if __name__ == "__main__":
    main()
