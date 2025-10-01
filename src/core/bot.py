import disnake

from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    intents=intents,
    test_guilds=[1279047464594440292], #TODO: move this id into config
    reload=True
)

def run(token: str) -> None:
    bot.run(token)