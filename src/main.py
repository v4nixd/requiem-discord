import atexit

import asyncio

from disnake.ext import commands

from core.utils import fetch_token, load_cogs
from core.bot import Bot
from database.models import db


class Main:
    """Main application controller for managing the bot lifecycle"""
    instance = None

    def __init__(self):
        self.bot = Bot(reload=True)
        self.bot.init()
        Main.instance = self

    @classmethod
    def get_bot(cls) -> commands.Bot:
        if not cls.instance:
            raise RuntimeError("Main instance NOT INITIALIZED")

        client = cls.instance.bot.client

        if not client:
            raise RuntimeError(
                "bot.client not initialized yet, but already is being fetched"
            )

        return client


def on_exit() -> None:
    print("Shutting down db")
    asyncio.run(db.shutdown())


if __name__ == "__main__":
    TOKEN = fetch_token()
    main = Main()
    bot = Main.get_bot()
    asyncio.run(db.create_all())
    atexit.register(on_exit)
    load_cogs(bot)
    bot.run(TOKEN)
