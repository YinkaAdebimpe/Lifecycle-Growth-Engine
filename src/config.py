import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
IMAGES_DIR = PROJECT_ROOT / "images"

for _dir in (RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, IMAGES_DIR):
    _dir.mkdir(parents=True, exist_ok=True)

RANDOM_SEED = 42
