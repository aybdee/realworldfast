from fastapi import APIRouter, Depends, HTTPException
from schemas.user import User
from crud import user as user_crud
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()


@router.post('/')
def register_users(user: User, db: Session = Depends(get_db)):
    try:
        user = user_crud.create_user(db, user)
        return user

    except user_crud.UserException as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )
