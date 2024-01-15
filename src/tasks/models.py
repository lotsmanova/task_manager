from datetime import datetime
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.tasks.schemas import Task


class Tasks(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    date_create: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def to_pydantic_model(self) -> Task:
        return Task(
            id=self.id,
            title=self.title,
            description=self.description,
            user_id=self.user_id,
            date_create=self.date_create
        )
