"""
Rutas para la interacción con el chatbot y la gestión del historial de mensajes.

Incluye endpoints para enviar preguntas al chatbot y recuperar el historial de mensajes de un usuario.
"""

from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import User, Message
from app.database import engine
from app.chatbot import ask_gpt

router = APIRouter()

@router.post("/ask")
# TODO: extraer la lógica de llamada a OpenAI en un servicio separado para facilitar pruebas y mantenimiento
# FIXME: la función ask() asume que el usuario existe, sin manejar múltiples sesiones o historial prolongado
async def ask(username: str, message: str):
    """
    Envía una pregunta al chatbot y almacena la interacción en la base de datos.

    Args:
        username (str): Nombre de usuario que realiza la pregunta.
        message (str): Pregunta o mensaje enviado al chatbot.

    Returns:
        dict: Respuesta generada por el chatbot.

    Raises:
        HTTPException: Si el usuario no existe en la base de datos.
    """
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        response = await ask_gpt(user.role, message)
        interaction = Message(username=username, question=message, response=response)
        session.add(interaction)
        session.commit()
        return {"response": response}

@router.get("/history/{username}")
# TODO: paginar o limitar el historial para evitar devolver grandes volúmenes de datos
def history(username: str):
    """
    Recupera el historial de mensajes de un usuario específico.

    Args:
        username (str): Nombre de usuario cuyo historial se desea consultar.

    Returns:
        list[Message]: Lista de mensajes asociados al usuario.
    """
    with Session(engine) as session:
        messages = session.exec(select(Message).where(Message.username == username)).all()
        return messages
