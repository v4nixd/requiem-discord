from openai import AsyncOpenAI


class Ai:
    def __init__(self):
        self.client: AsyncOpenAI | None = None

    def init(self, api_key: str) -> None:
        self.client = AsyncOpenAI(
            api_key=api_key
        )
