from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base):
    """Модель пользователя для БД"""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column()
