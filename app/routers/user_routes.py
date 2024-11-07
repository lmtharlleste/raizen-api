from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserOut
from app.cruds.user_crud import create_user, get_user_by_email, get_user_by_id
from app.db.session import get_user_collection

router = APIRouter()

@router.post("/user/register", response_model=UserOut)
async def register_user(user_create: UserCreate):
    user_collection = get_user_collection()
    existing_user = await user_collection.find_one({"email": user_create.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await create_user(user_create)
    return new_user

@router.get("/user/email/{email}", response_model=UserOut)
async def get_user_by_email_route(email: str):
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/user/id/{user_id}", response_model=UserOut)
async def get_user_by_id_route(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
