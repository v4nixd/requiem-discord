from core.utils import fetch_token
from core.bot import Bot

class Main:
    """Main application controller for managing the bot lifecycle"""
    instance = None

    def __init__(self):
        self.bot = Bot(reload=True)
        self.bot.init()
        Main.instance = self

    @classmethod
    def get_bot(cls) -> Bot:
        if not cls.instance:
            raise RuntimeError("Main instance NOT INITIALIZED")

        return cls.instance.bot

if __name__ == "__main__":
    TOKEN = fetch_token()
    main = Main()
    bot = Main.get_bot()
    bot.run(TOKEN)