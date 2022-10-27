from datetime import datetime

from sqlmodel import Session, select

from models import User, Product


def read_user_by_id(session: Session, id: str) -> User | None:
    statement = select(User).where(User.id == id)
    return session.exec(statement).first()


def read_user_by_email(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)


def create_product(session: Session, product: Product) -> Product | None:
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def read_products(session: Session, page: int, per_page: int = 25, is_expired: bool = True):
    offset = (page - 1) * per_page

    if is_expired:
        statement = select(Product).filter(Product.expiration_date < datetime.now())
    else:
        statement = select(Product).filter(Product.expiration_date > datetime.now())

    return session.exec(statement.offset(offset).limit(per_page)).all()


def get_products_count(session: Session, is_expired: bool = True):
    statement = session.query(Product)
    if is_expired:
        count = statement.filter(Product.expiration_date < datetime.now()).count()
    else:
        count = statement.filter(Product.expiration_date > datetime.now()).count()

    return count
