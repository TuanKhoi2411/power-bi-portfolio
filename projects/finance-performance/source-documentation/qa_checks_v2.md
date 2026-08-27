# QA checks v2

## Static/source checks

- [x] PBIP and dataset relative paths resolve.
- [x] Three pages exist at 1280×720.
- [x] Visual JSON parses.
- [x] SEC JSON exists.
- [x] Normalization logic independently reproduced.
- [x] Three duplicate Revenue quarter frames identified.
- [x] Overview sparkline bindings no longer use `Latest …` measures.
- [x] Balance measures use point-in-time aggregation.

## Expected refresh checks

| Metric | Expected |
|---|---:|
| Deterministic normalized facts | 645 |
| Latest Revenue | $109.417B |
| Latest Gross Profit | $54.770B |
| Latest Operating Income | $35.695B |
| Latest Net Income | $29.789B |
| Latest Assets | $383.266B |
| Latest Liabilities | $275.746B |
| Latest Cash | $39.544B |
| Latest Cash to Assets | 10.3179% |

## Desktop checks completed

- [x] Opened and refreshed in Power BI Desktop 2.156.951.0.
- [x] Confirmed Revenue $109.4B and Gross Margin 50.1% rendered.
- [x] Confirmed Balance & Liquidity displays Cash to Assets 10.3% and the revised trend.
- [x] Confirmed report visuals populated without unresolved binding errors.
- [x] Confirmed Executive Overview renders the latest-quarter margin ladder, SEC-frame YoY revenue growth, balance-risk trend, margin-quality trend, and CFO scorecard.
- [x] Confirmed Profitability & Growth renders quarterly-only cost ratios, gross-to-net conversion, growth-versus-margin, and driver detail without mixing annual facts.
- [x] Confirmed Balance & Liquidity renders net-asset/cash trends, latest position, cash coverage, capital/cash mix, and risk detail.
- [x] Confirmed all 84 visual JSON files parse and all referenced measures exist after redesign.
- [x] Saved the v2 project.

## Desktop checks still required

1. Confirm the refreshed table row count is 645 inside Power Query/Data view.
2. Spot-check the three deduplicated Revenue frames and all filing metadata.
3. Test every navigation/reset/slicer path.
4. Close and reopen the saved project for a separate smoke test.
# 2026-08-24 — Executive Overview visual review

- PASS: Quarterly Revenue Trend renders as an area chart with a continuous reporting-date axis and actual quarterly revenue values.
- PASS: Latest Quarter Revenue Allocation renders as a donut with Cost of Sales, Operating Expenses, Other & Tax, and Net Income.
- PASS: allocation components reconcile to Latest Revenue by construction.
- PASS: report reopened and saved in Power BI Desktop; review screenshot captured at `C:\pbi-portfolio-v2\finance-v2-review-overview.png`.
