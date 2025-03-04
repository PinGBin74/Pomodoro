from pydantic import BaseModel
from typing_extensions import Optional


class UserCreateSchema(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    google_access_token: Optional[str] = None
    yandex_access_token: Optional[str] = None
