from disnake.ext import commands

from core.utils import update_presence


class OnReadyEvent(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("OnReadyEvent cog Loaded")

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Logged in as {self.bot.user.name} | id: {self.bot.user.id}")
        await update_presence(self.bot)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnReadyEvent(bot))
