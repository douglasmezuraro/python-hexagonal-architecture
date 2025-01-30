from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
base = declarative_base()

class DatabaseFacade:

    def __init__(self) -> None:
        """Cria as tabelas no banco, caso ainda não existam"""
        base.metadata.create_all(bind=engine)

    def get_db(self) -> Generator[Session]:
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = session_local()
        try:
            yield db
        finally:
            db.close()
