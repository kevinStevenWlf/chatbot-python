# 🧠 FastAPI GPT Chatbot - Evaluador de Riesgos Laborales

¡Bienvenido a tu asistente conversacional experto en evaluación de riesgos laborales!  
Este proyecto es una API RESTful construida con **FastAPI** que integra el modelo **GPT-3.5-turbo** de OpenAI. Permite crear usuarios con un **rol específico**, enviarle preguntas al chatbot y consultar el historial de conversaciones, todo con persistencia local en **SQLite**.

---

## 🚀 ¿Qué hace este proyecto?

🔹 Permite registrar usuarios con un rol (ej. "experto en seguridad industrial").  
🔹 Usa la API de OpenAI para simular un chatbot especializado según ese rol.  
🔹 Guarda cada interacción (pregunta/respuesta) en una base de datos SQLite.  
🔹 Expone endpoints RESTful bien documentados (Swagger).  
🔹 Incluye pruebas unitarias y validación de calidad con Pyright.

---

## 🛠️ Tecnologías usadas

- 🐍 Python 3.9+
- ⚡ FastAPI
- 🧠 OpenAI (GPT-3.5)
- 💾 SQLite + SQLModel
- 🧪 Pytest
- 📄 .env (python-dotenv)
- ✅ Pyright

---

## 🧩 Endpoints disponibles

| Método | Endpoint                  | Descripción                                 |
|--------|---------------------------|---------------------------------------------|
| POST   | `/init_user`             | Crear usuario con rol                       |
| POST   | `/ask`                   | Enviar pregunta al chatbot                  |
| GET    | `/history/{username}`    | Consultar historial de interacciones        |
| GET    | `/health`                | Verificar estado del servicio               |

Puedes explorar todos los endpoints en Swagger UI:  
📘 http://127.0.0.1:8000/docs

---

## ⚙️ Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/backend-chatbot.git
cd backend-chatbot
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate 
.\venv\Scripts\activate         
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura tus credenciales

Crea un archivo `.env` en la raíz del proyecto con tu clave de OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

### 5. Ejecuta el servidor

```bash
uvicorn app.main:app --reload
```

---

## ✅ Cómo ejecutar pruebas

```bash
pytest
```

---

## 🧪 Ejemplo de prueba unitaria incluida

```python
def test_create_user():
    response = client.post("/init_user", params={"username": "test_user", "role": "analista de riesgos"})
    assert response.status_code == 200
```


## 🧼 Validación de calidad del código

Este proyecto fue validado con `pyright`:

```bash
pyright
```

---

## 📄 Licencia

Este proyecto fue desarrollado como parte de una prueba técnica para el rol de **Desarrollador Backend Python**.  
Puedes adaptarlo, mejorarlo y extenderlo a otros dominios.

---

### ✨ Autor

Desarrollado por KevinStevenWlf https://kevinstevenwlf.github.io/curriculum/.
