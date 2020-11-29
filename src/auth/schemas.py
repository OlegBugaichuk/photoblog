from pydantic import BaseModel
from typing import Optional


class ProfileBase(BaseModel):
    name: Optional[str] = ''
    surname: Optional[str] = ''
    avatar_url: Optional[str] = ''

    class Config:
        orm_mode = True


class BaseUser(BaseModel):
    email: str
    is_active: Optional[bool] = True

    
class CreateUser(BaseUser):
    password: str
    password_confirm: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserDetail(User):
    profile: ProfileBase