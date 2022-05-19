from sqlalchemy import Column, Integer, String
from db.database import Base


class Company(Base):
    
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    nav_name = Column(String(255))
    short_nav_name = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    city = Column(String(255))