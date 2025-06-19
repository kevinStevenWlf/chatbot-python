"""
Definición de los modelos de datos para usuarios y mensajes.

Incluye las clases User y Message que representan las tablas principales de la base de datos.
"""

from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    """
    Modelo de usuario para la base de datos.

    Campos:
        id (int, opcional): Identificador único del usuario.
        username (str): Nombre de usuario.
        role (str): Rol asignado al usuario.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    role: str

class Message(SQLModel, table=True):
    """
    Modelo de mensaje para almacenar interacciones con el chatbot.

    Campos:
        id (int, opcional): Identificador único del mensaje.
        username (str): Nombre de usuario que envió la pregunta.
        question (str): Pregunta realizada al chatbot.
        response (str): Respuesta generada por el chatbot.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    question: str
    response: str
