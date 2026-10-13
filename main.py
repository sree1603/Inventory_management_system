from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user





# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}




# from fastapi import FastAPI, Depends
# from models import Product
# from database import session,engine
# import database_models
# from sqlalchemy.orm import Session

# app = FastAPI()

# database_models.Base.metadata.create_all(bind = engine)

# @app.get("/")
# def greet():
#     return "hello welcome!"

# products = [
#     Product(id = 1, name = "phone", description = "budget phone", price = 99, quantity = 10),
#     Product(id = 2, name = "laptop", description = "gaming", price = 999, quantity = 6),
#     Product(id = 3, name = "Pen", description = "a blue ink pen", price = 1.9, quantity = 100),
#     Product(id = 4, name = "Table", description = "A wooden Table", price = 99.99, quantity = 20)
# ]

# def get_db():
#     db = session()
#     try:
#         yield db
#     finally:
#         db.close()

# def init_db():
#     db = session()
#     count = db.query(database_models.Product).count
#     if count == 0 :
#         for product in products:
#             db.add(database_models.Product(**product.model_dump()))
#             db.commit()

# init_db()

# @app.get("/products")
# def get_all_produts(db : Session = Depends(get_db)):

#     db_products = db.query(database_models.Product).all()
#     return db_products

#     # db connection
#     # db = session()
#     # # query
#     # db.query()
#     return products

# @app.get("/product/{id}")
# def get_product_by_id(id : int):
#     for product in products:
#         if product.id == id:
#             return product
#     return "product not found"

# @app.post("/product")
# def add_product(product: Product):
#     products.append(product)
#     return product

# @app.put("/product")
# def update_product(id : int, product : Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return "product aded successfully"
#     return " product not found"

# @app.delete("/product")
# def delete_product(id : int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             del products[i]
#             return "product deleted"
#     return "product not found"
