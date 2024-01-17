from typing import Annotated
from fastapi import Depends
from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.utils.unitofwork import IUnitOfWork, UnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
User_ver = Annotated[User, Depends(fastapi_users.current_user(active=True, verified=True))]
