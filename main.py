from sqlmodel import SQLModel, create_engine, Session

from seed import init_seed

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    with Session(engine) as session:
        init_seed(session)
