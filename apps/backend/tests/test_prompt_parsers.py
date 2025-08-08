import json
from pathlib import Path

PROMPTS = ["planner", "analyst", "codegen_terraform", "doc_impl_md", "diagram_mermaid", "refine_validate"]


def test_prompts_load():
    for name in PROMPTS:
        data = json.loads(Path(f"../../packages/prompts/{name}.json").read_text())
        assert "system" in data
