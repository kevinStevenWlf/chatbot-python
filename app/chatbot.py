"""
Módulo para la interacción con el modelo de lenguaje de OpenAI.

Incluye la función para enviar preguntas al modelo GPT y obtener respuestas personalizadas según el rol.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_gpt(role: str, question: str) -> str:
    """
    Envía una pregunta al modelo GPT de OpenAI con un contexto de rol específico.

    Args:
        role (str): Rol o especialidad que define el contexto del sistema.
        question (str): Pregunta o mensaje enviado por el usuario.

    Returns:
        str: Respuesta generada por el modelo o mensaje de error en caso de excepción.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "system", "content": f"Eres un experto en {role}."},
                {"role": "user", "content": question}
            ]
        )
        print("Respuesta de OpenAI:", response.choices[0].message.content)
        print("-=====", response.choices[0].message)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al conectarse a OpenAI: {str(e)}"
