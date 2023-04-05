from sqlalchemy.orm import Session
from models import user as user_models
from schemas import user as user_schema
from utils import crypt
import enum


class UserError(enum.Enum):
    EmailUsed = "This email is already used"


class UserException(Exception):
    def __init__(self, error: UserError):
        self.message = error.value


def find_by_email(db: Session, email: str):
    return db.query(user_models.User).filter(user_models.User.email == email).first()


def create_user(db: Session, user: user_schema.User):
    if find_by_email(db, user.email):
        raise UserException(UserError.EmailUsed)
    else:
        user.password = crypt.get_password_hash(user.password)
        new_user = user_models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
