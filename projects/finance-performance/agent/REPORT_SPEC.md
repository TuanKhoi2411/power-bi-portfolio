# Report blueprint — Apple Inc. Financial Performance

## Design contract

- Canvas: 1280×720.
- Preserve the existing clean white/soft-neutral cards, deep green/teal financial accent, amber comparison accent, and dark executive header.
- Use compact KPI labels, consistent currency scale, and clear fiscal-period context.
- Source/filing traceability and limitations must remain accessible.

## Page 01 — Apple Finance

Decision: establish direction across growth, profit, margins, and core balance-sheet context.

Required content:

- Revenue, Gross Profit, Operating Income, Net Income, and Gross Margin KPIs.
- Period, form, and metric slicers.
- Latest financial metrics comparison.
- Quarterly Revenue versus prior year.
- Assets, Liabilities, and Cash trend.
- Quarterly margin trend.
- Financial detail table with period context.

## Page 02 — Profitability & Growth

Decision: determine whether growth is translating into durable profitability.

Required content:

- Growth and margin KPIs with prior-period comparison.
- Revenue and profit trends on compatible period bases.
- Gross, operating, and net margin development.
- Cost structure and operating-expense analysis.
- Detail that exposes fiscal period, form, and filed date.

## Page 03 — Balance & Liquidity

Decision: assess the direction of assets, liabilities, cash, and liquidity resilience.

Required content:

- Assets, Liabilities, Cash, and relevant ratio KPIs.
- Point-in-time trends only for balance-sheet facts.
- Liability/asset and cash context with period comparability.
- A detail table supporting traceability to filings.

## Interaction contract

- Page navigation reaches all three pages.
- Period/form/metric slicers update intended visuals consistently.
- Reset action restores a documented default.
- Cross-filtering never mixes incompatible period types.
- Tooltips or tables preserve filing metadata needed to review selected facts.

## Screenshot/export contract

Export the report canvas only, without Power BI Desktop ribbon or side panes. Keep small financial labels and tables sharp enough to read on the portfolio page.
