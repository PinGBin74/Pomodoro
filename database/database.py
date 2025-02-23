from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings
from typing import Optional

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declarative_base,
    DeclarativeBase,
    declared_attr,
)

settings = Settings()
engine = create_engine(settings.db_url)


Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session


class Base(DeclarativeBase):
    id: any
    __name__: str

    __allow_unmapped__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
