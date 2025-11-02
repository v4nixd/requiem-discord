from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Database

db = Database()
Base = db.Base


class UserRole(Base):
    __tablename__ = "user_roles"

    role_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class UserReferral(Base):
    __tablename__ = "user_referrals"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True)
    referral_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    global_name: Mapped[str] = mapped_column(String, nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(String)
    banner_url: Mapped[str | None] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    joined_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    left_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    verified: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False)
    is_booster: Mapped[bool] = mapped_column(Boolean, default=False)
    premium_since: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    invited_by_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))

    last_message_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)
    last_seen_at: Mapped[datetime | None] = mapped_column(TIMESTAMP)

    roles: Mapped[list["UserRole"]] = relationship(
        backref="user", cascade="all, delete")
    referrals: Mapped[list["UserReferral"]] = relationship(
        backref="user", cascade="all, delete")


class ModerationLog(Base):
    __tablename__ = "modlogs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    moderator_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    target_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    reason: Mapped[str | None] = mapped_column(String)
