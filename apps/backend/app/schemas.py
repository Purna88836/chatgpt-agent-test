from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .models import SuggestionStatus, ArtifactType, ArtifactStatus


class ResourceBase(BaseModel):
    id: int
    provider: str
    kind: str
    name: str
    region: str
    class Config:
        orm_mode = True


class SuggestionCreate(BaseModel):
    account_id: int
    prompt_text: str


class SuggestionOut(BaseModel):
    id: int
    status: SuggestionStatus
    summary: Optional[str]
    created_at: datetime
    class Config:
        orm_mode = True


class ArtifactOut(BaseModel):
    id: int
    path: str
    content: str
    type: ArtifactType
    status: ArtifactStatus
    class Config:
        orm_mode = True
