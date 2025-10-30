from pydantic import BaseModel

class PostCreate(BaseModel):
    channel_id: int
    content: str


class PostResponse(BaseModel):
    id: int
    channel_id: int
    content: str

    class Config:
        from_attributes=True
