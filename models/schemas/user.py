from pydantic import BaseModel

from models.schemas.base import BaseSchema


class UserBase(BaseModel):
    
    username: str
    email: str
    phone: str
    role_id: int


class UserUpdate(UserBase):
    pass


class UserCreate(UserBase):

    password: str


class UserInLogin(BaseModel):

    username: str
    password: str


class UserResponse(BaseSchema, UserBase):

    access_token: str = None
    refresh_token: str = None