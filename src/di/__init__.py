from injector import Module, provider, singleton

from src.database.repositories import UserRepository
from src.domain.usecases.user.create import CreateUserUseCase

class AppModule(Module):

    @singleton
    @provider
    def provide_user_repository(self) -> UserRepository:
        return UserRepository()

    @singleton
    @provider
    def provide_create_user_usecase(self, user_repository: UserRepository) -> CreateUserUseCase:
        return CreateUserUseCase(user_repository)
