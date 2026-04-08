from sqlmodel import Session, SQLModel, create_engine

from src.core.config import Config

url = Config.instance().get_env_var("DATABASE_URL")
engine = create_engine(url, echo=False)


def get_session() -> Session:
    return Session(engine)


def init_db() -> None:
    print("Initializing database...")

    print("Importing models")
    import src.models  # noqa: F401
    print("Imported models successfully")

    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database initialized successfully")
