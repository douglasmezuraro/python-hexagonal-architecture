from typing import Generator

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from ioc.options import Options


class DatabaseFacade:
    base = declarative_base()
    _engine: Engine

    def __init__(self, options: Options) -> None:
        self._engine = create_engine(options.DATABASE_URL, connect_args={"check_same_thread": False})
        self.base.metadata.create_all(bind=self._engine)

    def get_db(self) -> Generator[Session]:
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        db = session_local()
        try:
            yield db
        finally:
            db.close()
