import pandas as pd
from pathlib import Path

RAW_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\raw")
CLEAN_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\clean")

print(f"Loading order items from: {RAW_PATH / 'olist_order_items_dataset.csv'}")
items = pd.read_csv(RAW_PATH / "olist_order_items_dataset.csv")
print(f"Order items loaded: {items.shape}")

print("Missing values in order items dataset:")
print(items.isna().sum())

items = items.drop_duplicates()

items['order_item_id'] = items['order_item_id'].astype(int)
items['price'] = items['price'].astype(float)
items['freight_value'] = items['freight_value'].astype(float)

items['shipping_limit_date'] = pd.to_datetime(items['shipping_limit_date'], errors='coerce')

CLEAN_PATH.mkdir(parents=True, exist_ok=True)
items.to_csv(CLEAN_PATH / "order_items_clean.csv", index=False)
print(f"Cleaned order items dataset saved at: {CLEAN_PATH / 'order_items_clean.csv'}")
