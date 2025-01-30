from ports.repositories.base import IRepository
from domain.models.user import User


class IUserRepository(IRepository[User]):
    ...
