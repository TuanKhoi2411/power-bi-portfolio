from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, _tree


ROOT = Path(r"C:\Users\ADMIN\Downloads\CP2 - New")
SOURCE = ROOT / "CreditRisk_Data.csv"
IMPORTANCE_OUT = ROOT / "risk_driver_importance.csv"
RULES_OUT = ROOT / "risk_rule_summary.csv"
SUMMARY_OUT = ROOT / "risk_model_summary.txt"


def prepare() -> pd.DataFrame:
    df = pd.read_csv(SOURCE, low_memory=False)
    df["TermMonths"] = df["term"].str.strip().str.extract(r"(\d+)").astype(float)
    df["LoanDate"] = pd.to_datetime(df["loan_issue_date"] + "-01")
    df["ExpectedRepayment"] = df["installment"] * df["TermMonths"]
    df["RecoveryRate"] = np.where(
        df["ExpectedRepayment"].gt(0),
        df["total_pymnt"] / df["ExpectedRepayment"],
        np.nan,
    )
    analysis_month = 2014 * 12 + 12
    loan_month = df["LoanDate"].dt.year * 12 + df["LoanDate"].dt.month
    df["LoanAgeMonths"] = analysis_month - loan_month + 1
    df["PctLoanAge"] = df["LoanAgeMonths"] / df["TermMonths"]
    adverse = df["loan_status"].isin(
        ["Charged Off", "Default", "Late (31-120 days)", "Late (16-30 days)"]
    )
    df["LoanLabel"] = np.select(
        [
            df["loan_status"].eq("Fully Paid"),
            adverse & df["RecoveryRate"].gt(0.70),
            df["loan_status"].eq("Current") & df["PctLoanAge"].gt(0.40),
            adverse & df["RecoveryRate"].lt(0.40),
        ],
        ["Good", "Good", "Good", "Bad"],
        default="Neutral",
    )
    df["Seasoned"] = df["PctLoanAge"].gt(0.40)
    return df


def aggregate_importance(transformed_names: np.ndarray, values: np.ndarray, numeric, categorical):
    totals = {name: 0.0 for name in [*numeric, *categorical]}
    for name, value in zip(transformed_names, values):
        clean = name.split("__", 1)[-1]
        matched = next((c for c in categorical if clean.startswith(c + "_")), None)
        if matched is None:
            matched = next((c for c in numeric if clean == c), clean)
        totals[matched] = totals.get(matched, 0.0) + float(value)
    return totals


def format_condition(feature: str, threshold: float, left: bool) -> str:
    labels = {
        "TermMonths": "Term months",
        "interest_rate": "Interest rate",
        "annual_income": "Annual income",
        "debt_to_income_ratio": "DTI",
        "loan_amount": "Loan amount",
        "delinquencies_2yrs": "Delinquencies",
        "public_record": "Public records",
        "GradeScore": "Grade score",
        "Verified": "Income verified",
    }
    op = "<=" if left else ">"
    if feature in {"interest_rate", "debt_to_income_ratio"}:
        value = f"{threshold:.1f}%"
    elif feature in {"annual_income", "loan_amount"}:
        value = f"${threshold:,.0f}"
    else:
        value = f"{threshold:.1f}"
    return f"{labels.get(feature, feature)} {op} {value}"


def tree_leaf_rules(model: DecisionTreeClassifier, columns: list[str], frame: pd.DataFrame):
    tree = model.tree_
    leaves = []

    def walk(node: int, conditions: list[str]):
        if tree.feature[node] != _tree.TREE_UNDEFINED:
            feature = columns[tree.feature[node]]
            threshold = tree.threshold[node]
            walk(tree.children_left[node], conditions + [format_condition(feature, threshold, True)])
            walk(tree.children_right[node], conditions + [format_condition(feature, threshold, False)])
            return
        mask = np.ones(len(frame), dtype=bool)
        # Reapply the path using the model itself to avoid parsing display strings.
        leaf_id = model.apply(frame[columns].to_numpy())
        mask = leaf_id == node
        loans = int(mask.sum())
        if loans == 0:
            return
        bad = int(frame.loc[mask, "IsBad"].sum())
        bad_rate = bad / loans
        leaves.append((" AND ".join(conditions), loans, bad, bad_rate))

    walk(0, [])
    return leaves


def main() -> None:
    df = prepare()
    eligible = df.loc[df["Seasoned"]].copy()
    eligible["IsBad"] = eligible["LoanLabel"].eq("Bad").astype(int)
    base_bad_rate = eligible["IsBad"].mean()

    numeric = [
        "loan_amount",
        "TermMonths",
        "interest_rate",
        "annual_income",
        "debt_to_income_ratio",
        "delinquencies_2yrs",
        "public_record",
    ]
    categorical = [
        "grade",
        "home_ownership",
        "income_verification_status",
        "purpose",
    ]
    x = eligible[numeric + categorical]
    y = eligible["IsBad"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42, stratify=y
    )
    prep = ColumnTransformer(
        [
            ("num", Pipeline([("imputer", SimpleImputer(strategy="median"))]), numeric),
            (
                "cat",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical,
            ),
        ]
    )
    forest = RandomForestClassifier(
        n_estimators=250,
        max_depth=10,
        min_samples_leaf=75,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1,
    )
    pipe = Pipeline([("prep", prep), ("model", forest)])
    pipe.fit(x_train, y_train)
    auc = roc_auc_score(y_test, pipe.predict_proba(x_test)[:, 1])
    names = pipe.named_steps["prep"].get_feature_names_out()
    totals = aggregate_importance(names, pipe.named_steps["model"].feature_importances_, numeric, categorical)
    label_map = {
        "loan_amount": "Loan Amount",
        "TermMonths": "Loan Term",
        "interest_rate": "Interest Rate",
        "annual_income": "Annual Income",
        "debt_to_income_ratio": "Debt-to-Income Ratio",
        "delinquencies_2yrs": "Delinquencies",
        "public_record": "Public Records",
        "grade": "Credit Grade",
        "home_ownership": "Home Ownership",
        "income_verification_status": "Income Verification",
        "purpose": "Loan Purpose",
    }
    importance = pd.DataFrame(
        [{"Driver": label_map.get(k, k), "Importance": v} for k, v in totals.items()]
    ).sort_values("Importance", ascending=False)
    importance["Rank"] = np.arange(1, len(importance) + 1)
    importance["ModelAUC"] = auc
    importance.to_csv(IMPORTANCE_OUT, index=False)

    grade_score = {g: i for i, g in enumerate("ABCDEFG", start=1)}
    tree_frame = eligible.copy()
    tree_frame["GradeScore"] = tree_frame["grade"].map(grade_score).fillna(0)
    tree_frame["Verified"] = (~tree_frame["income_verification_status"].eq("Not Verified")).astype(int)
    tree_features = [
        "TermMonths",
        "interest_rate",
        "annual_income",
        "debt_to_income_ratio",
        "loan_amount",
        "delinquencies_2yrs",
        "public_record",
        "GradeScore",
        "Verified",
    ]
    tree_frame[tree_features] = tree_frame[tree_features].fillna(tree_frame[tree_features].median())
    tree_model = DecisionTreeClassifier(
        max_depth=4,
        min_samples_leaf=300,
        class_weight="balanced",
        random_state=42,
    )
    tree_model.fit(tree_frame[tree_features], tree_frame["IsBad"])
    leaves = sorted(tree_leaf_rules(tree_model, tree_features, tree_frame), key=lambda x: (x[3], x[1]), reverse=True)

    rules = []

    def add_rule(name: str, source: str, mask: pd.Series):
        loans = int(mask.sum())
        bad = int(eligible.loc[mask, "IsBad"].sum()) if loans else 0
        rate = bad / loans if loans else 0.0
        rules.append(
            {
                "Rule": name,
                "RuleSource": source,
                "Loans": loans,
                "BadLoans": bad,
                "BadRate": rate,
                "LiftVsSeasonedPortfolio": rate / base_bad_rate if base_bad_rate else 0.0,
            }
        )

    add_rule(
        "Income < $30K AND interest > 17% AND grade E/F/G",
        "Assignment hypothesis",
        eligible["annual_income"].lt(30000)
        & eligible["interest_rate"].gt(17)
        & eligible["grade"].isin(["E", "F", "G"]),
    )
    add_rule(
        "Term = 60 months AND grade C",
        "Assignment example",
        eligible["TermMonths"].eq(60) & eligible["grade"].eq("C"),
    )
    for idx, (rule, loans, bad, rate) in enumerate(leaves[:4], start=1):
        rules.append(
            {
                "Rule": rule,
                "RuleSource": f"Decision tree leaf {idx}",
                "Loans": loans,
                "BadLoans": bad,
                "BadRate": rate,
                "LiftVsSeasonedPortfolio": rate / base_bad_rate if base_bad_rate else 0.0,
            }
        )
    pd.DataFrame(rules).sort_values("LiftVsSeasonedPortfolio", ascending=False).to_csv(RULES_OUT, index=False)

    SUMMARY_OUT.write_text(
        "\n".join(
            [
                f"Source rows: {len(df):,}",
                f"Seasoned rows (>40% term): {len(eligible):,}",
                f"Seasoned bad loans: {eligible['IsBad'].sum():,}",
                f"Seasoned bad-loan rate: {base_bad_rate:.6%}",
                f"Random-forest holdout AUC: {auc:.4f}",
            ]
        ),
        encoding="utf-8",
    )
    print(SUMMARY_OUT.read_text(encoding="utf-8"))
    print("\nTop drivers")
    print(importance.head(8).to_string(index=False))
    print("\nRules")
    print(pd.DataFrame(rules).sort_values("LiftVsSeasonedPortfolio", ascending=False).to_string(index=False))


if __name__ == "__main__":
    main()
