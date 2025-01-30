from typing import Protocol
from uuid import UUID

class IRepository[TModel](Protocol):

    async def create(self, model: TModel) -> TModel:
        ...

    async def retrieve(self, id: UUID) -> TModel:
        ...

    async def update(self, model: TModel) -> TModel:
        ...

    async def delete(self, id: UUID) -> None:
        ...
