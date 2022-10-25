from datetime import datetime
from sqlmodel import Session

from controller import read_user, create_user, create_product
from models import User, Product, Role


def init_seed(session: Session):
    # TODO replace with real password
    admin_user = User(name="Noor", email="noorhaidar@gmail.com", hash_password="", role=Role.ADMIN)

    user = read_user(session, admin_user.email)

    if user is None:
        create_user(session, admin_user)
        products = [
            Product(
                name="cable",
                creation_date=datetime.now(),
                user_id=admin_user.id,
                expiration_date=datetime.now(),
                image_url="https://images.unsplash.com/photo-1572721546624-05bf65ad7679?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1373&q=80"
            ),
            Product(
                name="charger",
                creation_date=datetime.now(),
                user_id=admin_user.id,
                expiration_date=datetime.now(),
                image_url="https://images.unsplash.com/photo-1572721546624-05bf65ad7679?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1373&q=80"
            )
        ]
        for product in products:
            create_product(session, product)
    else:
        print("seed is already active")
