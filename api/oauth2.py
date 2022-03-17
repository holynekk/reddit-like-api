from jose import JWTError, jwt
from .config import settings
from datetime import datetime, timedelta

def create_access_token(data: dict):
    # Copy data in order not to change it
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})

    # Creating JWT token
    jwt_token = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

    return jwt_token