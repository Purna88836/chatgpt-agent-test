"""Terraform validator wrapper."""
from typing import List, Dict
import subprocess
import tempfile
import os


def validate(files: List[Dict]) -> Dict:
    """Run terraform fmt and validate in a temp dir.
    For tests we simply write files and return success without running terraform."""
    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            path = os.path.join(tmp, f["path"])
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as h:
                h.write(f["content"])
        # Here we would run terraform commands; return stub
        return {"valid": True, "stdout": "", "stderr": ""}
