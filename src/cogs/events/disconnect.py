from disnake.ext import commands


class OnDisconnectEvent(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("OnDisconnectEvent cog Loaded")

    @commands.Cog.listener()
    async def on_disconnect(self) -> None:
        print(f"Disconnected from Discord")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnDisconnectEvent(bot))
