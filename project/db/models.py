from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime, Date
from db.base import Base
from sqlalchemy import Column


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    full_name = Column(String, index=True)
    password = Column(String)
    disabled = Column(Boolean)
    access_level = Column(String)
    sector = Column(String, index=True)
    city = Column(String, index=True)
    store = Column(String, index=True)
    cashier = Column(String, index=True)


class DbCheck(Base):
    __tablename__ = 'checks'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, index=True)
    date_time = Column(DateTime, index=True)
    total = Column(Integer)
    #points_spent = Column(Integer)
    #points_earned = Column(Integer)
    sector = Column(String, index=True)
    city = Column(String, index=True)
    store = Column(String, index=True)
    cashier = Column(String, index=True)
    payment_type = Column(String, index=True)


class DbProduct(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    check_id = Column(Integer, ForeignKey('checks.id', ondelete='CASCADE'), nullable=False)

    check = relationship('DbCheck', backref='products')

    name = Column(String, index=True)
    date_time = Column(DateTime, index=True)
    price = Column(Integer)
    #quantity = Column(Integer)
    #points_spent = Column(Integer)
    #points_earned = Column(Integer)
    sector = Column(String, index=True)
    city = Column(String, index=True)
    store = Column(String, index=True)
    cashier = Column(String, index=True)
    category = Column(String, index=True)
    payment_type = Column(String, index=True)



class DbProductByDate(Base):
    __tablename__ = 'products_by_date'
    #id = Column(Integer, primary_key=True, index=True)
    #check_id = Column(Integer, ForeignKey('checks.id', ondelete='CASCADE'), nullable=False)
    #check = relationship('DbCheck', backref='products')
    #name = Column(String, index=True)
    date = Column(Date, primary_key=True, index=True)
    total = Column(Integer)
    #points_spent = Column(Integer)
    #points_earned = Column(Integer)
    sector = Column(String, index=True)
    city = Column(String, index=True)
    store = Column(String, index=True)
    cashier = Column(String, index=True)
    category = Column(String, index=True)
    payment_type = Column(String, index=True)
