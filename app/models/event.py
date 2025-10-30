from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))
    target_datetime: Mapped[datetime] = mapped_column(nullable=False)
    is_processed: Mapped[bool] = mapped_column(default=False)
    search_prompt: Mapped[str] = mapped_column(Text)

    channel: Mapped["Channel"] = relationship(back_populates="events")
