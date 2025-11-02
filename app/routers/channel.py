from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.channel_schema import ChannelCreate, ChannelResponse, ChannelUpdate
from app.controllers.channel_controller import create_channel, get_channels, get_channel_by_id, toggle_active_of_channel, update_channel
from app.utils.logger import logger

router = APIRouter(prefix="/channels", tags=["channels"])

@router.post("/", response_model=ChannelResponse, status_code=201)
def create_channel_route(channel: ChannelCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating channel: {channel.name}")

    try:
        channel = create_channel(db, channel)
        logger.success(f"Channel created: id={channel.id}, name={channel.name}")
        return channel
    except Exception as e:
        logger.error(f"Failed to create channel: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/", response_model=list[ChannelResponse])
def get_channels_list_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info(f"Trying to fetch channeles!")

    try:
        channels_list = get_channels(db, skip, limit)
        logger.success(f"Found {len(channels_list)} channels") 
        return channels_list
    except Exception as e:
        logger.error(f"Failed to fetch channels: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{channel_id}", response_model=ChannelResponse)
def get_channel_route(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Trying to fetch channel with id: {channel_id}!")

    try:
        channel = get_channel_by_id(db, channel_id)
        
        if not channel:
            logger.error(f"Channel with id: {channel_id} was not found")
            raise HTTPException(status_code=404, detail="Channel not found")
        logger.success(f"Found channel with id: {channel_id}")

        return channel
    
    except Exception as e:
        logger.error(f"Failed to get information about channel with id: {channel_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
@router.patch("/{channel_id}/toggle_is_active", response_model=ChannelResponse)
def toggle_active_of_channel_route(channel_id: int, db: Session = Depends(get_db)):
    logger.info(f"Trying toggle field - is_active - for channel with id: {channel_id}")

    try:
        channel = toggle_active_of_channel(db, channel_id)

        if not channel:
            logger.error(f"Channel with id: {channel_id} was not found")
            return HTTPException(status_code=404, detail="Channel was not found")
        
        logger.success(f"is_active field for channel with id: {channel_id} was toggled")
        return channel

    except Exception as e:
        logger.error(f"Failed to toggle is_active field for channel with id: {channel_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.patch("/{channel_id}", response_model=ChannelResponse)
def update_channel_route(channel_id: int, channel_data: ChannelUpdate, db: Session = Depends(get_db)):
    logger.info(f"Trying to update info about channel with id: {channel_id}")

    try:
        channel = update_channel(db, channel_id, channel_data)

        if not channel:
            logger.error(f"Channel with id: {channel_id} was not found")
            return HTTPException(status_code=404, detail="Channel was not found")
        logger.success(f"Information of channel with id: {channel_id} was updated.")
        return channel

    except Exception as e:
        logger.error(f"Failed to update info of channel with id: {channel_id}: {e}")
        raise HTTPException(status_code=500, delattr=str(e))
    
@router.delete("/{channel_id}", status_code=204)   #response_model=dict
def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    logger.info()

    try:
        channel = get_channel_by_id(db, channel_id)

        if not channel:
            logger.error(f"Channel with id: {channel_id} was not found")
            raise HTTPException(status_code=404, detail="Channel was not found")
    
        db.delete(channel)
        db.commit()
        logger.success(f"Channel with id: {channel_id} was successfully deleted")

    except Exception as e:
        logger.error(f"Failed to delete channel with id: {channel_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
