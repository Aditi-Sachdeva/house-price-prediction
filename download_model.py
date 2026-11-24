import os
import gdown

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "best_house_price_model.pkl"
)

FILE_ID = "1mJ7hAF-oXhIhWBB8p0viWMS-mkcS28Rq"

if not os.path.exists(MODEL_PATH):
    print("Downloading trained model from Google Drive...")

    gdown.download(
        id=FILE_ID,
        output=MODEL_PATH,
        quiet=False
    )

    print("Model download completed.")
else:
    print("Model already exists. Skipping download.")