from ..celery_app import celery
from ..services import aws_discovery


@celery.task
def run_scan(account_id: int) -> list[dict]:
    endpoints = aws_discovery.discover_sagemaker_endpoints()
    return [aws_discovery.normalize_endpoint(e) for e in endpoints]
