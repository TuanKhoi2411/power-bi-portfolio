from pathlib import Path
from pypdf import PdfReader
import hashlib, re, sys

BASE=Path(__file__).resolve().parents[2]
REPO=BASE/'power-bi-portfolio-repo'
SITE=BASE/'github-pages-portfolio'
PAIRS=[
 (Path(r'C:\PowerBI Dashboard - KhoiPort\01_UK_Online_Retail_Sales\PowerBI_Project\UK_Online_Retail_Sales - pbix.pbix'),REPO/'projects/sales-performance/UK_Online_Retail_Sales_Performance_Dashboard.pbix'),
 (Path(r'C:\PowerBI Dashboard - KhoiPort\02_Apple_Finance\PowerBI_Project\Apple_Finance - pbix.pbix'),REPO/'projects/finance-performance/Apple_Inc_Financial_Performance_Dashboard.pbix'),
 (Path(r'C:\PowerBI Dashboard - KhoiPort\03_Portuguese_Bank_Marketing\PowerBI_Project\Portuguese_Bank_Marketing - pbix.pbix'),REPO/'projects/marketing-performance/Portuguese_Bank_Marketing_Performance_Dashboard.pbix'),
 (Path(r'C:\PowerBI Dashboard - KhoiPort\04_FinTech_Credit_Risk\PowerBI_Project\FinTech_Credit_Risk - pbix.pbix'),REPO/'projects/credit-risk-performance/FinTech_Credit_Risk_Dashboard.pbix'),
 (Path(r'C:\PowerBI Dashboard - KhoiPort\05_Sports_Health_Financial_Performance_GitHub\Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix'),REPO/'projects/financial-performance-dashboard/Sports_Health_Enterprise_Financial_Performance_Dashboard.pbix'),
]
ok=True
for pdf in REPO.glob('projects/*/preview/*.pdf'):
    pages=len(PdfReader(str(pdf)).pages); print('PDF',pdf.parent.parent.name,pages,pdf.stat().st_size); ok &= pages>=3
for source,target in PAIRS:
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    match=source.exists() and target.exists() and digest(source)==digest(target)
    print('PBIX',target.name,match,target.stat().st_size if target.exists() else 0); ok &= match
for page in ['sales-performance','marketing-performance','finance-performance','credit-risk-performance','sports-health-performance']:
    html=SITE/'power-bi/cases'/page/'preview.html'
    sources=re.findall(r'src="([^"]+)',html.read_text(encoding='utf-8'))
    exists=all((SITE/src.lstrip('/')).exists() for src in sources)
    print('PREVIEW',page,len(sources),exists); ok &= exists and len(sources)>=3
if not ok: sys.exit(1)
