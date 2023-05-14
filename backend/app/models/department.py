from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Department(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False)
    vacancies = relationship("Vacancy")

    class Config:
        orm_mode = True
