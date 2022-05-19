from api.dependencies.auth_jwt import auth_handler
from api.routes.crud import CrudApiRouter
from db.repositories.logging import LoggingRepositroy
from fastapi import Depends

from models.schemas.logging import LoggingCreate, LoggingResponse
from models.table_models.logging import Logging


class LoggingRouter(CrudApiRouter[Logging, LoggingResponse, LoggingCreate, LoggingCreate], LoggingRepositroy):


    def __init__(self, model = Logging, schema = LoggingResponse, model_name = "Logging", create_schema = LoggingCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = create_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])