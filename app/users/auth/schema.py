from pydantic import BaseModel, Field


class GoogleUserData(BaseModel):
    sub: str = Field(alias="id")
    email: str
    email_verified: bool = Field(alias="verified_email")
    name: str
    access_token: str


class YandexUserData(BaseModel):
    id: str
    login: str
    name: str = Field(alias="real_name")
    email: str | None = None
    access_token: str


class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str
