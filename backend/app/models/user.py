import datetime

from sqlalchemy import Integer, Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String)
    family_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    email = Column(String, index=True, unique=True, nullable=False)
    phone = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    summaries = relationship("Summary")

    class Config:
        orm_mode = True
