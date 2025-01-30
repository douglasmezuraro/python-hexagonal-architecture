from fastapi import APIRouter, Depends
from injector import Injector

from api.requests.user.create import CreateUserRequest
from di import AppModule
from domain.models import User
from domain.usecases.user import CreateUserUseCase

router = APIRouter(prefix="/users", tags=["Users"])
injector = Injector([AppModule])

@router.post("/", response_model=User)
async def create(request: CreateUserRequest, usecase: CreateUserUseCase = Depends(lambda: injector.get(CreateUserUseCase))) -> User:
    return await usecase.execute(request.model_validate(request, from_attributes=True))
