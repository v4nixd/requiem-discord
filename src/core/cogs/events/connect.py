from disnake.ext import commands

from src.core import console
from src.core.utils import Log

class OnConnectEvent(commands.Cog):
    """on_connect event handler"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        console.print(f"{Log.prefix("status")} Cog [b green]OnConnectEvent[/b green] loaded")

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        console.print(f"{Log.prefix("event")} [b green]Connected to discord[/b green]")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnConnectEvent(bot))