from db.repositories.curd_repository import CrudRepository

from models.schemas.category import CategoryCreate, CategoryResponse
from models.table_models.category import Category


class CategoryRepository(CrudRepository[Category, CategoryResponse, CategoryCreate, CategoryCreate]):

    def __init__(self, model = Category, schema = CategoryResponse, create_schema = CategoryCreate, model_name = "Category") -> None:
        super().__init__(model, schema, create_schema, model_name)