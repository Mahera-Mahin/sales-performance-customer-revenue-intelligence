from pathlib import Path
import pandas as pd

def test_sales_data_quality():
    path = Path(__file__).resolve().parents[1] / "data/raw/sales_transactions.csv"
    df = pd.read_csv(path)
    assert df["order_id"].is_unique
    assert df["customer_id"].notna().all()
    assert df["product_name"].notna().all()
    assert (df["units"] > 0).all()
    assert df["discount_pct"].between(0,1).all()
