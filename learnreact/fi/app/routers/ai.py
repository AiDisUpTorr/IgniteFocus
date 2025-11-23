from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chat import ChatCreate, ChatOut
from app.database.session import get_db
from app.services.llm_server import generate_completion
from app.models.chat import Chat


router = APIRouter()


@router.post("/generate", response_model=ChatOut)
def generate(chat_in: ChatCreate, db: Session = Depends(get_db)):
# call LLM service
    try:
        resp_text = generate_completion(chat_in.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# persist chat
    chat = Chat(prompt=chat_in.prompt, response=resp_text)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat