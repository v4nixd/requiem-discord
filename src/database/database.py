from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, Session


class Database:
    def __init__(self, url: str = "sqlite+aiosqlite:///database.db", echo: bool = False) -> None:
        self.engine = create_async_engine(url, echo=echo, future=True)
        self.Base = declarative_base()
        self._session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def create_all(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)

    async def drop_all(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(self.Base.metadata.drop_all)

    async def shutdown(self) -> None:
        await self.engine.dispose()

    def get_session(self) -> AsyncSession:
        return self._session_factory()
