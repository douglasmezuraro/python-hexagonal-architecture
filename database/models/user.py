from sqlalchemy import Column, DateTime, String, UUID
from database.facade import DatabaseFacade

class UserDB(DatabaseFacade.base):
    id = Column(UUID, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birthday = Column(DateTime)

    __tablename__ = 'users'
