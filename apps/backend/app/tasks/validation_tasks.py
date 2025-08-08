from ..celery_app import celery
from ..services import validator


@celery.task
def validate_terraform(files: list[dict]) -> dict:
    return validator.validate(files)
