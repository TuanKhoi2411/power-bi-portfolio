# BI Dashboard Creation Prompt — Apple Inc. Financial Performance

## Objective

Create or rebuild a complete Power BI product named **Apple Inc. Financial Performance Dashboard** using official SEC EDGAR company facts.

Management question:

> Are Apple Inc.'s growth, margins, liquidity, and cost structure moving sustainably according to official filings?

The report must turn filing facts into traceable operating and balance-sheet analysis. It is not an investment recommendation and must not add forecasts, targets, market prices, or analyst estimates unless separately sourced and explicitly requested.

## Required inputs

- Raw source: `data/sec-aapl-companyfacts.json`
- PBIP: `dashboard/Apple_Inc_Financial_Performance_Dashboard.pbip`
- Report: `dashboard/Apple_Finance.Report/`
- Model: `dashboard/Apple_Finance.SemanticModel/`
- Power Query: `powerbi/PowerQuery_M.txt`
- DAX: `model/measures.dax`
- Measure catalog: `model/measure_catalog.csv`
- Data dictionary: `model/data_dictionary.md`
- Relationship map: `model/relationship_map.md`
- Report blueprint: `agent/REPORT_SPEC.md`

## Source and accounting rules

- Publisher: U.S. Securities and Exchange Commission, EDGAR Company Facts.
- Entity: Apple Inc.; preserve company and CIK identifiers.
- Grain: one reported concept value for a period/frame, unit, form, filing date, and accession.
- Selected model refresh recorded during creation: 648 normalized financial facts.
- Preserve `Concept`, `MetricClass`, `PeriodType`, `StartDate`, `EndDate`, fiscal labels, `Value`, `Form`, `FiledDate`, `Frame`, and `AccessionNumber`.
- Distinguish instant balance-sheet facts from duration income/cash-flow facts.
- Use deterministic rules for overlapping facts, restatements, annual/quarterly periods, units, and filing versions.
- Do not sum point-in-time balance values or combine annual and quarterly flow facts without compatible period logic.
- Do not invent guidance, consensus estimates, valuation, target price, or future performance.

## Agent roles

1. **Manager/FP&A reviewer** — define operating questions and acceptance criteria.
2. **Financial-data analyst** — normalize XBRL facts, units, forms, periods, restatements, and reconciliation.
3. **Power BI specialist** — maintain M, TMDL, DAX, relationships, PBIR, and packaging.
4. **Accounting-integrity reviewer** — challenge instant/duration treatment, duplicate periods, ratios, and traceability.
5. **UI/UX reviewer** — preserve hierarchy, scale labels, filing context, and readable tables.
6. **QA reviewer** — execute structural, reconciliation, interaction, and Desktop validation.

## Required theme and layout

- Canvas: 1280×720.
- Distinct Finance theme: deep emerald/teal financial accent, amber comparison accent, dark executive header, clean white/soft-neutral cards.
- Five KPI cards with consistent USD scale and compact trend context.
- Four concise slicers for period/form/metric context as supported by the report.
- Use native visuals; avoid textbox/shape simulations.
- Preserve source traceability in detail views/tooltips.
- Avoid excessive narrative text and unused canvas space.
- Export clean report-canvas images without Power BI Desktop chrome.

## Required pages

### Page 01 — Apple Finance

Purpose: establish direction across growth, profit, margins, and balance-sheet context.

Required KPIs:

- Revenue
- Gross Profit
- Operating Income
- Net Income
- Gross Margin

Required analysis:

- latest financial metrics comparison;
- quarterly Revenue versus prior year;
- Assets, Liabilities, and Cash trend;
- quarterly margin trend;
- financial detail table with period and filing context.

### Page 02 — Profitability & Growth

Purpose: determine whether reported growth is translating into durable profitability.

Required analysis:

- Revenue and profit growth KPIs;
- Revenue, Gross Profit, Operating Income, and Net Income trend;
- Gross, operating, and net margin trend;
- cost-of-sales/operating-expense structure;
- detail by fiscal period/form/filed date.

### Page 03 — Balance & Liquidity

Purpose: assess assets, liabilities, cash, and liquidity resilience.

Required analysis:

- Assets, Liabilities, Cash, and supported ratio KPIs;
- point-in-time balance trends;
- cash and liability context;
- balance/liquidity driver visuals;
- traceable financial-fact detail table.

## Semantic-model requirements

- Imported tables: `FactFinance` and `DimDate`.
- Active relationship: `FactFinance[EndDate]` → `DimDate[Date]`.
- Current canonical measure count: **90**.
- Preserve fact metadata and the distinction between `PeriodType` values.
- Keep technical metric sort/category fields and deterministic metric selection logic.
- Preserve display folders, format strings, and table/column names unless a documented migration is required.
- Regenerate exports after TMDL changes:

```powershell
./scripts/export-model-documentation.ps1
```

## Required DAX families

Use exact definitions in `model/measures.dax`:

- Revenue, Cost of Sales, Gross Profit, Operating Expenses, Operating Income, Net Income;
- Assets, Liabilities, Cash and supported balance/liquidity metrics;
- Gross, operating, and net margins;
- latest-period metrics and deterministic prior-period/YoY comparisons;
- ratio/coverage measures;
- KPI display helpers.

Numeric measures must drive all charts, sorting, reconciliation, and conditional formatting. Formatted display measures are card text only.

## Power Query requirements

- Point `FactFinance` to the included SEC JSON.
- Normalize companyfacts concepts/units into the documented fact fields.
- Preserve filing metadata and selected fact traceability.
- Document concept mapping and any exclusions.
- If multiple facts represent the same metric/period, apply a deterministic filing/accession rule and record it.
- Any change to selection logic must include before/after fact counts and reconciliation impact.

## Interaction requirements

- Navigation reaches all three pages.
- Reset restores default period/form/metric context.
- Filters must not combine incompatible instant/duration or annual/quarterly contexts.
- Cross-highlighting and detail tables preserve selected period and filing traceability.
- Scales, units, signs, margins, and fiscal labels remain consistent.

## QA and acceptance

1. Run structural validation and confirm `qa/structural_validation.json` passes.
2. Refresh the SEC source and record normalized fact count.
3. Validate selected concepts, units, forms, periods, duplicates/restatements, and filing versions.
4. Reconcile Revenue, Gross Profit, Operating Income, Net Income, Assets, Liabilities, Cash, and margins for representative periods.
5. Confirm all 90 measures load without DAX errors.
6. Test all pages, slicers, navigation, reset, cross-filtering, and detail traceability.
7. Save PBIP and PBIX, close/reopen PBIX, and repeat a smoke test.
8. Disclose that the report is analytical portfolio work, not investment advice.

## Final deliverables

- Updated PBIP and `Apple_Inc_Financial_Performance_Dashboard.pbix`.
- Current DAX, catalog, dictionary, relationship/model notes, and Power Query.
- Structural validation JSON and updated QA notes.
- Sharp report-canvas screenshots when visuals change.

## Copy-ready instruction

> Work on `projects/finance-performance`. Follow repository/project `AGENTS.md` and read `BI_Dashboard_Creation_Prompt.md`, `agent/`, `model/`, `powerbi/`, and `qa/`. Use only the included Apple SEC EDGAR companyfacts JSON and canonical PBIP/TMDL. Preserve instant-versus-duration and filing traceability, the three-page 1280×720 Finance journey, and exact DAX/M logic unless intentionally revised. Run structural, accounting/reconciliation, interaction, refresh, save, and PBIX reopen QA. Do not add estimates or investment recommendations.
