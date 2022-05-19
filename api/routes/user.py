from api.dependencies.auth_jwt import auth_handler
from api.routes.crud import CrudApiRouter
from db.repositories.user import UserRepository

from models.table_models.user import User
from models.schemas.user import UserResponse, UserCreate, UserUpdate

from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from fastapi import Depends, Security, status
from fastapi.security import HTTPAuthorizationCredentials


class UserRouter(CrudApiRouter[User, UserResponse, UserCreate, UserUpdate], UserRepository):


    def __init__(self, model = User, schema = UserResponse, model_name = "User", create_schema = UserCreate, update_schema = UserUpdate) -> None:
        super().__init__(model, schema, model_name, create_schema, update_schema =  update_schema,
            get_all_route = [Depends(auth_handler.auth_wrapper)],
            get_one_route = [Depends(auth_handler.auth_wrapper)],
            put_route = [Depends(auth_handler.auth_wrapper)],
            post_route = [Depends(auth_handler.auth_wrapper)],
            delete_route = [Depends(auth_handler.auth_wrapper)])
        
        self.add_router("/refresh-token", self.update_token(), status.HTTP_200_OK, methods = ["POST"], dependencies = False, response_model = UserResponse)


    def post(self):
        async def create(request: UserCreate, db: Session = Depends(get_db)):
            request.password = auth_handler.get_password_hash(request.password)
            return await self.post_repository(request, db)

        return create


    def update_token(self):
        async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(auth_handler.security), db: Session = Depends(get_db)):
            refresh_token = credentials.credentials
            new_token = auth_handler.refresh_token(refresh_token)

            user = await self.get_by_id_repository(auth_handler.decode_token(new_token), db)

            return UserResponse(**user.__dict__, access_token = new_token, refresh_token = refresh_token)
        
        return refresh_token