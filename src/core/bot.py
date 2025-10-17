import disnake

from disnake.ext import commands

from core.config import fetch_config

intents = disnake.Intents.all()

bot = None


def init_bot():
    global bot
    config = fetch_config()
    bot = commands.Bot(
        command_prefix=".",
        intents=intents,
        test_guilds=[config["bot"]["test_guild"]],
        reload=True
    )
    return bot


def run(token: str) -> None:
    if not bot:
        raise RuntimeError("Bot not initialized - call init_bot() first")
    bot.run(token)
