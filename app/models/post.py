from sqlalchemy import ForeignKey, Text
from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))
    content: Mapped[str] = mapped_column(Text)

    channel: Mapped["Channel"] = relationship(back_populates="posts")
