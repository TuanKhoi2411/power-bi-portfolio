# Portuguese Bank — Marketing Performance

## Management question

Which audiences, channels, and campaign conditions are associated with stronger term-deposit subscription conversion?

## Dashboard

| Item | Detail |
|---|---|
| Power BI project | [`dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip`](./dashboard/Portuguese_Bank_Marketing_Performance_Dashboard.pbip) |
| Pages | Bank Marketing · Audience Segmentation · Campaign Effectiveness |
| Canvas | 1280 × 720 on every page |
| Semantic model | FactMarketing, 34 authored measures |
| Source | UCI Bank Marketing, 41,188 direct-marketing contacts |

The report starts with campaign performance, then isolates audience and campaign drivers without combining this dataset with unrelated Sales or Finance entities.

## Interactive presentation

[`Portuguese_Bank_Marketing_Performance_Interactive.html`](./Portuguese_Bank_Marketing_Performance_Interactive.html) is the accompanying 12-slide decision story. Download it and open locally in Chrome or Edge; all ten chart images are embedded.

Controls: `←` / `→` or `Space` to navigate, `F` for fullscreen, and `O` for overview.

## Source and refresh

- Included source: [`data/bank-additional-full.csv`](./data/bank-additional-full.csv)
- Publisher: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing)
- Before refreshing on another computer, replace `SourcePath` in `FactMarketing.tmdl` with the absolute path to the included CSV.

## Verification and limits

- PBIP package contains the project pointer, report definition, semantic model, valid active page, and three report pages.
- The HTML deck contains 12 slides, embedded visuals, and keyboard navigation.
- The model describes associations in historical campaign data; it does not prove causal lift.
- A fresh Power BI Desktop reopen was not performed during this repository packaging step.
