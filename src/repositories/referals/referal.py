from sqlalchemy import select
from src.database.postgresql.base.base import async_session, engine
from src.database.postgresql.tables.tables import Referals as _Referals
from src.repositories.referals.base import AbstractReferalsRepository


class ReferalRepository(AbstractReferalsRepository):
    session = async_session
    engine = engine

    async def create_referal(self, referr_id: int, reffered_id: int) -> None:
        async with self.session() as session:
            Referal = _Referals(reffer_id=referr_id, refferred_id=reffered_id)
            session.add(Referal)
            await session.commit()

    async def get_referals(self, referal_id: int) -> list | None:
        async with self.session() as session:
            Referal = select(_Referals).where(
                _Referals.reffer_id == referal_id
            )
            execute = await session.execute(Referal)
            try:
                Referals = execute.all()
                list_of_referals = []
                for row in Referals:
                    list_of_referals.append(row[0].refferred_id)
                return list_of_referals
            finally:
                return None
