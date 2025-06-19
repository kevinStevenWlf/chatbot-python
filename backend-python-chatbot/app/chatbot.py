import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_gpt(role: str, question: str) -> str:
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
