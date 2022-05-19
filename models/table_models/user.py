from sqlalchemy import Column, Integer, String
from db.database import Base


class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    phone = Column(String(255))
    role_id = Column(Integer)