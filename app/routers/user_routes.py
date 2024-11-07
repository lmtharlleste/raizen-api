from app.cruds.user_crud import create_user, get_user_by_email, get_user_by_id
from app.utils.auth import user_login
from app.models.user_model import User
from app.utils.auth_functions import get_current_user
from app.schemas.user_schema import UserCreate, UserOut, UserLogin, Token
from fastapi import APIRouter, Depends, HTTPException, status
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


@router.post("/user/login", response_model=Token)
async def login_user(user_credentials: UserLogin):  # Renomeado para evitar conflito
    token_data = await user_login(user_credentials)  # Usando o novo nome
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return token_data



@router.get("/user/email/{email}", response_model=UserOut)
async def get_user_by_email_route(email: str, current_user: User = Depends(get_current_user)):
    """
    Rota para obter usuário por email. Requer autenticação.
    """
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/user/id/{user_id}", response_model=UserOut)
async def get_user_by_id_route(user_id: str, current_user: User = Depends(get_current_user)):
    """
    Rota para obter usuário por ID. Requer autenticação.
    """
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user