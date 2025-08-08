"""Audit logging utilities."""
from sqlalchemy.orm import Session
from ..models import AuditLog


def log_action(db: Session, actor: str, action: str, meta: dict) -> None:
    log = AuditLog(actor=actor, action=action, meta_json=meta)
    db.add(log)
    db.commit()
