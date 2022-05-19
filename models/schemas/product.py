from datetime import date, datetime
from typing import Any, Optional
from pydantic import BaseModel

from models.schemas.base import BaseSchema


class ProductStatus(BaseModel):
    name: str
    is_active: bool

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_id: str
    name: str
    category_id: int
    company_id: int
    unit: str
    price: int
    guarantee: date
    retrieved_from: Optional[datetime] = None
    accepted: Optional[Any] = None


class ProductCreate(ProductBase):
    pass


class ProductResponse(BaseSchema, ProductBase):
    created: datetime



    