from pathlib import Path
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch

REPO = Path(__file__).resolve().parents[1]
SITE = REPO.parent / "github-pages-portfolio"
SOURCE = Path(r"C:\pbi-portfolio-v2")

PROJECTS = {
    "sales-performance": {
        "pdf": "UK_Online_Retail_Sales_Dashboard.pdf",
        "images": [SOURCE / "sales-review-current.png", SOURCE / "sales-review-customers.png", SOURCE / "sales-review-returns.png"],
        "site": ["sales-overview.png", "sales-customers.png", "sales-returns.png"],
        "crop": (60, 271, 1171, 954),
    },
    "marketing-performance": {
        "pdf": "Portuguese_Bank_Marketing_Dashboard.pdf",
        "images": [SOURCE / "marketing-review-overview.png", SOURCE / "marketing-review-benchmark.png", SOURCE / "marketing-review-campaign.png"],
        "site": ["marketing-overview.png", "marketing-benchmark.png", "marketing-campaign.png"],
        "crop": (60, 271, 1171, 954),
    },
    "finance-performance": {
        "pdf": "Apple_Finance_Dashboard.pdf",
        "images": [SOURCE / "finance-v2-final-overview.png", SOURCE / "finance-v2-final-profitability.png", SOURCE / "finance-v2-final-balance.png"],
        "site": ["finance-overview.png", "finance-profitability.png", "finance-balance.png"],
        "crop": (60, 271, 1171, 954),
    },
    "credit-risk-performance": {
        "pdf": "FinTech_Credit_Risk_Dashboard.pdf",
        "images": [SOURCE / "dashboard-backups/20260826_190500_before_theme_positive_colors/CreditRisk/axis_cleanup_portfolio_preview.png", SOURCE / "dashboard-backups/20260826_190500_before_theme_positive_colors/CreditRisk/risk_drivers_preview.png", SOURCE / "dashboard-backups/20260826_190500_before_theme_positive_colors/CreditRisk/pricing_verification_preview.png", SOURCE / "dashboard-backups/20260826_190500_before_theme_positive_colors/CreditRisk/axis_cleanup_preview.png"],
        "site": ["credit-overview.png", "credit-borrower-risk.png", "credit-pricing.png", "credit-risk-drivers.png"],
        "crop": (60, 271, 1171, 954),
    },
    "financial-performance-dashboard": {
        "pdf": "Sports_Health_Financial_Performance_Dashboard.pdf",
        "images": [SITE / "assets/cases/power-bi/native/sports-overview.png", SITE / "assets/cases/power-bi/native/sports-breakdown.png", SITE / "assets/cases/power-bi/native/sports-segments.png", SITE / "assets/cases/power-bi/native/sports-breakeven.png"],
        "site": ["sports-overview.png", "sports-breakdown.png", "sports-segments.png", "sports-breakeven.png"],
        "crop": None,
    },
}

PAGE = landscape((13.333 * inch, 7.5 * inch))

def clean_frame(path: Path, crop):
    image = Image.open(path).convert("RGB")
    if crop:
        image = image.crop(crop)
    # Fill the preview frame instead of placing a small dashboard inside a
    # padded canvas. This keeps labels legible and removes the dead space that
    # appeared around the former centered thumbnail.
    target_ratio = 16 / 9
    width, height = image.size
    current_ratio = width / height
    if current_ratio > target_ratio:
        target_width = round(height * target_ratio)
        left = (width - target_width) // 2
        image = image.crop((left, 0, left + target_width, height))
    elif current_ratio < target_ratio:
        target_height = round(width / target_ratio)
        # Power BI captures carry the report header at the top and page chrome
        # at the bottom. Anchor the crop to the top so the dashboard title is
        # never cut off while the lower Desktop chrome falls away.
        image = image.crop((0, 0, width, target_height))
    return image.resize((1600, 900), Image.Resampling.LANCZOS)

for slug, config in PROJECTS.items():
    preview = REPO / "projects" / slug / "preview"
    preview.mkdir(parents=True, exist_ok=True)
    site_dir = SITE / "assets/cases/power-bi/native"
    site_dir.mkdir(parents=True, exist_ok=True)
    rendered = []
    for index, (source, site_name) in enumerate(zip(config["images"], config["site"]), 1):
        if not source.exists():
            raise FileNotFoundError(source)
        frame = clean_frame(source, config["crop"])
        local_png = preview / f"page-{index:02}.png"
        frame.save(local_png, quality=95)
        frame.save(site_dir / site_name, quality=95)
        rendered.append(local_png)

    pdf_path = preview / config["pdf"]
    pdf = Canvas(str(pdf_path), pagesize=PAGE)
    for png in rendered:
        pdf.drawImage(str(png), 0, 0, width=PAGE[0], height=PAGE[1], preserveAspectRatio=False)
        pdf.showPage()
    pdf.save()
    print(pdf_path)
