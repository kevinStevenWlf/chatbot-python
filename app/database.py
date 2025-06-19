"""
Módulo para la configuración y manejo de la base de datos.

Incluye la inicialización del motor de la base de datos y la función para crear las tablas.
"""

from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.
    """
    SQLModel.metadata.create_all(engine)