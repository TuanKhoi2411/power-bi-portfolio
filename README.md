<div align="center">

# Power BI Analytics Portfolio

**Four decision-focused dashboard products across Sales, Marketing, and Finance**

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-D8FF4F?style=for-the-badge)](https://tuankhoi2411.github.io/)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tuan-khoi-nguyen-324139316/)

</div>

This repository demonstrates how I turn business questions into controlled data models, decision-ready Power BI reports, and concise management stories. Each project keeps the dashboard, its supporting evidence, and a standalone interactive presentation together.

## Portfolio index

| Domain | Dashboard product | Decision supported | Main deliverables |
|---|---|---|---|
| Sales | [UK Online Retail — Sales Performance](./projects/sales-performance/README.md) | Where is growth coming from, which customers and products matter, and how do returns affect sales quality? | PBIX · PBIP · source data · HTML story |
| Marketing | [Portuguese Bank — Marketing Performance](./projects/marketing-performance/README.md) | Which audiences and campaign conditions are associated with stronger subscription conversion? | PBIP · source data · HTML story |
| Finance | [Apple Inc. — Financial Performance](./projects/finance-performance/README.md) | Are growth, margins, liquidity, and cost structure moving sustainably? | PBIP · SEC source data · HTML story |
| Finance / BI | [Sports & Health Enterprise — Financial Performance](./projects/financial-performance-dashboard/README.md) | How can management move from a headline P&L into margin, cost, segment, and break-even drivers? | PBIX · HTML story |

## What to review

1. Start with each project README for the management question and a 60-second review path.
2. Open the HTML story for the decision narrative and recommended actions.
3. Use the PBIX for direct Power BI review, or download the complete PBIP folder to inspect the report and semantic model definitions.
4. Review the included raw data and refresh notes where the source is public.

## Delivery status

| Project | Dashboard | Interactive story | Data included | Published status |
|---|---:|---:|---:|---|
| UK Online Retail | PBIX + PBIP | 12 slides | Yes | Review-ready |
| Portuguese Bank | PBIP | 12 slides | Yes | Review-ready; PBIX not published |
| Apple Inc. | PBIP | 12 slides | Yes | Review-ready; PBIX not published |
| Sports & Health Enterprise | PBIX | 12 slides | No separate raw file | Review-ready |

## Repository guide

Each project is self-contained:

```text
projects/<project-name>/
├── README.md                 # business context, status, and review guide
├── *.html                   # standalone interactive management story
├── *.pbix                   # packaged Power BI report where available
├── dashboard/               # PBIP report + semantic model where available
└── data/                    # included public source file where available
```

## Quality standard

- Management question before charts.
- Separate Sales, Marketing, and Finance models rather than a forced cross-domain comparison.
- Overview plus decision-specific deep dives.
- Explicit model, page, source, and delivery status.
- Honest refresh dependencies and limitations.
- Standalone 12-slide HTML stories with presentation controls.

## Notes

- Public-source projects cite their publisher and retain the source file used for the model.
- PBIP files are project entry points, not standalone reports. Download the complete `dashboard/` folder before opening them.
- PBIP queries may retain the original local `SourcePath`; each project README explains what must be changed before refresh.
- These are portfolio case studies, not production systems or investment recommendations.

## Author

**Nguyen Tuan Khoi** — Finance & Data Analytics · Power BI · Process Automation

[GitHub Profile](https://github.com/TuanKhoi2411) · [Finance Case Studies](https://github.com/TuanKhoi2411/finance-analytics-case-studies) · [Email](mailto:tuankhoi24112003@gmail.com)
