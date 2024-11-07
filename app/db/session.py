# app/db/session.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI  # Importando diretamente o URI do MongoDB do config.py

client: AsyncIOMotorClient = None
database = None

# Função para inicializar a conexão com o banco de dados MongoDB
async def init_db():
    global client, database
    client = AsyncIOMotorClient(MONGO_URI)  # Usa a URL do MongoDB obtida do config.py
    database = client["raizen_db"]  # Defina o nome do banco de dados explicitamente aqui

# Função para acessar a coleção de usuários
def get_user_collection():
    if database is None:
        raise Exception("Database connection is not initialized")
    return database.get_collection("users")  # Acessa a coleção 'users'
