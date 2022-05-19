from db.repositories.curd_repository import CrudRepository

from models.table_models.role import Role
from models.schemas.role import RoleCreate, RoleResponse


class RoleRepositroy(CrudRepository[Role, RoleResponse, RoleCreate, RoleCreate]):

    def __init__(self, model = Role, schema = RoleResponse, create_schema = RoleCreate, model_name = "Role") -> None:
        super().__init__(model, schema, create_schema, model_name)