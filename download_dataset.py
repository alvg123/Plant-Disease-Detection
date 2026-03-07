import os

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if len(os.listdir(DATA_DIR)) == 0:
    print("Downloading dataset from Kaggle...")
    os.system("kaggle datasets download -d emmarex/plantdisease -p data --unzip")
    print("Download complete.")
else:
    print("Dataset already exists. Skipping download.")