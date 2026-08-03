from app.repositories.user_reposetries import UserReposetory
from app.core.security import (hash_password,verify_password,create_access_token)

class UserServices:

    def __init__(self):
        self.user_reposetory = UserReposetory()

    def register_user(self,full_name:str,email:str,password:str):

        existing_user = self.user_reposetory.get_user_by_email(email)

        if existing_user:

            return{
            "success": False,
            "message": "Email already exists.",
            "data": None
                }

        password_hash = hash_password(password)

        user_id = self.user_reposetory.create_user(
        full_name=full_name,
        email=email,
        password_hash=password_hash
        )

        return {
        "success": True,
        "message": "User registered successfully.",
        "data": {
            "user_id": user_id
        }
               }
    
    def login_user(self,email:str,password:str):

        user = self.user_reposetory.get_user_by_email(email)

        if not user:
            return {
            "success": False,
            "message": "Invalid email or Password.",
            "data": None
        }

        if not verify_password(password,user["password_hash"]):
            return {
            "success": False,
            "message": "Invalid email or password.",
            "data": None
        }

        token = create_access_token({
            "sub": user["email"],
            "user_id": user["user_id"],
            "role": user["role"]
        })

        self.user_reposetory.update_last_login(user["user_id"])

        return {
        "success": True,
        "message": "Login successful.",
        "data": {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "user_id": user["user_id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "role": user["role"]
            }
        }
    }






