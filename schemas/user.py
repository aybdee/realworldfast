from __future__ import annotations
from pydantic import BaseModel, validator
from email_validator import validate_email
from typing import List, Optional


class UserBase(BaseModel):
    email: str
    password: str

    # @validator("email", pre=True)
    # def is_valid_email(cls, email):
    #     validate_email(email)
    #     return email


class UserBaseEdit(BaseModel):
    email: Optional[str]
    password: Optional[str]

    # @validator("email", pre=True)
    # def is_valid_email(cls, email):
    #     validate_email(email)
    #     return email


class UserEdit(UserBaseEdit):
    username: Optional[str]
    bio: Optional[str]
    image: Optional[str]


class User(UserBase):
    username: str
    bio: Optional[str]
    image: Optional[str]


class UserDB(User):
    id: int
    token: Optional[str]
    following: Optional[List[UserDB]] = []

    class Config:
        orm_mode = True


UserDB.update_forward_refs()


class UserWrap(BaseModel):
    user: User


class UserBaseWrap(BaseModel):
    user: UserBase


class UserEditWrap(BaseModel):
    user: UserEdit
