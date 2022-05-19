from sqlalchemy import Column, Integer, String, Text, DateTime
from db.database import Base


class Logging(Base):
    
    __tablename__ = "logging"

    id = Column(Integer, primary_key=True)
    description = Column(Text)
    period = Column(DateTime)