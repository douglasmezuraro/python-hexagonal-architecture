from injector import Module, provider, singleton

from database.repositories.user import UserRepository
from domain.usecases.user.create import CreateUserUseCase

class UseCaseModule(Module):

    @singleton
    @provider
    def provide_create_user_usecase(self, user_repository: UserRepository) -> CreateUserUseCase:
        return CreateUserUseCase(user_repository)
