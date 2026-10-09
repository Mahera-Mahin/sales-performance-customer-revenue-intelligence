
import json
from pathlib import Path

import pandas as pd


# --------------------------------------------------
# 1. Define project paths
# --------------------------------------------------

BASE = Path(__file__).resolve().parents[1]

RAW_FILE = BASE / "data" / "raw" / "sales_transactions.csv"
PROCESSED_DIR = BASE / "data" / "processed"

ANALYTICS_FILE = PROCESSED_DIR / "sales_analytics.csv"
SUMMARY_FILE = PROCESSED_DIR / "kpi_summary.json"


# --------------------------------------------------
# 2. Validate input file and required columns
# --------------------------------------------------

if not RAW_FILE.exists():
    raise FileNotFoundError(
        f"Raw sales dataset not found: {RAW_FILE}"
    )

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW_FILE)

required_columns = [
    "order_id",
    "order_date",
    "customer_id",
    "customer_name",
    "segment",
    "industry",
    "region",
    "city",
    "salesperson",
    "product_name",
    "category",
    "units",
    "unit_price",
    "discount_pct",
    "gross_sales",
    "net_sales",
    "cost",
    "gross_margin",
    "order_status",
    "allocated_target",
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print(f"Loaded raw dataset: {len(df):,} rows")


# --------------------------------------------------
# 3. Prepare date-based analytical columns
# --------------------------------------------------

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="raise"
)

df["year"] = df["order_date"].dt.year

df["month_num"] = df["order_date"].dt.month

df["month"] = (
    df["order_date"]
    .dt.to_period("M")
    .astype(str)
)

df["quarter"] = (
    "Q" + df["order_date"].dt.quarter.astype(str)
)


# --------------------------------------------------
# 4. Calculate margin and target metrics
# --------------------------------------------------

df["margin_pct"] = (
    df["gross_margin"]
    / df["net_sales"].where(df["net_sales"] != 0)
)

df["target_variance"] = (
    df["net_sales"] - df["allocated_target"]
)

df["target_attainment_pct"] = (
    df["net_sales"]
    / df["allocated_target"].where(
        df["allocated_target"] != 0
    )
)


# --------------------------------------------------
# 5. Export the prepared analytical dataset
# --------------------------------------------------

df.to_csv(
    ANALYTICS_FILE,
    index=False,
    date_format="%Y-%m-%d"
)

print(f"Created: {ANALYTICS_FILE}")
print(f"Analytical dataset rows: {len(df):,}")
print(f"Analytical dataset columns: {len(df.columns)}")


# --------------------------------------------------
# 6. Calculate executive KPI summary
# --------------------------------------------------

completed = df[
    df["order_status"] == "Completed"
].copy()

revenue = completed["net_sales"].sum()

gross_margin = completed["gross_margin"].sum()

target = completed["allocated_target"].sum()

gross_margin_pct = (
    gross_margin / revenue * 100
    if revenue != 0
    else 0.0
)

target_attainment_pct = (
    revenue / target * 100
    if target != 0
    else 0.0
)

summary = {
    "rows": int(len(df)),
    "customers": int(df["customer_id"].nunique()),
    "regions": int(df["region"].nunique()),
    "products": int(df["product_name"].nunique()),
    "completed_revenue": round(float(revenue), 2),
    "gross_margin_pct": round(
        float(gross_margin_pct), 2
    ),
    "target_attainment_pct": round(
        float(target_attainment_pct), 2
    ),
}


# --------------------------------------------------
# 7. Export KPI summary JSON
# --------------------------------------------------

with open(
    SUMMARY_FILE,
    "w",
    encoding="utf-8"
) as file:
    json.dump(summary, file, indent=2)

print(f"Created: {SUMMARY_FILE}")
print("\nExecutive KPI Summary")

for key, value in summary.items():
    print(f"{key}: {value}")

print("\nSales analytics preparation completed successfully.")
