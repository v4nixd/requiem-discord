from disnake.ext import commands, tasks

class OnReadyEvent(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("OnReadyEvent cog Loaded")
        
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Logged in as {self.bot.user.name} | id: {self.bot.user.id}")
        
def setup(bot: commands.Bot) -> None:
    bot.add_cog(OnReadyEvent(bot))