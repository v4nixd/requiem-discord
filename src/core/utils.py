import os

from dotenv import load_dotenv

from disnake.ext import commands

load_dotenv()


def fetch_token() -> str:
    TOKEN = os.getenv("TOKEN")

    if not TOKEN:
        raise RuntimeError("TOKEN environment variable is None")

    return TOKEN


def load_cogs(bot: commands.Bot) -> None:
    print("Loading cogs")
    bot.load_extension("cogs.events.connect")
    bot.load_extension("cogs.events.ready")
    bot.load_extension("cogs.events.disconnect")
    bot.load_extension("cogs.events.resumed")
    print("Cogs loaded")
