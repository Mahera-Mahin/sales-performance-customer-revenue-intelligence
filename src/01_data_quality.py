import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data/raw/sales_transactions.csv"
df = pd.read_csv(DATA)

checks = {
    "rows": len(df),
    "duplicate_order_ids": int(df["order_id"].duplicated().sum()),
    "null_order_ids": int(df["order_id"].isna().sum()),
    "null_customer_ids": int(df["customer_id"].isna().sum()),
    "negative_net_sales": int((df["net_sales"] < 0).sum()),
    "invalid_discount_pct": int(((df["discount_pct"] < 0) | (df["discount_pct"] > 1)).sum()),
    "margin_mismatches": int((df["gross_margin"] - (df["net_sales"] - df["cost"])).abs().gt(0.01).sum()),
}
for k,v in checks.items():
    print(f"{k}: {v}")

assert checks["duplicate_order_ids"] == 0
assert checks["null_order_ids"] == 0
assert checks["null_customer_ids"] == 0
assert checks["negative_net_sales"] == 0
assert checks["invalid_discount_pct"] == 0
assert checks["margin_mismatches"] == 0
print("All data-quality checks passed.")
