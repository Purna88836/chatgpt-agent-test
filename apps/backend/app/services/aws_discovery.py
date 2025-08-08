"""Service for discovering AWS resources.
Currently returns a static example for testing."""
from typing import List, Dict


def discover_sagemaker_endpoints() -> List[Dict]:
    # Placeholder for boto3 call
    return [{"name": "endpoint-1", "region": "us-east-1"}]


def normalize_endpoint(raw: Dict) -> Dict:
    """Normalize boto3 result into Resource.normalized structure."""
    return {
        "kind": "sagemaker_endpoint",
        "name": raw["name"],
        "region": raw.get("region", "us-east-1"),
    }
