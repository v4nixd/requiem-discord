import os

from disnake import Activity, ActivityType, Status
from disnake.ext import commands

from dotenv import load_dotenv

load_dotenv()


def fetch_token() -> str:
    return os.getenv("TOKEN")


def load_cogs(bot: commands.Bot) -> None:
    print("loading cogs")
    bot.load_extension("cogs.events.connect")
    bot.load_extension("cogs.events.ready")


async def update_presence(bot: commands.Bot) -> None:
    await bot.change_presence(
        activity=Activity(
            type=ActivityType.listening,
            name="/help"
        ),
        status=Status.dnd
    )
