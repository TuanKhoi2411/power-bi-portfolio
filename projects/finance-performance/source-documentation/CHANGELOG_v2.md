# Changelog v2

- Reframed all three report pages around CFO decisions: profitability, cost burden, revenue growth, capital cushion, leverage, and liquidity.
- Replaced generic latest-metric bars and dense absolute-value charts with margin ladders, ratio trends, YoY variance, profit-conversion, and balance-risk comparisons.
- Added quarterly-only margin/cost/conversion measures to prevent annual SEC facts from being mixed into quarter trends.
- Rebuilt prior-year revenue comparison using SEC calendar-quarter frames and suppressed unmatched periods.
- Renamed the overview page and chart titles to state the analytical question each visual answers.

- Created standalone renamed PBIP/Report/SemanticModel artifacts.
- Repointed Power Query to the included SEC JSON.
- Changed deduplication key to metric/class/end date/frame, keeping the latest filed record.
- Reduced deterministic normalized fact count from 648 to 645 by removing three duplicate Revenue quarter frames.
- Added Balance Value and revised Assets, Liabilities, and Cash to avoid summing instant facts.
- Rebound all five overview sparklines to quarterly/margin trend measures.
- Added Cash to Assets, latest/PY/variance/display measures and used them in KPI, delta, sparkline, and leverage chart.
# 2026-08-24 — Executive Overview chart clarification

- Replaced the quarterly Revenue YoY column chart with an area chart of actual quarterly revenue so viewers can read scale, trend, and seasonality directly.
- Replaced the overlapping margin ladder with a donut of mutually exclusive latest-quarter revenue components: Cost of Sales, Operating Expenses, Other & Tax, and Net Income.
- Added three allocation measures; together with Latest Net Income, the donut reconciles exactly to Latest Revenue.
