"""
Archivo principal de la aplicación FastAPI para el chatbot.

Inicializa la base de datos y registra las rutas de usuario, chat e indicadores de salud.
"""

from fastapi import FastAPI
from app.database import init_db
from app.routes import user, chat, health

app = FastAPI()
init_db()

# Registro de rutas
app.include_router(user.router)
app.include_router(chat.router)
app.include_router(health.router)
