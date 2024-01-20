from typing import Optional

from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема для вывода информации"""

    id: int
    email: str
    username: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя"""

    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
