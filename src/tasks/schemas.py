from enum import Enum
from datetime import datetime

from pydantic import BaseModel, validator


class TaskStatus(str, Enum):
    create = 'create'
    process = 'process'
    finish = 'finish'


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    user_id: int
    date_create: datetime

    @validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value


class TaskAdd(BaseModel):

    title: str
    description: str
    status: TaskStatus
    user_id: int

    @validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value


class TaskEdit(BaseModel):

    title: str
    description: str
    status: TaskStatus

    @validator('status')
    def validate_status(cls, value):
        return value.value if isinstance(value, TaskStatus) else value
