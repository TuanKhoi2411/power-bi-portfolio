# QA checks v2

## Static/source checks

- [x] PBIP and dataset relative paths resolve.
- [x] Three pages exist at 1280×720.
- [x] Visual JSON parses.
- [x] Source CSV exists and uses semicolon delimiter.
- [x] Independent source reconciliation completed.
- [x] CampaignMonth is used as a categorical slicer.
- [x] No `unknown` rows were removed.

## Expected totals

| Metric | Expected |
|---|---:|
| Contacts | 41,188 |
| Conversions | 4,640 |
| Conversion Rate | 11.2654% |
| Average Duration | 258.285 sec |
| Average Campaign Contacts | 2.5676 |
| Cellular Share | 63.4748% |

## Desktop checks completed

- [x] Opened and refreshed in Power BI Desktop 2.156.951.0.
- [x] Confirmed 41.2K contacts, 4.6K conversions, and 11.3% conversion in the rendered report.
- [x] Confirmed month slicer is a categorical dropdown.
- [x] Confirmed Job/Age titles disclose the 500-contact threshold.
- [x] Saved the v2 project.

## Desktop checks still required

1. Confirm every month sort and all small-base suppression cases.
2. Add the duration warning to a tooltip/text card if direct on-canvas disclosure is required.
3. Test every navigation/reset/filter interaction.
4. Close and reopen the saved project for a separate smoke test.
# 2026-08-24 — Marketing visual review

- PASS: Overview combo chart renders Contacts on the primary axis and Conversion Rate on the secondary axis.
- PASS: Audience page uses prior campaign outcome rather than repeating the monthly chart.
- PASS: Campaign page uses average duration versus conversion rate rather than repeating the monthly chart.
- PASS: conversion delta renders as `▲ 1.1 pp` in the unfiltered latest-month context.
- PASS: the former prior-month line chart now shows monthly contribution to total conversions; May is visibly the largest contributor and low-volume months no longer appear artificially superior.
# 2026-08-25 — Date slicer review

- PASS: all three primary slicers bind to `FactMarketing[CampaignDate]` and use `Between` mode.
- PASS: calendar icons and two date inputs render within the header in Power BI Desktop.
- PASS: the three slicers retain the shared `Global time` synchronization group.
