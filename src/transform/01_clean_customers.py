import os
import pandas as pd

# Get the absolute path to the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Paths
RAW_PATH = os.path.join(PROJECT_ROOT, "data", "raw")
CLEAN_PATH = os.path.join(PROJECT_ROOT, "data", "clean")

# Make sure the clean folder exists
os.makedirs(CLEAN_PATH, exist_ok=True)

# Load customers dataset
customers = pd.read_csv(os.path.join(RAW_PATH, "olist_customers_dataset.csv"))

# Quick check
print("Customers loaded:", customers.shape)

# Save cleaned customers (just as an example)
customers.to_csv(os.path.join(CLEAN_PATH, "customers_clean.csv"), index=False)
print("Cleaned customers dataset saved at:", os.path.join(CLEAN_PATH, "customers_clean.csv"))
