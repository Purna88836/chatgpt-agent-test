from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Text, Enum
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()


class SuggestionStatus(str, enum.Enum):
    pending = "pending"
    running = "running"
    draft = "draft"
    approved = "approved"
    rejected = "rejected"


class ArtifactType(str, enum.Enum):
    doc = "doc"
    iac = "iac"
    workflow = "workflow"
    diagram = "diagram"


class ArtifactStatus(str, enum.Enum):
    draft = "draft"
    validated = "validated"
    approved = "approved"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    org_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class AccountConnection(Base):
    __tablename__ = "account_connections"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    provider = Column(String, nullable=False)
    config_json = Column(JSON, nullable=False)
    last_scan_at = Column(DateTime)
    status = Column(String, default="unknown")


class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account_connections.id"))
    provider = Column(String)
    kind = Column(String)
    name = Column(String)
    region = Column(String)
    normalized = Column(JSON)
    discovered_at = Column(DateTime, default=datetime.utcnow)


class Suggestion(Base):
    __tablename__ = "suggestions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_id = Column(Integer, ForeignKey("account_connections.id"))
    prompt_text = Column(Text)
    status = Column(Enum(SuggestionStatus), default=SuggestionStatus.pending)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Artifact(Base):
    __tablename__ = "artifacts"
    id = Column(Integer, primary_key=True)
    suggestion_id = Column(Integer, ForeignKey("suggestions.id"))
    path = Column(String)
    content = Column(Text)
    type = Column(Enum(ArtifactType))
    status = Column(Enum(ArtifactStatus), default=ArtifactStatus.draft)
    validation_log = Column(Text)


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    action = Column(String)
    meta_json = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)


class GithubInstall(Base):
    __tablename__ = "github_installs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    installation_id = Column(Integer)
    target_owner = Column(String)
    repos = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
