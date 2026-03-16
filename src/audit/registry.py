from collections.abc import Callable, Awaitable
from disnake import AuditLogEntry, AuditLogAction, TextChannel


class AuditHandler:

    handlers: dict[
        AuditLogAction,
        Callable[[AuditLogEntry, TextChannel], Awaitable[None]]
    ] = {}

    @classmethod
    def register(cls, *actions: AuditLogAction):
        def wrapper(func):
            for action in actions:
                cls.handlers[action] = func
            return func
        return wrapper
