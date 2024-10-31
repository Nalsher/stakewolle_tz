from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.config.config import url


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


engine = create_async_engine(url=url, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
