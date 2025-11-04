from datetime import datetime

from disnake import Member
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database.models import db, User


async def register_user(d_user: Member) -> User:
    async with db.get_session() as session:
        result = await session.execute(select(User).filter_by(id=d_user.id))
        user = result.scalars().first()

        if user:
            return user

        user = User(
            id=d_user.id,
            username=d_user.name,
            global_name=d_user.global_name or d_user.display_name,
            avatar_url=str(
                d_user.display_avatar.url
            ) if d_user.display_avatar else None,
            banner_url=str(
                d_user.guild_banner.url
            ) if d_user.guild_banner else str(
                d_user.banner.url
            ) if d_user.banner else None,
            created_at=d_user.created_at,
            joined_at=d_user.joined_at,
            verified=False,
            is_booster=True if d_user.premium_since else False,
            last_seen_at=datetime.utcnow()
        )

        session.add(user)
        try:
            await session.commit()
            await session.refresh(user)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

        return user


async def get_user(user_id: int) -> User | None:
    async with db.get_session() as session:
        result = await session.execute(select(User).filter_by(id=user_id))
        return result.scalars().first()


async def get_verified(user_id: int) -> bool:
    async with db.get_session() as session:
        result = await session.execute(select(User).filter_by(id=user_id, verified=True))
        return result.scalars().first() is not None


async def set_verified(user_id: int, state: bool) -> bool:
    async with db.get_session() as session:
        result = await session.execute(select(User).filter_by(id=user_id))
        user = result.scalars().first()

        if not user:
            return False

        user.verified = state
        try:
            await session.commit()
        except SQLAlchemyError as e:
            await session.rollback()
            return False

        return True
