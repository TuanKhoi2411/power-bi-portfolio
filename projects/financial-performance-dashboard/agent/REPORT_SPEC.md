# Report blueprint — Sports & Health Enterprise

## Documented report contract

- Four pages: Overview, Breakdown, Segments, and Breakeven.
- Existing README documents 73 visual containers across the packaged report.
- Preserve the existing financial-performance visual language unless redesign is requested.
- Use the live PBIX as the source of truth for exact canvas size, objects, interactions, colors, and DAX.

## Page 01 — Overview

Decision: establish KPI direction, monthly revenue, net profit, and executive P&L context.

Expected content:

- headline revenue/profit/margin KPIs;
- trend and headline P&L;
- management-oriented status or exception cues;
- filters and navigation into drivers.

## Page 02 — Breakdown

Decision: move below headline performance into operating drivers and supporting detail.

Expected content:

- revenue/cost/profit bridge or decomposition;
- variance and cost-driver analysis;
- detailed rows for investigation.

## Page 03 — Segments

Decision: compare contribution and performance across business segments.

Expected content:

- segment volume, revenue, profit, and margin;
- contribution and concentration views;
- cross-filterable segment detail.

## Page 04 — Breakeven

Decision: review profitability thresholds and the relationship between operating expense and EBIT.

Expected content:

- fixed/variable cost or operating-cost lens supported by the PBIX;
- break-even threshold and sensitivity views;
- clear limitations on modeled assumptions.

## Interaction and screenshot contract

- Preserve page navigation, filters, bookmarks, reset behavior, and cross-filtering verified in the PBIX.
- Export the clean report canvas, not Power BI Desktop chrome.
- If any expected content is absent from the live PBIX, document the difference rather than inventing it.
