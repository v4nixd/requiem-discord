from datetime import datetime

from disnake import AppCmdInter, Member, Embed
from disnake.ext import commands

from database import models
from database.repositories import user_repository

ADMIN_ROLE_ID = 1279053326507573373


class LookupCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("LookupCommand cog Loaded")

    @commands.slash_command(name="lookup")
    @commands.has_role(ADMIN_ROLE_ID)
    @commands.guild_only()
    async def purge(self, inter: AppCmdInter, target: Member) -> None:
        await inter.response.send_message(f"# Fetching `{target.id}`", ephemeral=True)

        result = await user_repository.get_user(target.id)

        if result is None:
            await inter.edit_original_response("User not found in database")
            return
        if not isinstance(result, models.User):
            await inter.edit_original_response("Unexpected error")
            return

        result: models.User

        embed = Embed(
            title="",
            description=f'```js\nid: {result.id}\nusername: "{result.username}"\nglobal_name: "{result.global_name}"\navatar_url: "{result.avatar_url}"\nbanner_url: "{result.banner_url}"\ncreated_at: {str(result.created_at)}\njoined_at: {str(result.joined_at)}\nleft_at: {str(result.left_at)}\nverified: {str(result.verified).lower()}\nis_booster: {str(result.is_booster).lower()}\npremium_since: {str(result.premium_since)}\n```',
            color=target.color,
            timestamp=datetime.utcnow()
        )

        embed.set_author(name=result.global_name, icon_url=result.avatar_url)

        await inter.edit_original_response(content=None, embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(LookupCommand(bot))
