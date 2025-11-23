from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.models.chat import Chat
from app.schemas.chat import ChatOut


router = APIRouter()


@router.get("/chats", response_model=List[ChatOut])
def list_chats(db: Session = Depends(get_db)):
    chats = db.query(Chat).order_by(Chat.created_at.desc()).limit(100).all()
    return chats