from pydantic import BaseModel, EmailStr


class UserAdd(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
