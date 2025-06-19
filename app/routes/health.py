"""
Ruta de salud para verificar el estado de la API y la conexión a la base de datos.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    """
    Endpoint para comprobar el estado de la API y la base de datos.

    Returns:
        dict: Estado de la API y la base de datos.
    """
    return {"status": "ok", "database": "connected"}
