from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlite3_db_name: str = "identifier.sqlite"
