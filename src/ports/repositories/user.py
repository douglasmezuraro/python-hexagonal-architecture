from src.ports.repositories.base import IRepository
from src.domain.models import User


class IUserRepository(IRepository[User]):
    ...
