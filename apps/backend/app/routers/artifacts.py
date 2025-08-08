from fastapi import APIRouter

router = APIRouter(prefix="/artifacts", tags=["artifacts"])


@router.get("/{artifact_id}")
async def get_artifact(artifact_id: int):
    return {"id": artifact_id, "content": "placeholder"}
