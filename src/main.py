from core import bot
from core.utils import fetch_token
from core.config import load_config
from core.bot import init_bot


def main() -> None:
    TOKEN = fetch_token()
    load_config("../config.yml")
    init_bot()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
