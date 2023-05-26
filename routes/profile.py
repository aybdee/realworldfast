from typing import Any, List
from fastapi import APIRouter, Depends, Path
from crud.user import find_by_username
from db.session import get_db
from sqlalchemy.orm import Session
from schemas.user import UserDB

from utils.auth import get_current_user_oauth
from utils.exceptions import ProfileException, ProfileError

router = APIRouter()

auth_mode = get_current_user_oauth


def insert_relationship(attribute: None | List[Any]):
    if attribute == None:
        return []
    else:
        return attribute


@router.get("{username}")
def get_profiles(
    username,
    current_user=Depends(get_current_user_oauth),
    db: Session = Depends(get_db),
):
    user = find_by_username(db, username)
    pass


@router.post("{username}/follow")
def follow_user(
    username: str = Path(title="username to follow"),
    current_user=Depends(get_current_user_oauth),
    db: Session = Depends(get_db),
):
    user = find_by_username(db, username)

    current_user.following = (
        [] if not current_user.following else current_user.following
    )
    if user not in current_user.following:
        current_user.following.append(user)
        db.commit()
        return UserDB.from_orm(current_user)
    else:
        return ProfileException(ProfileError.AlreadyFollowed)


@router.delete("{username}/follow")
def unfollow_user(username: str = Path(title="username to unfollow"), current_user= Depends(get_current_user_oauth), db:Session = Depends(get_db)):
    user = find_by_username(db,username)
    if user in current_user.following:
        current_user.following.remove(user) 
        db.commit()
        return UserDB.from_orm(current_user)
        
    else:
        return ProfileException(ProfileError.NotFollowing)
         
