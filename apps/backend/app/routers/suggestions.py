from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..deps import get_db
from ..models import Suggestion, SuggestionStatus, Artifact
from ..schemas import SuggestionCreate, SuggestionOut, ArtifactOut

router = APIRouter(tags=["suggestions"])


@router.post("/agent/run", response_model=SuggestionOut)
def run_agent(payload: SuggestionCreate, db: Session = Depends(get_db)):
    suggestion = Suggestion(user_id=1, account_id=payload.account_id, prompt_text=payload.prompt_text, status=SuggestionStatus.draft, summary="stub")
    db.add(suggestion)
    db.commit()
    db.refresh(suggestion)
    return suggestion


@router.get("/suggestions/{suggestion_id}", response_model=SuggestionOut)
def get_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    sug = db.get(Suggestion, suggestion_id)
    if not sug:
        raise HTTPException(status_code=404, detail="not found")
    return sug


@router.get("/suggestions/{suggestion_id}/artifacts", response_model=list[ArtifactOut])
def get_artifacts(suggestion_id: int, db: Session = Depends(get_db)):
    arts = db.query(Artifact).filter_by(suggestion_id=suggestion_id).all()
    return arts
