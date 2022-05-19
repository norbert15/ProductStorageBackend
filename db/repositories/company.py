from db.repositories.curd_repository import CrudRepository

from models.table_models.company import Company
from models.schemas.company import CompanyResponse, CompanyCreate


class CompanyRepository(CrudRepository[Company, CompanyResponse, CompanyCreate, CompanyCreate]):

    def __init__(self, model = Company, schema = CompanyResponse, create_schema = CompanyCreate, model_name = "Company") -> None:
        super().__init__(model, schema, create_schema, model_name)