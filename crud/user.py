from sqlalchemy.orm import Session
from models import user as user_models
from schemas import user as user_schema
from utils import crypt
from utils.exceptions import UserException, UserError


def find_by_email(db: Session, email: str):
    return db.query(user_models.User).filter(user_models.User.email == email).first()


def find_by_username(db: Session, username: str):
    return db.query(user_models.User).filter(user_models.User.username == username).first()


def create_user(db: Session, user: user_schema.User):
    if find_by_email(db, user.email):
        raise UserException(UserError.EmailUsed)
    if find_by_username(db, user.username):
        raise UserException(UserError.UsernameUsed)
    else:
        user.password = crypt.get_password_hash(user.password)
        new_user = user_models.User(**user.dict())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
