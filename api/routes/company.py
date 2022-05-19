from api.routes.crud import CrudApiRouter
from db.repositories.company import CompanyRepository

from models.table_models.company import Company
from models.schemas.company import CompanyResponse, CompanyCreate
from api.dependencies.auth_jwt import auth_handler
from fastapi import Depends


class CompanyRouter(CrudApiRouter[Company, CompanyResponse, CompanyCreate, CompanyCreate], CompanyRepository):

    def __init__(self, model = Company, schema = CompanyResponse, model_name = "Company", create_schema = CompanyCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = create_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])
