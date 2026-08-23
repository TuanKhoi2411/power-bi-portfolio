# QA checklist — Apple Financial Performance

## Source and fact selection

- [ ] Included SEC companyfacts JSON is used.
- [ ] Company, CIK, units, form, filed date, accession, fiscal period, and frame are preserved.
- [ ] Instant and duration facts are separated.
- [ ] Duplicate/restated period facts follow a deterministic documented rule.
- [ ] Concept mapping and exclusions are reviewed.

## Model and DAX

- [ ] `FactFinance` and `DimDate` load with the active EndDate relationship.
- [ ] All 90 measures parse and retain formats/folders.
- [ ] Revenue, Gross Profit, Operating Income, and Net Income reconcile on matched periods.
- [ ] Margin denominators use matching-period Revenue.
- [ ] Assets, Liabilities, and Cash use point-in-time logic.
- [ ] Latest/YoY cards reconcile to trend and detail visuals.
- [ ] Display measures are not used for numeric sorting/calculation.

## Report/Desktop

- [ ] Three pages exist at 1280×720 with valid active page/order.
- [ ] Navigation, reset, slicers, cross-filtering, and detail traceability work.
- [ ] Units, signs, currency scale, fiscal labels, and form context are readable.
- [ ] Instant/duration or annual/quarterly periods are not mixed misleadingly.
- [ ] PBIP refreshes; PBIX saves, closes, and reopens.
- [ ] Screenshots exclude Desktop chrome and remain sharp.
- [ ] Investment-advice limitation and unperformed tests are disclosed.
