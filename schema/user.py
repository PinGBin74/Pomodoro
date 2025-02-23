from social_core.tests.models import BaseModel


class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str
