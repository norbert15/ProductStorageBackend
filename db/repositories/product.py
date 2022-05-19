from db.repositories.curd_repository import CrudRepository
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from datetime import datetime

from models.schemas.product import ProductCreate, ProductResponse, ProductStatus
from models.table_models.product import Product


class ProductRepository(CrudRepository[Product, ProductResponse, ProductCreate, ProductCreate]):
    
    def __init__(self, model = Product, schema = ProductResponse, create_schema = ProductCreate, model_name = "Product") -> None:
        super().__init__(model, schema, create_schema, model_name)


    async def put_status(self, id: int, product_status: ProductStatus, db: Session):
        product = db.query(Product).filter(Product.id == id)

        if not product.first():
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Product with id not exists')

        data = {
            product_status.name: datetime.now() if product_status.is_active else None
        }

        try:
            product.update(data)
            db.commit()
        except HTTPException as he:
            raise HTTPException(**he)

        return True
