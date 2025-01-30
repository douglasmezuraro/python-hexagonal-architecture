from datetime import datetime

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    birthday: datetime
