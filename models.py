from datetime import datetime
from enum import Enum

from sqlmodel import Field, SQLModel


class Role(Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class Product(SQLModel, table=True):
    name: str
    id: int = Field(default=None, primary_key=True)
    creation_date: datetime
    expiration_date: datetime
    image_url: str
    user_id: str


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    hash_password: str
    role: Role
