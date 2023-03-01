from sqlalchemy.orm.session import Session
from schemas import ProductBase
from db.models import DbProduct
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import func, or_

def create_product(db: Session, check_id, name, date_time, price, points_spent, 
        points_earned, sector, city, store, cashier, category):

    new_product = DbProduct(
        #name = request.name,
        #date_time = request.date_time,
        #total = request.total,
        #points_spent = request.points_spent,
        #points_earned = request.points_earned,
        #sector = request.sector,
        #city = request.city,
        #store = request.store,
        #cashier = equest.cashier,
        check_id = check_id,
        name = name,
        date_time = date_time,
        price = price,
        points_spent = points_spent,
        points_earned = points_earned,
        sector = sector,
        city = city,
        store = store,
        cashier = cashier,
        category = category
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_products(db: Session, date_time_start, date_time_end, sector, city, store, cashier, category):
    print(date_time_start)
    print(date_time_end)
    print(sector)
    print(city)
    print(store)
    print(cashier)
    #if not date_time:
    #    date_time = True
    #if not sector:
    #    sector = True
    #if not city:
    #    city = True
    #if not store:
    #    store = True
    #if not cashier:
    #    cashier = True
    #return db.query(DbCheck).filter(DbCheck.date_time == date_time).all()
    #print(db.query(DbProduct).all())
                               #filter(func.date(DbProduct.date_time) >= date_time_start).\
                               #filter(func.date(DbProduct.date_time) <= date_time_end).\
    return db.query(DbProduct).\
                               filter(DbProduct.date_time >= date_time_start).\
                               filter(DbProduct.date_time <= date_time_end).\
                               filter(or_(DbProduct.category == category, True)).\
                               all()
                               #filter(DbCheck.sector = sector).
                               #filter(DbCheck.city = city).
                               #filter(DbCheck.store = store).
                               #filter(DbCheck.cashier = cashier).
