import os

from pathlib import Path

from dotenv import load_dotenv
from disnake import File
from disnake.ext import commands

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"


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
    # ----------------
    bot.load_extension("cogs.commands.verification")
    bot.load_extension("cogs.commands.purge")
    print("Cogs loaded")


def get_asset(name: str) -> File:
    path = ASSETS_DIR / name
    return File(path, filename=name)
