from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import(UserCreate,UserLogin)
from app.services.user_services import UserServices
from fastapi import Depends
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/auth",tags=["Authentication"])

service = UserServices()

@router.post("/signup")
def signup_user(user:UserCreate):

    return service.register_user(full_name=user.full_name,
                                 email=user.email,
                                 password=user.password)
@router.post("/token")
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    result = service.login_user(
        email=form_data.username,
        password=form_data.password
    )

    if not result["success"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": result["data"]["access_token"],
        "token_type": "bearer"
    }

@router.get("/profile")
def profile(current_user=Depends(get_current_user)):

    return {"sucess":True,"data":current_user}

    