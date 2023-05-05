from __future__ import annotations
from pydantic import BaseModel, validator
from email_validator import validate_email
from typing import List, Optional


class Profile(BaseModel):
    username: str
    bio: str
    image: str
    following: bool


class ProfileWrap:
    profile: Profile
