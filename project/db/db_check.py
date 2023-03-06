from sqlalchemy.orm.session import Session
from schemas import CheckBase
from db.models import DbCheck
from sqlalchemy.sql.sqltypes import DateTime
from db.db_product import create_product
from datetime import datetime
from .models import DbProductByDate, DbProduct

def create_check(db: Session, request: CheckBase):
    #products = [Product() for product in request.products]
    new_check = DbCheck(
        number = request.number,
        date_time = request.date_time,
        total = request.total,
        #points_spent = request.points_spent,
        #points_earned = request.points_earned,
        sector = request.sector,
        city = request.city,
        store = request.store,
        cashier = request.cashier,
        products = []
    )

    db.add(new_check)
    db.commit()
    db.refresh(new_check)
    for product in request.products:
        for i in range(product.quantity):
            new_check.products.append(
                create_product(
                db,
                new_check.id,
                product.name,
                request.date_time,
                product.price,
                #product.points_spent,
                #product.points_earned,
                request.sector,
                request.city,
                request.store,
                request.cashier,
                product.category,
                request.payment_type
            ))
        date = request.date_time.date()
        date_product = db.query(DbProductByDate)\
            .filter(DbProductByDate.date == date)\
            .filter(DbProduct.category == product.category)
        if date_product.count():
            date_product.first().total += product.price * product.quantity
        else:
            new_date_product = DbProductByDate(
                date = date,
                total = product.price * product.quantity,
                #points_spent = points_spent,
                #points_earned = points_earned,
                sector = request.sector,
                city = request.city,
                store = request.store,
                cashier = request.cashier,
                category = product.category,
                payment_type = request.payment_type
            )
    db.commit()

    db.commit()
    db.refresh(new_check)
    return new_check


def get_checks(db: Session, date_time_start, date_time_end, sector, city, store, cashier, payment_type):
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
    return db.query(DbCheck).all()
    return db.query(DbCheck)\
        .filter(
            and_(
                or_(DbCheck.date_time >= date_time_start, date_time_start == ''), 
                or_(DbCheck.date_time <= date_time_end, date_time_end == '')
            )
        )\
        .filter(or_(DbCheck.sector == sector, sector == ''))\
        .filter(or_(DbCheck.city== city, city == ''))\
        .filter(or_(DbCheck.store == store, store == ''))\
        .filter(or_(DbCheck.cashier == cashier, cashier == ''))\
        .filter(or_(DbCheck.payment_type == payment_type, payment_type == ''))\
        .all()
        #filter(DbCheck.sector = sector).
        #filter(DbCheck.city = city).
        #filter(DbCheck.store = store).
        #filter(DbCheck.cashier = cashier).
