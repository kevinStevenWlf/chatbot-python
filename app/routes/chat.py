from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models import User, Message
from app.database import engine
from app.chatbot import ask_gpt

router = APIRouter()

@router.post("/ask")
async def ask(username: str, message: str):
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
def history(username: str):
    with Session(engine) as session:
        messages = session.exec(select(Message).where(Message.username == username)).all()
        return messages
