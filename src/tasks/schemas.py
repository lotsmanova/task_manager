from enum import Enum
from datetime import datetime
from pydantic import BaseModel, field_validator


class TaskStatus(str, Enum):
    create = 'create'
    process = 'process'
    finish = 'finish'


class Task(BaseModel):
    """Общая схема задачи"""

    id: int
    title: str
    description: str
    status: TaskStatus
    owner_id: int
    date_create: datetime

    @field_validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value


class TaskAdd(BaseModel):
    """Схема для создания задачи"""

    title: str
    description: str
    status: TaskStatus
    owner_id: int

    @field_validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value


class TaskEdit(BaseModel):
    """Схема для редактирования задачи"""

    title: str
    description: str
    status: TaskStatus
    owner_id: int

    @field_validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value
