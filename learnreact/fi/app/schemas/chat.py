from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatCreate(BaseModel):
    prompt: str


class ChatOut(BaseModel):
    id: int
    user_id: int
    prompt: str
    response: Optional[str]
    created_at: datetime


class Config:
    orm_mode = True