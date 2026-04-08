from disnake import AppCmdInter, Member
from disnake.ext import commands

from src.core.database import get_session
from src.core.utils import Utils
from src.services.registration import RegistrationService


class RegistrationCommand(commands.Cog):
    def __init__(self, bot: commands.InteractionBot) -> None:
        self.bot: commands.InteractionBot = bot
        print("RegistrationCommand cog initialized")

    @commands.slash_command(
        name="register", description="Register yourself in the database"
    )
    async def register(self, inter: AppCmdInter) -> None:
        service = RegistrationService(get_session())
        user = service.get_user(inter.author.id)
        if user is not None:
            await inter.response.send_message(
                "You are already registered!", ephemeral=True
            )
            return
        author = Utils.require_member(inter.author)
        service.register_user(author)
        user = service.get_user(inter.author.id)
        if not user:
            await inter.response.send_message(
                "An error occurred while registering you. Please try again later.",
                ephemeral=True,
            )
            return
        await inter.response.send_message(
            f"You have been registered!\nUsername: {user.username}\nID: `{user.id}`",
            ephemeral=True,
        )

    @commands.slash_command(name="register_guild")
    async def register_guild(self, inter: AppCmdInter) -> None:
        await inter.response.defer(ephemeral=True)

        service = RegistrationService(get_session())

        guild = Utils.require_guild(inter.guild)
        await service.register_guild(guild)

        await inter.edit_original_response("Guild registered successfully!")

    @commands.slash_command(name="lookup")
    async def lookup(self, inter: AppCmdInter, member: Member) -> None:
        await inter.response.defer(ephemeral=True)

        service = RegistrationService(get_session())
        user = service.get_user(member.id)

        if user is None:
            await inter.edit_original_response("User not found.")
            return

        await inter.edit_original_response(
            f"User found!\nUsername: {user.username}\nID: `{user.id}`"
        )


def setup(bot: commands.InteractionBot) -> None:
    bot.add_cog(RegistrationCommand(bot))
