# 03_clean_products.py
import pandas as pd
from pathlib import Path

# Paths
RAW_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\raw")
CLEAN_PATH = Path(r"C:\Users\Jamal\Desktop\olist-project\data\clean")
CLEAN_PATH.mkdir(parents=True, exist_ok=True)

# Load products dataset
products = pd.read_csv(RAW_PATH / "olist_products_dataset.csv")
print(f"Products loaded: {products.shape}")

# Check missing values
print("Missing values in products dataset:")
print(products.isna().sum())

# Fill missing product category names with 'unknown'
products['product_category_name'] = products['product_category_name'].fillna('unknown')

# Fill numeric columns' missing values with 0
numeric_cols = ['product_name_lenght', 'product_description_lenght', 
                'product_photos_qty', 'product_weight_g', 
                'product_length_cm', 'product_height_cm', 'product_width_cm']

products[numeric_cols] = products[numeric_cols].fillna(0)

# Save cleaned products dataset
products.to_csv(CLEAN_PATH / "products_clean.csv", index=False)
print(f"Cleaned products dataset saved at: {CLEAN_PATH / 'products_clean.csv'}")
