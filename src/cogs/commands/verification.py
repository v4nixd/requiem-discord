from disnake import MessageInteraction
from disnake.ext import commands
from disnake.utils import get

from ui.embeds import VerificationUI
from database.repositories import user_repository

VERIFIED_ROLE_ID = 1279053939408638014
USER_ROLE_ID = 1279053761154646090
ADMIN_ROLE_ID = 1279053326507573373


class VerificationCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        print("VerificationCommands cog Loaded")

    @commands.command(name="verify_embed", hidden=True)
    @commands.has_role(ADMIN_ROLE_ID)
    @commands.guild_only()
    async def verify_embed(self, ctx: commands.Context) -> None:
        verify_ui = VerificationUI()
        await ctx.send(
            components=[verify_ui],
            file=verify_ui.get_file()
        )

    @commands.Cog.listener("on_button_click")
    async def handle_buttons(self, inter: MessageInteraction) -> None:  # type: ignore
        if not inter.guild:
            print("on_button_click event has no inter.guild")
            return

        member = inter.guild.get_member(inter.author.id)
        if not member:
            print(
                "on_button_click event "
                f"couldnt find member with userid {inter.author.id} "
                f"in guild with id {inter.guild.id}"
            )
            return

        if inter.component.custom_id == "verify_user":
            verified_role = get(inter.guild.roles, id=VERIFIED_ROLE_ID)
            user_role = get(inter.guild.roles, id=USER_ROLE_ID)
            if not verified_role or not user_role:
                print(
                    "Tried to verify user with non existent role, "
                    f"either {VERIFIED_ROLE_ID} or {USER_ROLE_ID}"
                )
                return

            if await user_repository.get_user(member.id) == None:
                await user_repository.register_user(member)

            await user_repository.set_verified(member.id, True)
            await member.add_roles(verified_role, user_role)
            await inter.response.send_message(
                "🔓 Вам выдан доступ к серверу",
                ephemeral=True,
                delete_after=2
            )
        elif inter.component.custom_id == "verify_admin":
            admin_role = get(inter.guild.roles, id=ADMIN_ROLE_ID)
            if not admin_role:
                print(f"Admin role not found with id {ADMIN_ROLE_ID}")
                return

            if not admin_role in member.roles:
                await inter.response.send_message(
                    "🔒 У вас недостаточно прав",
                    ephemeral=True,
                    delete_after=2
                )
            else:
                await inter.response.send_message(
                    f"Welcome to admin panel, {member.display_name}!",
                    ephemeral=True
                )


def setup(bot: commands.Bot) -> None:
    bot.add_cog(VerificationCommands(bot))
