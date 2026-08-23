# BI Dashboard Creation Prompt — UK Online Retail Sales Performance

## Objective

Create or rebuild a complete Power BI product named **UK Online Retail Sales Performance Dashboard**. It must behave like a decision-ready Sales management report, not a generic chart gallery.

Management question:

> Where is growth coming from, which customers and products matter, and how do returns affect sales quality?

The finished product must connect commercial scale, customer concentration, product contribution, geography, and return leakage using only the included public UCI Online Retail data.

## Required inputs

- Raw source: `data/Online Retail.xlsx`
- PBIP entry point: `dashboard/UK_Online_Retail_Sales_Performance_Dashboard.pbip`
- Canonical report: `dashboard/UK_Online_Retail_Sales.Report/`
- Canonical model: `dashboard/UK_Online_Retail_Sales.SemanticModel/`
- Power Query: `powerbi/PowerQuery_M.txt`
- Full DAX inventory: `model/measures.dax`
- Measure catalog: `model/measure_catalog.csv`
- Data dictionary: `model/data_dictionary.md`
- Relationship map: `model/relationship_map.md`
- Report blueprint: `agent/REPORT_SPEC.md`

## Source and business rules

- Publisher: UCI Machine Learning Repository, Online Retail.
- Grain: one invoice transaction line.
- Source row count recorded during the creation task: 541,909 data rows.
- Coverage: 1 December 2010–9 December 2011.
- Preserve invoice, product, quantity, date, price, customer, and country fields.
- Classify an invoice as cancellation/return when the invoice begins with `C` or quantity is negative.
- Do not silently discard unknown customers, missing descriptions, returns, cancellations, or non-positive prices.
- Keep Gross Sales, Return Amount, and Net Sales distinct.
- Do not invent cost, margin, marketing spend, targets, budget, or forecast fields that are absent from the dataset.

## Agent roles

1. **Manager agent** — protect scope, management question, acceptance criteria, and portfolio relevance.
2. **Data analyst agent** — profile source quality, reconcile measures, and challenge misleading aggregations.
3. **Power BI specialist** — maintain Power Query, TMDL, DAX, relationships, PBIR visual bindings, and PBIX packaging.
4. **UI/UX reviewer** — enforce the 1280×720 grid, hierarchy, navigation, contrast, labels, and screenshot quality.
5. **QA reviewer** — run structural validation, refresh/reconciliation checks, interaction checks, and Desktop reopen verification.

## Required theme and layout

- Canvas: 1280×720.
- White/soft-neutral panels on a light canvas.
- Dark navy text, purple analytical accent, coral return/leakage accent, teal action/navigation state.
- Five KPI cards across the upper analytical area with compact supporting deltas/sparklines.
- Four concise slicers; avoid duplicated field labels.
- Left navigation/filter rail or the existing compact navigation treatment must remain consistent across pages.
- Use restrained borders and shadows; do not place grey fill directly behind KPI values.
- Use native Power BI visuals. Textboxes are for page titles/short labels, not for simulating charts.
- Fill the canvas with decision-useful visuals while preserving breathing room.
- Portfolio screenshots must show the report canvas only, not Desktop ribbon, Filters, Build, or Data panes.

## Required pages

### Page 01 — UK Retail Sales

Purpose: establish commercial scale, trend, geography, product concentration, and return quality.

Required KPIs:

- Net Sales
- Gross Sales
- Orders
- Units Sold
- Return Rate

Required analysis:

- Top 5 Countries by Net Sales
- Top 5 Products by Merchandise Net Sales
- Sales mix by transaction type
- Monthly Net Sales versus prior-year context where valid
- Country performance detail table

Required slicers:

- Date range
- Country
- Product
- Transaction type

### Page 02 — Customer Insights

Purpose: identify valuable customers, repeat behavior, concentration, and data-coverage limitations.

Required KPIs:

- Customer Identified Net Sales
- Customers
- Net Sales per Customer
- Orders per Customer
- Repeat Customer Rate

Required analysis:

- Top customers by Net Sales
- Repeat versus one-time customer comparison
- Customer concentration/ranking
- Customer trend and customer detail table
- Customer identification coverage disclosure

### Page 03 — Product & Returns

Purpose: separate merchandise demand from return/cancellation leakage.

Required KPIs:

- Merchandise Net Sales
- Return Amount
- Returned Units
- Active Products
- Return Rate

Required analysis:

- Monthly Net Sales and Return Amount
- Gross Sales and Returns by transaction type
- Top 5 products by merchandise sales
- Top 5 products by return amount
- Product performance detail table

## Semantic-model requirements

- Import-mode tables: `FactSales` and `DimDate`.
- Active relationship: `FactSales[SalesDate]` → `DimDate[Date]`.
- Keep the Date table contiguous and preserve month/year sort fields.
- Technical columns should not replace explicit measures in visuals.
- Preserve display folders, format strings, data types, sort-by behavior, and existing table/column names unless a migration is explicitly requested.
- Current canonical measure count: **74**.
- Regenerate model documentation after TMDL changes:

```powershell
./scripts/export-model-documentation.ps1
```

## Required DAX families

Use the exact formulas in `model/measures.dax`. Required families include:

- base: Gross Sales, Return Amount, Net Sales, Units Sold, Returned Units, Orders, Customers;
- efficiency: Average Order Value, Average Selling Price, Net Sales per Customer, Orders per Customer;
- quality: Return Rate, Gross to Net Rate, customer data coverage;
- movement: previous month, MoM, previous year, YoY, percentage-point variance;
- ranking: country, product, customer, Top 5/Top 10, merchandise-only logic;
- display: KPI text measures used only for presentation.

Never use formatted KPI text measures for aggregation, chart axes, conditional calculations, or numeric sorting.

## Power Query requirements

- Update `SourcePath` in `FactSales` to the repository workbook before refresh.
- Promote headers and enforce the documented data types using the `en-GB` locale.
- Trim text and explicitly label unknown product/customer values.
- Create `SalesLineId`, `SalesDate`, `IsCancellation`, `TransactionType`, `NetSalesAmount`, `GrossSalesAmount`, `ReturnAmount`, `UnitsSold`, `ReturnedUnits`, and `HasValidPrice` exactly as documented in `powerbi/PowerQuery_M.txt`.
- Any changed transformation must be documented with its effect on row count and reconciliation totals.

## Interaction requirements

- Page navigation reaches all three pages.
- Reset action restores the documented default filter state.
- Slicers affect all intended visuals.
- Cross-highlighting must not create misleading denominators.
- Top-N visuals must use numeric rank measures and descending sorting.
- Long product names must remain readable or be exposed through tooltips/detail tables.

## QA and acceptance

Before handoff:

1. Run `./scripts/validate-pbip-structure.ps1`.
2. Confirm `qa/structural_validation.json` passes.
3. Refresh the source and reconcile Gross Sales, Return Amount, Net Sales, Orders, Customers, and Return Rate.
4. Confirm all 74 measures load without DAX errors.
5. Test navigation, reset, slicers, cross-filtering, Top-N sorting, and tables.
6. Inspect all pages at 100% and Fit to page.
7. Save PBIP and PBIX, close Power BI Desktop, reopen the PBIX, and repeat a smoke test.
8. Save clean page screenshots if the portfolio images are updated.
9. Record tests and unresolved limitations in `qa/validation_results.md`.

Do not claim completion if Desktop refresh/reopen has not been performed after the latest model change.

## Final deliverables

- Updated PBIP report and semantic model.
- `UK_Online_Retail_Sales_Performance_Dashboard.pbix`.
- Updated `model/measures.dax`, catalog, dictionary, and relationship map.
- Updated Power Query/build instructions.
- Structural validation JSON and QA notes.
- Sharp report-canvas screenshots when visual output changes.

## Copy-ready instruction

> Work on `projects/sales-performance`. Follow the repository and project `AGENTS.md`. Rebuild or enhance the UK Online Retail Sales dashboard using only the included UCI workbook and canonical PBIP/TMDL. Read `BI_Dashboard_Creation_Prompt.md`, all files in `agent/`, `model/`, `powerbi/`, and `qa/`. Preserve the three-page 1280×720 decision journey, use the exact DAX/Power Query definitions unless the requested change requires revision, validate source totals and interactions, open and reopen the final PBIX in Power BI Desktop, and disclose any test that was not performed.
