from sqlmodel import select

from src.models.user import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> User | None:
        statement = select(User).where(User.id == id)
        return self.session.exec(statement).first()

    def create(self, id: int, username: str) -> User:
        user = User(id=id, username=username)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
