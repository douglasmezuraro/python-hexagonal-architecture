from src.domain.models import User
from src.ports.repositories.user import IUserRepository


class CreateUserUseCase:
    _user_repository: IUserRepository

    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    async def execute(self, user: User) -> User:
        return await self._user_repository.create(user)
