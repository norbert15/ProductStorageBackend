from api.routes.crud import CrudApiRouter
from db.repositories.company import CompanyRepository

from models.table_models.role import Role
from models.schemas.role import RoleCreate, RoleResponse
from api.dependencies.auth_jwt import auth_handler
from fastapi import Depends


class RoleRouter(CrudApiRouter[Role, RoleResponse, RoleCreate, RoleCreate], CompanyRepository):

    def __init__(self, model = Role, schema = RoleResponse, model_name = "Role", create_schema = RoleCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = create_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])
