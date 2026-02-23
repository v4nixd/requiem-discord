from disnake import Activity, ActivityType, Status
from disnake.ext import commands

from src.config import Config


class Utils:
    @staticmethod
    def load_cogs(bot: commands.InteractionBot) -> None:
        print("Loading cogs...")
        bot.load_extensions("src/cogs/events")
        # bot.load_extensions("src/cogs/commands")
        print("Cogs loaded successfully")

    @staticmethod
    async def update_presence(bot: commands.InteractionBot) -> None:
        config = Config().instance().config
        activity = config["bot"]["activity"]

        await bot.change_presence(
            activity=Activity(
                type=ActivityType[activity["type"]],
                name=activity["name"]
            ),
            status=Status[activity["status"]]
        )
