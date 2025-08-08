from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db
from ..models import AccountConnection

router = APIRouter(prefix="/connect", tags=["connect"])


@router.post("/aws")
def connect_aws(role_arn: str, db: Session = Depends(get_db)):
    acc = AccountConnection(user_id=1, provider="aws", config_json={"role_arn": role_arn})
    db.add(acc)
    db.commit()
    db.refresh(acc)
    return {"account_id": acc.id}
