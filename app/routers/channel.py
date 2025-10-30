from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.channel_schema import ChannelCreate, ChannelResponse, ChannelUpdate
from app.controllers.channel_controller import create_channel, get_channels, get_channel_by_id, toggle_active_of_channel, update_channel

router = APIRouter(prefix="/channels", tags=["channels"])

@router.post("/", response_model=ChannelResponse, status_code=201)
def create_channel_route(channel: ChannelCreate, db: Session = Depends(get_db)):
    return create_channel(db, channel)

@router.get("/", response_model=list[ChannelResponse])
def get_channels_list_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_channels(db, skip, limit)

@router.get("/{channel_id}", response_model=ChannelResponse)
def get_channel_route(channel_id: int, db: Session = Depends(get_db)):
    channel = get_channel_by_id(db, channel_id)
    
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    return channel

@router.patch("/{channel_id}/toggle_is_active", response_model=ChannelResponse)
def toggle_active_of_channel_route(channel_id: int, db: Session = Depends(get_db)):
    channel = toggle_active_of_channel(db, channel_id)

    if not channel:
        return HTTPException(status_code=404, detail="Channel was not found")
    
    return channel

@router.patch("/{channel_id}", response_model=ChannelResponse)
def update_channel_route(channel_id: int, channel_data: ChannelUpdate, db: Session = Depends(get_db)):
    channel = update_channel(db, channel_id, channel_data)

    if not channel:
        return HTTPException(status_code=404, detail="Channel was not found")
    
    return channel

@router.delete("/{channel_id}", status_code=204)   #response_model=dict
def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    channel = get_channel_by_id(db, channel_id)

    if not channel:
        raise HTTPException(status_code=404, detail="Channel was not found")
    
    db.delete(channel)
    db.commit()

    # return {"message": "Channel - {channel.name} - was deleted successfully"}
    

