import os

from dotenv import load_dotenv

from src.core import console, bot, utils

def main() -> None:
    console.clear()
    utils.load_cogs()
    load_dotenv()
    bot.run(token=os.getenv("TOKEN"))

if __name__=="__main__":
    main()