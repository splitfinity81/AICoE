"""Generate AI-CoE-AI-TCO-Calculator.xlsx.

FinOps-for-AI calculator: token-budget x model-routing x cache-hit modelling.
Sheets:
  1. Read me - how to use the calculator
  2. Pricing reference - per-1k-token rates (editable)
  3. Inputs - per-use-case inputs (users, q/u/d, tokens, model mix, cache, fallback, retry, infra)
  4. Run-rate forecast - monthly + annual cost computed from inputs + pricing
  5. Scenarios - three pre-loaded scenarios (High / Mid / Low intensity)
  6. Per-seat vs per-token - M365 Copilot per-seat vs Foundry per-token trade-off
  7. WAF binding - Well-Architected Framework Cost Optimisation pillar binding
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

OUT = Path(__file__).parent / "AI-CoE-AI-TCO-Calculator.xlsx"

BLUE = "0067B8"
NAVY = "0B1F3A"
LIGHT = "EAF4FB"
AMBER = "FFE69C"
GREEN = "C6E0B4"
PURPLE = "742A9B"

HEADER_FILL = PatternFill("solid", fgColor=BLUE)
HEADER_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(name="Segoe UI", bold=True, color="FFFFFF", size=14)
TITLE_FILL = PatternFill("solid", fgColor=NAVY)
SUB_FILL = PatternFill("solid", fgColor=PURPLE)
BODY_FONT = Font(name="Segoe UI", size=10)
BOLD_BODY = Font(name="Segoe UI", size=10, bold=True)
BAND_FILL = PatternFill("solid", fgColor=LIGHT)
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
RESULT_FILL = PatternFill("solid", fgColor=GREEN)

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


def write_rows(ws, start_row: int, rows, ncols: int, band: bool = True, input_cols=None) -> None:
    input_cols = input_cols or []
    for r, row in enumerate(rows, start=start_row):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.font = BODY_FONT
            cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
            cell.border = BORDER
            if c in input_cols:
                cell.fill = INPUT_FILL
            elif band and (r - start_row) % 2 == 1:
                cell.fill = BAND_FILL


def set_widths(ws, widths) -> None:
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def build_readme(wb: Workbook) -> None:
    ws = wb.active
    ws.title = "1. Read me"
    add_title(ws, "AI TCO / FinOps Calculator - how to use", 2)
    rows = [
        ["Purpose", "Model the annual run-rate cost of an AI use-case across model routing, cache-hit, fallback/retry, and supporting infra. Compare per-seat (M365 Copilot) vs per-token (Foundry) economics."],
        ["Author", "Yuri Baijnath - CSU Cloud & AI Lead (South Africa), Microsoft"],
        ["Version", "1.0 - 2026-06-03"],
        ["When to use", "Pre-pilot sizing (Gate 2), production go-live forecast (Gate 3), quarterly attestation re-forecast (Gate 4)."],
        ["Inputs (yellow cells)", "Edit only yellow cells. Sheets: 2. Pricing reference, 3. Inputs, 5. Scenarios."],
        ["Results (green cells)", "Computed from inputs. Do not overwrite. Sheets: 4. Run-rate forecast, 6. Per-seat vs per-token."],
        ["Pricing currency", "USD per 1,000 tokens (industry convention). Convert to ZAR at sheet 4 footer."],
        ["Model routing", "gpt-4o (heavy reasoning), gpt-4o-mini (default), Phi-3 (fast/cheap fallback). Adjust mix on sheet 3."],
        ["Cache-hit assumption", "Cached responses cost ~10% of un-cached (storage + lookup only). Default cache-hit 30%."],
        ["Fallback / retry", "Fallback fires when primary model rejects (Content Safety / Prompt Shields / timeout). Retry fires on transient failure. Both add tokens."],
        ["Per-seat trade-off", "M365 Copilot is per-user-per-month; Foundry agents are per-token. Sheet 6 surfaces the cross-over point."],
        ["Cross-references", "Objection 1.3 (Copilot per-seat doesn't pencil); Objection 4.6 (cost overrun at scale); VBD D3 (FinOps for AI); WAF Cost Optimisation pillar."],
        ["Disclaimer", "Pricing changes. Re-verify on https://azure.microsoft.com/en-us/pricing/ before any customer commit. All figures are planning estimates, not quotes."],
    ]
    for r, row in enumerate(rows, start=3):
        ws.cell(row=r, column=1, value=row[0]).font = BOLD_BODY
        ws.cell(row=r, column=1).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws.cell(row=r, column=2, value=row[1]).font = BODY_FONT
        ws.cell(row=r, column=2).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        for c in (1, 2):
            ws.cell(row=r, column=c).border = BORDER
        ws.row_dimensions[r].height = 32
    set_widths(ws, [24, 110])


def build_pricing(wb: Workbook) -> None:
    ws = wb.create_sheet("2. Pricing reference")
    headers = ["Item", "Unit", "USD / unit", "Notes"]
    rows = [
        ["gpt-4o input", "1k tokens", 0.0025, "Heavy reasoning, vision; check Azure pricing for current"],
        ["gpt-4o output", "1k tokens", 0.010, ""],
        ["gpt-4o-mini input", "1k tokens", 0.00015, "Default workhorse"],
        ["gpt-4o-mini output", "1k tokens", 0.0006, ""],
        ["Phi-3-medium input", "1k tokens", 0.00005, "Fallback / fast lane (planning estimate)"],
        ["Phi-3-medium output", "1k tokens", 0.0002, ""],
        ["text-embedding-3-large", "1k tokens", 0.00013, "Vector index ingestion"],
        ["Cached output (uplift factor)", "ratio", 0.10, "Cached call cost as % of un-cached - tune per workload"],
        ["AI Search S1", "instance / month", 250, "Vector index host (planning estimate)"],
        ["Blob storage (hot)", "GB / month", 0.020, "Document corpus + prompt logs"],
        ["Content Safety call", "1k calls", 0.75, "Both input + output filter"],
        ["Defender for Cloud AI", "resource / month", 7, "Per protected resource (estimate)"],
        ["Purview AI Hub", "user / month", 4, "Per monitored user (estimate)"],
        ["Log Analytics ingestion", "GB", 2.30, "Monitoring + audit log"],
        ["M365 Copilot license", "user / month", 30, "Per-seat baseline (USD list)"],
    ]
    add_title(ws, "Pricing reference - edit yellow cells to match latest published Azure rates", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers), input_cols=[3])
    set_widths(ws, [34, 18, 14, 60])


PRICE = {
    "in_4o": "'2. Pricing reference'!$C$3",
    "out_4o": "'2. Pricing reference'!$C$4",
    "in_mini": "'2. Pricing reference'!$C$5",
    "out_mini": "'2. Pricing reference'!$C$6",
    "in_phi": "'2. Pricing reference'!$C$7",
    "out_phi": "'2. Pricing reference'!$C$8",
    "embed": "'2. Pricing reference'!$C$9",
    "cache_factor": "'2. Pricing reference'!$C$10",
    "search": "'2. Pricing reference'!$C$11",
    "blob": "'2. Pricing reference'!$C$12",
    "cs": "'2. Pricing reference'!$C$13",
    "defender": "'2. Pricing reference'!$C$14",
    "purview": "'2. Pricing reference'!$C$15",
    "loga": "'2. Pricing reference'!$C$16",
    "seat": "'2. Pricing reference'!$C$17",
}


def build_inputs(wb: Workbook) -> None:
    ws = wb.create_sheet("3. Inputs")
    headers = ["Parameter", "Value", "Unit", "Notes"]
    rows = [
        ["Use-case name", "Claims triage agent (sample)", "", "Replace with your use-case"],
        ["Users", 500, "active users", "Concurrent / licensed seat count"],
        ["Queries per user per day", 12, "queries", "Empirical; instrument and refine"],
        ["Working days per month", 22, "days", ""],
        ["Avg input tokens per query", 1500, "tokens", "Includes system + retrieved context"],
        ["Avg output tokens per query", 400, "tokens", ""],
        ["% routed to gpt-4o", 0.20, "share 0-1", "Heavy reasoning calls"],
        ["% routed to gpt-4o-mini", 0.65, "share 0-1", "Default workhorse"],
        ["% routed to Phi-3", 0.15, "share 0-1", "Fast/cheap fallback"],
        ["Cache-hit rate", 0.30, "share 0-1", "Higher for FAQ / repeated intents"],
        ["Fallback rate (CS/Prompt-Shield reject -> re-route)", 0.05, "share 0-1", "Adds full second call at fallback model"],
        ["Retry rate (transient)", 0.02, "share 0-1", "Adds full second call at same model"],
        ["Vector index size", 50, "GB", "Document corpus indexed"],
        ["Embeddings refresh per month", 5, "GB", "Delta re-indexed monthly"],
        ["Blob storage (logs + corpus)", 200, "GB", ""],
        ["Content Safety enabled", 1, "1=yes 0=no", ""],
        ["Defender for Cloud AI resources", 6, "resources", "Foundry endpoint, AI Search, KV, etc."],
        ["Purview AI Hub monitored users", 500, "users", "Usually = active users"],
        ["Log Analytics ingestion / month", 20, "GB", ""],
        ["M365 Copilot per-seat sizing (for comparison)", 500, "seats", "Used on sheet 6"],
        ["USD->ZAR FX", 18.50, "ZAR per USD", "Update at fiscal start"],
    ]
    add_title(ws, "Inputs - edit yellow cells. One use-case per workbook (copy sheet to model more).", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers), input_cols=[2])
    set_widths(ws, [50, 18, 16, 50])


IN = {  # cell refs into '3. Inputs'!B*
    "users": "'3. Inputs'!$B$4",
    "qpd": "'3. Inputs'!$B$5",
    "wdays": "'3. Inputs'!$B$6",
    "in_tok": "'3. Inputs'!$B$7",
    "out_tok": "'3. Inputs'!$B$8",
    "mix_4o": "'3. Inputs'!$B$9",
    "mix_mini": "'3. Inputs'!$B$10",
    "mix_phi": "'3. Inputs'!$B$11",
    "cache": "'3. Inputs'!$B$12",
    "fb": "'3. Inputs'!$B$13",
    "retry": "'3. Inputs'!$B$14",
    "vec_gb": "'3. Inputs'!$B$15",
    "embed_gb": "'3. Inputs'!$B$16",
    "blob_gb": "'3. Inputs'!$B$17",
    "cs_on": "'3. Inputs'!$B$18",
    "def_res": "'3. Inputs'!$B$19",
    "purv_u": "'3. Inputs'!$B$20",
    "loga_gb": "'3. Inputs'!$B$21",
    "seats": "'3. Inputs'!$B$22",
    "fx": "'3. Inputs'!$B$23",
}


def build_forecast(wb: Workbook) -> None:
    ws = wb.create_sheet("4. Run-rate forecast")
    headers = ["Line item", "Monthly USD", "Annual USD", "Annual ZAR", "How computed"]
    add_title(ws, "Run-rate forecast - per-token Foundry path (per-seat path on sheet 6)", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))

    # queries/month
    q = f"({IN['users']}*{IN['qpd']}*{IN['wdays']})"
    # effective billable queries after cache hit (cached calls cost cache_factor of normal)
    eff = f"({q}*((1-{IN['cache']})+({IN['cache']}*{PRICE['cache_factor']})))"
    # multipliers: retry adds same-model second call; fallback adds full second call
    mult = f"(1+{IN['retry']}+{IN['fb']})"

    def model_cost(mix_key, in_price, out_price):
        return f"({eff}*{IN[mix_key]}*({IN['in_tok']}/1000*{in_price}+{IN['out_tok']}/1000*{out_price})*{mult})"

    c_4o = model_cost("mix_4o", PRICE["in_4o"], PRICE["out_4o"])
    c_mini = model_cost("mix_mini", PRICE["in_mini"], PRICE["out_mini"])
    c_phi = model_cost("mix_phi", PRICE["in_phi"], PRICE["out_phi"])
    c_embed = f"({IN['embed_gb']}*1024*1024/4*{PRICE['embed']}/1000)"  # rough: GB->tokens approx via 4 chars/token
    c_search = f"{PRICE['search']}"
    c_blob = f"({IN['blob_gb']}*{PRICE['blob']})"
    c_cs = f"(IF({IN['cs_on']}=1,{q}*2/1000*{PRICE['cs']},0))"
    c_def = f"({IN['def_res']}*{PRICE['defender']})"
    c_purv = f"({IN['purv_u']}*{PRICE['purview']})"
    c_loga = f"({IN['loga_gb']}*{PRICE['loga']})"

    lines = [
        ("gpt-4o (heavy reasoning)", c_4o, "% mix * (input+output tokens * price) * (1+retry+fallback), cache-adjusted"),
        ("gpt-4o-mini (default)", c_mini, "as above"),
        ("Phi-3 (fast lane)", c_phi, "as above"),
        ("Embeddings refresh", c_embed, "Embedding tokens per GB delta * price"),
        ("AI Search (vector index host)", c_search, "S1 instance"),
        ("Blob storage (logs + corpus)", c_blob, "GB * price"),
        ("Content Safety", c_cs, "2 calls per query (input + output filter)"),
        ("Defender for Cloud AI", c_def, "Resources * price"),
        ("Purview AI Hub", c_purv, "Monitored users * price"),
        ("Log Analytics", c_loga, "Ingestion GB * price"),
    ]
    row = 3
    for label, formula, note in lines:
        ws.cell(row=row, column=1, value=label).font = BODY_FONT
        ws.cell(row=row, column=2, value=f"={formula}").font = BODY_FONT
        ws.cell(row=row, column=3, value=f"=B{row}*12").font = BODY_FONT
        ws.cell(row=row, column=4, value=f"=C{row}*{IN['fx']}").font = BODY_FONT
        ws.cell(row=row, column=5, value=note).font = BODY_FONT
        for c in range(1, 6):
            ws.cell(row=row, column=c).border = BORDER
            ws.cell(row=row, column=c).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        for c in (2, 3, 4):
            ws.cell(row=row, column=c).number_format = "#,##0.00"
        row += 1
    # total
    last = row - 1
    ws.cell(row=row, column=1, value="TOTAL (per-token path)").font = BOLD_BODY
    ws.cell(row=row, column=2, value=f"=SUM(B3:B{last})").font = BOLD_BODY
    ws.cell(row=row, column=3, value=f"=SUM(C3:C{last})").font = BOLD_BODY
    ws.cell(row=row, column=4, value=f"=SUM(D3:D{last})").font = BOLD_BODY
    ws.cell(row=row, column=5, value="Sum of above").font = BOLD_BODY
    for c in range(1, 6):
        ws.cell(row=row, column=c).fill = RESULT_FILL
        ws.cell(row=row, column=c).border = BORDER
    for c in (2, 3, 4):
        ws.cell(row=row, column=c).number_format = "#,##0.00"
    # cost per query and per user/month
    row += 2
    ws.cell(row=row, column=1, value="Cost per query (USD)").font = BOLD_BODY
    ws.cell(row=row, column=2, value=f"=B{last+1}/({IN['users']}*{IN['qpd']}*{IN['wdays']})").number_format = "#,##0.0000"
    row += 1
    ws.cell(row=row, column=1, value="Cost per user / month (USD)").font = BOLD_BODY
    ws.cell(row=row, column=2, value=f"=B{last+1}/{IN['users']}").number_format = "#,##0.00"
    row += 1
    ws.cell(row=row, column=1, value="Cost per user / month (ZAR)").font = BOLD_BODY
    ws.cell(row=row, column=2, value=f"=B{row-1}*{IN['fx']}").number_format = "#,##0.00"

    set_widths(ws, [40, 18, 18, 18, 60])
    for r in range(3, row + 1):
        ws.row_dimensions[r].height = 22


def build_scenarios(wb: Workbook) -> None:
    ws = wb.create_sheet("5. Scenarios")
    headers = ["Parameter", "Low intensity", "Mid intensity (default)", "High intensity", "Unit", "Notes"]
    rows = [
        ["Users", 200, 500, 2000, "users", "Concurrent licensed users"],
        ["Queries per user per day", 5, 12, 30, "queries", "Low = ad-hoc; mid = daily; high = power"],
        ["Working days per month", 22, 22, 22, "days", ""],
        ["Avg input tokens", 800, 1500, 3000, "tokens", "Heavier RAG -> larger context"],
        ["Avg output tokens", 200, 400, 800, "tokens", ""],
        ["% gpt-4o", 0.05, 0.20, 0.40, "share", "More reasoning -> more 4o"],
        ["% gpt-4o-mini", 0.70, 0.65, 0.50, "share", ""],
        ["% Phi-3", 0.25, 0.15, 0.10, "share", ""],
        ["Cache-hit rate", 0.45, 0.30, 0.15, "share", "Lower for varied workloads"],
        ["Fallback rate", 0.03, 0.05, 0.08, "share", ""],
        ["Retry rate", 0.01, 0.02, 0.04, "share", ""],
        ["Vector index (GB)", 10, 50, 250, "GB", ""],
        ["Blob storage (GB)", 50, 200, 1000, "GB", ""],
        ["Defender resources", 4, 6, 12, "resources", ""],
        ["Log Analytics (GB/mo)", 5, 20, 100, "GB", ""],
        ["Indicative annual USD (est.)", "see sheet 4", "see sheet 4", "see sheet 4", "USD", "Re-run sheet 4 with these inputs to compute"],
    ]
    add_title(ws, "Three pre-loaded scenarios - copy column into sheet 3 to re-cost", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers), input_cols=[2, 3, 4])
    set_widths(ws, [34, 16, 22, 16, 12, 50])


def build_per_seat(wb: Workbook) -> None:
    ws = wb.create_sheet("6. Per-seat vs per-token")
    headers = ["Path", "Monthly USD", "Annual USD", "Annual ZAR", "How computed"]
    add_title(ws, "Per-seat (M365 Copilot) vs per-token (Foundry) trade-off", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))

    # Per-seat: seats * seat price
    seat_monthly = f"={IN['seats']}*{PRICE['seat']}"
    # Per-token total comes from sheet 4 (we look it up - the TOTAL row)
    # The TOTAL row in sheet 4 is at row 13 (3..12 = 10 lines, row 13 = total)
    token_monthly = "='4. Run-rate forecast'!B13"

    rows_data = [
        ("M365 Copilot per-seat", seat_monthly, "Seats * per-user-per-month"),
        ("Foundry agent per-token (from sheet 4)", token_monthly, "Total of sheet 4"),
    ]
    row = 3
    for label, formula, note in rows_data:
        ws.cell(row=row, column=1, value=label).font = BODY_FONT
        ws.cell(row=row, column=2, value=formula).font = BODY_FONT
        ws.cell(row=row, column=3, value=f"=B{row}*12").font = BODY_FONT
        ws.cell(row=row, column=4, value=f"=C{row}*{IN['fx']}").font = BODY_FONT
        ws.cell(row=row, column=5, value=note).font = BODY_FONT
        for c in range(1, 6):
            ws.cell(row=row, column=c).border = BORDER
            ws.cell(row=row, column=c).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        for c in (2, 3, 4):
            ws.cell(row=row, column=c).number_format = "#,##0.00"
        row += 1
    # delta
    ws.cell(row=row, column=1, value="Delta (per-seat - per-token), annual USD").font = BOLD_BODY
    ws.cell(row=row, column=3, value="=C3-C4").font = BOLD_BODY
    ws.cell(row=row, column=3).number_format = "#,##0.00"
    ws.cell(row=row, column=4, value="=D3-D4").font = BOLD_BODY
    ws.cell(row=row, column=4).number_format = "#,##0.00"
    for c in range(1, 6):
        ws.cell(row=row, column=c).fill = RESULT_FILL
        ws.cell(row=row, column=c).border = BORDER
    row += 2
    notes = [
        "Reading the trade-off:",
        "  - If Foundry < per-seat: per-token path is cheaper at current usage; revisit at adoption inflection.",
        "  - If per-seat < Foundry: M365 Copilot is the right entry point; expand to Foundry agents for heavy reasoning only.",
        "  - Crossover usually lies between 10-25 q/u/d depending on input-token size and model mix.",
        "Important: M365 Copilot bundles M365 surface integration value not captured in token economics; assess qualitatively.",
        "Cross-references: Objection 1.3 (per-seat doesn't pencil), Objection 4.6 (cost overrun), VBD D3 (FinOps for AI).",
    ]
    for n in notes:
        ws.cell(row=row, column=1, value=n).font = BODY_FONT
        ws.cell(row=row, column=1).alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=5)
        row += 1
    set_widths(ws, [44, 18, 18, 18, 50])


def build_waf(wb: Workbook) -> None:
    ws = wb.create_sheet("7. WAF binding")
    headers = ["WAF Cost Optimisation principle", "How this calculator binds", "Owner"]
    rows = [
        ["Choose the right resources", "Model routing tab (3. Inputs rows 9-11) defaults to mini; routes 4o only for heavy reasoning", "Engineering lead"],
        ["Set up budgets and maintain cost constraints", "Annual ZAR figure (sheet 4) feeds Azure budget alert; recommended alert at 75/90/100%", "FinOps lead"],
        ["Dynamically allocate and de-allocate", "Cache-hit rate (3. Inputs row 12) drives semantic caching choice; fallback rate row 13 sizes Phi-3 capacity", "Engineering lead"],
        ["Optimise rates", "Pricing reference (sheet 2) editable; verify against Reservation / Commitment discounts before commit", "Procurement lead"],
        ["Monitor and report cost", "Log Analytics line on sheet 4 funds the monitoring estate; combine with Cost Mgmt + AI Studio metrics", "Operations lead"],
        ["Refine over time", "Quarterly attestation should re-run this workbook with refreshed inputs; drift > 15% triggers re-baseline", "FinOps lead + CSA"],
    ]
    add_title(ws, "Well-Architected Framework - Cost Optimisation pillar binding", len(headers))
    for c, h in enumerate(headers, start=1):
        ws.cell(row=2, column=c, value=h)
    style_header(ws, 2, len(headers))
    write_rows(ws, 3, rows, len(headers))
    set_widths(ws, [36, 60, 22])
    for r in range(3, 3 + len(rows)):
        ws.row_dimensions[r].height = 36


def main() -> None:
    wb = Workbook()
    build_readme(wb)
    build_pricing(wb)
    build_inputs(wb)
    build_forecast(wb)
    build_scenarios(wb)
    build_per_seat(wb)
    build_waf(wb)
    wb.save(str(OUT))
    print(f"Wrote {OUT.name} with {len(wb.sheetnames)} sheets: {wb.sheetnames}")


if __name__ == "__main__":
    main()
