from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base


class Channel(Base):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default='true')

    posts: Mapped[list["Post"]] = relationship(back_populates="channel")
    events: Mapped[list["Event"]] = relationship(back_populates="channel")
