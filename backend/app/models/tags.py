from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Tags(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
