from disnake import MessageInteraction
from disnake.ext import commands

from ui.embeds import VerificationUI


class VerificationCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("VerificationCommands cog Loaded")

    @commands.command(name="verify_embed")
    async def verify_embed(self, ctx: commands.Context) -> None:
        verify_ui = VerificationUI()
        await ctx.send(
            components=[verify_ui],
            file=verify_ui.get_file()
        )

    @commands.Cog.listener("on_button_click")
    async def handle_buttons(self, inter: MessageInteraction) -> None:  # type: ignore
        if inter.component.custom_id == "verify_user":
            await inter.response.send_message(
                "🔓 Вам выдан доступ к серверу",
                ephemeral=True
            )


def setup(bot: commands.Bot) -> None:
    bot.add_cog(VerificationCommands(bot))
