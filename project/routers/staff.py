from .auth import User
from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User
from db.db_user import get_all_users
from sqlalchemy.orm.session import Session
from db.base import get_db



router = APIRouter(
    tags=["staff"]
)

@router.get("/users/all", response_model=None)
async def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/user/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
