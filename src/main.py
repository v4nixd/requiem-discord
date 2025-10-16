from core import bot
from core.utils import fetch_token


def main() -> None:
    TOKEN = fetch_token()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
