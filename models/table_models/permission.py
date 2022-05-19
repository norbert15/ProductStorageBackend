from sqlalchemy import Column, Integer, String, Text
from db.database import Base


class Permission(Base):
    
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    page = Column(String(25))
    description = Column(Text)
    role_id = Column(Integer)