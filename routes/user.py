from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserBaseWrap, UserDB, UserEditWrap, UserWrap
from crud import user as user_crud
from sqlalchemy.orm import Session
from db.session import get_db
from utils.auth import create_access_token, get_current_user
from utils.crypt import verify_password
from utils.exceptions import UserError, UserException

router = APIRouter()


@router.post('/')
def register_users(user: UserWrap, db: Session = Depends(get_db)):
    try:
        user = user_crud.create_user(db, user.user)
        user_wrapped = {"user": user}
        return user_wrapped

    except user_crud.UserException as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )


@router.post('/login')
def login_user(userCred: UserBaseWrap, db: Session = Depends(get_db)):
    user = user_crud.find_by_email(db, userCred.user.email)
    try:
        if user:
            if verify_password(userCred.user.password, user.password):
                token = create_access_token({"email": user.email})
                user.token = token
                user_m = UserDB.from_orm(user)
                db.commit()
                return {"user": user_m}
            else:
                raise user_crud.UserException(
                    UserError.PasswordIncorrect)
        else:
            raise user_crud.UserException(
                UserError.EmailNotExist)

    except user_crud.UserException as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )


@router.get("/")
async def get_user(current_user: UserDB = Depends(get_current_user), db: Session = Depends(get_db)):
    user_m = UserDB.from_orm(current_user)
    return {"user": user_m}


@router.put('/')
async def update_user(user: UserEditWrap, current_user: UserDB = Depends(get_current_user),  db: Session = Depends(get_db)):
    properties = [
        'email',
        'password',
        'bio',
        'image',
        'username',
    ]
    try:
        if user.user.email:
            if user_crud.find_by_email(db, user.user.email):
                raise UserException(user_crud.UserError.EmailUsed)
        if user.user.username:
            if user_crud.find_by_username(db, user.user.username):
                raise UserException(user_crud.UserError.EmailUsed)
        for property in properties:
            if getattr(user, property):
                setattr(current_user, property, getattr(user, property))
        user_m = UserDB.from_orm(current_user)
        db.commit()
        return {"user": user_m}

    except UserException as e:
        raise HTTPException(
            status_code=400,
            detail=e.message
        )

        # if user.user.username and user_crud.find_by_username(db, user.username):

    pass
