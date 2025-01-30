from uuid import UUID

from fastapi import APIRouter, Depends
from injector import Injector

from src.di import AppModule
from src.domain.models import User
from src.domain.usecases.user import CreateUserUseCase

router = APIRouter(prefix="/users", tags=["Users"])
injector = Injector([AppModule])  # Criando o container de injeção

@router.post("/", response_model=UUID)
async def create(user: User, usecase: CreateUserUseCase = Depends(lambda: injector.get(CreateUserUseCase))) -> UUID:
    return await usecase.execute(user)
