# QA checklist — Portuguese Bank Marketing

## Data

- [ ] Included UCI CSV is used with the correct delimiter.
- [ ] 41,188 contact rows are reviewed before exclusions.
- [ ] Target `yes`/`no` mapping is correct.
- [ ] `unknown` categories are retained or explicitly documented.
- [ ] Derived bands and technical campaign date are reproducible.

## Model and measures

- [ ] All 34 measures parse and retain formats/folders.
- [ ] Contacts, Conversions, and Conversion Rate reconcile.
- [ ] Prior-contact, cellular-share, prior-success, and per-1K measures reconcile.
- [ ] Previous-month/MoM logic uses the intended month context.
- [ ] Formatted KPI measures are display-only.

## Responsible analysis

- [ ] No observational association is presented as causal.
- [ ] Duration leakage is disclosed.
- [ ] Rates display sample/contact volume.
- [ ] Small-base segments are not promoted without caveat.
- [ ] Recommendations are hypotheses/tests, not unsupported targeting rules.

## Report/Desktop

- [ ] Three pages exist at 1280×720 with valid active page/order.
- [ ] Navigation, reset, slicers, cross-highlighting, and tables work.
- [ ] Labels and `unknown` categories remain readable.
- [ ] PBIP refreshes; PBIX saves, closes, and reopens.
- [ ] Screenshots exclude Desktop chrome.
- [ ] Limitations and unperformed tests are recorded.
