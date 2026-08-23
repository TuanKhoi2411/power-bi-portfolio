# Build provenance for the three PBIP dashboards

## Source task

The Sales, Finance, and Marketing dashboards were developed in Codex task `019f8896-46eb-7fa1-88ac-a344a69e62e5`, titled `Build Power BI dashboard`.

This document records the actual creation workflow recovered from that task and its surviving workspace. The current PBIP/PBIR/TMDL files in this repository are the canonical implementation.

## Original workflow

1. Inspect a reference PBIX read-only.
2. Decode legacy `Report/Layout` as UTF-16LE and inspect registered theme resources.
3. Record the 1280×720 grid, header, navigation rail, slicers, KPI/card positions, chart zones, fonts, palette, border, radius, and shadow behavior.
4. Download three public datasets from UCI and SEC.
5. Build a combined PBIP/TMDL/PBIR proof of concept.
6. Fix PBIR page/visual folder IDs, page ordering, and `activePageName` until Power BI Desktop opened the project correctly.
7. Refresh the model and validate source row counts and representative measures.
8. Add base, ratio, movement, variance, quality, ranking, and display measures.
9. Improve date slicers, KPI composites, Top-N charts, page navigation, reset behavior, labels, and display units.
10. Split Sales, Finance, and Marketing into independent PBIP projects.
11. Add two domain-specific deep-dive pages to each project.
12. Apply visibly distinct themes and varied deep-dive layouts.
13. Save standalone PBIX files and build separate HTML management stories.

## Original build tooling recovered

The surviving workspace contains these build-stage files:

- `build_pbip.py` — generated the initial PBIP, TMDL, PBIR page, and visual structure.
- `apply_kpi_enhancements.py` — added KPI movement/delta treatment and supporting measure bindings.
- `apply_credit_risk_layouts.py` — varied deep-dive layouts using a reference dashboard's structural ideas.
- `apply_distinct_themes.py` — separated Sales, Finance, and Marketing visual identities.
- `extend_company_dashboards.py` — added Customer/Product, Profitability/Liquidity, and Audience/Campaign pages.
- `split_company_projects.py` — separated the combined proof of concept into three standalone PBIP projects.
- `FactSales.pq`, `FactFinance.pq`, `FactMarketing.pq` — standalone copies of the Power Query transformations.
- domain DAX scripts and canonical TMDL tables.

Those scripts targeted an intermediate combined workspace and contain historical paths/assumptions, so they are not treated as the current build interface. Their validated outputs have been preserved in the source-controlled PBIP/PBIR/TMDL artifacts. The current reproducible interface is each project's full creation prompt, exact Power Query export, exact DAX export, report specification, and QA package.

## Reference design DNA

The first build extracted an Ocean–Amber reference system with:

- 1280×720 canvas;
- dark header and left navigation/filter rail;
- five KPI cards with compact trends;
- three upper analysis visuals plus two wider lower visuals;
- Segoe UI;
- core colors `#209FBD`, `#FFB702`, `#FB8500`, `#8ECAE7`, `#023046`, `#252423`, `#717A90`, and `#EEF1F7`.

The current standalone dashboards later diverged intentionally: Sales uses a purple analytical direction, Finance uses emerald/teal with amber, and Marketing uses navy/purple/coral/mint. The shared quality standard remains; the domains are not forced into one identical theme.

## Recorded source/model evidence

The creation workflow recorded these refresh results:

| Table/domain | Refreshed rows |
|---|---:|
| Sales | 541,909 |
| Apple Finance selected facts | 648 |
| Marketing | 41,188 |
| Combined Date table | 6,940 |

Representative values recorded during the original combined-model QA:

| Measure | Result |
|---|---:|
| Sales Net Sales | £9,747,747.93 |
| Sales Gross Sales | £10,666,684.54 |
| Sales Return Amount | £896,812.49 |
| Sales Orders | 20,728 |
| Marketing Conversion Rate | 11.2654% |
| Latest selected Apple quarterly Revenue | $109,417,000,000 |
| Latest selected Apple quarterly Gross Margin | 50.0562% |

Sales and Marketing values were independently re-read from the included source files during the documentation update. Finance values remain recorded creation-task evidence and must be revalidated after selection-logic changes.

## Current standalone implementation

| Project | Measures | Pages | Report visuals |
|---|---:|---:|---:|
| Sales | 74 | 3 | 84 |
| Marketing | 34 | 3 | 84 |
| Apple Finance | 90 | 3 | 84 |

Intermediate chat counts belong to earlier combined builds. Always use current TMDL and `qa/structural_validation.json` for the current artifact state.
