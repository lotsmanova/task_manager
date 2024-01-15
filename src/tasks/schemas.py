from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    user_id: int
    date_create: datetime