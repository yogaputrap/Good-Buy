from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .schemas import ProductCreate, CategoryCreate, CartCreate, UserCreate, AccountCreate
from .models import Product, Category, Cart, User, Account
from .services import get_products, get_product_by_id, create_product, get_categories, get_category_by_id, get_users, get_user_by_id
from .auth import get_current_user


app = FastAPI(
    title="Good Buy - API Documentation",
    version="1.0.0",
)


@app.get("/products", response_model=List[Product])
def read_products():
    return get_products()


@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=Product)
def create_new_product(product: ProductCreate):
    return create_product(product.dict())


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate):
    products = get_products()
    for idx, p in enumerate(products):
        if p.id == product_id:
            updated_product = Product(id=product_id, **product.dict())
            products[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    products = get_products()
    for p in products:
        if p.id == product_id:
            products.remove(p)
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/categories", response_model=List[Category])
def read_categories():
    return get_categories()


@app.get("/categories/{category_id}", response_model=Category)
def read_category(category_id: int):
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.post("/categories", response_model=Category)
def create_new_category(category: CategoryCreate):
    categories = get_categories()
    new_id = max([cat.id for cat in categories]) + 1 if categories else 1
    new_category = Category(id=new_id, **category.dict())
    categories.append(new_category.dict())
    return new_category

@app.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryCreate):
    categories = get_categories()
    for idx, c in enumerate(categories):
        if c.id == category_id:
            updated_category = Category(id=category_id, **category.dict())
            categories[idx] = updated_category
            return updated_category
    raise HTTPException(status_code=404, detail="Category not found")


@app.delete("/categories/{category_id}", response_model=dict)
def delete_category(category_id: int):
    categories = get_categories()
    for c in categories:
        if c.id == category_id:
            categories.remove(c)
            return {"detail": "Category deleted"}
    raise HTTPException(status_code=404, detail="Category not found")


@app.get("/users", response_model=List[User])
def read_users():
    return get_users()


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=User)
def create_new_user(user: UserCreate):
    users = get_users()
    new_id = max([user.id for user in users]) + 1 if users else 1
    new_user = User(id=new_id, **user.dict())
    users.append(new_user.dict())
    return new_user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    users = get_users()
    for idx, u in enumerate(users):
        if u.id == user_id:
            updated_user = User(id=user_id, **user.dict())
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int):
    users = get_users()
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/carts", response_model=List[Cart])
def read_carts():
    return load_data("carts.json")


@app.post("/carts", response_model=Cart)
def create_cart(cart: CartCreate):
    return Cart(id=len(load_data("carts.json")) + 1, **cart.dict())


@app.put("/carts/{cart_id}", response_model=Cart)
def update_cart(cart_id: int, cart: CartCreate):
    carts = load_data("carts.json")
    for idx, c in enumerate(carts):
        if c["id"] == cart_id:
            updated_cart = {**c, **cart.dict()}
            carts[idx] = updated_cart
            return updated_cart
    raise HTTPException(status_code=404, detail="Cart not found")


@app.delete("/carts/{cart_id}", response_model=dict)
def delete_cart(cart_id: int):
    carts = load_data("carts.json")
    for c in carts:
        if c["id"] == cart_id:
            carts.remove(c)
            return {"detail": "Cart deleted"}
    raise HTTPException(status_code=404, detail="Cart not found")


@app.get("/account/{user_id}", response_model=Account)
def read_account(user_id: int):
    account = get_account_by_user_id(user_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@app.put("/account/{user_id}", response_model=Account)
def update_account(user_id: int, account_data: AccountCreate):
    accounts = get_accounts()
    for idx, acc in enumerate(accounts):
        if acc.user_id == user_id:
            updated_account = Account(id=acc.id, user_id=user_id, balance=account_data.balance)
            accounts[idx] = updated_account
            return updated_account
    raise HTTPException(status_code=404, detail="Account not found")


@app.delete("/account/{user_id}", response_model=dict)
def delete_account(user_id: int):
    accounts = get_accounts()
    for acc in accounts:
        if acc.user_id == user_id:
            accounts.remove(acc)
            return {"detail": "Account deleted"}
    raise HTTPException(status_code=404, detail="Account not found")