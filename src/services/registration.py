from disnake import Guild
from disnake import Member as DisnakeMember
from sqlmodel import Session

from src.models.user import User
from src.repositories.user import UserRepository


class RegistrationService:
    def __init__(self, session: Session):
        self.session = session
        self.users = UserRepository(session)

    async def register_guild(self, guild: Guild) -> None:
        async for member in guild.fetch_members(limit=1000):
            if self.users.get_by_id(member.id) is None:
                self.register_user(member)

    def register_user(self, member: DisnakeMember) -> User:
        return self.users.create(id=member.id, username=member.name)

    def get_user(self, id: int) -> User | None:
        return self.users.get_by_id(id)
