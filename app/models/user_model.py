# app/models/user_model.py

from pydantic import BaseModel
from typing import Optional
from pydantic.networks import EmailStr
from bson import ObjectId


class User(BaseModel):
    full_name: str
    email: EmailStr
    cpf: str
    hashed_password: str

    class Config:
        orm_mode = True

class UserInDB(User):
    id: str
