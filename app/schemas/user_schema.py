from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    cpf: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: str
    full_name: str
    email: EmailStr
    cpf: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    exp: datetime  # Deve ser do tipo datetime, não str

    class Config:
        orm_mode = True
