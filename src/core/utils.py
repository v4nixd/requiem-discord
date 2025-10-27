import os

from dotenv import load_dotenv

from disnake.ext import commands

load_dotenv()

def fetch_token() -> str:
    return os.getenv("TOKEN")

def load_cogs(bot: commands.Bot) -> None:
    print("Loading cogs")
    bot.load_extension("cogs.events.connect")
    bot.load_extension("cogs.events.ready")
    print("Cogs loaded")