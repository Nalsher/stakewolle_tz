from typing import List

from sqlalchemy import ARRAY, INTEGER, ForeignKey

from src.database.postgresql.base.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    referals: Mapped[List[int]] = mapped_column(ARRAY(INTEGER), nullable=True)


class Referals(Base):
    __tablename__ = "referals"

    reffer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    refferred_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
