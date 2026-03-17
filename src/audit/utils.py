from disnake import AuditLogEntry, Guild, Member, TextChannel
from disnake.abc import GuildChannel

from src.config import Config


def require_member(obj) -> Member:
    if not isinstance(obj, Member):
        raise TypeError("Expected Member")
    return obj


def require_channel(obj) -> GuildChannel:
    if not isinstance(obj, GuildChannel):
        raise TypeError("Expected Channel")
    return obj


def get_logs_channel(guild: Guild) -> TextChannel:
    config = Config().instance().config
    channel_id = int(config["bot"]["logs"]["channel_id"])

    logs_channel = guild.get_channel(channel_id)
    if not logs_channel:
        raise ValueError(f"Logs Channel not found ({channel_id})")
    elif not isinstance(logs_channel, TextChannel):
        raise ValueError(
            f"Logs Channel is not typeof TextChannel ({channel_id})")

    return logs_channel


def extract_color(entry: AuditLogEntry) -> int:
    return 0
