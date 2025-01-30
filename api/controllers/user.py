from fastapi import APIRouter, Depends

from api.requests.user.create import CreateUserRequest
from ioc.di import injector
from domain.models.user import User
from domain.usecases.user.create import CreateUserUseCase

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
async def create(request: CreateUserRequest, usecase: CreateUserUseCase = Depends(lambda: injector.get(CreateUserUseCase))) -> User:
    return await usecase.execute(request.model_validate(request, from_attributes=True))
