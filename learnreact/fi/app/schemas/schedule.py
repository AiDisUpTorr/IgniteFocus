from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ScheduleCreate(BaseModel):
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: Optional[datetime]


class ScheduleOut(ScheduleCreate):
    id: int
    user_id: int
    created_at: datetime


class Config:
    orm_mode = True