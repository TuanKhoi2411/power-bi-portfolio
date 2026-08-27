# Apple Inc. Financial Performance v2

## Purpose

An isolated improvement package for source-traceable Apple growth, profitability, balance-sheet, and liquidity analysis using SEC EDGAR Company Facts. It is analytical portfolio work, not investment advice.

## Open

Open `dashboard/Apple_Inc_Financial_Performance_v2.pbip`. The semantic model points to the included SEC JSON.

## Source and validation baseline

- Publisher: U.S. Securities and Exchange Commission.
- Source: [Apple Company Facts, CIK 0000320193](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json).
- Grain: one selected concept/period/frame/filing fact.
- Original normalized rows: 648.
- v2 deterministic rows: 645 after removing three duplicated quarterly Revenue frames represented in both 10-Q and later 10-K filings.
- Latest selected quarter in the included source: end date 2026-06-27, Revenue $109.417B, Gross Profit $54.770B, Operating Income $35.695B, Net Income $29.789B, Assets $383.266B, Liabilities $275.746B, Cash $39.544B.

## v2 improvements

- Deduplication now chooses the latest filing per metric, class, end date, and frame regardless of form.
- Balance-sheet measures use MAX in date/metric context rather than summing point-in-time values.
- Overview sparklines now use true quarterly/margin measures instead of global `Latest …` measures that remove date filters.
- Added and displayed Cash to Assets with prior-year variance on Balance & Liquidity.
- Retained accession, form, filed date, frame, and period metadata for traceability.

## MCP and Desktop status

No Power BI report/model MCP operations were exposed. The package was prepared by direct PBIP/PBIR/TMDL inspection, then opened, refreshed, visually checked, and saved in Power BI Desktop. A separate close/reopen smoke test remains.

## Licensing and reuse

SEC filing facts are official public records, but comply with SEC fair-access and attribution guidance. The upstream GitHub repository has no root LICENSE; do not redistribute its report assets without permission.
