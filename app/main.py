from fastapi import FastAPI
from app.api.endpoints import router as api_router

# Crear una instancia de FastAPI
app = FastAPI()

# Incluir el router definido en api_router con el prefijo "/api"
app.include_router(api_router, prefix="/api")
