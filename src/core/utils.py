from src.core.bot import bot

class Log():
    def prefix(prefix: str, color: str | None = "blue") -> str:
        return f"[[b {color}]{prefix}[/b {color}]]"

def load_cogs() -> None:
    bot.load_extensions("src/core/cogs/events")
    bot.load_extensions("src/core/cogs/commands")