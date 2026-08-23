# Metric definitions — Sales

Exact formulas and formats are in `measures.dax` and `measure_catalog.csv`.

| Metric | Business definition | Filter behavior / caution |
|---|---|---|
| Gross Sales | Positive, valid-price sale value before return leakage | Excludes cancellation/return lines from positive gross sales |
| Return Amount | Absolute monetary value of cancellation/negative-quantity lines | Must remain separate from Gross Sales |
| Net Sales | Signed transaction value after returns/cancellations | Reconcile with Gross Sales and Return Amount sign logic |
| Orders | Distinct non-cancelled invoice numbers | Not a count of transaction lines |
| Customers | Distinct identified customer IDs | Excludes `Unknown` from identified-customer count only |
| Average Order Value | Net Sales divided by Orders | Blank-safe through `DIVIDE` |
| Return Rate | Return Amount divided by Gross Sales | Monetary leakage rate, not returned-unit rate |
| Gross to Net Rate | Net Sales divided by Gross Sales | Falls as return/cancellation leakage rises |
| Merchandise Net Sales | Net Sales restricted to valid merchandise codes/descriptions | Excludes postage, fees, adjustments, invalid names |
| Repeat Customer Rate | Repeat identified customers divided by identified customers | Does not represent anonymous purchases |
| Customer Data Coverage | Identified-customer sales or records relative to the relevant total | Must accompany customer segmentation |
| MoM / YoY | Current comparable-period movement against prior month/year | Final partial month handling is explicit in DAX |
