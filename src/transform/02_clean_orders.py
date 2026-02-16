
import pandas as pd
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_PATH = SCRIPT_DIR.parent.parent / "data" / "raw"
CLEAN_PATH = SCRIPT_DIR.parent.parent / "data" / "clean"
CLEAN_PATH.mkdir(parents=True, exist_ok=True)

orders_file = RAW_PATH / "olist_orders_dataset.csv"
print(f"Loading orders from: {orders_file}")
orders = pd.read_csv(orders_file)
print(f"Orders loaded: {orders.shape}")

missing_values = orders.isnull().sum()
print("Missing values in orders dataset:")
print(missing_values)

date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors='coerce')

orders_clean_path = CLEAN_PATH / "orders_clean.csv"
orders.to_csv(orders_clean_path, index=False)
print(f"Cleaned orders dataset saved at: {orders_clean_path}")
