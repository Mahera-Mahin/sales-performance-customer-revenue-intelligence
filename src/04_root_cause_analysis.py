import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "data/processed/sales_analytics.csv"
OUT = BASE / "data/processed"

df = pd.read_csv(INPUT)

# Only completed sales are included in business KPIs
df = df[df["order_status"] == "Completed"].copy()


# ============================================================
# 1. REGIONAL YEARLY PERFORMANCE
# ============================================================

regional = (
    df.groupby(["year", "region"])
    .agg(
        revenue=("net_sales", "sum"),
        target=("allocated_target", "sum"),
        gross_margin=("gross_margin", "sum"),
        units=("units", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
    )
    .reset_index()
)

regional["attainment_pct"] = (
    regional["revenue"] / regional["target"] * 100
)

regional["margin_pct"] = (
    regional["gross_margin"] / regional["revenue"] * 100
)

regional["revenue_yoy_pct"] = (
    regional
    .sort_values(["region", "year"])
    .groupby("region")["revenue"]
    .pct_change() * 100
)

regional.to_csv(
    OUT / "rca_regional_yearly.csv",
    index=False
)


# ============================================================
# 2. 2025 REGION + CATEGORY ANALYSIS
# ============================================================

category = (
    df[df["year"] == 2025]
    .groupby(["region", "category"])
    .agg(
        revenue=("net_sales", "sum"),
        target=("allocated_target", "sum"),
        gross_margin=("gross_margin", "sum"),
        units=("units", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
    )
    .reset_index()
)

category["attainment_pct"] = (
    category["revenue"] /
    category["target"] * 100
)

category["margin_pct"] = (
    category["gross_margin"] /
    category["revenue"] * 100
)

category["target_gap"] = (
    category["revenue"] -
    category["target"]
)

category.to_csv(
    OUT / "rca_2025_region_category.csv",
    index=False
)


# ============================================================
# 3. PRODUCT-LEVEL ROOT CAUSE
# ============================================================

focus = df[
    (df["year"] == 2025)
    &
    (
        (
            (df["region"] == "East")
            &
            (df["category"] == "Engines")
        )
        |
        (
            (df["region"] == "West")
            &
            (df["category"].isin(
                ["Power Systems", "Services"]
            ))
        )
    )
].copy()

product = (
    focus
    .groupby(
        ["region", "category", "product_name"]
    )
    .agg(
        revenue=("net_sales", "sum"),
        target=("allocated_target", "sum"),
        gross_margin=("gross_margin", "sum"),
        units=("units", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
    )
    .reset_index()
)

product["attainment_pct"] = (
    product["revenue"] /
    product["target"] * 100
)

product["margin_pct"] = (
    product["gross_margin"] /
    product["revenue"] * 100
)

product["target_gap"] = (
    product["revenue"] -
    product["target"]
)

product.to_csv(
    OUT / "rca_focus_products.csv",
    index=False
)


# ============================================================
# 4. EAST INDUSTRIAL ENGINES — CUSTOMER SEGMENT
# ============================================================

east_engine = df[
    (df["year"] == 2025)
    &
    (df["region"] == "East")
    &
    (df["product_name"] == "Industrial Engines")
]

segment = (
    east_engine
    .groupby("segment")
    .agg(
        revenue=("net_sales", "sum"),
        units=("units", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
        gross_margin=("gross_margin", "sum"),
    )
    .reset_index()
)

segment["margin_pct"] = (
    segment["gross_margin"] /
    segment["revenue"] * 100
)

segment["avg_order_value"] = (
    segment["revenue"] /
    segment["orders"]
)

segment.to_csv(
    OUT / "rca_east_industrial_engines_segment.csv",
    index=False
)


# ============================================================
# 5. PRODUCT YEAR-OVER-YEAR ANALYSIS
# ============================================================

product_yoy = (
    df[df["region"].isin(["East", "West"])]
    .groupby(
        ["region", "product_name", "year"]
    )
    .agg(
        revenue=("net_sales", "sum"),
        units=("units", "sum"),
        orders=("order_id", "nunique"),
        customers=("customer_id", "nunique"),
        gross_margin=("gross_margin", "sum"),
    )
    .reset_index()
)

product_yoy["margin_pct"] = (
    product_yoy["gross_margin"] /
    product_yoy["revenue"] * 100
)

product_yoy["avg_order_value"] = (
    product_yoy["revenue"] /
    product_yoy["orders"]
)

product_yoy = product_yoy.sort_values(
    ["region", "product_name", "year"]
)

product_yoy["revenue_yoy_pct"] = (
    product_yoy
    .groupby(["region", "product_name"])["revenue"]
    .pct_change() * 100
)

product_yoy.to_csv(
    OUT / "rca_product_yoy.csv",
    index=False
)


print("==========================================")
print("ROOT-CAUSE ANALYSIS COMPLETED")
print("==========================================")

print("Created:")
print("✓ rca_regional_yearly.csv")
print("✓ rca_2025_region_category.csv")
print("✓ rca_focus_products.csv")
print("✓ rca_east_industrial_engines_segment.csv")
print("✓ rca_product_yoy.csv")