import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/init_user", params={"username": "test_user", "role": "analista de riesgos"})
    assert response.status_code == 200
    assert "Usuario test_user creado" in response.json()["message"]