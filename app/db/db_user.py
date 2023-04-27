from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from hash import Hash

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        email = request.email,
        full_name = request.full_name,
        phone_number = request.phone_number,
        password = Hash.bcrypt(request.password),
        #disabled = False,
        access_level = request.access_level,
        sector = request.sector,
        #city = request.city,
        store = request.store,
        #cashier = request.cashier
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    #return list[db.query(DbUser).all()[-17]]
    return db.query(DbUser).all()

def get_user(db: Session, email: str):
    return db.query(DbUser).filter(DbUser.email == email).first()

