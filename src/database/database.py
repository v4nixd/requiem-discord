from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, Session


class Database:
    def __init__(self, url: str = "sqlite:///database.db", echo: bool = False) -> None:
        self.engine = create_engine(url, echo=echo, future=True)
        self.Base = declarative_base()

        self._session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )
        self.Session = scoped_session(self._session_factory)

    def create_all(self) -> None:
        self.Base.metadata.create_all(self.engine)

    def drop_all(self) -> None:
        self.Base.metadata.drop_all(self.engine)

    def get_session(self) -> Session:
        return self.Session()

    def shutdown(self) -> None:
        self.Session.remove()
        self.engine.dispose()
