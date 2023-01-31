from .auth import User
from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User


router = APIRouter(
    tags=["staff"]
)


@router.get("/user/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
