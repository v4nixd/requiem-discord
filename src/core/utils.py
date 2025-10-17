import os

from disnake import Activity, ActivityType, Status
from disnake.ext import commands
from dotenv import load_dotenv

from core.config import fetch_config

load_dotenv()


def fetch_token() -> str:
    return os.getenv("TOKEN")


def load_cogs(bot: commands.Bot) -> None:
    print("loading cogs")
    bot.load_extension("cogs.events.connect")
    bot.load_extension("cogs.events.ready")


async def update_presence(bot: commands.Bot) -> None:
    config = fetch_config()
    await bot.change_presence(
        activity=Activity(
            type=ActivityType[config["bot"]["activity"]["type"]],
            name=config["bot"]["activity"]["name"]
        ),
        status=Status[config["bot"]["status"]]
    )
