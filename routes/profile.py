from fastapi import APIRouter, Depends
from crud.user import find_by_username
from db.session import get_db
from sqlalchemy.orm import Session

from utils.auth import get_current_user_oauth

router = APIRouter()

auth_mode = get_current_user_oauth


@router.get("{username}")
def get_profiles(current_user=Depends(get_current_user_oauth), db: Session = Depends(get_db)):
    user = find_by_username(db, username)
    pass


@router.post("{username}/follow")
def get_profiles(current_user=Depends(get_current_user_oauth), db: Session = Depends(get_db)):
    user = find_by_username(db, username)
    current_user.following.append(user.id)
    pass
