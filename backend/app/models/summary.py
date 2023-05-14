from sqlalchemy import Column, Integer, ForeignKey, Boolean, Float, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Summary(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    ready_to_move = Column(Boolean, nullable=False)
    car_license = Column(Boolean, nullable=False)
    only_remote = Column(Boolean, nullable=False)
    ready_for_trips = Column(Boolean, nullable=False)
    pref_salary = Column(Float, nullable=False)
    pref_position = Column(String, nullable=False)
    skills = Column(String, nullable=False)
    pref_city = Column(String, nullable=False)
    citizenship = Column(String, nullable=False)
    education = Column(String, nullable=False)
    busyness = Column(String, nullable=False)
    tags = relationship("SummaryTags")

    class Config:
        orm_mode = True
        