from fastapi import APIRouter, Depends
from injector import Injector

from src.api.requests.user.create import CreateUserRequest
from src.di import AppModule
from src.domain.models import User
from src.domain.usecases.user import CreateUserUseCase

router = APIRouter(prefix="/users", tags=["Users"])
injector = Injector([AppModule])

@router.post("/", response_model=User)
async def create(request: CreateUserRequest, usecase: CreateUserUseCase = Depends(lambda: injector.get(CreateUserUseCase))) -> User:
    return await usecase.execute(request.model_validate(request, from_attributes=True))
