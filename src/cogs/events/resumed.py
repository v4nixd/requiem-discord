from disnake.ext import commands


class OnResumedEvent(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("OnResumedEvent cog Loaded")

    @commands.Cog.listener()
    async def on_resumed(self) -> None:
        print(f"Resumed session, connected to Discord")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnResumedEvent(bot))
