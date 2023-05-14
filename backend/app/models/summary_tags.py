from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class SummaryTags(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    summary_id = Column(Integer, ForeignKey('summary.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
