from db.repositories.curd_repository import CrudRepository

from models.table_models.logging import Logging
from models.schemas.logging import LoggingCreate, LoggingResponse


class LoggingRepositroy(CrudRepository[Logging, LoggingResponse, LoggingCreate, LoggingCreate]):

    def __init__(self, model = Logging, schema = LoggingResponse, create_schema = LoggingCreate, model_name = "Logging") -> None:
        super().__init__(model, schema, create_schema, model_name)