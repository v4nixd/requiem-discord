from datetime import datetime

from disnake import Member

from database.models import db, User


def register_user(d_user: Member) -> User:
    with db.get_session() as session:
        user = session.query(User).filter_by(id=d_user.id).first()

        if user:
            return user

        user = User(
            id=d_user.id,
            username=d_user.name,
            global_name=d_user.global_name or d_user.display_name,
            avatar_url=str(
                d_user.display_avatar.url) if d_user.display_avatar else None,
            created_at=d_user.created_at,
            joined_at=datetime.utcnow(),
            verified=False
        )

        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def get_user(user_id: int) -> User | None:
    with db.get_session() as session:
        return session.query(User).filter_by(id=user_id).first()


def get_verified(user_id: int) -> bool:
    with db.get_session() as session:
        return session.query(User).filter_by(id=user_id, verified=True).count() > 0


def set_verified(user_id: int, state: bool) -> bool:
    with db.get_session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        user.verified = state
        session.commit()
        return True
