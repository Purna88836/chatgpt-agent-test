from ..celery_app import celery
from ..services import github_app


@celery.task
def open_pr(suggestion_id: int, repo: str) -> str:
    return github_app.open_pr(repo, f"ai/{suggestion_id}", [])
