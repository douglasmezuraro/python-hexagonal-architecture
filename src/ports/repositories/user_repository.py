from src.ports.repositories import IRepository
from src.domain.models import User


class IUserRepository(IRepository[User]):
    ...
