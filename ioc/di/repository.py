from injector import Module, provider, singleton

from database.facade import DatabaseFacade
from database.repositories.user import UserRepository

class RepositoryModule(Module):

    @singleton
    @provider
    def provide_user_repository(self, database_facade: DatabaseFacade) -> UserRepository:
        return UserRepository(database_facade)
