from injector import Module, provider, singleton

from database.facade import DatabaseFacade
from database.repositories.user import UserRepository
from domain.usecases.user.create import CreateUserUseCase

class AppModule(Module):

    @singleton
    @provider
    def provide_database_facade(self) -> DatabaseFacade:
        return DatabaseFacade()

    @singleton
    @provider
    def provide_user_repository(self, database_facade: DatabaseFacade) -> UserRepository:
        return UserRepository(database_facade)

    @singleton
    @provider
    def provide_create_user_usecase(self, user_repository: UserRepository) -> CreateUserUseCase:
        return CreateUserUseCase(user_repository)
