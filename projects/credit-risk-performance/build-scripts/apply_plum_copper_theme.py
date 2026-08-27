from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "FinTech_Credit_Risk.Report"

# A distinct editorial palette: plum structure, smoky blue analysis,
# copper emphasis, sage positive state, and warm ivory surfaces.
COLORS = {
    "#0B3954": "#4B2142",
    "#087E8B": "#D98324",
    "#5BC0BE": "#7A9E7E",
    "#FF5A5F": "#C94C4C",
    "#F2B134": "#E1A948",
    "#6C63FF": "#8A6FA8",
    "#8FA3B8": "#9A8C83",
    "#D9E2EC": "#DED6CE",
    "#F5F8FC": "#FAF7F2",
    "#102A43": "#2B2230",
    "#23A776": "#6E9674",
    "#486581": "#746B75",
    "#FF6B6B": "#D98324",
    "#60627A": "#746B75",
    "#25263A": "#2B2230",
    "#35A7C7": "#5B6C8F",
    "#F25F5C": "#C94C4C",
    "#25C2A0": "#6E9674",
    "#7B61FF": "#8A6FA8",
    "#EEF3F8": "#F1EAE4",
    "#B8C4D2": "#CEC4BB",
}


def recolor(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in COLORS.items():
        updated = updated.replace(old, new)
    updated = updated.replace(
        "FinTech Risk Control — Deep Navy & Coral",
        "FinTech Risk Control — Plum, Copper & Ivory",
    )
    updated = updated.replace(
        "Ocean Amber Template A — extracted from read-only reference",
        "Plum Copper Editorial — original CP2 redesign",
    )
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


changed = []
for file in REPORT.rglob("*.json"):
    if recolor(file):
        changed.append(file.relative_to(ROOT).as_posix())

# Keep the refinement utility aligned with the delivered report palette.
refiner = ROOT / "refine_customer_and_trends.py"
if refiner.exists() and recolor(refiner):
    changed.append(refiner.name)

print(f"Applied Plum/Copper/Ivory theme to {len(changed)} files.")
for item in changed:
    print(item)
