from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class Responses(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    summary_id = Column(Integer, ForeignKey('summary.id'))
