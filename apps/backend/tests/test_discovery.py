from app.services.aws_discovery import normalize_endpoint

def test_normalize_endpoint():
    raw = {"name": "ep", "region": "us-east-1"}
    norm = normalize_endpoint(raw)
    assert norm["kind"] == "sagemaker_endpoint"
    assert norm["name"] == "ep"
