from pydantic import BaseModel, Field, field_validator


class GoogleUserData(BaseModel):
    """
    Schemas for Yandex And Google Auth.
    """
    sub: str = Field(alias="id")
    email: str
    email_verified: bool = Field(alias="verified_email")
    name: str
    access_token: str

    @field_validator("sub", mode="before")
    @classmethod
    def validate_sub(cls, v):
        return str(v)


class YandexUserData(BaseModel):
    id: str
    login: str
    name: str = Field(alias="real_name")
    email: str | None = None
    access_token: str

    @field_validator("id", mode="before")
    @classmethod
    def validate_id(cls, v):
        return str(v)


class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str
