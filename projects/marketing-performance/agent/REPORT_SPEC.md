# Report blueprint — Portuguese Bank Marketing Performance

## Design contract

- Canvas: 1280×720.
- Preserve the existing white/soft-neutral canvas, dark text, purple campaign accent, coral conversion accent, and teal action/navigation treatment.
- Use executive KPI cards, clear segmentation labels, and high-contrast conversion comparisons.
- Every recommendation must be framed as a testable hypothesis, not a proven causal action.

## Page 01 — Bank Marketing

Decision: establish overall campaign volume, conversion, channel, and timing context.

Required content:

- Contacts, Conversions, Conversion Rate, average duration, and campaign-frequency KPIs.
- Core audience/channel/time slicers.
- Conversion and contact trends/context.
- Channel or outcome mix.
- Segment ranking and a detail table for investigation.

## Page 02 — Audience Segmentation

Decision: locate audience groups associated with higher or lower conversion while preserving base-size context.

Required content:

- Age, job, education, marital, loan/default, and prior-contact lenses where supported.
- Both contact volume and conversion rate; never show rate alone for small groups.
- `unknown` categories visible or explicitly disclosed.
- Segment detail suitable for forming campaign-test hypotheses.

## Page 03 — Campaign Effectiveness

Decision: compare campaign frequency, channel, prior outcome, month/day-of-week context, and conversion.

Required content:

- Contacts, Conversions, Conversion Rate, campaign contacts, prior-contact rate, and cellular share.
- Campaign-frequency bands and prior-outcome comparisons.
- Duration shown with a leakage note.
- A table or chart that lets reviewers compare volume, rate, and sample size together.

## Interaction contract

- Page navigator reaches all three pages.
- Slicers update every intended visual and reset to a documented default.
- Cross-filtering keeps both numerator and denominator in the same context.
- Small-base segments must not be visually promoted without population size.

## Screenshot/export contract

Capture the clean report canvas, not the Power BI Desktop application window. Export at a resolution that keeps labels and table values legible on the portfolio site.
