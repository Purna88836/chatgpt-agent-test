"""LLM agent stub."""
from typing import Dict


def plan(goal: str, snapshot: Dict) -> Dict:
    """Return a trivial plan."""
    return {"plan": [{"id": "step1", "tool": "noop", "inputs": {}, "success": True}]}
