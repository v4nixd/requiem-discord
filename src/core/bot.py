import disnake

from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix=".",
    intents=intents,
    test_guilds=[1279047464594440292],  # TODO: move this to config.yml
    reload=True
)


def run(token: str) -> None:
    bot.run(token)
