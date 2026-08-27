# Portuguese Bank Marketing Performance v2

## Purpose

An isolated improvement package for evaluating campaign contacts, conversions, audience segments, channels, timing context, frequency, and prior outcomes without causal overclaiming.

## Open

Open `dashboard/Portuguese_Bank_Marketing_Performance_v2.pbip`. The model points to the included semicolon-delimited CSV.

## Source and validation baseline

- Publisher: UCI Machine Learning Repository.
- Dataset: [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).
- Grain: one outbound contact.
- Contacts: 41,188; conversions: 4,640; conversion rate: 11.2654%.
- Average duration: 258.285 seconds; average campaign contacts: 2.5676.
- Prior-contact rate: 13.6569%; cellular share: 63.4748%; successful-prior-outcome share: 3.3335%.

## v2 improvements

- Replaced the artificial date-range slicer with a categorical campaign-month slicer; the dataset has no complete calendar date/year.
- Added reviewable-base measures and applied the 500-contact threshold to headline job/age conversion rankings.
- Added explicit sample-size status, contact share, and duration leakage warning measures.
- Preserved volume tables and conversion counts so rates are not interpreted without a base.
- Retained `unknown` categories and observational language.

## Interpretation limits

Call duration is observed after contact and must not be treated as a pre-call targeting feature. The data is observational: use “associated with” and test hypotheses rather than claiming lift or causality.

## MCP and Desktop status

No Power BI report/model MCP operations were exposed. The v2 package was prepared via PBIP/PBIR/TMDL inspection, then opened, refreshed, visually checked, and saved in Power BI Desktop. A separate close/reopen smoke test remains.

## Licensing and reuse

The upstream repository has no root LICENSE. Keep the report derivative private unless redistribution rights are confirmed. Verify the UCI dataset license and attribution on its source page.
