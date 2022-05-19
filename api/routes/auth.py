from api.dependencies.auth_jwt import AuthHandler
from api.routes.crud import CrudApiRouter
from db.repositories.user import UserRepository
from models.schemas.user import UserInLogin, UserResponse
from models.table_models.user import User
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.dependencies.database import get_db 


auth_handler = AuthHandler()


class AuthRouter(CrudApiRouter[User, UserResponse, UserInLogin, UserInLogin], UserRepository):


    def __init__(self, model = User, schema = UserResponse, model_name = "User", create_schema = UserInLogin) -> None:
        super().__init__(model, schema, model_name, create_schema = create_schema, get_all_route = False, get_one_route = False, put_route = False, post_route = False, delete_route = False)

        self.add_router("/login", self.auth(), status.HTTP_202_ACCEPTED, methods = ['POST'], dependencies = [], response_model = UserResponse)

    
    def auth(self):
        async def login(request: UserInLogin, db: Session = Depends(get_db)):
            user = await self.get_by_username_repositroy(request.username, db)

            if not user.first() or not auth_handler.verify_password(request.password, user.first().password):
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND, 
                    detail = "Username or password is incorrect",
                    headers={'error': 'Incorrect'}
                )
            
            access_token = auth_handler.encode_token(user.first().id)
            refresh_token = auth_handler.encode_refresh_token(user.first().id)
            
            return UserResponse(**user.first().__dict__, access_token = access_token, refresh_token = refresh_token)

        return login