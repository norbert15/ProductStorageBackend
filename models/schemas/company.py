from pydantic import BaseModel

from models.schemas.base import BaseSchema


class CompanyBase(BaseModel):
    nav_name: str
    short_nav_name: str
    phone: str
    email: str
    city: str


class CompanyCreate(CompanyBase):
    pass


class CompanyResponse(BaseSchema, CompanyBase):
    pass