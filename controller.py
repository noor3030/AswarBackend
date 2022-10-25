from sqlmodel import Session, select

from models import User, Product


def read_user(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)


def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
