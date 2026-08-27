from __future__ import annotations

import json
import re
import shutil
import sys
import uuid
from pathlib import Path


ROOT = Path(r"C:\PowerBI Dashboard - KhoiPort\02_Apple_Finance")
PROJECT = ROOT / "PowerBI_Project"
REPORT = PROJECT / "Apple_Finance_v2.Report"
MODEL = PROJECT / "Apple_Finance_v2.SemanticModel"
PAGES = REPORT / "definition" / "pages"
TABLES = MODEL / "definition" / "tables"
FACT = TABLES / "FactFinance.tmdl"

sys.path.insert(0, str(ROOT / "Build_Scripts"))
import apply_finance_review_20260827 as r1


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def lit(value: str) -> dict:
    return {"expr": {"Literal": {"Value": value}}}


def guid() -> str:
    return str(uuid.uuid4())


def measure_proj(name: str, display: str | None = None) -> dict:
    return r1.measure_projection(name, display)


def column_proj(entity: str, prop: str, display: str | None = None) -> dict:
    return r1.column_projection(entity, prop, display)


def add_ref(table: str) -> None:
    path = MODEL / "definition" / "model.tmdl"
    text = path.read_text(encoding="utf-8-sig")
    line = f"ref table {table}"
    if line not in text:
        text = text.rstrip() + "\n" + line + "\n"
        path.write_text(text, encoding="utf-8")


def write_dimensions() -> None:
    capital = TABLES / "CapitalStructure.tmdl"
    if not capital.exists():
        capital.write_text(f'''table CapitalStructure
\tlineageTag: {guid()}

\tcolumn Component
\t\tdataType: string
\t\tisKey
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [Component]
\t\tsortByColumn: ComponentSort

\tcolumn ComponentSort
\t\tdataType: int64
\t\tisHidden
\t\tformatString: 0
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [ComponentSort]

\tpartition CapitalStructure = calculated
\t\tmode: import
\t\tsource = DATATABLE ( "Component", STRING, "ComponentSort", INTEGER, {{ {{ "Liabilities", 1 }}, {{ "Net Assets", 2 }} }} )
''', encoding="utf-8")
    bridge = TABLES / "NetIncomeBridge.tmdl"
    if not bridge.exists():
        bridge.write_text(f'''table NetIncomeBridge
\tlineageTag: {guid()}

\tcolumn Step
\t\tdataType: string
\t\tisKey
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [Step]
\t\tsortByColumn: StepSort

\tcolumn StepSort
\t\tdataType: int64
\t\tisHidden
\t\tformatString: 0
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [StepSort]

\tpartition NetIncomeBridge = calculated
\t\tmode: import
\t\tsource = DATATABLE ( "Step", STRING, "StepSort", INTEGER, {{ {{ "Prior-year Net Income", 1 }}, {{ "Revenue impact", 2 }}, {{ "Cost of Sales impact", 3 }}, {{ "Operating Expense impact", 4 }}, {{ "Other & Tax impact", 5 }} }} )
''', encoding="utf-8")
    refresh = TABLES / "LastRefresh.tmdl"
    if not refresh.exists():
        refresh.write_text(f'''table LastRefresh
\tlineageTag: {guid()}

\tcolumn RefreshedAt
\t\tdataType: dateTime
\t\tformatString: mmm d, yyyy h:mm AM/PM
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: RefreshedAt

\tpartition LastRefresh = m
\t\tmode: import
\t\tsource = #table ( type table [RefreshedAt = datetimezone], {{ {{ DateTimeZone.FixedUtcNow() }} }} )
''', encoding="utf-8")
    cash_bridge = TABLES / "CashFlowBridge.tmdl"
    if not cash_bridge.exists():
        cash_bridge.write_text(f'''table CashFlowBridge
\tlineageTag: {guid()}

\tcolumn Step
\t\tdataType: string
\t\tisKey
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [Step]
\t\tsortByColumn: StepSort

\tcolumn StepSort
\t\tdataType: int64
\t\tisHidden
\t\tformatString: 0
\t\tlineageTag: {guid()}
\t\tsummarizeBy: none
\t\tsourceColumn: [StepSort]

\tpartition CashFlowBridge = calculated
\t\tmode: import
\t\tsource = DATATABLE ( "Step", STRING, "StepSort", INTEGER, {{ {{ "Opening Cash", 1 }}, {{ "Operating Cash Flow", 2 }}, {{ "Capital Expenditure", 3 }}, {{ "Share Repurchases", 4 }}, {{ "Dividends", 5 }}, {{ "Other Cash Movement", 6 }} }} )
''', encoding="utf-8")
    for name in ("CapitalStructure", "NetIncomeBridge", "LastRefresh", "CashFlowBridge"):
        add_ref(name)


def measure_block(name: str, expr: str, fmt: str | None, folder: str) -> str:
    out = f"\n\tmeasure '{name}' = {expr}\n"
    if fmt:
        out += f"\t\tformatString: {fmt}\n"
    out += f"\t\tdisplayFolder: {folder}\n\t\tlineageTag: {guid()}\n"
    return out


def update_fact_model() -> tuple[dict[str, str], dict[str, str]]:
    text = FACT.read_text(encoding="utf-8-sig")
    packaged = r"C:\PowerBI Dashboard - KhoiPort\02_Apple_Finance\Data\sec-aapl-companyfacts.json"
    packaged_tmdl = packaged.replace("\\", "\\\\")
    text = re.sub(
        r'SourcePath = "[^"]+sec-aapl-companyfacts\.json"',
        lambda _: f'SourcePath = "{packaged_tmdl}"',
        text,
    )
    concept_anchor = '{"Liabilities", "Total Liabilities", "Balance", 9}'
    if '"Operating Cash Flow", "Cash Flow"' not in text:
        insert = concept_anchor + ''',
\t\t\t            {"NetCashProvidedByUsedInOperatingActivities", "Operating Cash Flow", "Cash Flow", 10},
\t\t\t            {"PaymentsToAcquirePropertyPlantAndEquipment", "Capital Expenditure", "Cash Flow", 11},
\t\t\t            {"PaymentsForRepurchaseOfCommonStock", "Share Repurchases", "Cash Flow", 12},
\t\t\t            {"PaymentsOfDividends", "Dividends Paid", "Cash Flow", 13}'''
        text = text.replace(concept_anchor, insert)

    kpi_map = {
        "KPI Revenue Display": ("KPI Revenue Value", "[Latest Revenue]", '$0.0,,,"B"'),
        "KPI Gross Profit Display": ("KPI Gross Profit Value", "[Latest Gross Profit]", '$0.0,,,"B"'),
        "KPI Operating Income Display": ("KPI Operating Income Value", "[Latest Operating Income]", '$0.0,,,"B"'),
        "KPI Net Income Display": ("KPI Net Income Value", "[Latest Net Income]", '$0.0,,,"B"'),
        "KPI Gross Margin Display": ("KPI Gross Margin Value", "[Latest Gross Margin]", "0.0%"),
        "KPI Operating Margin Display": ("KPI Operating Margin Value", "[Latest Operating Margin]", "0.0%"),
        "KPI Net Margin Display": ("KPI Net Margin Value", "[Latest Net Margin]", "0.0%"),
        "KPI Opex Ratio Display": ("KPI Opex Ratio Value", "[Latest Operating Expense Ratio]", "0.0%"),
        "KPI Assets Display": ("KPI Assets Value", "[Latest Assets]", '$0.0,,,"B"'),
        "KPI Liabilities Display": ("KPI Liabilities Value", "[Latest Liabilities]", '$0.0,,,"B"'),
        "KPI Cash Display": ("KPI Cash Value", "[Latest Cash]", '$0.0,,,"B"'),
        "KPI Liabilities to Assets Display": ("KPI Liabilities to Assets Value", "[Latest Liabilities to Assets]", "0.0%"),
        "KPI Cash Coverage Display": ("KPI Cash Coverage Value", "[Latest Cash Coverage]", "0.0%"),
        "KPI Cash to Assets Display": ("KPI Cash to Assets Value", "[Latest Cash to Assets]", "0.0%"),
    }
    delta_bases = {
        "Latest Assets YoY": "Latest Assets YoY", "Latest Liabilities YoY": "Latest Liabilities YoY",
        "Latest Cash YoY": "Latest Cash YoY", "Latest Liabilities to Assets Variance pp": "Latest Liabilities to Assets Variance pp",
        "Latest Cash to Assets Variance pp": "Latest Cash to Assets Variance pp", "Latest Revenue YoY": "Latest Revenue YoY",
        "Latest Gross Profit YoY": "Latest Gross Profit YoY", "Latest Operating Income YoY": "Latest Operating Income YoY",
        "Latest Net Income YoY": "Latest Net Income YoY", "Latest Gross Margin Variance pp": "Latest Gross Margin Variance pp",
        "Latest Operating Margin Variance pp": "Latest Operating Margin Variance pp", "Latest Net Margin Variance pp": "Latest Net Margin Variance pp",
        "Latest Opex Ratio Variance pp": "Latest Opex Ratio Variance pp",
    }
    delta_map = {f"KPI YoY Display {k}": f"KPI YoY Value {k}" for k in delta_bases}

    additions = ""
    existing_names = set(re.findall(r"^\s*measure\s+'([^']+)'", text, re.M))
    for _, (new, expr, fmt) in kpi_map.items():
        if new not in existing_names:
            additions += measure_block(new, expr, fmt, r"Display\KPI Numeric")
    delta_fmt = '"YoY: ▲ "0.0%;"YoY: ▼ "0.0%;"YoY: "0.0%'
    for old, new in delta_map.items():
        base = old.removeprefix("KPI YoY Display ")
        if new not in existing_names:
            additions += measure_block(new, f"[{base}]", delta_fmt, r"Display\KPI Delta Numeric")

    extra = {
        "Operating Cash Flow": ("CALCULATE ( [Finance Value], FactFinance[DisplayMetric] = \"Operating Cash Flow\", FactFinance[MetricClass] = \"Cash Flow\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Capital Expenditure": ("CALCULATE ( [Finance Value], FactFinance[DisplayMetric] = \"Capital Expenditure\", FactFinance[MetricClass] = \"Cash Flow\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Share Repurchases": ("CALCULATE ( [Finance Value], FactFinance[DisplayMetric] = \"Share Repurchases\", FactFinance[MetricClass] = \"Cash Flow\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Dividends Paid": ("CALCULATE ( [Finance Value], FactFinance[DisplayMetric] = \"Dividends Paid\", FactFinance[MetricClass] = \"Cash Flow\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Free Cash Flow": ("[Operating Cash Flow] - [Capital Expenditure]", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Total Capital Returned": ("[Share Repurchases] + [Dividends Paid]", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "FCF Margin": ("DIVIDE ( [Free Cash Flow], [Revenue] )", "0.0%", r"Finance\Cash Flow"),
        "Payout of FCF": ("DIVIDE ( [Total Capital Returned], [Free Cash Flow] )", "0.0%", r"Finance\Cash Flow"),
        "Cash Conversion": ("DIVIDE ( [Operating Cash Flow], [Net Income] )", "0.0%", r"Finance\Cash Flow"),
        "Quarterly Operating Cash Flow": ("CALCULATE ( [Operating Cash Flow], FactFinance[PeriodType] = \"Quarter\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly Capital Expenditure": ("CALCULATE ( [Capital Expenditure], FactFinance[PeriodType] = \"Quarter\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly Share Repurchases": ("CALCULATE ( [Share Repurchases], FactFinance[PeriodType] = \"Quarter\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly Dividends Paid": ("CALCULATE ( [Dividends Paid], FactFinance[PeriodType] = \"Quarter\" )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly Free Cash Flow": ("[Quarterly Operating Cash Flow] - [Quarterly Capital Expenditure]", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly Total Capital Returned": ("[Quarterly Share Repurchases] + [Quarterly Dividends Paid]", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Quarterly FCF Margin": ("DIVIDE ( [Quarterly Free Cash Flow], [Quarterly Revenue] )", "0.0%", r"Finance\Cash Flow"),
        "Quarterly Payout of FCF": ("DIVIDE ( [Quarterly Total Capital Returned], [Quarterly Free Cash Flow] )", "0.0%", r"Finance\Cash Flow"),
        "Latest Cash Flow Date": ("CALCULATE ( MAX ( FactFinance[EndDate] ), REMOVEFILTERS ( DimDate ), FactFinance[MetricClass] = \"Cash Flow\", FactFinance[PeriodType] = \"Quarter\" )", "yyyy-mm-dd", r"Finance\Cash Flow"),
        "Latest Operating Cash Flow": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Operating Cash Flow], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Capital Expenditure": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Capital Expenditure], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Share Repurchases": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Share Repurchases], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Dividends Paid": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Dividends Paid], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Free Cash Flow": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Free Cash Flow], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Total Capital Returned": ("VAR LatestDate = [Latest Cash Flow Date] RETURN CALCULATE ( [Quarterly Total Capital Returned], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = LatestDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest FCF Margin": ("DIVIDE ( [Latest Free Cash Flow], CALCULATE ( [Quarterly Revenue], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = [Latest Cash Flow Date] ) )", "0.0%", r"Finance\Cash Flow"),
        "Latest Payout of FCF": ("DIVIDE ( [Latest Total Capital Returned], [Latest Free Cash Flow] )", "0.0%", r"Finance\Cash Flow"),
        "Latest Cash Prior Quarter": ("VAR LatestDate = CALCULATE ( MAX ( FactFinance[EndDate] ), REMOVEFILTERS ( DimDate ), FactFinance[DisplayMetric] = \"Cash & Equivalents\" ) VAR PriorDate = CALCULATE ( MAX ( FactFinance[EndDate] ), REMOVEFILTERS ( DimDate ), FactFinance[DisplayMetric] = \"Cash & Equivalents\", FactFinance[EndDate] < LatestDate ) RETURN CALCULATE ( [Cash], REMOVEFILTERS ( DimDate ), FactFinance[EndDate] = PriorDate )", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Latest Other Cash Movement": ("[Latest Cash] - [Latest Cash Prior Quarter] - [Latest Operating Cash Flow] + [Latest Capital Expenditure] + [Latest Share Repurchases] + [Latest Dividends Paid]", '$#,0,,,"B"', r"Finance\Cash Flow"),
        "Cash Flow Bridge Value": ("SWITCH ( SELECTEDVALUE ( CashFlowBridge[Step] ), \"Opening Cash\", [Latest Cash Prior Quarter], \"Operating Cash Flow\", [Latest Operating Cash Flow], \"Capital Expenditure\", - [Latest Capital Expenditure], \"Share Repurchases\", - [Latest Share Repurchases], \"Dividends\", - [Latest Dividends Paid], \"Other Cash Movement\", [Latest Other Cash Movement] )", '$#,0,,,"B"', r"Finance\Bridge"),
        "Cash Flow Bridge Reconciliation Check": ("[Latest Cash Prior Quarter] + [Latest Operating Cash Flow] - [Latest Capital Expenditure] - [Latest Share Repurchases] - [Latest Dividends Paid] + [Latest Other Cash Movement] - [Latest Cash]", '$#,0', r"Finance\QA"),
        "Latest Capital Component Amount": ("SWITCH ( SELECTEDVALUE ( CapitalStructure[Component] ), \"Liabilities\", [Latest Liabilities], \"Net Assets\", [Latest Net Asset Position] )", '$#,0,,,"B"', r"Finance\Balance Sheet"),
        "Latest Capital Component Ratio": ("DIVIDE ( [Latest Capital Component Amount], [Latest Assets] )", "0.0%", r"Finance\Balance Sheet"),
        "Latest Cost of Sales PY Amount": ("[Latest Revenue Previous Year] - [Latest Gross Profit Previous Year]", '$#,0,,,"B"', r"Finance\Bridge"),
        "Latest Operating Expenses PY Amount": ("[Latest Gross Profit Previous Year] - [Latest Operating Income Previous Year]", '$#,0,,,"B"', r"Finance\Bridge"),
        "Latest Other and Tax PY Amount": ("[Latest Operating Income Previous Year] - [Latest Net Income Previous Year]", '$#,0,,,"B"', r"Finance\Bridge"),
        "Net Income Bridge Value": ("SWITCH ( SELECTEDVALUE ( NetIncomeBridge[Step] ), \"Prior-year Net Income\", [Latest Net Income Previous Year], \"Revenue impact\", [Latest Revenue] - [Latest Revenue Previous Year], \"Cost of Sales impact\", - ( [Latest Cost of Sales Amount] - [Latest Cost of Sales PY Amount] ), \"Operating Expense impact\", - ( [Latest Operating Expenses Amount] - [Latest Operating Expenses PY Amount] ), \"Other & Tax impact\", - ( [Latest Other and Tax Amount] - [Latest Other and Tax PY Amount] ) )", '$#,0,,,"B"', r"Finance\Bridge"),
        "Net Income Bridge Reconciliation Check": ("[Latest Net Income Previous Year] + ( [Latest Revenue] - [Latest Revenue Previous Year] ) - ( [Latest Cost of Sales Amount] - [Latest Cost of Sales PY Amount] ) - ( [Latest Operating Expenses Amount] - [Latest Operating Expenses PY Amount] ) - ( [Latest Other and Tax Amount] - [Latest Other and Tax PY Amount] ) - [Latest Net Income]", '$#,0', r"Finance\QA"),
        "Header As Of Label": ("\"Data through \" & FORMAT ( MAX ( DimDate[Date] ), \"MMM yyyy\" )", None, r"Display\Context"),
        "Last Refresh Label": ("\"Refreshed \" & FORMAT ( MAX ( LastRefresh[RefreshedAt] ), \"dd MMM yyyy HH:mm\" ) & \" UTC\"", None, r"Display\Context"),
        "Header Context Label": ("[Header As Of Label] & \" · \" & [Last Refresh Label]", None, r"Display\Context"),
    }
    # Header As Of Label was added in Round 1; replace its expression, do not duplicate.
    text = re.sub(r"\n\tmeasure 'Header As Of Label'.*?(?=\n\t(?:measure|column) )", "\n", text, flags=re.S)
    existing_names = set(re.findall(r"^\s*measure\s+'([^']+)'", text, re.M))
    for name, (expr, fmt, folder) in extra.items():
        if name not in existing_names:
            additions += measure_block(name, expr, fmt, folder)

    text = text.replace("\n\tcolumn Company", additions + "\n\tcolumn Company")
    # Remove the old string measures after report bindings are replaced below.
    string_names = set(kpi_map) | set(delta_map)
    for name in string_names:
        text = re.sub(rf"\n\tmeasure '{re.escape(name)}'.*?(?=\n\t(?:measure|column) )", "\n", text, flags=re.S)
    text = text.replace('"#777777"', '"#4A6663"')
    FACT.write_text(text, encoding="utf-8")
    return {old: new for old, (new, _, _) in kpi_map.items()}, delta_map


def replace_measure_binding(data: dict, old: str, new: str) -> None:
    def walk(node):
        if isinstance(node, dict):
            for key, value in list(node.items()):
                if isinstance(value, str):
                    node[key] = value.replace(old, new)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(data)


def bind_numeric_cards(kpi_map: dict[str, str], delta_map: dict[str, str]) -> None:
    combined = {**kpi_map, **delta_map}
    for path in PAGES.glob("*/visuals/*/visual.json"):
        data = read_json(path)
        if data.get("visual", {}).get("visualType") != "cardVisual":
            continue
        raw = json.dumps(data)
        for old, new in combined.items():
            if old in raw:
                replace_measure_binding(data, old, new)
                r1.set_alt_text(data, "Numeric financial KPI card for " + new.replace("KPI ", ""))
                raw = json.dumps(data)
        write_json(path, data)


def add_units_and_contrast() -> None:
    currency = {
        ("FinancePage", "FinancePage_Chart1"), ("FinancePage", "FinancePage_Chart2"),
        ("BalanceLiquidityPage", "Chart2"),
    }
    ratio = {("ProfitabilityGrowthPage", "Chart1")}
    for page, visual in currency | ratio:
        path = PAGES / page / "visuals" / visual / "visual.json"
        data = read_json(path)
        objects = data["visual"].setdefault("objects", {})
        labels = objects.setdefault("labels", [{"properties": {}}])
        props = labels[0].setdefault("properties", {})
        props["show"] = lit("true")
        if (page, visual) in currency:
            props["labelDisplayUnits"] = lit("1000000000D")
            props["labelPrecision"] = lit("1D")
            axis = objects.setdefault("valueAxis", [{"properties": {}}])
            axis[0].setdefault("properties", {})["labelDisplayUnits"] = lit("1000000000D")
            axis[0]["properties"]["labelPrecision"] = lit("1D")
        write_json(path, data)
    theme = REPORT / "StaticResources" / "RegisteredResources" / "BusinessPulseTheme.json"
    data = read_json(theme)
    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and v == "#829A97" and k in {"neutral", "foregroundNeutralSecondary"}:
                    node[k] = "#4A6663"
                else:
                    walk(v)
        elif isinstance(node, list):
            for x in node: walk(x)
    walk(data)
    write_json(theme, data)


def convert_capital_structure() -> None:
    path = PAGES / "BalanceLiquidityPage" / "visuals" / "Chart1" / "visual.json"
    data = read_json(path)
    data["visual"]["visualType"] = "clusteredBarChart"
    data["visual"]["query"] = {"queryState": {
        "Category": {"projections": [column_proj("CapitalStructure", "Component", "Capital component")]},
        "Y": {"projections": [measure_proj("Latest Capital Component Ratio", "% of Assets")]},
    }}
    data["visual"]["objects"] = r1.axis_objects(False, True)
    data["visual"]["objects"]["dataPoint"] = [{"properties": {"fill": {"solid": {"color": lit("'#0F766E'")}}}}]
    data["filterConfig"] = {"filters": [
        r1.filter_item("Column", "CapitalStructure", "Component", "Categorical"),
        r1.filter_item("Measure", "FactFinance", "Latest Capital Component Ratio", "Advanced"),
    ]}
    r1.set_title(data, "Capital Structure | Liabilities vs Net Assets (% of Assets)")
    r1.set_alt_text(data, "Capital structure split between liabilities and net assets as a percentage of total assets.")
    write_json(path, data)


def create_waterfall() -> None:
    path = PAGES / "FinancePage" / "visuals" / "FinancePage_Chart5" / "visual.json"
    data = read_json(path)
    data["visual"]["visualType"] = "waterfallChart"
    data["visual"]["query"] = {"queryState": {
        "Category": {"projections": [column_proj("NetIncomeBridge", "Step", "Bridge step")]},
        "Y": {"projections": [measure_proj("Net Income Bridge Value", "Net income impact")]},
    }}
    data["visual"]["objects"] = r1.axis_objects(False, True)
    data["visual"]["objects"]["labels"][0]["properties"]["labelDisplayUnits"] = lit("1000000000D")
    data["visual"]["objects"]["labels"][0]["properties"]["labelPrecision"] = lit("1D")
    data["visual"]["objects"]["valueAxis"][0]["properties"]["labelDisplayUnits"] = lit("1000000000D")
    data["visual"]["objects"]["valueAxis"][0]["properties"]["labelPrecision"] = lit("1D")
    r1.set_title(data, "Net Income Bridge | What Changed vs Prior Year")
    r1.set_alt_text(data, "Waterfall reconciling prior-year net income to current net income through revenue, cost, operating expense, and other-and-tax impacts.")
    data["filterConfig"] = {"filters": [r1.filter_item("Column", "NetIncomeBridge", "Step", "Categorical"), r1.filter_item("Measure", "FactFinance", "Net Income Bridge Value", "Advanced")]}
    write_json(path, data)


def create_header_context(page: str, template_visual: Path) -> None:
    folder = PAGES / page / "visuals" / "HeaderContext"
    folder.mkdir(exist_ok=True)
    data = read_json(template_visual)
    data["name"] = uuid.uuid4().hex[:20]
    data["position"] = {"x": 300, "y": 15, "z": 50000, "width": 285, "height": 36, "tabOrder": 200}
    visual = data["visual"]
    visual["visualType"] = "cardVisual"
    visual["query"] = {"queryState": {"Data": {"projections": [measure_proj("Header Context Label", "Reporting context")]}}}
    visual["objects"] = {
        "label": [{"properties": {"show": lit("false")}, "selector": {"id": "default"}}],
        "value": [{"properties": {"fontSize": lit("9D"), "fontColor": {"solid": {"color": lit("'#FFFFFF'")}}, "fontFamily": lit("'Segoe UI'")}, "selector": {"id": "default"}}],
        "fillCustom": [{"properties": {"show": lit("false")}}],
        "outline": [{"properties": {"show": lit("false")}, "selector": {"id": "default"}}],
    }
    visual["visualContainerObjects"] = {
        "title": [{"properties": {"show": lit("false")}}],
        "background": [{"properties": {"show": lit("false")}}],
        "border": [{"properties": {"show": lit("false")}}],
        "dropShadow": [{"properties": {"show": lit("false")}}],
        "general": [{"properties": {"altText": lit("'Dynamic data-through date and refresh timestamp.'")}}],
    }
    write_json(folder / "visual.json", data)


def reframe_and_accessibility() -> None:
    headers = {
        "FinancePage": "APPLE INC. | SEC FILINGS OVERVIEW",
        "ProfitabilityGrowthPage": "APPLE INC. | PROFITABILITY FROM SEC FILINGS",
        "BalanceLiquidityPage": "APPLE INC. | BALANCE & LIQUIDITY FROM SEC FILINGS",
    }
    template = PAGES / "FinancePage" / "visuals" / "FinancePage_Delta1" / "visual.json"
    for page, text in headers.items():
        prefix = "FinancePage_" if page == "FinancePage" else ""
        hpath = PAGES / page / "visuals" / f"{prefix}Header" / "visual.json"
        h = read_json(hpath)
        raw = json.dumps(h)
        raw = re.sub(r"APPLE FINANCIAL HEALTH \| [^\\\"]+", text, raw)
        h = json.loads(raw)
        r1.set_alt_text(h, text)
        write_json(hpath, h)
        create_header_context(page, template)

        # Source footer is a transparent card using a dynamic-free attribution string encoded as the card label.
        fdir = PAGES / page / "visuals" / "SourceFooter"
        fdir.mkdir(exist_ok=True)
        foot = read_json(template)
        foot["name"] = uuid.uuid4().hex[:20]
        foot["position"] = {"x": 65, "y": 696, "z": 51000, "width": 1190, "height": 20, "tabOrder": 9900}
        foot["visual"]["query"] = {"queryState": {"Data": {"projections": [measure_proj("Source Attribution", "Source")]}}}
        foot["visual"]["visualContainerObjects"] = {"title": [{"properties": {"show": lit("false")}}], "background": [{"properties": {"show": lit("false")}}], "border": [{"properties": {"show": lit("false")}}], "dropShadow": [{"properties": {"show": lit("false")}}], "general": [{"properties": {"altText": lit("'Source attribution for Apple SEC filings.'")}}]}
        foot["visual"]["objects"] = {"label": [{"properties": {"show": lit("false")}, "selector": {"id": "default"}}], "value": [{"properties": {"fontSize": lit("9D"), "fontColor": {"solid": {"color": lit("'#4A6663'")}}}, "selector": {"id": "default"}}]}
        write_json(fdir / "visual.json", foot)

    # Every visual gets an accessibility description; decorative rail may be empty.
    for path in PAGES.glob("*/visuals/*/visual.json"):
        data = read_json(path)
        typ = data.get("visual", {}).get("visualType", "visual")
        name = path.parent.name
        if name.endswith("Rail") or name == "Rail":
            desc = ""
        elif typ == "pageNavigator":
            desc = "Navigate between financial analysis pages."
        elif typ == "slicer":
            desc = "Filter the report using this financial reporting field."
        elif typ == "actionButton":
            desc = "Clear all filters on this page."
        else:
            desc = r1.title_text(data) or f"Apple financial report {typ}."
        r1.set_alt_text(data, desc)
        write_json(path, data)


def narrow_rail_and_expand() -> None:
    for page in ("FinancePage", "ProfitabilityGrowthPage", "BalanceLiquidityPage"):
        prefix = "FinancePage_" if page == "FinancePage" else ""
        base = PAGES / page / "visuals"
        # Rail and navigator become compact; filters move into the header row.
        for name, pos in {
            f"{prefix}Rail": {"x": 8, "y": 75, "width": 48, "height": 620},
            f"{prefix}Navigator": {"x": 8, "y": 90, "width": 48, "height": 246},
            f"{prefix}Filter1": {"x": 600, "y": 8, "width": 135, "height": 49},
            f"{prefix}Filter2": {"x": 745, "y": 8, "width": 135, "height": 49},
            f"{prefix}Filter3": {"x": 890, "y": 8, "width": 135, "height": 49},
            f"{prefix}PrimarySlicer": {"x": 1035, "y": 8, "width": 220, "height": 49},
            f"{prefix}Clear": {"x": 8, "y": 654, "width": 48, "height": 34},
        }.items():
            path = base / name / "visual.json"
            data = read_json(path)
            data["position"].update(pos)
            write_json(path, data)

        # Scale all data visuals from old content range [189.5,1255] into [70,1255].
        old_start, old_end, new_start, new_end = 189.5, 1255.0, 70.0, 1255.0
        scale = (new_end - new_start) / (old_end - old_start)
        for path in base.glob("*/visual.json"):
            if path.parent.name in {f"{prefix}Rail", f"{prefix}Navigator", f"{prefix}Filter1", f"{prefix}Filter2", f"{prefix}Filter3", f"{prefix}PrimarySlicer", f"{prefix}Clear", f"{prefix}Header", "HeaderContext", "SourceFooter"}:
                continue
            data = read_json(path); pos = data.get("position", {})
            x = pos.get("x", 0); w = pos.get("width", 0)
            if x >= old_start:
                pos["x"] = round(new_start + (x - old_start) * scale, 1)
                pos["width"] = round(w * scale, 1)
            write_json(path, data)

    # Coherent tab sequence based on visual role and position.
    for page in PAGES.iterdir():
        if not page.is_dir(): continue
        for path in page.glob("visuals/*/visual.json"):
            data = read_json(path); name = path.parent.name; pos = data.get("position", {})
            if "Header" in name: order = 100
            elif "Slicer" in name or "Filter" in name: order = 200 + int(pos.get("x", 0))
            elif "KPI" in name or "Delta" in name or "Spark" in name: order = 2000 + int(pos.get("x", 0))
            elif "Chart" in name: order = 5000 + int(pos.get("y", 0))*2 + int(pos.get("x", 0))
            else: order = 9000 + int(pos.get("y", 0))
            pos["tabOrder"] = order
            write_json(path, data)


def add_source_measure() -> None:
    text = FACT.read_text(encoding="utf-8-sig")
    if "measure 'Source Attribution'" not in text:
        block = measure_block("Source Attribution", '"Source: Apple Inc. 10-K / 10-Q filings, SEC EDGAR"', None, r"Display\Context")
        text = text.replace("\n\tcolumn Company", block + "\n\tcolumn Company")
        FACT.write_text(text, encoding="utf-8")


def create_cash_flow_page() -> None:
    source = PAGES / "ProfitabilityGrowthPage"
    target = PAGES / "CashFlowCapitalReturnsPage"
    existing_page_name = None
    if target.exists():
        existing_page_name = read_json(target / "page.json").get("name")
        shutil.rmtree(target)
    shutil.copytree(source, target)
    page = read_json(target / "page.json")
    page["name"] = existing_page_name or uuid.uuid4().hex[:20]
    page["displayName"] = "Cash Flow & Capital Returns"
    write_json(target / "page.json", page)
    # Fresh visual ids and folders.
    visual_root = target / "visuals"
    for folder in list(visual_root.iterdir()):
        data = read_json(folder / "visual.json")
        new_id = uuid.uuid4().hex[:20]
        data["name"] = new_id
        write_json(folder / "visual.json", data)

    # Header wording.
    h = read_json(visual_root / "Header" / "visual.json")
    raw = json.dumps(h).replace("APPLE INC. | PROFITABILITY FROM SEC FILINGS", "APPLE INC. | CASH FLOW & CAPITAL RETURNS")
    write_json(visual_root / "Header" / "visual.json", json.loads(raw))
    # KPI cards and sparklines. Delta visuals are hidden because distinct cash-flow YoY measures are not added here.
    kpis = [
        ("Latest Operating Cash Flow", "Operating Cash Flow"), ("Latest Free Cash Flow", "Free Cash Flow"),
        ("Latest FCF Margin", "FCF Margin"), ("Latest Total Capital Returned", "Total Capital Returned"), ("Latest Payout of FCF", "Payout of FCF"),
    ]
    spark_measures = ["Quarterly Operating Cash Flow", "Quarterly Free Cash Flow", "Quarterly FCF Margin", "Quarterly Total Capital Returned", "Quarterly Payout of FCF"]
    for i, (measure, label) in enumerate(kpis, 1):
        path = visual_root / f"KPI{i}" / "visual.json"; data = read_json(path)
        data["visual"]["query"] = {"queryState": {"Data": {"projections": [measure_proj(measure, label)]}}}
        r1.set_alt_text(data, label + " KPI from Apple SEC cash-flow filings.")
        write_json(path, data)
        sp = visual_root / f"Spark{i}" / "visual.json"; s = read_json(sp)
        spark_measure = spark_measures[i - 1]
        s["visual"]["query"] = {"queryState": {"Category": {"projections": [column_proj("DimDate", "Date", "Quarter")]}, "Y": {"projections": [measure_proj(spark_measure, label)]}}}
        write_json(sp, s)
        dp = visual_root / f"Delta{i}" / "visual.json"; d = read_json(dp); d["position"]["height"] = 0; d["position"]["width"] = 0; write_json(dp, d)

    charts = {
        "Chart1": ("waterfallChart", "Cash Bridge | Opening Cash to Closing Cash", ["Cash Flow Bridge Value"]),
        "Chart2": ("lineChart", "Earnings Quality | Operating Cash Flow vs Net Income", ["Quarterly Operating Cash Flow", "Quarterly Net Income"]),
        "Chart3": ("lineChart", "Free Cash Flow Margin | Quarterly Trend", ["Quarterly FCF Margin"]),
        "Chart4": ("clusteredColumnChart", "Capital Returns | Buybacks vs Dividends", ["Quarterly Share Repurchases", "Quarterly Dividends Paid"]),
    }
    for name, (typ, title, measures) in charts.items():
        path = visual_root / name / "visual.json"; data = read_json(path); data["visual"]["visualType"] = typ
        if name == "Chart1":
            data["visual"]["query"] = {"queryState": {"Category": {"projections": [column_proj("CashFlowBridge", "Step", "Cash bridge step")]}, "Y": {"projections": [measure_proj("Cash Flow Bridge Value", "Cash movement")]}}}
        else:
            data["visual"]["query"] = {"queryState": {"Category": {"projections": [column_proj("DimDate", "Date", "Quarter")]}, "Y": {"projections": [measure_proj(m, m) for m in measures]}}}
        data["visual"]["objects"] = r1.axis_objects(len(measures)>1, False)
        for axis_name in ("valueAxis", "categoryAxis"):
            if axis_name in data["visual"]["objects"]:
                data["visual"]["objects"][axis_name][0]["properties"]["title"] = {"expr": {"Literal": {"Value": "false"}}}
        if name in {"Chart1", "Chart2", "Chart4"}:
            labels = data["visual"]["objects"].setdefault("labels", [{"properties": {}}])
            label_props = labels[0].setdefault("properties", {})
            label_props["show"] = lit("true")
            label_props["labelDisplayUnits"] = lit("1000000000D")
            label_props["labelPrecision"] = lit("1D")
            value_axis = data["visual"]["objects"].setdefault("valueAxis", [{"properties": {}}])
            axis_props = value_axis[0].setdefault("properties", {})
            axis_props["labelDisplayUnits"] = lit("1000000000D")
            axis_props["labelPrecision"] = lit("1D")
        r1.set_title(data, title); r1.set_alt_text(data, title + " using reported SEC cash-flow values.")
        if name == "Chart1":
            data["filterConfig"] = {"filters": [r1.filter_item("Column", "CashFlowBridge", "Step", "Categorical"), r1.filter_item("Measure", "FactFinance", "Cash Flow Bridge Value", "Advanced")]}
        else:
            data["filterConfig"] = {"filters": [r1.filter_item("Column", "DimDate", "Date", "Categorical")] + [r1.filter_item("Measure", "FactFinance", m, "Advanced") for m in measures]}
        write_json(path, data)
    # Table max five columns.
    t = visual_root / "Chart5" / "visual.json"; data = read_json(t); data["visual"]["visualType"] = "tableEx"
    data["visual"]["query"] = {"queryState": {"Values": {"projections": [column_proj("DimDate", "Date", "Quarter")] + [measure_proj(m,m) for m in ["Quarterly Operating Cash Flow","Quarterly Capital Expenditure","Quarterly Free Cash Flow","Quarterly Payout of FCF"]]}}}
    r1.set_title(data, "Quarterly Cash Flow & Payout Detail"); r1.set_alt_text(data, "Quarterly operating cash flow, capital expenditure, free cash flow and payout ratio.")
    write_json(t, data)

    pages_meta = read_json(PAGES / "pages.json")
    if page["name"] not in pages_meta["pageOrder"]:
        pages_meta["pageOrder"].append(page["name"])
    write_json(PAGES / "pages.json", pages_meta)


def main() -> None:
    write_dimensions()
    kpi_map, delta_map = update_fact_model()
    add_source_measure()
    bind_numeric_cards(kpi_map, delta_map)
    add_units_and_contrast()
    convert_capital_structure()
    create_waterfall()
    reframe_and_accessibility()
    narrow_rail_and_expand()
    create_cash_flow_page()
    # Run accessibility once more so the cloned page and its controls are covered.
    reframe_and_accessibility()
    print("Round 2 changes applied to canonical Apple Finance PBIP.")


if __name__ == "__main__":
    main()
