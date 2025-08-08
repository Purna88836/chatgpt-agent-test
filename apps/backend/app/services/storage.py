"""Local file storage for artifacts (development)."""
import os
from typing import Dict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "artifacts"))


def save_artifact(path: str, content: str) -> str:
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return full_path
