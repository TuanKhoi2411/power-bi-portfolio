# Changelog v2

## 2026-08-27 — Campaign Effectiveness chart differentiation

- Replaced the duplicated Contact Channel Mix donut with `Prior Contact Strategy | Volume vs Conversion`.
- The combo chart compares contact volume and conversion rate for first-time versus previously contacted prospects.
- Source validation: first-time contacts = 35,563 at 8.8% conversion; previously contacted = 5,625 at 26.6% conversion.
- The new view supports retargeting decisions and does not duplicate the channel-efficiency view on the Bank Marketing page.

- Created standalone renamed PBIP/Report/SemanticModel artifacts.
- Repointed M to the included CSV.
- Changed all primary time slicers from artificial CampaignDate range to categorical CampaignMonth dropdown.
- Added Segment Conversion Rate (500+ Contacts), Segment Conversions per 1K (500+ Contacts), Sample Size Status, Duration Leakage Warning, and Contact Share.
- Applied the 500-contact conversion-rate measure to overall Job and audience Job/Age ranking visuals.
- Updated titles to disclose the minimum base.
# 2026-08-24 — Marketing chart differentiation and conversion direction

- Replaced the Overview contacts/conversions chart with a dual-axis combo: contact volume columns and conversion-rate line.
- Replaced the repeated Audience chart with conversion rate by prior campaign outcome.
- Replaced the repeated Campaign chart with monthly average contact duration versus conversion rate.
- Added `Conversion Rate Change Display` so KPI deltas explicitly show ▲/▼ and percentage-point movement.
# 2026-08-24 — Conversion contribution visual

- Replaced the shifted prior-month line comparison with a column chart showing each month's share of total conversions.
- Added `Conversion Contribution`, which combines outcome volume and campaign scale without overstating small-sample monthly rates.
# 2026-08-25 — Calendar range slicer

- Replaced the top-right Campaign Month dropdown on all three pages with a synchronized `Between` slicer bound to `CampaignDate`.
- The slicer now exposes two calendar-enabled date inputs while preserving the existing global time sync group.
