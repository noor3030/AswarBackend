from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session
from starlette.middleware.cors import CORSMiddleware
import controller as controller
import models as models
from seed import init_seed
from typing import Union

from fastapi import FastAPI

app = FastAPI()

engine = create_engine("sqlite:///database1.db")
SQLModel.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pagination(BaseModel):
    total: int
    result: list[models.Product]


@app.get("/products", response_model=Pagination, tags=["product"])
def read_products(page: int, per_page: int = 25, is_expired: bool = True):
    session = Session(engine)
    return Pagination(
        total=controller.get_products_count(session),
        result=controller.read_products(session, page, per_page,is_expired)
    )


@app.get("/users/{id}", response_model=models.User, tags=["user"])
def read_user(id: str):
    session = Session(engine)
    return controller.read_user_by_id(session, id)


def main():
    with Session(engine) as session:
        init_seed(session)


main()
