from datetime import datetime

from fastapi import FastAPI, UploadFile, Form, Request
from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

import controller as controller
import models as models
from save_image import save_image
from seed import init_seed

app = FastAPI()

engine = create_engine("sqlite:///database1.db")
SQLModel.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081"
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
        total=controller.get_products_count(session, is_expired),
        result=controller.read_products(session, page, per_page, is_expired)
    )


@app.post("/products", response_model=models.Product | None, tags=["product"])
async def create_product(
        request: Request,
        image: UploadFile,
        name: str = Form(None),
        creation_date: datetime = Form(),
        expiration_date: datetime = Form(),
):
    session = Session(engine)

    image_url = await save_image(image, request)
    product = models.Product(
        name=name,
        creation_date=creation_date,
        expiration_date=expiration_date,
        image_url=image_url
    )

    return controller.create_product(session, product)


@app.get("/users/{id}", response_model=models.User, tags=["user"])
def read_user(id: str):
    session = Session(engine)
    return controller.read_user_by_id(session, id)


def main():
    with Session(engine) as session:
        init_seed(session)


main()
