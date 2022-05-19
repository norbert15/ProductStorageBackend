from resources.generic import CREATE_SCHEMA, MODEL_SCHEMA, RESPONSE_SCHEMA, UPDATE_SCHEMA, Generic
from sqlalchemy.orm import Session
from fastapi import status, HTTPException


class CrudRepository(Generic[MODEL_SCHEMA, RESPONSE_SCHEMA, CREATE_SCHEMA, UPDATE_SCHEMA]):


    def __init__(self, model: MODEL_SCHEMA, schema: RESPONSE_SCHEMA, create_schema: CREATE_SCHEMA, model_name: str, update_schema: UPDATE_SCHEMA = None) -> None:
        super().__init__()

        self.model = model
        self.schema = schema
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.model_name = model_name


    async def get_all_repository(self, db: Session):
        return db.query(self.model).all()


    async def get_by_id_repository(self, id: int, db: Session):
        model = db.query(self.model).filter(self.model.id == id)

        if not model.first():

            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"{self.model_name} with id is not exists",
                headers = {"error": "Not exists"}
            )

        return model.first()


    async def post_repository(self, request: CREATE_SCHEMA, db: Session):
        model = self.model(**request.dict())

        try:
            db.add(model)
            db.commit()
            db.refresh(model)

        except HTTPException as he:
            raise HTTPException(**he)

        return request


    async def put_repository(self, id: int, request: UPDATE_SCHEMA, db: Session):
        model = db.query(self.model).filter(self.model.id == id)

        if not model.first():
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"{self.model_name} with id is not exists",
                headers = {"error": "Not exists"}
            )

        try:
            model.update(request.dict())
            db.commit()

        except HTTPException as he:
            raise HTTPException(**he)

        return request


    async def delete_repository(self, id: int, db: Session):
        model = db.query(self.model).filter(self.model.id == id)

        if not model.first():
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"{self.model_name} with id is not exists",
                headers = {"error": "Not exists"}
            )

        try:
            model.delete()
            db.commit()

        except HTTPException as he:
            raise HTTPException(**he)
        
        return True