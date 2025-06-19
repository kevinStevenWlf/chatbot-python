"""
Rutas para la gestión de usuarios en la aplicación.

Incluye endpoint para inicializar (crear) un usuario con un rol específico.
"""

from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from app.models import User
from app.database import engine

router = APIRouter()

@router.post("/init_user")
def create_user(username: str, role: str):
    """
    Crea un nuevo usuario con el nombre de usuario y rol especificados.

    Args:
        username (str): Nombre de usuario a crear.
        role (str): Rol asignado al usuario.

    Returns:
        dict: Mensaje de confirmación de creación de usuario.
    """
    with Session(engine) as session:
        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        return {"message": f"Usuario {username} creado con rol {role}"}
