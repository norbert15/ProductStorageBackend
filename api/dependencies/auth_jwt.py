from typing import Optional
import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler():


    security = HTTPBearer()
    pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = "auto")
    SECRET = "klsdgwj4h43j9öjweiojnvoqnvoanklnvlksdnbneroiboier"
    ALOGORITHM = 'HS256'


    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)


    def verify_password(self, plain_password, hashed_password):
        try:
            return self.pwd_context.verify(plain_password, hashed_password)
        except Exception:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = "Username or password is incorrect",
                headers={'error': 'Incorrect'}
                )

    
    def encode_token(self, user_id: int):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, hours=10),
            'iat': datetime.utcnow(),
            'scope': 'access_token',
            'sub': user_id
        }

        return jwt.encode(payload, self.SECRET, self.ALOGORITHM)

    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET, self.ALOGORITHM)

            if (payload['scope'] == 'access_token'):
                return payload['sub']

            raise HTTPException(status_code=401, detail='Scope for the token is invalid')

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Not authenticated')

        except jwt.InvalidTokenError:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Invalid access token')


    def encode_refresh_token(self, user_id: int):
        payload = {
            'exp' : datetime.utcnow() + timedelta(days=0, hours=10),
            'iat' : datetime.utcnow(),
	        'scope': 'refresh_token',
            'sub' : user_id
        }

        return jwt.encode(payload, self.SECRET, self.ALOGORITHM)

    
    def refresh_token(self, refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, self.SECRET, self.ALOGORITHM)
            if payload['scope'] == 'refresh_token':
                return self.encode_token(payload['sub']) 

            raise HTTPException(status_code=401, detail='Scope for the token is invalid')

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Refresh token expired')

        except jwt.InvalidTokenError:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Invalid refresh token')

    
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth_handler = AuthHandler()