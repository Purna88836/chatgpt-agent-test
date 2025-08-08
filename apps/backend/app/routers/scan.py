from fastapi import APIRouter

router = APIRouter(prefix="/scan", tags=["scan"])


@router.post("/{account_id}")
async def run_scan(account_id: int):
    # In real app enqueue Celery task
    return {"job_id": f"scan-{account_id}"}
