from sqlalchemy import Column, Integer, ForeignKey, Boolean, Float, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Summary(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    ready_to_move = Column(Boolean)
    car_license = Column(Boolean)
    only_remote = Column(Boolean)
    ready_for_trips = Column(Boolean)
    pref_salary = Column(Float)
    pref_position = Column(String)
    skills = Column(String)
    pref_city = Column(String)
    citizenship = Column(String)
    education = Column(String)
    busyness = Column(String)
    tags = relationship("SummaryTags")

    class Config:
        orm_mode = True
