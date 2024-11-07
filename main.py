from fastapi import FastAPI
from app.db.session import init_db
from app.routers import user_routes  # Importe as rotas de usuário

app = FastAPI()

# Inicializa o banco de dados no início
@app.on_event("startup")
async def startup_db():
    await init_db()

@app.on_event("shutdown")
async def shutdown_db():
    if app.state.database:
        app.state.database.client.close()

# Incluindo o roteador com o prefixo /api/v1
app.include_router(user_routes.router, prefix="/api/v1")
