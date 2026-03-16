from disnake import AuditLogAction, AuditLogEntry, TextChannel, Embed, Member

from src.audit.registry import AuditHandler
from src.audit.common import build_diff_embed_base, build_embed
from src.audit.utils import require_member
from src.audit.constants import GUILD_UPDATE_FIELDS_RU, MEMBER_UPDATE_FIELDS_RU


@AuditHandler.register(AuditLogAction.guild_update)
async def handle_guild_update(entry: AuditLogEntry, logs_channel: TextChannel):
    """
    Triggers:
    - Changing the guild vanity URL
    - Changing the guild invite splash
    - Changing the guild AFK channel or timeout
    - Changing the guild voice server region
    - Changing the guild icon, banner, or discovery splash
    - Changing the guild moderation settings
    - Changing things related to the guild widget
    """

    action_name, embed_base = build_diff_embed_base(
        entry, AuditLogAction.guild_update, GUILD_UPDATE_FIELDS_RU)

    moderator = require_member(entry.user)

    content = f"\n> **Модератор**: {moderator.mention} ||`{moderator.id}`||" \
        f"\n> **Причина**: `{entry.reason}`"

    embed = build_embed(entry, action_name, embed_base, content)

    await logs_channel.send(embed=embed)


@AuditHandler.register(AuditLogAction.member_update)
async def handle_member_update(entry: AuditLogEntry, logs_channel: TextChannel):

    action_name, embed_base = build_diff_embed_base(
        entry, AuditLogAction.member_update, MEMBER_UPDATE_FIELDS_RU)

    target = require_member(entry.target)
    moderator = require_member(entry.user)

    content = f"\n> **Цель**: {target.mention} ||`{target.id}`||" \
        f"\n> **Модератор**: {moderator.mention} ||`{moderator.id}`||" \
        f"\n> **Причина**: `{entry.reason}`"

    embed = build_embed(entry, action_name, embed_base, content)

    await logs_channel.send(embed=embed)
