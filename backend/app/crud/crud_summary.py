from typing import Any

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.summary import Summary
from app.schemas.summary import SummaryCreate, SummaryUpdate


class CRUDSummary(CRUDBase[Summary, SummaryCreate, SummaryUpdate]):
    def get_resume_id(self, db: Session, user_id: Any):
        return db.query(Summary).filter(Summary.user_id == user_id).first().id


summary = CRUDSummary(Summary)
