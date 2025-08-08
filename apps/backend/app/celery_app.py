from celery import Celery
from .config import settings

celery = Celery(
    "llmops",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery.conf.task_routes = {
    "app.tasks.discovery_tasks.*": {"queue": "default"},
}
