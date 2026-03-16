from disnake import AuditLogEntry, TextChannel
from disnake.ext import commands

from src.audit.registry import AuditHandler
from src.audit import handlers  # DO NOT REMOVE, IMPORTANT FOR LOADING HANDLERS
from src.audit.utils import get_logs_channel


class OnAuditLogEntryCreateEvent(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot: commands.InteractionBot = bot
        print("OnAuditLogEntryCreateEvent cog initialized")

    @commands.Cog.listener()
    async def on_audit_log_entry_create(self, entry: AuditLogEntry) -> None:
        logs_channel: TextChannel = get_logs_channel(entry.guild)

        handler = AuditHandler.handlers.get(entry.action)

        if handler:
            await handler(entry, logs_channel)
        else:
            print("Unknown/Unhandled action:", entry.action.value)


def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(OnAuditLogEntryCreateEvent(bot))
