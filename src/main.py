import time
import atexit

import asyncio

from disnake.ext import commands
from openai import AsyncOpenAI

from core.utils import fetch_tokens, load_cogs
from core.bot import Bot
from core.ai import Ai
from database.models import db


class Main:
    """Main application controller for managing the bot lifecycle"""
    instance = None

    def __init__(self):
        self.bot = Bot(reload=True)
        self.ai = Ai()
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

    @classmethod
    def get_ai(cls):
        if not cls.instance:
            raise RuntimeError("Main instance NOT INITIALIZED")

        client = cls.instance.ai.client

        if not client:
            raise RuntimeError(
                "ai.client not initialized yet, but already is being fetched"
            )

        return client


def on_exit() -> None:
    print("Shutting down db")
    asyncio.run(db.shutdown())


if __name__ == "__main__":
    TOKENS = fetch_tokens()
    main = Main()
    bot = Main.get_bot()
    main.ai.init(api_key=TOKENS[1])
    asyncio.run(db.create_all())
    atexit.register(on_exit)
    time.sleep(3)
    load_cogs(bot)
    bot.run(TOKENS[0])
