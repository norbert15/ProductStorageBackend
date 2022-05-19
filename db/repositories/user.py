from fastapi import HTTPException, status
from api.dependencies.auth_jwt import auth_handler
from db.repositories.curd_repository import CrudRepository

from models.table_models.user import User
from models.schemas.user import UserResponse, UserCreate, UserUpdate
from sqlalchemy.orm import Session


class UserRepository(CrudRepository[User, UserResponse, UserCreate, UserUpdate]):

    def __init__(self, model = User, schema = UserResponse, create_schema = UserCreate, model_name = "User") -> None:
        super().__init__(model, schema, create_schema, model_name)


    async def get_by_username_repositroy(self, username: str, db: Session):
        user = db.query(User).filter(User.username == username)

        if not user.first():
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = "Username or password is incorrect",
                headers={'error': 'Incorrect'}
            )
        
        return user

    
    async def put_repository(self, id: int, request: UserUpdate, db: Session):
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


    async def get_by_token_repository(self, token: str, db: Session):
        user = db.query(User).filter(User.id == auth_handler.decode_token(token))

        if not user.first():
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = "User with token not exist",
                headers={'error': 'Not exist'}
            )
        
        return user

