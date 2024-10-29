from src.database.postgresql.base.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    referal_code: Mapped[str] = mapped_column(nullable=False)
    referals: Mapped[list[int]]
