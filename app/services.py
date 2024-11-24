import json
from typing import List, Optional
from .models import Product, Category, Cart, User, Account


def load_data(filename: str):
    with open(f"app/data/{filename}", "r") as file:
        return json.load(file)


def get_products() -> List[Product]:
    return [Product(**item) for item in load_data("products.json")]


def get_product_by_id(product_id: int) -> Optional[Product]:
    products = get_products()
    return next((product for product in products if product.id == product_id), None)


def create_product(product_data) -> Product:
    products = get_products()
    new_id = max([product.id for product in products]) + 1 if products else 1
    product = Product(id=new_id, **product_data)
    products.append(product.dict())
    return product


def get_categories() -> List[Category]:
    return [Category(**item) for item in load_data("categories.json")]


def get_category_by_id(category_id: int) -> Optional[Category]:
    categories = get_categories()
    return next((category for category in categories if category.id == category_id), None)


def get_users() -> List[User]:
    return [User(**item) for item in load_data("users.json")]


def get_user_by_id(user_id: int) -> Optional[User]:
    users = get_users()
    return next((user for user in users if user.id == user_id), None)


def get_accounts() -> List[Account]:
    return [Account(**item) for item in load_data("accounts.json")]


def get_account_by_user_id(user_id: int) -> Optional[Account]:
    accounts = get_accounts()
    return next((account for account in accounts if account.user_id == user_id), None)
