from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from disnake import AuditLogEntry, Member, Role, User

from src.audit.utils import require_member


def extract_diff(entry: AuditLogEntry) -> list[tuple[str, Any, Any]]:
    before_data = vars(entry.before)
    after_data = vars(entry.after)

    diff: list[tuple[str, Any, Any]] = []

    for key in sorted(set(before_data) | set(after_data)):
        before = before_data.get(key)
        after = after_data.get(key)

        if before != after:
            diff.append((key, before, after))

    return diff


def stringify_iterable(values: Iterable[Any]) -> str:
    items = [stringify_diff_value(v) for v in values]

    if not items:
        return "Пусто"

    return ", ".join(items)


def stringify_diff_value(value: Any) -> str:
    if value is None:
        return "Нету"

    if isinstance(value, bool):
        return "Да" if value else "Нет"

    if isinstance(value, (Member, User)):
        return f"{value} ({value.id})"

    if isinstance(value, Role):
        return f"@{value.name} ({value.id})"

    if isinstance(value, str):
        return value if value.strip() else "Пусто"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, (list, tuple, set)):
        return stringify_iterable(value)

    if hasattr(value, "name"):
        name = getattr(value, "name", None)
        if name is not None:
            return str(name)

    return str(value)


def format_diff_line(
    key: str,
    before: Any,
    after: Any,
    fields: dict[str, str],
) -> str:
    if key in ("mute", "deaf"):
        print(key)
        state_key = f"{key}{'0' if after else '1'}"
        print(state_key)
        field_name = fields.get(state_key, state_key)
        print(field_name)
        return f"> **{field_name}**"

    field_name = fields.get(key, key)

    before_str = stringify_diff_value(before)
    after_str = stringify_diff_value(after)

    return f"> **{field_name}**: `{before_str}` ➡️ `{after_str}`"


def format_diff(entry: AuditLogEntry, fields: dict[str, str]) -> list[str]:
    diff = extract_diff(entry)

    if not diff:
        return ["> **Изменений не обнаружено**"]

    return [format_diff_line(key, before, after, fields) for key, before, after in diff]


def format_diff_raw(entry: AuditLogEntry) -> str:
    diff = extract_diff(entry)

    if not diff:
        return "No difference found"

    lines = []

    for key, before, after in diff:
        lines.append(f"- ({key}): {before}")
        lines.append(f"+ ({key}): {after}")

    result = "\n".join(lines)

    target = require_member(entry.target)
    moderator = require_member(entry.user)

    return (
        "\n```diff"
        f"\n$ (target): <@{str(target.id)}>"
        f"\n$ (moderator): <@{str(moderator.id)}>"
        f"\n$ (action): <{str(entry.action)}>"
        f"\n{result}"
        "\n```"
    )
