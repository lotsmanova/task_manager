from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from src.database import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    description = Column(String(200))
    user_id = Column(ForeignKey("user.id"))
    date_create = Column(TIMESTAMP, default=datetime.utcnow)

