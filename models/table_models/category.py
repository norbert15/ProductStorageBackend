from sqlalchemy import Column, Integer, String
from db.database import Base


class Category(Base):
    
    __tablename__ = "categorys"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    company_ids = Column(String(255))