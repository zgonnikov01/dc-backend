from typing import List
from pydantic import BaseModel

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


class CheckBase(BaseModel):
    number: str
    date_time: str
    total: int
    points_spent: int
    points_earned: int
    sector: str
    city: str
    store: str
    cashier: str

    class Config():
        orm_mode = True



class ProductBase(BaseModel):
    check_id: int
    name: str
    price: int
    quantity: int
    date_time: str
    points_spent: int
    points_earned: int
    sector: str
    city: str
    store: str
    cashier: str

    class Config():
        orm_mode = True


