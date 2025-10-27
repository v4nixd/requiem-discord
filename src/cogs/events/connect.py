from disnake.ext import commands, tasks


class OnConnectEvent(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("OnConnectEvent cog Loaded")

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        print(f"Connected to Discord")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnConnectEvent(bot))
