from pydantic import BaseModel, Field, model_validator


class TaskSchema(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int

    class Config:
        from_attributes = True

    @model_validator(mode="after")
    def check_nome_of_pomodoro_count_is_not_None(self):
        if self.name is None and self.pomodoro_count is None:
            return ValueError("name or pomodoro_count must be provided")
        return self
