import os

from pathlib import Path

from dotenv import load_dotenv
from disnake import File, Activity, ActivityType, Status
from disnake.ext import commands

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"


def fetch_tokens() -> tuple[str, str]:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

    if not DISCORD_TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable is None")
    if not OPENAI_TOKEN:
        raise RuntimeError("OPENAI_TOKEN environment variable is None")

    return (DISCORD_TOKEN, OPENAI_TOKEN)


def load_cogs(bot: commands.Bot) -> None:
    print("Loading cogs")
    bot.load_extension("cogs.events.connect")
    bot.load_extension("cogs.events.ready")
    bot.load_extension("cogs.events.disconnect")
    bot.load_extension("cogs.events.resumed")
    # ----------------
    bot.load_extension("cogs.commands.verification")
    bot.load_extension("cogs.commands.purge")
    bot.load_extension("cogs.commands.lookup")
    bot.load_extension("cogs.commands.ask")
    print("Cogs loaded")


async def update_presence(bot: commands.Bot) -> None:
    await bot.change_presence(
        activity=Activity(
            type=ActivityType.playing,
            name="В активной разработке 🚧"
        ),
        status=Status.idle
    )


def get_asset(name: str) -> File:
    path = ASSETS_DIR / name
    return File(path, filename=name)
