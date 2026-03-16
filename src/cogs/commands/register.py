import json

from disnake import AppCmdInter
from disnake.ext import commands

from src.requiem_api.client import AsyncAPIClient


class RegisterCommand(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot: commands.InteractionBot = bot
        print("RegisterCommand cog initialized")

    @commands.slash_command(
        name="register", description="Register your account with the bot"
    )
    async def register(self, inter: AppCmdInter) -> None:
        api = AsyncAPIClient.instance()
        if api is None:
            await inter.response.send_message(
                "API client not initialized. Please try again later.", ephemeral=True
            )
            return

        result = await api.sync_user(
            discord_id=inter.author.id,
            username=inter.author.name,
            global_name=inter.author.display_name,
            avatar=str(inter.author.avatar.url) if inter.author.avatar else None,
            banner=str(inter.author.banner.url) if inter.author.banner else None,
        )

        result_json = json.dumps(
            json.loads(result), indent=2, ensure_ascii=False, default=str
        )

        message = "\n".join(
            [
                "Успешная регистрация",
                "Информация для разработчиков: ```json",
                result_json,
                "```",
                f"`createdAt`: <t:{int(result.createdAt.timestamp())}:R>",
                f"`updatedAt`: <t:{int(result.updatedAt.timestamp())}:R>",
            ]
        )

        await inter.response.send_message(message, ephemeral=True)


def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(RegisterCommand(bot))
