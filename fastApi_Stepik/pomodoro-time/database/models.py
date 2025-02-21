from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declarative_base,
    DeclarativeBase,
    declared_attr,
)
from typing import Optional


class Base(DeclarativeBase):
    id: any
    __name__: str

    __allow_unmapped__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(nullable=False)


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[Optional[str]]
    name: Mapped[str]
