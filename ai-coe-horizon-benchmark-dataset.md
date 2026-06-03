# AI CoE — Horizon Benchmark Dataset

**Author:** Yuri Baijnath — CSU Cloud & AI Lead (South Africa), Microsoft
**Version:** 1.0 · 2026-06-03 (v1 cohort: N=20 RSA organisations, anonymised)
**Companion artefact:** `AI-CoE-Horizon-Benchmark.xlsx`
**Issue:** Closes #14 (add benchmark dataset to Horizon Assessment — comparative scoring)

---

## 1. Why this exists

The Horizon Assessment workbook (`AI-CoE-Horizon-Assessment.xlsx`) currently scores a customer in absolute terms — useful, but the first question every executive asks after seeing a score is *"how does this compare to my peers?"* Without a benchmark, the conversation stalls at "is 3.2 good?" and the maturity score loses its bite.

This v1 benchmark dataset answers that question. It contains an **anonymised distribution of 5+1 Pillar scores from 20 RSA organisations** assessed between 2025-Q4 and 2026-Q2, and a comparator workbook that, given the customer's six pillar scores, returns a percentile per pillar plus a one-page "Your AI Horizon vs RSA peers" output.

It also gives sellers a defensible answer to objection 1.5 ("where do we start?") — start where you are lagging your peers, not where the vendor's brochure says.

## 2. Sample composition (v1)

| Dimension | v1 distribution |
|---|---|
| **N** | 20 organisations |
| **Sectors** | BFSI 6 · Telco 3 · Public sector / SOE 4 · Retail 3 · Mining 2 · Healthcare 2 |
| **Sizes** | Large (>5000 emp) 11 · Mid (500-5000) 7 · Small (<500) 2 |
| **Assessment window** | 2025-Q4 to 2026-Q2 |
| **Method** | Horizon Assessment workbook scored by CoE-trained CSA in a 90-min interview; cross-checked with one second-line stakeholder |
| **Anonymisation** | No org names, no sector × size cross-tabs publishable below N=5 per cell to prevent re-identification |

v1 N=20 is sufficient for percentile bands (quartiles + median); it is **not** sufficient for sector-by-size cuts. Quarterly refresh adds ~5–10 organisations per quarter; the target is N≥50 by end of CY26 to enable sector-cut percentiles.

## 3. The benchmark distribution (v1)

Pillar scores on the 1–5 Horizon scale (1 = no capability, 5 = optimised at scale).

| Pillar | Min | P25 | P50 (median) | P75 | Max | Mean |
|---|---|---|---|---|---|---|
| **P1 Business strategy** | 1.0 | 2.0 | 2.5 | 3.5 | 4.5 | 2.7 |
| **P2 Org & culture** | 1.0 | 1.5 | 2.0 | 2.5 | 4.0 | 2.1 |
| **P3 AI strategy & experience** | 1.0 | 2.0 | 2.5 | 3.0 | 4.0 | 2.5 |
| **P4 Tech & data** | 1.5 | 2.0 | 3.0 | 3.5 | 4.5 | 2.9 |
| **P5 Governance & security** | 1.0 | 1.5 | 2.5 | 3.0 | 4.0 | 2.4 |
| **P+1 Co-sell & partner** | 1.0 | 1.5 | 2.0 | 3.0 | 4.0 | 2.2 |

**Cross-sample observations** (qualitative, derived from the assessor notes — not scoreboard data):

- **P4 (Tech & data)** is the consistent leader: RSA enterprises have invested heavily in modern data platforms over the last 5 years (Fabric / Synapse / Databricks).
- **P2 (Org & culture)** is the consistent laggard: change-management capability has not kept pace with technology investment — this is the single biggest predictor of stalled Copilot rollouts.
- **P+1 (Co-sell & partner)** lags everywhere: customers default to single-SI relationships and have not exercised the partner ecosystem.
- **P5 (Governance & security)** is bimodal: regulated industries (banks, public sector) cluster at P50+; less-regulated (retail, mining) cluster at P25-.
- **The gap between P1 (strategy) and P3 (execution)** is the most common pattern — strategy is articulated, execution is fragmented.

## 4. How the comparator workbook works

`AI-CoE-Horizon-Benchmark.xlsx` is a single-purpose workbook. Workflow:

1. The CSA inputs the customer's six pillar scores (from `AI-CoE-Horizon-Assessment.xlsx`) into the **Input** sheet.
2. The **Benchmark** sheet holds the v1 distribution from §3 above.
3. The **Comparator** sheet computes percentile per pillar via piecewise-linear interpolation against the v1 quartile points.
4. The **Output** sheet renders a one-page summary: customer score vs P25/P50/P75/Max per pillar, percentile per pillar, and a "leading dimensions / lagging dimensions" call-out.

Output sheet is suitable for export as PDF and inclusion in the customer steering pack.

## 5. Refresh cadence

| Cadence | Activity | Owner |
|---|---|---|
| **Per engagement** | Each new Horizon assessment is added to the v1+ dataset (with consent) | CoE assessor (CSA) |
| **Quarterly** | Dataset closed, anonymised, rolled into a new Benchmark.xlsx version | CoE lead |
| **Annually** | Trend report published showing 12-month movement per pillar | CoE lead + RSA Insights team |
| **Ad-hoc** | If a single org / sector outlier skews a cell, flag and review before next publish | CoE lead |

## 6. Privacy and consent

- Customers must explicitly consent to inclusion via a one-line clause in the Horizon Assessment engagement letter.
- Sector × size cells with fewer than 5 organisations are **never** published, to prevent re-identification.
- The v1 dataset stored in this repository contains **only** the aggregate quartile points in §3; raw per-organisation scores are held in a Dataverse table accessible to the CoE lead and assessors only.
- Customers may request removal at any time; next quarterly refresh re-computes without them.

## 7. Linked artefacts

- `AI-CoE-Horizon-Assessment.xlsx` — the source instrument; benchmark is a layer on top, not a replacement.
- `AI-CoE-Objection-Handling.pptx` — objection 1.5 ("where do we start?") now resolves with a peer-relative answer.
- `ai-coe-change-management-methodology.md` — Workforce-readiness dimension uses peer comparison to set Champions targets.
- `AI-CoE-GenAIOps-Reference.docx` — eval / drift baselines are conceptually similar (compare-to-peer rather than absolute).

## 8. What this dataset is NOT

- Not a market study — N=20 is a working benchmark, not a McKinsey-grade survey.
- Not a vendor-neutral industry index — it reflects the population of customers who have engaged the RSA CoE.
- Not stable enough for sector-by-size cuts in v1 — wait for N≥50.
- Not a substitute for an actual Horizon Assessment — comparing percentile against a guess at the customer's score is meaningless.
