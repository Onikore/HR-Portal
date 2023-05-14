from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class VacancyTags(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
