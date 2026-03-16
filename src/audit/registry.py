from collections.abc import Awaitable, Callable

from disnake import AuditLogAction, AuditLogEntry, TextChannel


class AuditHandler:
    handlers: dict[
        AuditLogAction, Callable[[AuditLogEntry, TextChannel], Awaitable[None]]
    ] = {}

    @classmethod
    def register(cls, *actions: AuditLogAction):
        def wrapper(func):
            for action in actions:
                cls.handlers[action] = func
            return func

        return wrapper
