# Metric definitions — Finance

Exact formulas, fact-selection logic, and formats are in `measures.dax` and `measure_catalog.csv`.

| Metric | Business definition | Period treatment / caution |
|---|---|---|
| Revenue | Reported operating revenue selected from mapped SEC concepts | Duration fact; compare compatible fiscal periods |
| Cost of Sales | Reported cost associated with revenue | Duration fact; concept mapping can evolve |
| Gross Profit | Revenue less Cost of Sales or mapped reported value | Reconcile on matched periods |
| Operating Expenses | Mapped reported operating-expense facts | Avoid double counting components and totals |
| Operating Income | Reported income from operations | Duration fact |
| Net Income | Reported net income attributable under mapped logic | Duration fact; filing/version selection matters |
| Gross Margin | Gross Profit divided by Revenue | Matching-period denominator required |
| Operating Margin | Operating Income divided by Revenue | Matching-period denominator required |
| Net Margin | Net Income divided by Revenue | Matching-period denominator required |
| Assets | Total assets at period end | Instant fact; select, never sum across dates |
| Liabilities | Total liabilities at period end | Instant fact; select, never sum across dates |
| Cash | Mapped cash and cash-equivalent balance | Instant fact; taxonomy/concept coverage must be reviewed |
| Latest value | Deterministic selected metric for latest valid period | Requires stable period/form/filing selection |
| YoY | Comparable current-period value versus prior-year period | Do not mix annual and quarterly durations |
