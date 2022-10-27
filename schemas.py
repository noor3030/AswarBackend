from pydantic import BaseModel

from enums import Role


class User(BaseModel):
    id: int
    name: str
    email: str
    role: Role
