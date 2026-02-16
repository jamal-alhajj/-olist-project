# 04_enrich_revenue.py
import pandas as pd
from pathlib import Path

# Paths
CLEAN_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\clean")
OUTPUT_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\enriched")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# Load cleaned datasets
print("Loading cleaned datasets...")
orders = pd.read_csv(CLEAN_PATH / "orders_clean.csv")
items = pd.read_csv(CLEAN_PATH / "order_items_clean.csv")
customers = pd.read_csv(CLEAN_PATH / "customers_clean.csv")

print(f"Orders loaded: {orders.shape}")
print(f"Order items loaded: {items.shape}")
print(f"Customers loaded: {customers.shape}")

# Merge orders with order items
orders_items = pd.merge(items, orders, on="order_id", how="left")

# Merge with customers
full_data = pd.merge(orders_items, customers, on="customer_id", how="left")

# Calculate revenue per order item
full_data["revenue"] = full_data["price"] + full_data["freight_value"]

# Calculate total revenue per order
order_revenue = full_data.groupby("order_id")["revenue"].sum().reset_index()
order_revenue.rename(columns={"revenue": "total_revenue"}, inplace=True)

# Save enriched data
order_revenue.to_csv(OUTPUT_PATH / "orders_revenue.csv", index=False)
print(f"Enriched revenue dataset saved at: {OUTPUT_PATH / 'orders_revenue.csv'}")
