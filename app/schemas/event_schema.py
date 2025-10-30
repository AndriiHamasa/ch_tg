from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    channel_id: int
    target_datetime: datetime
    search_prompt: str


class EventResponse(BaseModel):
    id: int
    channel_id: int
    target_datetime: datetime
    is_processed: bool
    search_prompt: str

    class Config:
        from_attributes=True
