from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database1.db")
SQLModel.metadata.create_all(engine)
