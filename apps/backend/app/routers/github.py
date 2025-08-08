from fastapi import APIRouter

router = APIRouter(prefix="/github", tags=["github"])


@router.post("/install/callback")
async def install_callback():
    return {"status": "ok"}


@router.post("/webhook")
async def webhook():
    return {"ok": True}
