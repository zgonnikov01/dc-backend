from .auth import User
from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User
from db.db_user import get_all_users
from sqlalchemy.orm.session import Session
from db.base import get_db
from schemas import ProductBase
import schemas
from datetime import datetime
from db import models
from db import db_check

from routers.auth import (
    get_user_provider,
    get_user_basic,
    get_user_manager,
    get_user_full_access,
    get_user_admin
)



router = APIRouter(
    tags=["checks"]
)


@router.post("/post_check")
async def post_check(
        request: schemas.CheckBase,
        db: Session = Depends(get_db),
        user: User = Depends(get_user_provider)
    ):
    return db_check.create_check(db, request)

#@router.get("/get_checks")
async def get_checks(
        date_time_start: datetime | str = '',
        date_time_end: datetime | str = '',
        sector: str = '',
        city: str = '',
        store: str = '',
        cashier: str = '',
        payment_type: str = '',
        db: Session = Depends(get_db),
        user: User = Depends(get_user_basic)
        ):
    return db_check.get_checks(db, date_time_start, date_time_end, sector, city, store, cashier, payment_type)

#@router.get("/get_sales", response_model=list[Product])
#async def get_users(db: Session = Depends(get_db)):
#    return get_all_users(db)
