"""Generate AI-CoE-Why-A-CoE.docx from ai-coe-why-a-coe-pain-points.md.

Customer-facing C-suite leave-behind that names all 13 buyer pain points an AI CoE
exists to solve, with the CoE response and proof artefact for each.

Author: Yuri Baijnath -- CSU Cloud & AI Lead (South Africa), Microsoft.
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).parent / "AI-CoE-Why-A-CoE.docx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
PURPLE = RGBColor(0x74, 0x2A, 0x9B)


def shade(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def H(doc, text, level):
    p = doc.add_heading(text, level=level)
    for r in p.runs:
        r.font.name = "Segoe UI"
        if level == 0:
            r.font.color.rgb = NAVY; r.font.size = Pt(24)
        elif level == 1:
            r.font.color.rgb = BLUE; r.font.size = Pt(15)
        elif level == 2:
            r.font.color.rgb = PURPLE; r.font.size = Pt(13)
        else:
            r.font.color.rgb = NAVY; r.font.size = Pt(12)


def P(doc, text, italic=False, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = "Segoe UI"; r.font.size = Pt(11)
    r.italic = italic; r.bold = bold


def B(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.font.name = "Segoe UI"; r.font.size = Pt(11)


def T(doc, headers, rows):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tbl.style = "Light Grid Accent 1"
    hdr = tbl.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        shade(hdr[i], "0067B8")
        for para in hdr[i].paragraphs:
            for r in para.runs:
                r.font.name = "Segoe UI"; r.font.size = Pt(10); r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for r_i, row in enumerate(rows, start=1):
        for c_i, val in enumerate(row):
            cell = tbl.rows[r_i].cells[c_i]
            cell.text = str(val)
            for para in cell.paragraphs:
                for r in para.runs:
                    r.font.name = "Segoe UI"; r.font.size = Pt(10)


def pain(doc, n, title, hear, hurts, response, artefact):
    H(doc, f"Pain {n} — {title}", 2)
    P(doc, "What we hear:", bold=True)
    P(doc, f"\u201c{hear}\u201d", italic=True)
    P(doc, "Why it hurts:", bold=True)
    P(doc, hurts)
    P(doc, "CoE response:", bold=True)
    P(doc, response)
    P(doc, "Proof artefact:", bold=True)
    P(doc, artefact)


def main() -> None:
    doc = Document()
    for s in doc.sections:
        s.left_margin = Cm(2); s.right_margin = Cm(2)
        s.top_margin = Cm(2); s.bottom_margin = Cm(2)

    H(doc, "Why an AI CoE — the 13 buyer pain points", 0)
    P(doc, "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft", italic=True)
    P(doc, "Version 1.0 · 2026-06-03 · Audience: C-suite (CEO, CFO, CIO, CISO, CDO, COO) — first conversation", italic=True)

    H(doc, "Lead message", 1)
    P(doc, "You do not have an AI problem. You have thirteen AI problems, and they compound. Most enterprises in South Africa have addressed two or three in isolation — a pilot here, a policy there, a Copilot deployment somewhere else — and discovered that the unaddressed ten quietly cancel the value of the three that worked.")
    P(doc, "An AI Centre of Excellence is the operating capability that collapses all thirteen into a single delivery, governance, and measurement system. It is not a team, a tool, or a slide; it is the set of rituals, controls, and reusable patterns that turn AI from a portfolio of disconnected bets into a compounding capability.")
    P(doc, "This document names the thirteen pain points, in the language we hear them in the room, and points to the artefact in the Microsoft AI CoE pack that closes each one.")

    H(doc, "The 13 pain points, grouped", 1)
    T(doc, ["Bucket", "#", "Pillar", "Owner role"], [
        ["Strategy & ROI", "1–4", "Pillar 1 — Business Strategy", "CEO / CFO"],
        ["People & Adoption", "5–8", "Pillar 2 — Org & Culture", "CHRO / COO"],
        ["Tech & Data", "9–11", "Pillars 3 & 4 — AI Strategy + Tech & Data", "CIO / CDO"],
        ["Governance & Risk", "12–13", "Pillar 5 — Governance & Security", "CISO / Risk"],
    ])
    P(doc, "Pillar +1 (Co-sell & Partner) shows up in how the CoE is delivered, not as a standalone pain point.", italic=True)

    # Bucket 1
    H(doc, "Bucket 1 — Strategy & ROI (CEO / CFO)", 1)
    pain(doc, 1, "Pilot purgatory",
         "We've run twelve proofs-of-concept. None of them are in production. Every executive review starts with the same slide.",
         "Cost without compounding. Pilot budgets recur annually; benefits do not. Executive patience expires before the third refresh cycle.",
         "A funded path from pilot to platform — the F1–F10 factory pattern, with a Tier-2 (mid) and Tier-3 (frontier) router that turns pilots into reusable building blocks instead of disposable demos.",
         "AI-CoE-Pitch-Deck-Respined.pptx slides 4–6 (moat grid, factory) · AI-CoE-VBD-Reference-Deck.pptx.")
    pain(doc, 2, "ROI is unproven",
         "Show me the business case. I cannot defend per-seat Copilot to the CFO without a number.",
         "Without a defensible ROI model, AI competes against every other capex line on instinct, and instinct loses to a spreadsheet.",
         "A unit-economics TCO model the CFO can re-run with their own inputs — not a vendor slide. Industry-anchored $1 : $3–$5 benchmark, with assumptions visible.",
         "AI-CoE-AI-TCO-Calculator.xlsx (7-sheet model) · Pitch-Deck-Respined slide 9 (ATO economics).")
    pain(doc, 3, "Build-vs-buy paralysis",
         "Do we build this internally with our team, buy it from an ISV, or wait for Microsoft to ship it as a feature?",
         "The wrong answer costs 18 months. Build-internally underestimates eval + governance + change. Buy-from-ISV creates a fourth surface to govern. Wait-for-feature misses the window.",
         "A repeatable decision frame — Build (factory pattern, sovereign data, durable IP) · Buy (commodity workflow, vendor owns the eval) · Wait (feature is on a known roadmap inside 2 quarters). The CoE owns the call, not the LOB.",
         "AI-CoE-Objection-Handling.pptx Pillar 1 · AI-CoE-Model-Choice-OnePager.docx.")
    pain(doc, 4, "Wait-and-see",
         "The tech is moving too fast. We'll wait for it to stabilise before we invest.",
         "Waiting is a position, not a neutral. Competitors who started in 2024 now have proprietary evals, change muscle, and reusable patterns. The cost of catching up in 2027 exceeds the cost of starting in 2026.",
         "A 90-day landing pattern that produces evidence, not infrastructure — one funded VBD, one platform pattern, one governance attestation. The CoE makes \u201cwait\u201d the more expensive option after the first quarterly review.",
         "AI-CoE-Horizon-Assessment.xlsx · Pitch-Deck-Respined slides 14–16 (90-day landing).")

    # Bucket 2
    H(doc, "Bucket 2 — People & Adoption (CHRO / COO)", 1)
    pain(doc, 5, "Shadow AI sprawl",
         "My CISO tells me 40% of our knowledge workers are already pasting customer data into ChatGPT. We have no visibility and no policy that holds.",
         "POPIA exposure, IP leakage, and a governance position that is unenforceable by the time you write it.",
         "Sanctioned alternatives (M365 Copilot, Foundry-hosted chat under tenant controls), Purview DLP on consumer-AI endpoints, and a Champions network that pulls usage onto the sanctioned surface faster than policy pushes it off the unsanctioned one.",
         "AI-CoE-Sovereign-AI-RSA-Report.md · AI-CoE-Change-Readiness-Workbook.xlsx (Champions ratio 1:25).")
    pain(doc, 6, "Skills gap",
         "We don't have prompt engineers. We don't have ML engineers. We don't have AI product managers. Where do we hire from?",
         "The local talent market for senior AI roles is thin. Building inside takes 9–12 months. Outside hires turn over in 14.",
         "A role ladder the CoE itself enables — prompt engineer (from BAs in 6 weeks), Copilot Studio maker (from power users in 4 weeks), Foundry engineer (from senior dev in 12 weeks). Microsoft Learn paths, Champions kit, and partner co-delivery cover the gap.",
         "AI-CoE-Change-Management-Methodology.md · AI-CoE-How-To-Use.pptx.")
    pain(doc, 7, "Change fatigue",
         "We just rolled out SAP S/4, we're mid-migration on the data platform, and the COO told finance there are no more transformations this year.",
         "Every prior transformation makes the next one harder. AI initiatives launched into change-fatigued organisations land at 12% adoption, not 60%, and the CFO writes off the licences.",
         "ADKAR-based readiness scoring before broad-launch, with Green / Amber / Red gates. Amber means a 30-day pre-launch plan; Red means do not broad-launch — run a 90-day fixture programme first. The CoE protects adoption by refusing to launch into a Red.",
         "AI-CoE-Change-Readiness-Workbook.xlsx · AI-CoE-Change-Management-Methodology.md.")
    pain(doc, 8, "Adoption stall",
         "We bought 8,000 Copilot licences. Six months in, 1,400 are active and the CFO wants to cancel the renewal.",
         "Licence cost is fixed; value scales with active use. A 17% activation rate destroys the business case on the next renewal.",
         "A 5-KPI measurement scaffold — three activity-leading (active users, prompts/user, scenario coverage), two outcome-lagging (hours-saved per role, quality lift). Weekly Champions ritual closes the loop between usage data and use-case backlog.",
         "AI-CoE-Change-Management-Methodology.md · AI-CoE-Operating-Playbook.docx.")

    # Bucket 3
    H(doc, "Bucket 3 — Tech & Data (CIO / CDO)", 1)
    pain(doc, 9, "Data is not ready",
         "Our data is in 47 systems, nobody trusts the customer master, and the data lake is read-only because the lineage is broken. AI on top of that is fiction.",
         "AI quality is a function of data quality. Bad inputs produce hallucinations that the business correctly does not trust, which kills adoption faster than any change-management failure.",
         "A data-readiness gate inside F1–F10 — every use case is scored Green / Amber / Red on data fitness before build starts. Fabric + Purview as the platform pattern; the CoE refuses to build on data graded Red.",
         "AI-CoE-GenAIOps-Reference.docx (L4 Data layer) · AI-CoE-VBD-Reference-Deck.pptx (data-foundation VBDs).")
    pain(doc, 10, "Integration debt",
         "The use case is obvious — but it needs to call SAP, write to ServiceNow, and read from the mainframe. The integration cost is bigger than the AI cost.",
         "AI value lives in workflows, not chat. Workflows live in systems-of-record built in 2008. The integration line item silently doubles the project.",
         "Copilot Studio + Logic Apps + the agent registry pattern — connectors for SAP, ServiceNow, Dynamics, mainframe, and 1,400+ pre-built endpoints. The CoE owns a reusable integration library so the second use case pays a fraction of the first one's tax.",
         "AI-CoE-VBD-Reference-Deck.pptx (Studio agents) · Pitch-Deck-Respined slide 10.")
    pain(doc, 11, "Surface confusion",
         "M365 Copilot, Copilot Studio, Azure AI Foundry — what's the difference and which one do we buy?",
         "The wrong surface choice produces the right capability in the wrong place. Six months of build on Foundry that should have been a Studio agent. A Studio agent that needs the data plane of Foundry. The cost is rework.",
         "A single decision frame — M365 Copilot for productivity at the desktop, Copilot Studio for low-code agents on workflows, Azure AI Foundry for custom build with full model choice and data-plane control. The CoE makes the call per use case.",
         "Pitch-Deck-Respined slides 9–11 (three-surface moat grid) · AI-CoE-Model-Choice-OnePager.docx.")

    # Bucket 4
    H(doc, "Bucket 4 — Governance & Risk (CISO / Risk)", 1)
    pain(doc, 12, "Governance debt",
         "We have a Responsible AI policy. It's in a SharePoint deck. The regulator asked us to demonstrate it in controls and we couldn't.",
         "Policy without controls is slideware. AGSA, SARB, FSCA, and the Information Regulator increasingly ask for evidence, not assertion. The quarterly attestation gap is now a regulator-graded risk.",
         "Five lifecycle gates — G-Build · G-Eval · G-Release · G-Monitor · G-Retire — wired into Foundry, Purview, and Azure AI Content Safety. Every agent in production has an evidence trail the regulator can sample. Quarterly attestation is a report, not a project.",
         "AI-CoE-Responsible-AI-Governance.md · AI-CoE-GenAIOps-Reference.docx (L6) · AI-CoE-Eskom-Executive-Briefing.pptx.")
    pain(doc, 13, "Sovereignty / POPIA / data residency",
         "The data must stay in South Africa. The CISO needs to demonstrate it. And the model weights must not leak to a US-hosted endpoint we don't control.",
         "Sovereignty is no longer an objection — it is a procurement gate. SA North and SA West, Foundry-hosted OpenAI in-region, Phi and Mistral as sovereign-friendly defaults, and Azure Local for the hardest cases all need to be on the table from slide one.",
         "A three-tier sovereignty pattern — Microsoft-managed posture in SA region (default), customer-controlled weights on AKS (sensitive), on-premise via Azure Local (extreme). The CoE specifies the tier per workload and produces the residency evidence.",
         "AI-CoE-Sovereign-AI-RSA-Report.md · Pitch-Deck-Respined slide 12 · AI-CoE-Eskom-Executive-Briefing.pptx.")

    H(doc, "The compounding argument", 1)
    P(doc, "Each pain point in isolation is solvable. Many enterprises have solved two or three.")
    P(doc, "The reason an AI CoE exists is that the combination of all thirteen — running concurrently, across business, technology, and governance — exceeds the operating capacity of any line-of-business team, any single platform team, and any one vendor relationship.")
    P(doc, "The CoE is the seam. It owns the rituals (Pillar 1–2), the patterns (Pillar 3–4), the controls (Pillar 5), and the partner motion (Pillar +1). Stand it up once, and the marginal cost of the fourteenth use case approaches zero.")
    P(doc, "That is the offer.", bold=True)

    H(doc, "How to use this document", 1)
    T(doc, ["You are…", "Read…"], [
        ["Preparing a first executive meeting", "The whole document, in order — it sequences the conversation."],
        ["Briefing a single C-suite role", "The bucket for that role + the proof-artefact links."],
        ["Responding to a specific objection", "Find the pain point that contains it; hand the prospect the linked artefact."],
        ["Building the business case", "Pain 2 → TCO Calculator. Pain 8 → 5-KPI scaffold. Pain 12 → attestation evidence."],
    ])

    doc.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
