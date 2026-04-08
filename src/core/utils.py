from disnake import Activity, ActivityType, Guild, Member, Status
from disnake.abc import GuildChannel
from disnake.ext import commands

from src.core.config import Config


class Utils:
    @staticmethod
    def load_cogs(bot: commands.InteractionBot) -> None:
        print("Loading cogs...")
        bot.load_extensions("src/cogs/events")
        bot.load_extensions("src/cogs/commands")
        print("Cogs loaded successfully")

    @staticmethod
    async def update_presence(bot: commands.InteractionBot) -> None:
        config = Config().instance().config
        activity = config["bot"]["activity"]

        await bot.change_presence(
            activity=Activity(
                type=ActivityType[activity["type"]], name=activity["name"]
            ),
            status=Status[activity["status"]],
        )

    @staticmethod
    def require_guild(obj) -> Guild:
        if not isinstance(obj, Guild):
            raise TypeError("Expected Guild")
        return obj

    @staticmethod
    def require_member(obj) -> Member:
        if not isinstance(obj, Member):
            raise TypeError("Expected Member")
        return obj

    @staticmethod
    def require_channel(obj) -> GuildChannel:
        if not isinstance(obj, GuildChannel):
            raise TypeError("Expected Channel")
        return obj
