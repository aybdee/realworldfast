from pydantic import BaseModel, validator
from email_validator import validate_email


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

    # @validator("email", pre=True)
    # def is_valid_email(cls, email):
    #     validate_email(email)
    #     return email
