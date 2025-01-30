from uuid import UUID, uuid4

from src.domain.models import User
from src.ports.repositories.user import IUserRepository
from src.database.facade import DatabaseFacade
from src.database.models.user import UserDB


class UserRepository(IUserRepository):
    _database_facade: DatabaseFacade

    def __init__(self, database_facade: DatabaseFacade) -> None:
        self._database_facade = database_facade

    async def create(self, model: User) -> User:
        user = UserDB()
        user.id = uuid4()
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.birthday = model.birthday

        db = next(self._database_facade.get_db())
        db.add(user)
        db.commit()
        db.refresh(user)

        return User.model_validate(user, from_attributes=True)

    async def retrieve(self, id: UUID) -> User:
        raise NotImplementedError()

    async def update(self, model: User) -> User:
        raise NotImplementedError()

    async def delete(self, id: UUID) -> None:
        raise NotImplementedError()
