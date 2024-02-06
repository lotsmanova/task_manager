from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.crud import user_crud
from src.auth.jwt import create_access_token, get_user_by_token
from src.auth.schemas import UserRead, UserAdd
from src.auth.security import verify_password
from src.database import get_async_session


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register/", response_model=UserRead)
async def create_user(user: UserAdd, session: AsyncSession = Depends(get_async_session)) -> UserRead:
    try:
        user_db = await user_crud.add_user(session, user)
        return user_db

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email was already registered.",
        )


@router.post("/login/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                session: AsyncSession = Depends(get_async_session)):
    user = await user_crud.get_user_by_username(session, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
    jwt_token = create_access_token({"sub": form_data.username})
    return {"access_token": jwt_token, "token_type": "bearer"}


@router.get("/about_me/", response_model=UserRead)
async def read_user(session: AsyncSession = Depends(get_async_session),
                    username: str = Depends(get_user_by_token)) -> UserRead:
    user = await user_crud.get_user_by_username(session, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
