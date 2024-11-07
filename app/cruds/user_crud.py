# app/crud/user_crud.py

from app.db.session import get_user_collection
from app.models.user_model import UserInDB
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext
from bson import ObjectId


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user_create: UserCreate):
    user_collection = get_user_collection()

    
    hashed_password = pwd_context.hash(user_create.password)

    
    user_data = {
        "full_name": user_create.full_name,
        "email": user_create.email,
        "cpf": user_create.cpf,
        "hashed_password": hashed_password,
    }

    
    result = await user_collection.insert_one(user_data)

    user = await user_collection.find_one({"_id": result.inserted_id})
    return UserInDB(id=str(user["_id"]), full_name=user["full_name"], email=user["email"], cpf=user["cpf"], hashed_password=user["hashed_password"])



async def get_user_by_email(email: str) -> UserInDB:
    user_collection = get_user_collection()

    user = await user_collection.find_one({"email": email})

    if not user:
        return None  # Ou levante uma exceção, se necessário

    return UserInDB(
        id=str(user["_id"]),
        full_name=user["full_name"],
        email=user["email"],
        cpf=user["cpf"],
        hashed_password=user["hashed_password"]
    )


async def get_user_by_id(user_id: str) -> UserInDB:
    user_collection = get_user_collection()

    # Convertendo o ID para o formato ObjectId
    user_object_id = ObjectId(user_id)
    
    user = await user_collection.find_one({"_id": user_object_id})

    if not user:
        return None  # Ou levante uma exceção, dependendo do seu fluxo

    return UserInDB(
        id=str(user["_id"]),
        full_name=user["full_name"],
        email=user["email"],
        cpf=user["cpf"],
        hashed_password=user["hashed_password"]
    )