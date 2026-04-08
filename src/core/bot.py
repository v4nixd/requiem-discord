from disnake import Intents
from disnake.ext import commands


class Bot:
    def __init__(
        self, intents: Intents = Intents.default(), reload: bool = False
    ) -> None:
        self.intents = intents
        self.intents.members = True
        self.reload = reload
        self.client: commands.InteractionBot = commands.InteractionBot(
            intents=self.intents, reload=self.reload
        )

    def run(self, token: str) -> None:
        if not self.client:
            raise RuntimeError("Bot client is not initialized")

        if not token:
            raise ValueError("Token must be provided to run the bot")

        self.client.run(token)
