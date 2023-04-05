from __future__ import annotations
from pydantic import BaseModel, validator
from email_validator import validate_email
from typing import List, Optional


class UserBase(BaseModel):
    email: str
    password: str

    @validator("email", pre=True)
    def is_valid_email(cls, email):
        validate_email(email)
        return email


class User(UserBase):
    username: str
    bio: Optional[str]
    image: Optional[str]
    token: Optional[str]


class UserDB(User):
    id: int
    following: List[UserDB] = []

    class Config:
        orm_mode = True


UserDB.update_forward_refs()
