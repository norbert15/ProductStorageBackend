from datetime import date, datetime
from typing import Any, Optional
from pydantic import BaseModel

from models.schemas.base import BaseSchema


class CategoryBase(BaseModel):
    name: str
    company_ids: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(BaseSchema, CategoryBase):
    pass