from sqlalchemy import Column, Integer, String, DateTime, Date
from datetime import datetime
from db.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_id = Column(String(255))
    name = Column(String(255))
    category_id = Column(Integer)
    company_id = Column(Integer)
    unit = Column(String(50))
    price = Column(Integer)
    guarantee = Column(Date)
    retrieved_from = Column(DateTime, nullable=True, default=None)
    accepted = Column(DateTime, nullable=True, default=None)
    created = Column(DateTime, default=datetime.now())
    deleted = Column(DateTime, nullable=True, default=None)