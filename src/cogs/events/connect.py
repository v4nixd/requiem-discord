from disnake.ext import commands

from src.utils import Utils


class OnConnectEvent(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot: commands.InteractionBot = bot
        print("OnConnectEvent cog initialized")

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        await Utils.update_presence(self.bot)
        print("Bot connected to Discord")


def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(OnConnectEvent(bot))
