from typing import Optional
from fastapi import Depends, Request
from fastapi_mail import FastMail, MessageSchema
from fastapi_users import (BaseUserManager, IntegerIDMixin)
from src.config import conf
from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """Менеджер для выполнения действий после регистрации"""

    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.username} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
