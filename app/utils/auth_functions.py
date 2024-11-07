from datetime import timedelta, datetime
from fastapi import HTTPException, status, Depends
from app.schemas.user_schema import UserLogin
from app.cruds.user_crud import get_user_by_email
from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Lendo as variáveis de ambiente
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")  # Substitua pelo valor no .env
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Algoritmo de encriptação do JWT
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))  # Valor padrão se não encontrado no .env

# Configuração do OAuth2 para o Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/user/login")

# Contexto do PassLib para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar se a senha fornecida é a mesma que o hash armazenado
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Função para criar o token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Valor padrão de expiração

    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    # Retornar o token e a data de expiração
    return encoded_jwt, expire  # Retornando o token e a expiração

# No user_login
async def user_login(user_credentials: UserLogin):
    """
    Autentica o usuário com base no email e senha fornecidos.
    Retorna o token JWT se o login for bem-sucedido.
    """
    # Procurando o usuário no banco de dados pelo email
    user = await get_user_by_email(user_credentials.email)
    
    # Se o usuário não existir, retorna erro de autenticação
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    # Verificando se a senha fornecida corresponde à senha armazenada
    if not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    # Gerar o token JWT
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token, exp = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    
    return {"access_token": token, "token_type": "bearer", "exp": exp}

# Função para verificar o token JWT
def verify_token(token: str):
    """
    Função responsável por verificar o token JWT.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Retorna o payload (os dados decodificados) do token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")



async def get_current_user(token: str = Depends(oauth2_scheme), user_id: str = None):
    """
    Função que retorna o usuário atual com base no token JWT fornecido e valida se
    o token corresponde ao ID do usuário na URL.
    """
    # Verifica e decodifica o token JWT
    payload = verify_token(token)  
    email = payload.get("sub")  # O "sub" contém o email do usuário no payload
    
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    
    # Recupera o usuário do banco de dados com o email extraído do token
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
    
    # Se o parâmetro `user_id` for passado na URL, comparamos com o ID do usuário no token
    if user_id and str(user.id) != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para acessar esse usuário")
    
    return user  