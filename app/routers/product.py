from fastapi import Depends, APIRouter
from routers.auth import get_current_active_user, User
from db.db_user import get_all_users
from sqlalchemy.orm.session import Session
from db.base import get_db
from db import db_product
import schemas
from datetime import datetime, date, timedelta
from db.models import DbProduct

from random import random

router = APIRouter(
    tags=["product"]
)

#@router.post("/post_check", response_model=schemas.CheckBase)
#async def post_check(request: schemas.CheckBase, db: Session = Depends(get_db)):
#    return db_check.create_check(db, request)

from routers.auth import get_user_basic

@router.get("/get_card_graph")
async def get_card_graph(
        category: str,
        date_time_start: datetime,
        date_time_end: datetime,
        sector: str = '',
        city: str = '',
        store: str = '',
        cashier: str = '',
        payment_type: str = '',
        db: Session = Depends(get_db),
        user: User = Depends(get_user_basic)
        ):
    products = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)

    categories = {
        'Моб. телефоны': 3000000,
        'Аксессуары': 1500000,
        'Комп. техника': 1150000,
        'Билайн': 3000,
        'МТС': 2770,
        'Мегафон': 700,
        'YOTA': 90,
        'ТЕЛЕ2': 180,
        'ДСО': 3700000,
        'Настройки': 3800000,
        'ВСК cтрахование': 1150000,
    }
    print(category)
    plan = categories[category]

    start = date_time_start
    end = date_time_end
    total = int((end - start).days)
    BREAKPOINTS = 10 - 1
    INC = total // BREAKPOINTS

    dates = [(start + timedelta(x)).date() for x in range(total, INC, -(INC))][::-1]

    i = 0
    def date_to_str(date):
        months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return f'{months[date.month]} {date.year % 2000}'
    date_strs = list(map(lambda x: date_to_str(x), [start, *dates]))
    graph = {'dates': date_strs, 'fact': [], 'plan': [], 'pred': []}
    curfact = curplan = curpred = 0
    for j in range(BREAKPOINTS + 1):
        #graph['plan'].append(int(plan / BREAKPOINTS * j))
        while i < len(products) and products[i].date_time.date() <= dates[j]:
            curfact += products[i].price
            i += 1
        graph['fact'].append(curfact)
    print(graph)
    return graph


@router.get("/get_sales_data/all")
async def get_sales_data_all(
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

    #products = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)
    categories = [
        ['Моб. телефоны', 3000000, 3500000],
        ['Аксессуары', 1500000, 1700000],
        ['Комп. техника', 1150000, 970000],
        ['Билайн', 3000, 4879],
        ['МТС', 2770, 2312],
        ['Мегафон', 700, 321],
        ['YOTA', 90, 42],
        ['ТЕЛЕ2', 180, 423],
        ['ДСО', 3700000, 3298983],
        ['Настройки', 3800000, 583321],
        ['ВСК cтрахование', 1150000, 902321]
    ]

    data = {}
    for category in categories:
        fact = sum([x.price for x in db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category[0], payment_type)])
        data[category[0]] = {
                'fact': fact,
                'plan': category[1],
                'pred': category[2]#round(float(fact) * random() * 10, 2),
            }



        #data[category] = db_product.get_products(db, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type)


    return data


#@router.get("/get_sales", response_model=list[Product])
#async def get_users(db: Session = Depends(get_db)):
#    return get_all_users(db)


