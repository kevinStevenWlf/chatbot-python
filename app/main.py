from fastapi import FastAPI
from app.database import init_db
from app.routes import user, chat, health

app = FastAPI()
init_db()

app.include_router(user.router)
app.include_router(chat.router)
app.include_router(health.router)
