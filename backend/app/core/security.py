from datetime import datetime,timedelta
from typing import Optional

from jose import JWTError,jwt
from passlib.context import CryptContext
from app.config.settings import Settings

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str) -> str:

    #Hash a Plain text password
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against its hash.
    """
    return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data:dict,expires_delta:Optional[timedelta] = None):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(
            minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        Settings.SECRET_KEY,
        algorithm=Settings.ALGORITHM
    )

    return encoded_jwt

def verify_token(token:str):

    try:

        payload = jwt.decode(token,
                             Settings.SECRET_KEY,
                             algorithms=[Settings.ALGORITHM]
                             )
        return payload
    except JWTError:
        return None
    

