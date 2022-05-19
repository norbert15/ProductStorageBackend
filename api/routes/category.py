from api.routes.crud import CrudApiRouter
from db.repositories.category import CategoryRepository

from models.schemas.category import CategoryCreate, CategoryResponse
from models.table_models.category import Category
from api.dependencies.auth_jwt import auth_handler
from fastapi import Depends


class CategoryRouter(CrudApiRouter[Category, CategoryResponse, CategoryCreate, CategoryCreate], CategoryRepository):

    def __init__(self, model = Category, schema = CategoryResponse, model_name = "Category", create_schema = CategoryCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = create_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])