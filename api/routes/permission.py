from typing import List

from sqlalchemy.orm import Session
from api.dependencies.auth_jwt import auth_handler
from api.dependencies.database import get_db
from api.routes.crud import CrudApiRouter
from db.repositories.permission import PermissionRepository
from fastapi import Depends, status

from models.schemas.permission import PermissionCreate, PermissionResponse, PermissionUpdate
from models.table_models.permission import Permission


class PermissionRouter(CrudApiRouter[Permission, PermissionResponse, PermissionCreate, PermissionCreate], PermissionRepository):

    def __init__(self, model = Permission, schema = PermissionResponse, model_name = "Permission", create_schema = PermissionCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = PermissionCreate,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])

        self.add_router("/list", self.post_list(), status.HTTP_201_CREATED, methods = ["POST"], dependencies = [Depends(auth_handler.auth_wrapper)])
        self.add_router("/update/list", self.put_list(), status.HTTP_202_ACCEPTED, methods = ["PUT"], dependencies = [Depends(auth_handler.auth_wrapper)])


    def post_list(self):
        async def create_permission_by_list(permission_list: List[PermissionCreate], db: Session = Depends(get_db)):
            for permission in permission_list:
                await self.post_repository(permission, db)

            return permission_list

        return create_permission_by_list


    def put_list(self):
        async def update_permission_list(permission_list: List[PermissionUpdate], db: Session = Depends(get_db)):
            for permission in permission_list:
                await self.put_repository(permission.id, PermissionCreate(**permission.dict()), db)

            return permission_list

        return update_permission_list