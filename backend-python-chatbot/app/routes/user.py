from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from app.models import User
from app.database import engine

router = APIRouter()

@router.post("/init_user")
def create_user(username: str, role: str):
    with Session(engine) as session:
        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        return {"message": f"Usuario {username} creado con rol {role}"}
