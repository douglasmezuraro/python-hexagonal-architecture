from uuid import UUID, uuid4

from src.domain.models import User
from src.ports.repositories import IUserRepository


class UserRepository(IUserRepository):

    async def create(self, model: User) -> UUID:
        return uuid4()

    async def retrieve(self, id: UUID) -> User:
        raise NotImplementedError()

    async def update(self, model: User) -> None:
        raise NotImplementedError()

    async def delete(self, id: UUID) -> None:
        raise NotImplementedError()
