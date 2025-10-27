from disnake import Intents
from disnake.ext import commands


class Bot:
    """Wrapper around disnake.commands.Bot for flexible initialization"""

    def __init__(self, intents: Intents = Intents.all(), prefix: str = ".", reload: bool = False):
        self.intents = intents
        self.command_prefix = prefix
        self.reload = reload
        self.client: commands.Bot | None = None

    def init(self) -> None:
        """Initialize the internal disnake bot instance"""
        self.client = commands.Bot(
            intents=self.intents,
            command_prefix=self.command_prefix,
            reload=self.reload
        )

    def run(self, token: str) -> None:
        """Run the bot with the provided token"""
        if not self.client:
            raise RuntimeError("Bot NOT INITIALIZED. Call init() first")

        if not token:
            raise ValueError("Token not provided to run()")

        self.client.run(token)
