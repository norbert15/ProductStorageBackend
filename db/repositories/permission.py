from db.repositories.curd_repository import CrudRepository
from models.table_models.permission import Permission
from models.schemas.permission import PermissionCreate, PermissionResponse


class PermissionRepository(CrudRepository[Permission, PermissionResponse, PermissionCreate, PermissionCreate]):

    def __init__(self, model = Permission, schema = PermissionResponse, create_schema = PermissionCreate, model_name = "Permission", update_schema = PermissionCreate) -> None:
        super().__init__(model, schema, create_schema, model_name, update_schema)