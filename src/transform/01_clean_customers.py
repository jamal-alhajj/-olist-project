import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

RAW_PATH = os.path.join(PROJECT_ROOT, "data", "raw")
CLEAN_PATH = os.path.join(PROJECT_ROOT, "data", "clean")

os.makedirs(CLEAN_PATH, exist_ok=True)

customers = pd.read_csv(os.path.join(RAW_PATH, "olist_customers_dataset.csv"))

print("Customers loaded:", customers.shape)

customers.to_csv(os.path.join(CLEAN_PATH, "customers_clean.csv"), index=False)
print("Cleaned customers dataset saved at:", os.path.join(CLEAN_PATH, "customers_clean.csv"))
