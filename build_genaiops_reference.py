"""Generate AI-CoE-GenAIOps-Reference.docx from ai-coe-genaiops-reference.md content.

Companion Word artefact for issue #11 (productise VBD C13 beyond a workshop).
"""

from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = Path(__file__).parent / "AI-CoE-GenAIOps-Reference.docx"

BLUE = RGBColor(0x00, 0x67, 0xB8)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)


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
            r.font.color.rgb = NAVY; r.font.size = Pt(26)
        elif level == 1:
            r.font.color.rgb = BLUE; r.font.size = Pt(16)
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


def main() -> None:
    doc = Document()
    for s in doc.sections:
        s.left_margin = Cm(2); s.right_margin = Cm(2)
        s.top_margin = Cm(2); s.bottom_margin = Cm(2)

    H(doc, "AI CoE — GenAIOps & Agent-Ops Reference", 0)
    P(doc, "Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft", italic=True)
    P(doc, "Version 1.0 · 2026-06-03 · Companion to AI-CoE-VBD-Reference-Deck.pptx (VBD C13)", italic=True)

    H(doc, "1. Why this exists", 1)
    P(doc, "VBD C13 today reads as a workshop. Competitors lead with productised offerings — IBM watsonx Orchestrate, Salesforce Agentforce, ServiceNow Now Assist, Accenture Switchboard. Microsoft has the equivalent stack across all three surfaces (M365 Copilot, Copilot Studio, Foundry); the CoE pack now packages it as one named artefact: a registry + lifecycle gates + eval & telemetry blueprint grounded in shipping Microsoft products.")

    H(doc, "2. The agent inventory model — the registry", 1)
    P(doc, "Every agent in the customer estate is registered in a single inventory regardless of surface. You cannot govern, evaluate, or cost what you cannot enumerate.")
    T(doc, ["Inventory field", "Source", "Required"], [
        ["Agent ID", "Generated (GUID)", "Yes"],
        ["Display name", "Author", "Yes"],
        ["Surface", "M365 / Copilot Studio / Foundry / 3rd-party", "Yes"],
        ["Owner (named human)", "CoE charter", "Yes"],
        ["Sponsor (LOB)", "Use-case sign-off", "Yes"],
        ["Lifecycle stage", "Build / Eval / Pilot / Prod / Sunset", "Yes"],
        ["Models invoked", "Foundry catalog reference(s)", "Yes"],
        ["Data sources", "AI Search index, SharePoint label, Dataverse table, API", "Yes"],
        ["HITL gate", "Required: yes/no; if yes, queue identifier", "Yes"],
        ["RAI impact tier", "T1 limited / T2 augmented / T3 autonomous", "Yes"],
        ["Eval suite", "PromptFlow / Azure AI Evaluations run ID", "Yes"],
        ["Kill-switch", "Azure Policy assignment ID", "Yes"],
        ["Cost centre", "FinOps tag", "Yes"],
    ])
    P(doc, "Implementation: Dataverse table coe_AgentRegistry fronted by a Power App that CoE leads, sponsors, and CISOs read. The registry is the single source of truth that every other GenAIOps mechanism reads from.")

    H(doc, "3. Reference architecture — six layers", 1)
    T(doc, ["Layer", "Microsoft product", "Purpose"], [
        ["L1 Experience", "M365, Copilot Studio canvas, custom UI, embedded chat", "Where the human interacts with the agent"],
        ["L2 Orchestration & registry", "Copilot Studio, Foundry Agent Service, Semantic Kernel, Dataverse registry", "Which agent, which flow, which tool — tracked centrally"],
        ["L3 Reasoning", "Foundry model catalog (OpenAI, Anthropic, Llama, Mistral, Cohere, NVIDIA NIM, Hugging Face, Phi) + routing", "Model inference; routing chooses cost/latency-appropriate model"],
        ["L4 Grounding & memory", "AI Search, Cosmos DB vector, Graph connectors, Dataverse, Fabric OneLake", "Retrieval, structured grounding, short/long-term memory"],
        ["L5 Eval & telemetry", "PromptFlow, Azure AI Evaluations, App Insights, Log Analytics, Foundry tracing", "Continuous offline + online eval, drift detection, cost telemetry"],
        ["L6 Governance & safety", "Content Safety, Prompt Shields, Purview AI Hub, Defender for Cloud AI, Azure Policy kill-switch", "Pre/post filtering, audit, posture management, emergency disable"],
    ])
    P(doc, "Visual reference: docs/images/genaiops-reference-architecture.svg")

    H(doc, "4. Agent lifecycle gates", 1)
    P(doc, "Every agent traverses five gates. The four governance gates in AI-CoE-AI-Governance-Playbook.docx bind to these; the lifecycle gates are the technical execution view.")
    T(doc, ["Gate", "Owner", "Mandatory artefact", "Tool"], [
        ["G-Build", "Agent author", "Registry record + system-prompt + tool list, version-pinned", "GitHub + Dataverse"],
        ["G-Eval", "CoE eval lead", "Offline eval pack >= 50 reference cases; thresholds met", "PromptFlow + Azure AI Evaluations"],
        ["G-Release", "Customer CISO + business sponsor", "Pilot approval; kill-switch tested; HITL queue live; dashboards green", "Foundry deployment + Azure Policy"],
        ["G-Monitor", "Customer ops (run-time)", "Online eval weekly; drift report monthly; cost dashboard weekly; incident channel staffed", "App Insights + AI Hub + Sentinel"],
        ["G-Retire", "Agent owner", "Sunset notice + 30-day grace + user comms + cost-tag closeout", "Registry + Azure Policy disable"],
    ])
    P(doc, "Skipping a gate requires written sign-off from CoE lead + CISO logged in the registry.")

    H(doc, "5. Eval harness blueprint", 1)
    P(doc, "Offline (pre-release, per change):", bold=True)
    B(doc, "Reference set: >= 50 cases per agent; >= 200 for T2/T3 agents.")
    B(doc, "Scorers: groundedness, relevance, fluency, safety (Content Safety), task-success.")
    B(doc, "Threshold gating configured per agent in the registry; release blocked on failure.")
    B(doc, "Tooling: PromptFlow flows in GitHub; Azure AI Evaluations SDK run via Azure DevOps.")
    P(doc, "Online (continuous, per-sample):", bold=True)
    B(doc, "Sample rate 1-5% of production traffic, sampled on prompt category.")
    B(doc, "Scorers: groundedness, safety, user-feedback (thumbs / implicit), reviewer override.")
    B(doc, "Drift detector: weekly rolling-window; alert if any scorer drops > 5% vs trailing 30-day baseline.")
    B(doc, "Tooling: App Insights → Log Analytics → Workbook; Fabric export for trend analysis.")
    P(doc, "Reviewer feedback loop:", bold=True)
    B(doc, "Every HITL override captured (prompt, response, reason, reviewer ID).")
    B(doc, "Override pack auto-ingested into the next offline eval set monthly.")
    B(doc, "Closes the loop: reviewer pain becomes future eval coverage.")

    H(doc, "6. Telemetry & cost dashboards", 1)
    T(doc, ["Dashboard", "Audience", "KPIs"], [
        ["Agent operations", "CoE lead, ops team", "Latency p50/p95, error rate, throughput, deployment freshness"],
        ["Quality & safety", "CISO, RAI lead", "Eval-score trends, safety-block rate, drift alerts, HITL override rate"],
        ["Adoption & value", "Sponsor, LOB lead", "DAU/WAU/MAU, depth (turns/session), containment, satisfaction"],
        ["FinOps for AI", "FinOps lead, CoE lead", "$/query, $/user, model-mix economics, cache-hit %, routing efficiency (sources AI-CoE-AI-TCO-Calculator.xlsx)"],
    ])

    H(doc, "7. Drift, safety, cost monitoring — what triggers what", 1)
    T(doc, ["Signal", "Threshold (default)", "Owner", "Action"], [
        ["Safety block rate spike", "> 2x trailing 7-day avg", "RAI lead", "Investigate prompts; tune Content Safety; potentially hotfix system-prompt"],
        ["Groundedness drop", "> 5% vs 30-day baseline", "CoE eval lead", "Re-evaluate retrieval pipeline; check index freshness"],
        ["$/query rising", "> 15% vs 30-day baseline", "FinOps lead", "Inspect model mix, cache-hit, fallback rate"],
        ["HITL override rate up", "> 1.5x trailing 7-day", "Sponsor + eval lead", "Add to next eval set; iterate prompt or retrieval"],
        ["Kill-switch invoked", "Any", "CISO", "IR run-book; root-cause within 24h; gate review"],
    ])

    H(doc, "8. Sample repo layout (publishable canonical)", 1)
    P(doc, "/coe-genaiops-starter")
    for line in [
        "/infra/bicep/agent-runtime.bicep — Foundry + AI Search + Content Safety + Key Vault",
        "/infra/bicep/observability.bicep — App Insights + Log Analytics + Workbooks",
        "/infra/policy/kill-switch-initiative.json",
        "/agents/agent-template/ — system prompt, tool manifest, eval reference cases, PromptFlow YAML, registry record",
        "/ops/powerbi/ — agent-ops, quality-safety, adoption-value, finops-for-ai PBIX files",
        "/docs/ — incident, kill-switch, eval-failure run-books",
    ]:
        B(doc, line)
    P(doc, "The repo is not in this pack; this layout is the canonical reference for partners building under MAICPP and for customer build teams under VBD C13.")

    H(doc, "9. RACI", 1)
    T(doc, ["Activity", "CoE lead", "Agent author", "CISO", "RAI lead", "FinOps", "Sponsor"], [
        ["Register agent", "A", "R", "I", "I", "I", "C"],
        ["Run offline eval", "A", "R", "C", "C", "I", "I"],
        ["Approve release", "A", "C", "A", "C", "C", "A"],
        ["Operate (run)", "A", "R", "C", "C", "C", "I"],
        ["Quarterly drift review", "A", "C", "A", "R", "C", "C"],
        ["Retire", "A", "R", "I", "I", "C", "C"],
    ])

    H(doc, "10. Linked artefacts", 1)
    B(doc, "AI-CoE-VBD-Reference-Deck.pptx — C13 entry now points to this document.")
    B(doc, "AI-CoE-AI-Governance-Playbook.docx — four governance gates this lifecycle binds to.")
    B(doc, "AI-CoE-AI-Impact-Assessment.xlsx — risk tier and control selection drive registry fields.")
    B(doc, "AI-CoE-AI-TCO-Calculator.xlsx — FinOps-for-AI dashboard data source.")
    B(doc, "AI-CoE-Objection-Handling.pptx — objection 3.3 rebuttal anchors here.")
    B(doc, "ACC-5 Document Intelligence + Foundry Pattern — first agent pattern on this lifecycle.")

    H(doc, "11. What this document is NOT", 1)
    B(doc, "Not a replacement for Foundry, Copilot Studio, or M365 admin docs — those are authoritative.")
    B(doc, "Not a managed service: the CoE provides the pattern; customer or partner runs the registry.")
    B(doc, "Not pre-built code: the sample repo layout is canonical; the repo itself is customer-instantiated under MAICPP.")

    doc.save(str(OUT))
    print(f"Wrote {OUT.name}")


if __name__ == "__main__":
    main()
