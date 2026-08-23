# Report blueprint — UK Online Retail Sales Performance

## Design contract

- Canvas: 1280×720, fit-to-page friendly.
- Existing palette: soft off-white background, navy text, purple analytical accent, coral returns accent, teal navigation/action state.
- Typography: Segoe UI family; compact executive labels and clear KPI hierarchy.
- Use white cards with subtle borders/shadows; avoid Power BI Desktop chrome in portfolio screenshots.
- Each page requires page navigation, context slicers, a reset action, KPI cards, trends, driver visuals, and a detail table.

## Page 01 — UK Retail Sales

Decision: establish the commercial baseline and locate geographic/product concentration.

Required content:

- Net Sales, Gross Sales, Orders, Units Sold, and Return Rate KPIs.
- Country, transaction type, and product slicers.
- Top countries by Net Sales.
- Top products by Merchandise Net Sales.
- Sales mix by transaction type.
- Monthly Net Sales versus prior year.
- Country performance detail table.

## Page 02 — Customer Insights

Decision: identify valuable customers, repeat behavior, and customer-data coverage.

Required content:

- Identified-customer sales, Customers, Net Sales per Customer, Orders per Customer, and Repeat Customer Rate.
- Customer identification/data-coverage disclosure.
- Customer ranking and concentration views.
- Repeat versus one-time customer comparison.
- Trend and customer-level detail suitable for management follow-up.

## Page 03 — Product & Returns

Decision: separate merchandise demand from leakage caused by returns/cancellations.

Required content:

- Product and returns KPIs.
- Monthly Net Sales and Return Amount trend.
- Gross Sales and Returns by transaction type.
- Top products by Merchandise Sales.
- Top products by Return Amount.
- Product performance detail table.

## Interaction contract

- Page navigator switches among all three pages.
- Slicers filter every intended visual on the page.
- Reset action restores the documented default state.
- Cross-highlighting is meaningful; table selection must not produce misleading totals.
- Top-N visuals use numeric rank measures and display a stable tie-breaking order.

## Screenshot/export contract

For the portfolio, capture the report canvas only at readable resolution. Hide Power BI Desktop ribbons, Filters, Build, and Data panes. Do not use a blurry full-window screenshot as the hero image.
