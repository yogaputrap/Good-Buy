from typing import List, Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int


class Category(BaseModel):
    id: int
    name: str


class CartItem(BaseModel):
    product_id: int
    quantity: int


class Cart(BaseModel):
    id: int
    user_id: int
    items: List[CartItem]


class User(BaseModel):
    id: int
    username: str
    password: str
    email: str


class Account(BaseModel):
    id: int
    user_id: int
    balance: float
