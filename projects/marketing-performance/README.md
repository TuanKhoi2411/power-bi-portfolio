# Portuguese Bank — Marketing Performance

Power BI portfolio project for audience segmentation, campaign effectiveness, and term-deposit subscription analysis.

## Review in 60 seconds

| Question | Answer |
|---|---|
| Management question | Which audiences, channels, and campaign conditions are associated with stronger subscription conversion? |
| What I built | A three-page Power BI report, semantic model, and a 12-slide management story. |
| Evidence | 41,188 direct-marketing contacts from the UCI Bank Marketing dataset. |
| Status | PBIX, PBIP, source CSV, and HTML story are published. |

## Goal

Build a marketing review product that helps decision-makers:

- Establish campaign scale and subscription conversion.
- Compare audience characteristics and response patterns.
- Identify campaign conditions associated with stronger outcomes.
- Separate descriptive evidence from causal claims.

## Dashboard pages

| Page | Decision lens |
|---|---|
| Bank Marketing | Establish overall campaign and conversion performance. |
| Audience Segmentation | Compare response patterns across customer groups. |
| Campaign Effectiveness | Investigate contact and campaign conditions linked to conversion. |

## Key portfolio signals

- Three report pages at 1280 × 720.
- `FactMarketing` semantic model.
- 34 authored measures.
- 41,188 source-backed marketing contacts.
- Distinct Marketing theme and decision flow.

## Main artifacts

| Artifact | Use |
|---|---|
| [`Portuguese_Bank_Marketing_Performance_Dashboard.pbix`](./Portuguese_Bank_Marketing_Performance_Dashboard.pbix) | Packaged Power BI report for immediate review in Power BI Desktop. |
| [`dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`](./dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip) | Entry point for the complete PBIP report and semantic model. |
| [`Portuguese_Bank_Marketing_Performance_Interactive.html`](./Portuguese_Bank_Marketing_Performance_Interactive.html) | Standalone 12-slide management story; download and open in Chrome or Edge. |
| [`data/bank-additional-full.csv`](./data/bank-additional-full.csv) | Raw public source data used by the model. |

## Data and model

- Publisher: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing).
- Grain: one direct-marketing contact per record.
- Model: `FactMarketing` with explicit authored measures.
- Before refreshing on another computer, replace `SourcePath` in `FactMarketing.tmdl` with the absolute path to the included CSV.

## How to review

1. Open the HTML story for the decision narrative and key caveats.
2. Open the PBIX for immediate dashboard interaction in Power BI Desktop.
3. For model inspection, download the complete `dashboard/` folder before opening the PBIP file.
4. Start with overall conversion, then compare segments, and finish with campaign conditions.

HTML controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## QA status and limits

- The PBIP contains the project pointer, report definition, semantic model, three pages, and a valid active-page reference.
- The PBIP was opened in Power BI Desktop with its visuals and data model loaded, then exported to the published PBIX.
- The HTML story contains 12 slides, embedded visuals, and keyboard navigation.
- A separate post-export reopen of the PBIX was not performed during this update.
- The model shows historical associations; it does not prove that a contact strategy caused conversion.

## Portfolio talking points

- Demonstrates audience segmentation without overstating causality.
- Connects campaign KPIs to drill-down questions and management interpretation.
- Keeps the raw public source, model, report, and narrative artifact together.

## Agent build package

To rebuild or extend this dashboard with an agent, start with [project instructions](./AGENTS.md), then use the [copy-ready build prompt](./agent/BUILD_PROMPT.md), [data/model contract](./agent/DATA_MODEL_SPEC.md), [report blueprint](./agent/REPORT_SPEC.md), and [build/QA checklist](./agent/BUILD_AND_QA.md).
