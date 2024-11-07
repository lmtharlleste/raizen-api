from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user_schema import UserCreate, UserLogin, UserOut, Token
from app.cruds.user_crud import create_user, get_user_by_email, get_user_by_id
from app.utils.auth_functions import user_login, get_current_user
from app.db.session import get_user_collection

router = APIRouter()

@router.post("/user/register", response_model=UserOut)
async def register_user(user_create: UserCreate):
    """
    Rota para registrar um novo usuário.
    """
    user_collection = get_user_collection()
    existing_user = await user_collection.find_one({"email": user_create.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    new_user = await create_user(user_create)
    return new_user

@router.post("/user/login", response_model=Token)
async def login_user(user_credentials: UserLogin):
    """
    Rota de login do usuário. Recebe as credenciais de email e senha e retorna um token JWT.
    """
    token_data = await user_login(user_credentials)
    
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )
    
    return token_data

@router.get("/user/email/{email}", response_model=UserOut)
async def get_user_by_email_route(email: str, current_user: UserOut = Depends(get_current_user)):
    """
    Rota para buscar um usuário pelo email. Usuário precisa estar autenticado.
    """
    if current_user['email'] != email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Não autorizado a acessar este usuário")
    
    user = await get_user_by_email(email)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return user

@router.get("/user/id/{user_id}", response_model=UserOut)
async def get_user_by_id_route(user_id: str, current_user: UserOut = Depends(get_current_user)):
    """
    Rota para buscar um usuário pelo ID. Usuário precisa estar autenticado.
    """
    user = await get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if current_user['id'] != user['id']:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Não autorizado a acessar este usuário")
    
    return user
