from disnake.ext import commands


class OnReadyEvent(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot: commands.InteractionBot = bot
        print("OnReadyEvent cog initialized")

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Bot ready")


def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(OnReadyEvent(bot))
