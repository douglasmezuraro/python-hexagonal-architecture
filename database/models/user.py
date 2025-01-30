from sqlalchemy import Column, DateTime, String, UUID
from database.facade import base, engine

class UserDB(base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birthday = Column(DateTime)


base.metadata.create_all(bind=engine)
