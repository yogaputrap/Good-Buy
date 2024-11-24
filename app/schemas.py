from pydantic import BaseModel
from typing import List, Optional


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class CategoryCreate(BaseModel):
    name: str


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartCreate(BaseModel):
    user_id: int
    items: List[CartItemCreate]


class UserCreate(BaseModel):
    username: str
    password: str
    email: str


class AccountCreate(BaseModel):
    user_id: int
    balance: float
