from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tags import Tags
from app.schemas.tags import TagCreate, TagUpdate


class CRUDTags(CRUDBase[Tags, TagCreate, TagUpdate]):
    def get_all(self, db: Session) -> List[Tags]:
        return db.query(self.model).all()



tags = CRUDTags(Tags)
