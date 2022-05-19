from typing import Any, Callable, List, Optional, Union
from fastapi import APIRouter, Depends, status
from api.dependencies.database import get_db 
from sqlalchemy.orm import Session
from db.repositories.curd_repository import CrudRepository
from resources.generic import MODEL_SCHEMA, RESPONSE_SCHEMA, CREATE_SCHEMA, DEPENDENCIES, UPDATE_SCHEMA


class CrudApiRouter(CrudRepository[MODEL_SCHEMA, RESPONSE_SCHEMA, CREATE_SCHEMA, UPDATE_SCHEMA], APIRouter):


    def __init__(
        self, model: MODEL_SCHEMA, 
        schema: RESPONSE_SCHEMA,  
        model_name: str, 
        create_schema: Optional[CREATE_SCHEMA] = None,
        update_schema: Optional[UPDATE_SCHEMA] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        post_route: Union[bool, DEPENDENCIES] = True,
        put_route: Union[bool, DEPENDENCIES] = True,
        delete_route: Union[bool, DEPENDENCIES] = True) -> None:

        super().__init__(model, schema, create_schema, model_name)
        
        self.model = model
        self.schema = schema
        self.create_schema = create_schema
        self.update_schema = update_schema

        if get_all_route:
            self.add_router("/", self.get(), status.HTTP_200_OK, methods = ['GET'], dependencies = get_all_route, response_model = List[schema],)

        if get_one_route:
            self.add_router("/{id}", self.get_by_id(), status.HTTP_200_OK, methods = ['GET'], dependencies = get_one_route, response_model = schema)

        if post_route:
            self.add_router("/", self.post(), status.HTTP_201_CREATED, methods = ['POST'], dependencies = post_route, response_model = create_schema)
        
        if put_route:
            self.add_router("/{id}", self.put(), status.HTTP_202_ACCEPTED, methods = ['PUT'], dependencies = put_route, response_model = update_schema)
        
        if delete_route:
            self.add_router("/{id}", self.delete(), status.HTTP_200_OK, methods = ['DELETE'], dependencies = delete_route)


    def add_router(self, path: str, endpoint: Callable[..., Any], status_code: int, methods: List[str], dependencies: Union[bool, DEPENDENCIES], response_model: Optional[Any] = None):
        self.add_api_route(
            path = path,
            endpoint = endpoint,
            response_model = response_model,
            status_code = status_code,
            methods = methods,
            dependencies = [] if isinstance(dependencies, bool) else dependencies
        )


    def get(self):
        async def get_all(db: Session = Depends(get_db)):
            return await self.get_all_repository(db)

        return get_all


    def get_by_id(self):
        async def get_one(id: int, db: Session = Depends(get_db)):
            return await self.get_by_id_repository(id, db)
        
        return get_one


    def post(self):
        async def create(request: self.create_schema, db: Session = Depends(get_db)):
            return await self.post_repository(request, db)

        return create


    def put(self):
        async def edit(id: int, request: self.update_schema, db: Session = Depends(get_db)):
            return await self.put_repository(id, request, db)

        return edit


    def delete(self):
        async def delete_one(id: int, db: Session = Depends(get_db)):
            return await self.delete_repository(id, db)

        return delete_one