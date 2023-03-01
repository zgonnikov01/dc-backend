from sqlalchemy.orm.session import Session
from schemas import CheckBase
from db.models import DbCheck
from sqlalchemy.sql.sqltypes import DateTime
from db.db_product import create_product

def create_check(db: Session, request: CheckBase):
    print(request)
    #products = [Product() for product in request.products]
    new_check = DbCheck(
        number = request.number,
        date_time = request.date_time,
        total = request.total,
        points_spent = request.points_spent,
        points_earned = request.points_earned,
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
                product.date_time,
                product.price,
                product.points_spent,
                product.points_earned,
                product.sector,
                product.city,
                product.store,
                product.cashier,
                product.category
            ))
    print('-' * 100)
    print(new_check.id)
    print('-' * 100)
    
    db.commit()
    db.refresh(new_check)
    return new_check


def get_checks(db: Session, date_time, sector, city, store, cashier):
    print(date_time)
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
    return db.query(DbCheck).all()
