from datetime import datetime

from sqlmodel import SQLModel, Field, Column, DateTime
from enums import Role


class Product(SQLModel, table=True):
    name: str
    id: int = Field(default=None, primary_key=True)
    creation_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False
        )
    )
    expiration_date: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False
        )
    )
    image_url: str
    user_id: str


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    hash_password: str
    role: Role
