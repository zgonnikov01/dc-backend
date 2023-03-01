from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User
from db.db_user import get_all_users
from sqlalchemy.orm.session import Session
from db.base import get_db
from db import db_product
import schemas
from datetime import datetime
from db.models import DbProduct


router = APIRouter(
    tags=["product"]
)

#@router.post("/post_check", response_model=schemas.CheckBase)
#async def post_check(request: schemas.CheckBase, db: Session = Depends(get_db)):
#    return db_check.create_check(db, request)

@router.get("/get_products")
async def get_products(
        date_time_start: datetime | bool = True,
        date_time_end: datetime | bool = True,
        sector: str = True,
        city: str = True,
        store: str = True,
        cashier: str = True,
        category: str = True,
        db: Session = Depends(get_db)
        ):
    return db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category)

@router.get("/get_products_daily")
async def get_products_daily(
        date_time_start: datetime | bool = True,
        date_time_end: datetime | bool = True,
        sector: str = True,
        city: str = True,
        store: str = True,
        cashier: str = True,
        category: str = True,
        db: Session = Depends(get_db)
        ):
    products = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category)
    d = {}
    total = 0
    for product in products:
        print(product)
        date = product.date_time.date
        if date not in d:
            d[date] = []
        d[date].append(product)
        total += product.price
    #return list(d.values())
    return total

async def get_all_products_by_date(
        date_time_start: datetime | bool,
        date_time_end: datetime | bool,
        db: Session = Depends(get_db)
        ):
    pass
#@router.get("/get_sales", response_model=list[Product])
#async def get_users(db: Session = Depends(get_db)):
#    return get_all_users(db)
