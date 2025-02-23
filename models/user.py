from pip._vendor.rich.table import Column
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declarative_base,
    DeclarativeBase,
    declared_attr,
)
from database import Base


class UserProfile(Base):
    __tablename__ = "UserProfile"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    access_token: Mapped[str] = mapped_column(nullable=False)
