from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: str
    discordId: str
    username: str | None
    globalName: str | None
    avatar: str | None
    banner: str | None
    createdAt: datetime
    updatedAt: datetime
