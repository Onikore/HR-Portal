from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Vacancy(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    department_id = Column(Integer, ForeignKey('department.id'))
    name = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    min_salary = Column(Float, nullable=False)
    max_salary = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    tags = relationship("VacancyTags")

    class Config:
        orm_mode = True
