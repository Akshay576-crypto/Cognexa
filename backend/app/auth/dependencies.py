from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.config.settings import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_current_user(token: str = Depends(oauth2_scheme)):

    print("TOKEN RECEIVED:", repr(token))

    try:
        payload = jwt.decode(
            token,
            Settings.SECRET_KEY,
            algorithms=[Settings.ALGORITHM]
        )

        email = payload.get("sub")
        user_id = payload.get("user_id")
        role = payload.get("role")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Access Token"
            )

        return {
            "user_id": user_id,
            "email": email,
            "role": role
        }

    except JWTError as e:
        print("JWT ERROR:", e)

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )