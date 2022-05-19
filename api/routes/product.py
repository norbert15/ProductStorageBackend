from api.dependencies.auth_jwt import auth_handler
from api.routes.crud import CrudApiRouter
from db.repositories.product import ProductRepository
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from fastapi import Depends, status

from models.schemas.product import ProductCreate, ProductResponse, ProductStatus
from models.table_models.product import Product


class ProductRouter(CrudApiRouter[Product, ProductResponse, ProductCreate, ProductCreate], ProductRepository):


    def __init__(self, model = Product, schema = ProductResponse, model_name = "Product", create_schema = ProductCreate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema = create_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])

        self.add_router("/status/{id}", self.put_status_by_id(), status.HTTP_202_ACCEPTED, methods = ['PUT'], dependencies = [Depends(auth_handler.auth_wrapper)])


    def put_status_by_id(self):
        async def put_status_by_id(id: int, product_status: ProductStatus, db: Session = Depends(get_db)):
            return await self.put_status(id, product_status, db)

        return put_status_by_id