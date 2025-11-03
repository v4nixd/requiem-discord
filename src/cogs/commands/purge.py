from disnake import AppCmdInter
from disnake.ext import commands

ADMIN_ROLE_ID = 1279053326507573373


class PurgeCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("PurgeCommand cog Loaded")

    @commands.slash_command(name="purge")
    @commands.has_role(ADMIN_ROLE_ID)
    @commands.guild_only()
    async def purge(self, inter: AppCmdInter, amount: int) -> None:
        await inter.response.defer(ephemeral=True)
        deleted = await inter.channel.purge(limit=amount)  # type: ignore
        await inter.edit_original_response(
            f"🧹 Удалено {len(deleted)} сообщений.",
            delete_after=3
        )


def setup(bot: commands.Bot) -> None:
    bot.add_cog(PurgeCommand(bot))
