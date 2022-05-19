from pydantic import BaseModel

from models.schemas.base import BaseSchema


class RoleBase(BaseModel):

    name: str
    color: str
    

class RoleCreate(RoleBase):
    pass


class RoleResponse(BaseSchema, RoleBase):
    pass