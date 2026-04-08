from __future__ import annotations

from src.core.bot import Bot
from src.core.config import Config
from src.core.database import init_db
from src.core.utils import Utils


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
    init_db()
    Utils.load_cogs(bot)
    bot.run(TOKEN)
