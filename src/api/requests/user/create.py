import uuid
from datetime import datetime

from pydantic import BaseModel

from src.domain.models.user import User


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    birthday: datetime

    def to_entity(self) -> User:
        return User( 
            id=uuid.uuid4(),
            first_name=self.first_name,
            last_name=self.last_name,
            birthday=self.birthday)