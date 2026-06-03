"""Generate AI-CoE-Academy-Curriculum.xlsx.

Three sheets:
  1. Role x Tier x MS Learn x Cert matrix
  2. Cohort blueprint (per wave)
  3. 12-week delivery rhythm
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side

OUT = Path(__file__).parent / "AI-CoE-Academy-Curriculum.xlsx"

# Microsoft palette
BLUE = "0067B8"
CYAN = "50E6FF"
NAVY = "0B1F3A"
LIGHT = "EAF4FB"

HEADER_FILL = PatternFill("solid", fgColor=BLUE)
HEADER_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=11)
BODY_FONT = Font(name="Segoe UI", size=10)
BAND_FILL = PatternFill("solid", fgColor=LIGHT)
TITLE_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=14)
TITLE_FILL = PatternFill("solid", fgColor=NAVY)

THIN = Side(border_style="thin", color="C0C0C0")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def style_header(ws, row: int, ncols: int) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = BORDER


def style_body(ws, start_row: int, end_row: int, ncols: int) -> None:
    for r in range(start_row, end_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.border = BORDER
            if (r - start_row) % 2 == 1:
                cell.fill = BAND_FILL


def add_title(ws, text: str, ncols: int) -> None:
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    cell = ws.cell(row=1, column=1, value=text)
    cell.fill = TITLE_FILL
    cell.font = TITLE_FONT
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 28


def build_matrix_sheet(wb: Workbook) -> None:
    ws = wb.active
    ws.title = "Role x Tier Matrix"

    headers = [
        "Track",
        "Persona",
        "CoE Tier",
        "5+1 Pillar",
        "Format / Duration",
        "Anchor MS Learn paths",
        "Sector lab content",
        "Certification gate",
        "Pass criteria",
        "Seats / cohort",
    ]
    rows = [
        [
            "1. Executive Sponsor",
            "C-suite, EGM/GM, Board",
            "T1",
            "1 Business Strategy",
            "4 x half-day over 12 wk",
            "AI for Business Leaders (curated subset)",
            "PFMA business case; AGSA evidence walkthrough; regulator briefing simulation",
            "None (peer-review of own pilot business case)",
            "Can defend AI investment to CFO/AGSA/Board",
            "5–10",
        ],
        [
            "2. AI Product Owner",
            "BU heads, PMs, transformation leads",
            "T1+T2",
            "1, 3",
            "1 day/week x 12 wk (12 days)",
            "Microsoft Copilot Foundations; AI-900; Foundry Product Owner",
            "Horizon Assessment scoping; ACC-4 pilot-gate dry-run; KPI tree (time-to-decision, FTE-recovery)",
            "AI-900",
            "Signed-off use-case brief in pilot intake by wk 10",
            "10–15",
        ],
        [
            "3. AI Engineer",
            "Senior devs, ML engineers, platform engineers",
            "T2+T3",
            "3, 4, 5",
            "2 days/week x 12 wk (24 days)",
            "AI-102; Foundry Agent Service deep dive; GenAIOps with PromptFlow",
            "Build ACC-1 Banking CX Agent; Purview AI Hub; deploy via Bicep against ACC-2; eval harness",
            "AI-102",
            "Committed agent passing eval + Purview onboarded + Defender clean",
            "15–30",
        ],
        [
            "4. Data Engineer",
            "Data engineers, analytics engineers, BI leads",
            "T2",
            "4, 5",
            "2 days/week x 12 wk",
            "DP-700; Fabric for AI grounding; Purview Data Map",
            "POPIA-classified ingestion to OneLake; Purview lineage e2e; ground agent with RLS",
            "DP-700",
            "E2E pipeline live + sensitivity labels + RLS-bound grounding",
            "10–20",
        ],
        [
            "5. Copilot Champion",
            "Business power-users (HR/Fin/Ops/Legal)",
            "T1",
            "2 Org & Culture",
            "2 hr/week x 12 wk (24 hrs)",
            "Copilot Champion path; Copilot Studio Maker",
            "Role-based prompt library; FTE-hour recovery survey; one Studio agent for BU pain point",
            "M365 Copilot Specialist (Applied Skill)",
            "Published prompt library + shipped Studio agent + month-1 value-capture",
            "25–50",
        ],
    ]

    add_title(ws, "AI CoE Academy (RSA) — Role × Tier × MS Learn × Certification Matrix", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    for r, row in enumerate(rows, start=3):
        for c, val in enumerate(row, start=1):
            ws.cell(row=r, column=c, value=val)
    style_body(ws, 3, 2 + len(rows), len(headers))

    widths = [22, 30, 10, 18, 22, 32, 40, 28, 38, 14]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[chr(64 + i) if i <= 26 else "A" + chr(64 + i - 26)].width = w
    for r in range(3, 3 + len(rows)):
        ws.row_dimensions[r].height = 90


def build_cohort_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("Cohort Blueprint")
    headers = ["Track", "First-wave seats", "Steady-state seats (waves 2+)", "Funding source", "Partner role"]
    rows = [
        ["Executive Sponsor", 6, 6, "ECIF (Microsoft anchored)", "None (Microsoft-led)"],
        ["AI Product Owner", 12, 15, "ECIF + MAICPP", "Co-delivery with partner PMO"],
        ["AI Engineer", 20, 30, "MAICPP partner-funded", "Partner leads instructor labour + labs"],
        ["Data Engineer", 12, 18, "MAICPP partner-funded", "Partner leads"],
        ["Copilot Champion", 30, 50, "MAICPP + customer training budget", "Partner runs cohort engine"],
        ["TOTAL per wave", 80, 119, "—", "—"],
    ]
    add_title(ws, "Cohort Blueprint — seats and funding per wave", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    for r, row in enumerate(rows, start=3):
        for c, val in enumerate(row, start=1):
            ws.cell(row=r, column=c, value=val)
    style_body(ws, 3, 2 + len(rows), len(headers))
    # Bold the TOTAL row
    for c in range(1, len(headers) + 1):
        ws.cell(row=2 + len(rows), column=c).font = Font(name="Segoe UI", bold=True, size=10)

    widths = [26, 18, 30, 30, 35]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[chr(64 + i)].width = w


def build_rhythm_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("12-Week Rhythm")
    headers = ["Week", "Activity", "All tracks?", "Notes"]
    rows = [
        ["-2", "Baseline assessment + track placement", "Yes", "Skill-Navigator placement test routes learners"],
        ["1", "Kickoff + sponsor address + cohort norms", "Yes", "Executive Sponsor track opens the wave"],
        ["2–4", "Foundation modules", "Per track", "Microsoft Learn paths anchor self-paced load"],
        ["5", "Mid-wave checkpoint + sector lab #1", "Per track", "First sector-specific lab"],
        ["6–8", "Build / specialise", "Per track", "Engineers building, PMs scoping, Champions running office hours"],
        ["9", "Sector lab #2 + mock cert (Eng/Data)", "Per track", "AI-102/DP-700 under exam conditions"],
        ["10", "Pilot-gate dry-run (PO track lead)", "Yes", "Other tracks attend as panellists"],
        ["11", "Certification sittings", "Per track", "AI-900/AI-102/DP-700/Applied Skill"],
        ["12", "Showcase + value-capture + next-wave nomination", "Yes", "Customer Exco attends; sets up wave 2"],
    ]
    add_title(ws, "12-Week Delivery Rhythm", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    for r, row in enumerate(rows, start=3):
        for c, val in enumerate(row, start=1):
            ws.cell(row=r, column=c, value=val)
    style_body(ws, 3, 2 + len(rows), len(headers))
    widths = [10, 45, 12, 45]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[chr(64 + i)].width = w


def build_kpi_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("KPIs")
    headers = ["KPI", "Target", "Source", "Owner"]
    rows = [
        ["Cohort completion rate", ">= 80%", "LMS attendance", "Partner PMO"],
        ["Certification pass rate (gated tracks)", ">= 75% first attempt", "Pearson VUE / Credly", "Partner instructor lead"],
        ["Sponsor track pass criteria met", "100%", "Peer review", "Microsoft CoE lead"],
        ["Use-cases shipped into pilot intake (PO track)", ">= 1 per learner", "Customer intake log", "Customer transformation office"],
        ["Engineer track agents committed to repo", ">= 1 per learner", "GitHub / DevOps", "Customer platform team"],
        ["Champion track prompt libraries published", ">= 1 per learner", "Customer SharePoint", "BU sponsor"],
        ["Net Promoter Score", ">= +30", "End-of-wave survey", "Microsoft CoE lead"],
    ]
    add_title(ws, "KPIs — per wave", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    for r, row in enumerate(rows, start=3):
        for c, val in enumerate(row, start=1):
            ws.cell(row=r, column=c, value=val)
    style_body(ws, 3, 2 + len(rows), len(headers))
    widths = [42, 22, 28, 30]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[chr(64 + i)].width = w


def main() -> None:
    wb = Workbook()
    build_matrix_sheet(wb)
    build_cohort_sheet(wb)
    build_rhythm_sheet(wb)
    build_kpi_sheet(wb)
    wb.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(wb.sheetnames)} sheets: {wb.sheetnames}")


if __name__ == "__main__":
    main()
