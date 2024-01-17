from typing import Optional
from fastapi import Depends, Request
from fastapi_mail import FastMail, MessageSchema
from fastapi_users import (BaseUserManager, IntegerIDMixin)
from src.config import conf
from src.auth.models import User
from src.auth.utils import get_user_db
from src.config import SECRET_AUTH


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH
    verification_token_secret = SECRET_AUTH

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.username} has registered.")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        message = MessageSchema(
            subject=f"Verification {user.email}",
            recipients=[user.email],
            body=f"Verification requested for user {user.username}. Verification token: {token}",
            subtype="plain"
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        print(f"Verification requested for user {user.username}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
