from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User
from db.db_user import get_all_users
from sqlalchemy.orm.session import Session
from db.base import get_db
from db import db_product
import schemas
from datetime import datetime
from db.models import DbProduct

from random import random

router = APIRouter(
    tags=["product"]
)

#@router.post("/post_check", response_model=schemas.CheckBase)
#async def post_check(request: schemas.CheckBase, db: Session = Depends(get_db)):
#    return db_check.create_check(db, request)


@router.get("/get_sales_data")
async def get_sales_data(
        date_time_start: datetime | str = '',
        date_time_end: datetime | str = '',
        sector: str = '',
        city: str = '',
        store: str = '',
        cashier: str = '',
        category: str = '',
        payment_type: str = '',
        db: Session = Depends(get_db)
        ):
    products = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)
    d = {}
    total = 0
    for product in products:
        date = product.date_time.date
        if date not in d:
            d[date] = []
        d[date].append(product)
        total += product.price
    #return list(d.values())
    return total


@router.get("/get_sales_data/all")
async def get_sales_data_all(
        date_time_start: datetime | str = '',
        date_time_end: datetime | str = '',
        sector: str = '',
        city: str = '',
        store: str = '',
        cashier: str = '',
        payment_type: str = '',
        db: Session = Depends(get_db)
        ):

    #products = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)
    categories = [
        ['Моб. телефоны', 3000000],
        ['Аксессуары', 1500000],
        ['Комп. техника', 1150000],
        ['Билайн', 3000],
        ['МТС', 2770],
        ['Мегафон', 700],
        ['YOTA', 90],
        ['ТЕЛЕ2', 180],
        ['ДСО', 3700000],
        ['Настройки', 3800000],
        ['ВСК cтрахование', 1150000]
    ]
    data = {}
    for category in categories:
        fact = await get_sales_data(
                date_time_start, #date_time_start: datetime | str = '',
                date_time_end, #date_time_end: datetime | str = '',
                sector, #sector: str = '',
                city, #city: str = '',
                store, #store: str = '',
                cashier, #cashier: str = '',
                category, #category: str = '',
                payment_type, #payment_type: str = '',
                db #db: Session = Depends(get_db)
                ),
        fact = fact[0]

        data[category] = {
                'fact': fact,
                'plan': 10000000,
                'pred': round(float(fact) * random() * 10, 2),
            }



        #data[category] = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)


    return data


#@router.get("/get_sales", response_model=list[Product])
#async def get_users(db: Session = Depends(get_db)):
#    return get_all_users(db)


