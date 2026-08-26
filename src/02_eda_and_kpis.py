import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE/"data/processed/sales_analytics.csv")
df = df[df["order_status"]=="Completed"].copy()

region = df.groupby("region").agg(
    revenue=("net_sales","sum"),
    gross_margin=("gross_margin","sum"),
    customers=("customer_id","nunique"),
    orders=("order_id","nunique"),
    target=("allocated_target","sum")
).reset_index()
region["margin_pct"] = region["gross_margin"]/region["revenue"]
region["attainment_pct"] = region["revenue"]/region["target"]
region.to_csv(BASE/"data/processed/regional_kpis.csv", index=False)

product = df.groupby(["category","product_name"]).agg(
    revenue=("net_sales","sum"),
    gross_margin=("gross_margin","sum"),
    units=("units","sum"),
    orders=("order_id","nunique")
).reset_index()
product["margin_pct"] = product["gross_margin"]/product["revenue"]
product.to_csv(BASE/"data/processed/product_kpis.csv", index=False)

customer = df.groupby(["customer_id","customer_name","segment","region"]).agg(
    revenue=("net_sales","sum"),
    orders=("order_id","nunique"),
    units=("units","sum")
).reset_index()
customer["avg_order_value"] = customer["revenue"]/customer["orders"]
customer.to_csv(BASE/"data/processed/customer_kpis.csv", index=False)

monthly = df.assign(month=pd.to_datetime(df["order_date"]).dt.to_period("M").astype(str)).groupby("month").agg(
    revenue=("net_sales","sum"),
    gross_margin=("gross_margin","sum"),
    target=("allocated_target","sum")
).reset_index()
monthly["attainment_pct"] = monthly["revenue"]/monthly["target"]
monthly.to_csv(BASE/"data/processed/monthly_kpis.csv", index=False)

print("KPI tables exported.")
