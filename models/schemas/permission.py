from pydantic import BaseModel

from models.schemas.base import BaseSchema


class PermissionBase(BaseModel):
    page: str
    description: str
    role_id: int


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(PermissionBase):
    id: int


class PermissionResponse(BaseSchema, PermissionBase):
    pass