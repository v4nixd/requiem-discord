import inspect

from disnake import AuditLogAction, AuditLogEntry, Embed, Member

from src.audit.constants import AUDIT_LOG_ACTION_RU
from src.audit.formatters import format_diff, format_diff_raw


def fetch_action_name(entry: AuditLogEntry) -> str:
    return AUDIT_LOG_ACTION_RU.get(
        entry.action, entry.action.name.replace("_", " ").title()
    )


def validate_entry_action(entry: AuditLogEntry, target: AuditLogAction) -> None:
    caller = inspect.stack()[1].function

    if not entry.action == target:
        raise ValueError(
            f"{caller} - expected: `{target.name}` |got: `{entry.action.name}`"
        )


def build_diff_embed_base(
    entry: AuditLogEntry,
    expected_action: AuditLogAction,
    fields_map: dict[str, str],
) -> tuple[str, str]:
    validate_entry_action(entry, expected_action)

    action_name = fetch_action_name(entry)

    changes = format_diff(entry, fields_map)

    embed_base = "\n".join(changes)

    return action_name, embed_base


def set_author(entry: AuditLogEntry, embed: Embed) -> None:
    if isinstance(entry.user, Member):
        author = entry.user
    else:
        print("entry.user is not typeof Member")
        return

    embed.set_author(
        name=author.name, icon_url=author.avatar.url if author.avatar else None
    )


def build_embed(
    entry: AuditLogEntry, action_name: str, embed_base: str, content: str
) -> Embed:
    embed_base += content
    embed_base += format_diff_raw(entry)

    embed = Embed(title=action_name, description=embed_base, timestamp=entry.created_at)

    embed.set_footer(text=f"ID: {entry.id} | HASH: {hash(entry)}")

    set_author(entry, embed)

    return embed
