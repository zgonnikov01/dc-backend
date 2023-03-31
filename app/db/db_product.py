from sqlalchemy.orm.session import Session
from schemas import ProductBase
from db.models import DbProduct
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import func, or_, and_

def create_product(db: Session, check_id, name, date_time, price, sector, city, store, cashier, category, payment_type):

    new_product = DbProduct(
        check_id = check_id,
        name = name,
        date_time = date_time,
        price = price,
        #points_spent = points_spent,
        #points_earned = points_earned,
        sector = sector,
        city = city,
        store = store,
        cashier = cashier,
        category = category,
        payment_type = payment_type
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_products(db: Session, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type):
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
    return db.query(DbProduct)\
        .filter(
            and_(
                or_(DbProduct.date_time >= date_time_start, date_time_start == ''), 
                or_(DbProduct.date_time <= date_time_end, date_time_end == '')
            )
        )\
        .filter(or_(DbProduct.sector == sector, sector == ''))\
        .filter(or_(DbProduct.city== city, city == ''))\
        .filter(or_(DbProduct.store == store, store == ''))\
        .filter(or_(DbProduct.cashier == cashier, cashier == ''))\
        .filter(or_(DbProduct.category == category, category == ''))\
        .filter(or_(DbProduct.payment_type == payment_type, payment_type == ''))\
        .all()
        #filter(DbCheck.sector = sector).
        #filter(DbCheck.city = city).
        #filter(DbCheck.store = store).
        #filter(DbCheck.cashier = cashier).

def get_products_graph(db: Session, date_time_start, date_time_end, sector, city, store, cashier, category, payment_type):
    data = db.query(DbProduct)\
        .filter(
            and_(
                or_(DbProduct.date_time >= date_time_start, date_time_start == ''), 
                or_(DbProduct.date_time <= date_time_end, date_time_end == '')
            )
        )\
        .filter(or_(DbProduct.sector == sector, sector == ''))\
        .filter(or_(DbProduct.city== city, city == ''))\
        .filter(or_(DbProduct.store == store, store == ''))\
        .filter(or_(DbProduct.cashier == cashier, cashier == ''))\
        .filter(or_(DbProduct.category == category, category == ''))\
        .filter(or_(DbProduct.payment_type == payment_type, payment_type == ''))\
        .all()
    print(data[1])
