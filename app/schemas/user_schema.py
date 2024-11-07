# app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr


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
