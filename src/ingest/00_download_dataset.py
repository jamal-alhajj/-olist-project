import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

RAW_PATH = "data/raw"

os.makedirs(RAW_PATH, exist_ok=True)

api = KaggleApi()
api.authenticate()

dataset = "olistbr/brazilian-ecommerce"

print("Downloading dataset...")
api.dataset_download_files(dataset, path=RAW_PATH)

zip_path = os.path.join(RAW_PATH, "brazilian-ecommerce.zip")

print("Extracting dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(RAW_PATH)

print("Download complete!")
