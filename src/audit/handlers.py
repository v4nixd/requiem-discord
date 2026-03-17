from disnake import (
    AuditLogAction,
    AuditLogEntry,
    TextChannel
)

from src.audit.common import build_diff_embed_base, build_embed, fetch_action_name
from src.audit.constants import (
    GUILD_UPDATE_FIELDS_RU,
    MEMBER_UPDATE_FIELDS_RU,
    CHANNEL_FIELDS_RU
)
from src.audit.registry import AuditHandler
from src.utils import Utils


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
        entry, AuditLogAction.guild_update, GUILD_UPDATE_FIELDS_RU
    )

    moderator = Utils.require_member(entry.user)

    content = (
        f"\n> **Модератор**: {moderator.mention} ||`{moderator.id}`||"
        # f"\n> **Причина**: `{entry.reason}`"
    )

    embed = build_embed(entry, action_name, embed_base, content)

    await logs_channel.send(embed=embed)


@AuditHandler.register(AuditLogAction.member_update)
async def handle_member_update(entry: AuditLogEntry, logs_channel: TextChannel):

    action_name, embed_base = build_diff_embed_base(
        entry, AuditLogAction.member_update, MEMBER_UPDATE_FIELDS_RU
    )

    target = Utils.require_member(entry.target)
    moderator = Utils.require_member(entry.user)

    content = (
        f"\n> **Цель**: {target.mention} ||`{target.id}`||"
        f"\n> **Модератор**: {moderator.mention} ||`{moderator.id}`||"
        f"\n> **Причина**: `{entry.reason}`"
    )

    embed = build_embed(entry, action_name, embed_base, content)

    await logs_channel.send(embed=embed)


@AuditHandler.register(AuditLogAction.channel_create, AuditLogAction.channel_delete, AuditLogAction.channel_update)
async def handle_channel_logs(entry: AuditLogEntry, logs_channel: TextChannel):

    # action_name, embed_base = build_diff_embed_base(
    #     entry, entry.action, CHANNEL_FIELDS_RU
    # )
    action_name = fetch_action_name(entry)

    print(entry.before)
    channel = Utils.require_channel(entry.target)
    moderator = Utils.require_member(entry.user)

    content = (
        f"\n> **Канал**: {channel.mention} ||`{channel.id}`||"
        f"\n> **Модератор**: {moderator.mention} ||`{moderator.id}`||"
    )

    embed = build_embed(entry, action_name, "", content)

    await logs_channel.send(embed=embed)

# @AuditHandler.register(AuditLogAction.message_delete)
# async def handle_message_delete(entry: AuditLogEntry, logs_channel: TextChannel):
#     action_name = fetch_action_name(entry)
#     message = entry.before
