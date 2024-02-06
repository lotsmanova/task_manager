from typing import Annotated
from fastapi import Depends
from src.utils.unitofwork import IUnitOfWork, UnitOfWork

# Depend for app
UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
