from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Note(Base):
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(String(300), nullable=True)
    is_public: Mapped[bool] = mapped_column(default=True)
    is_completed: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column()