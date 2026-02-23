from __future__ import annotations

from src.bot import Bot
from src.config import Config
from src.utils import Utils


class Main:
    _instance: Main | None = None

    def __init__(self) -> None:
        self.bot = Bot(reload=True)

    @staticmethod
    def instance() -> Main:
        if not Main._instance:
            Main._instance = Main()
        return Main._instance


if __name__ == "__main__":
    main = Main.instance()
    bot = main.bot.client
    config = Config.instance()
    TOKEN = config.get_env_var("DISCORD_TOKEN")
    Utils.load_cogs(bot)
    bot.run(TOKEN)
