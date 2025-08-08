from app.services.validator import validate


def test_validator_accepts_files(tmp_path):
    files = [{"path": "main.tf", "content": "terraform {}"}]
    result = validate(files)
    assert result["valid"] is True
