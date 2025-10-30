from pydantic import BaseModel

class ChannelCreate(BaseModel):
    name: str
    description: str
    is_active: bool = True

class ChannelResponse(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool

    class Config:
        from_attributes=True

class ChannelUpdate(BaseModel):
    name: str = None
    description: str = None
    is_active: bool = None
