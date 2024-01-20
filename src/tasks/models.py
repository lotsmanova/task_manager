from datetime import datetime
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import ChoiceType
from src.database import Base
from src.tasks.schemas import Task


class Tasks(Base):
    """Модель задач"""

    STATUS = [
        ('create', 'create'),
        ('process', 'process'),
        ('finish', 'finish'),
    ]

    __tablename__ = "task"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column(ChoiceType(STATUS), default='create')
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    date_create: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def to_pydantic_model(self) -> Task:
        return Task(
            id=self.id,
            title=self.title,
            description=self.description,
            status=self.status.value,
            user_id=self.user_id,
            date_create=self.date_create
        )
