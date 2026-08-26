import pandas as pd
from pathlib import Path
from scipy.stats import f_oneway

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE/"data/processed/sales_analytics.csv")
df = df[df["order_status"]=="Completed"].copy()

# H0: mean order value is equal across customer segments.
# H1: at least one segment differs.
groups = [g["net_sales"].values for _,g in df.groupby("segment")]
stat,p = f_oneway(*groups)

decision = "Reject H0" if p < 0.05 else "Fail to reject H0"
result = (
    "One-way ANOVA: Average Order Value by Customer Segment\n"
    "H0: Mean order value is equal across segments.\n"
    "H1: At least one segment differs.\n"
    f"F-statistic: {stat:.4f}\n"
    f"p-value: {p:.6g}\n"
    f"Decision at alpha=0.05: {decision}\n"
)
(BASE/"data/processed/hypothesis_test.txt").write_text(result)
print(result)
