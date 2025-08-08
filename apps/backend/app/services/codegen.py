"""Generate Terraform and docs stubs."""
from typing import List, Dict


def generate_files(snapshot: Dict) -> List[Dict]:
    return [
        {"path": "terraform/main.tf", "content": "# terraform"},
        {"path": "docs/implementation.md", "content": "# Implementation\n"},
    ]
