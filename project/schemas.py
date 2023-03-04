from typing import List
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    full_name: str
    password : str
    disabled: bool
    access_level: str
    sector: str
    city: str
    store: str
    cashier: str

    class Config():
        orm_mode = True


class UserDisplay(BaseModel):
    email: str
    full_name: str
    disabled: bool
    access_level: str
    sector: str
    city: str
    store: str
    cashier: str

    class Config():
        orm_mode = True


class ProductBase(BaseModel):
    #check_id: int
    name: str
    price: int
    quantity: int
    #date_time: datetime
    #points_spent: int
    #points_earned: int
    #sector: str
    #city: str
    #store: str
    #cashier: str
    category: str
    #payment_type: str

    class Config():
        orm_mode = True


class ProductRequest(BaseModel):
    name: str
    price: int
    date_time: datetime
    #points_spent: int
    #points_earned: int
    sector: str
    city: str
    store: str
    cashier: str
    category: str


#class ProductRequest(BaseModel):
#    date_time: datetime
#    sector: str
#    city: str
#    store: str
#    cashier: str


class CheckBase(BaseModel):
    number: str
    date_time: datetime
    total: int
    #points_spent: int
    #points_earned: int
    sector: str
    city: str
    store: str
    cashier: str
    payment_type: str
    products: list[ProductBase]

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


#class User(BaseModel):
#    username: str
#    email: str | None = None
#    full_name: str | None = None
#    disabled: bool | None = None
#
#
#class UserInDB(User):
#    hashed_password: str

