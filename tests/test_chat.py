import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_chatbot():
    client.post("/init_user", params={"username": "test_user2", "role": "riesgos laborales"})

    response = client.post("/ask", params={"username": "test_user2", "message": "Dime un consejo de seguridad"})
    assert response.status_code == 200
    assert "response" in response.json()