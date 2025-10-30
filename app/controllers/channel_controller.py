from sqlalchemy.orm import Session
from app.models.channel import Channel
from app.schemas.channel_schema import ChannelCreate, ChannelUpdate

def create_channel(db: Session, channel: ChannelCreate):
    db_channel = Channel(name=channel.name, description=channel.description)
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def get_channels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Channel).offset(skip).limit(limit).all()

def get_channel_by_id(db: Session, id: int):
    return db.query(Channel).filter(Channel.id==id).first()

def toggle_active_of_channel(db: Session, id: int):
    db_channel = db.query(Channel).filter(Channel.id==id).first()

    if not db_channel:
        return None

    db_channel.is_active = not db_channel.is_active
    db.commit()
    db.refresh(db_channel)
    return db_channel

def update_channel(db: Session, id: int, channel_data: ChannelUpdate):
    db_channel = db.query(Channel).filter(Channel.id==id).first()

    if not db_channel:
        return None

    update_data = channel_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_channel, key, value)

    db.commit()
    db.refresh(db_channel)
    return db_channel
    

