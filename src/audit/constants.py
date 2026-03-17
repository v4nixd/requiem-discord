# TODO: Move this to .yaml file

from disnake import AuditLogAction, Color

AUDIT_LOG_ACTION_RU = {
    AuditLogAction.guild_update: "Обновлены настройки сервера",
    AuditLogAction.channel_create: "Создан канал",
    AuditLogAction.channel_update: "Изменён канал",
    AuditLogAction.channel_delete: "Удалён канал",
    AuditLogAction.overwrite_create: "Создано разрешение канала",
    AuditLogAction.overwrite_update: "Изменено разрешение канала",
    AuditLogAction.overwrite_delete: "Удалено разрешение канала",
    # AuditLogAction.member_kick: "Пользователь кикнут",
    AuditLogAction.member_prune: "Массовое удаление неактивных участников",
    # AuditLogAction.member_ban_add: "Пользователь забанен",
    # AuditLogAction.member_ban_remove: "Пользователь разбанен",
    AuditLogAction.member_update: "Обновлён участник",
    AuditLogAction.member_role_update: "Изменены роли участника",
    AuditLogAction.member_move: "Участник перемещён в голосовой канал",
    AuditLogAction.member_disconnect: "Участник отключён от голосового канала",
    AuditLogAction.bot_add: "Добавлен бот",
    AuditLogAction.role_create: "Создана роль",
    AuditLogAction.role_update: "Изменена роль",
    AuditLogAction.role_delete: "Удалена роль",
    AuditLogAction.invite_create: "Создано приглашение",
    AuditLogAction.invite_update: "Изменено приглашение",
    AuditLogAction.invite_delete: "Удалено приглашение",
    AuditLogAction.webhook_create: "Создан вебхук",
    AuditLogAction.webhook_update: "Изменён вебхук",
    AuditLogAction.webhook_delete: "Удалён вебхук",
    AuditLogAction.emoji_create: "Создан эмодзи",
    AuditLogAction.emoji_update: "Изменён эмодзи",
    AuditLogAction.emoji_delete: "Удалён эмодзи",
    AuditLogAction.message_delete: "Удалено сообщение",
    AuditLogAction.message_bulk_delete: "Массово удалены сообщения",
    AuditLogAction.message_pin: "Сообщение закреплено",
    AuditLogAction.message_unpin: "Сообщение откреплено",
    AuditLogAction.integration_create: "Создана интеграция",
    AuditLogAction.integration_update: "Изменена интеграция",
    AuditLogAction.integration_delete: "Удалена интеграция",
    AuditLogAction.stage_instance_create: "Создана Stage-комната",
    AuditLogAction.stage_instance_update: "Изменена Stage-комната",
    AuditLogAction.stage_instance_delete: "Удалена Stage-комната",
    AuditLogAction.sticker_create: "Создан стикер",
    AuditLogAction.sticker_update: "Изменён стикер",
    AuditLogAction.sticker_delete: "Удалён стикер",
    AuditLogAction.guild_scheduled_event_create: "Создано событие",
    AuditLogAction.guild_scheduled_event_update: "Изменено событие",
    AuditLogAction.guild_scheduled_event_delete: "Удалено событие",
    AuditLogAction.thread_create: "Создан тред",
    AuditLogAction.thread_update: "Изменён тред",
    AuditLogAction.thread_delete: "Удалён тред",
    AuditLogAction.application_command_permission_update: "Изменены права команды приложения",
}

AUDIT_LOG_ACTION_COLORS = {
    AuditLogAction.guild_update: Color.yellow(),
    AuditLogAction.channel_create: Color.brand_green(),
    AuditLogAction.channel_update: Color.yellow(),
    AuditLogAction.channel_delete: Color.brand_red(),
    AuditLogAction.overwrite_create: Color.brand_green(),
    AuditLogAction.overwrite_update: Color.yellow(),
    AuditLogAction.overwrite_delete: Color.brand_red(),
    # AuditLogAction.member_kick: Color.brand_red(),
    AuditLogAction.member_prune: Color.brand_red(),
    # AuditLogAction.member_ban_add: Color.brand_red(),
    # AuditLogAction.member_ban_remove: Color.brand_red(),
    AuditLogAction.member_update: Color.yellow(),
    AuditLogAction.member_role_update: Color.yellow(),
    AuditLogAction.member_move: Color.blurple(),
    AuditLogAction.member_disconnect: Color.brand_red(),
    AuditLogAction.bot_add: Color.brand_green(),
    AuditLogAction.role_create: Color.brand_green(),
    AuditLogAction.role_update: Color.yellow(),
    AuditLogAction.role_delete: Color.brand_red(),
    AuditLogAction.invite_create: Color.brand_green(),
    AuditLogAction.invite_update: Color.yellow(),
    AuditLogAction.invite_delete: Color.brand_red(),
    AuditLogAction.webhook_create: Color.brand_green(),
    AuditLogAction.webhook_update: Color.yellow(),
    AuditLogAction.webhook_delete: Color.brand_red(),
    AuditLogAction.emoji_create: Color.brand_green(),
    AuditLogAction.emoji_update: Color.yellow(),
    AuditLogAction.emoji_delete: Color.brand_red(),
    AuditLogAction.message_delete: Color.brand_red(),
    AuditLogAction.message_bulk_delete: Color.brand_red(),
    AuditLogAction.message_pin: Color.brand_green(),
    AuditLogAction.message_unpin: Color.brand_red(),
    AuditLogAction.integration_create: Color.brand_green(),
    AuditLogAction.integration_update: Color.yellow(),
    AuditLogAction.integration_delete: Color.brand_red(),
    AuditLogAction.stage_instance_create: Color.brand_green(),
    AuditLogAction.stage_instance_update: Color.yellow(),
    AuditLogAction.stage_instance_delete: Color.brand_red(),
    AuditLogAction.sticker_create: Color.brand_green(),
    AuditLogAction.sticker_update: Color.yellow(),
    AuditLogAction.sticker_delete: Color.brand_red(),
    AuditLogAction.guild_scheduled_event_create: Color.brand_green(),
    AuditLogAction.guild_scheduled_event_update: Color.yellow(),
    AuditLogAction.guild_scheduled_event_delete: Color.brand_red(),
    AuditLogAction.thread_create: Color.brand_green(),
    AuditLogAction.thread_update: Color.yellow(),
    AuditLogAction.thread_delete: Color.brand_red(),
    AuditLogAction.application_command_permission_update: Color.yellow(),
}

GUILD_UPDATE_FIELDS_RU = {
    "name": "Название сервера",
    "icon": "Иконка сервера",
    "banner": "Баннер сервера",
    "splash": "Splash изображение",
    "discovery_splash": "Discovery splash",

    "owner": "Владелец сервера",

    "preferred_locale": "Язык сервера",
    "description": "Описание сервера",

    "afk_channel": "AFK канал",
    "afk_timeout": "AFK таймер",

    "system_channel": "Системный канал",
    "system_channel_flags": "Настройки системных сообщений",

    "rules_channel": "Канал правил",
    "public_updates_channel": "Канал обновлений",

    "verification_level": "Уровень проверки",
    "explicit_content_filter": "Фильтр откровенного контента",
    "default_message_notifications": "Уведомления по умолчанию",
    "mfa_level": "2FA для модерации",

    "vanity_url_code": "Vanity URL",

    "widget_enabled": "Виджет сервера",
    "widget_channel": "Канал виджета",

    "premium_progress_bar_enabled": "Полоса прогресса бустов",
}

MEMBER_UPDATE_FIELDS_RU = {
    "nick": "Изменён никнейм",
    "mute0": "Мут микрофона",
    "mute1": "Размут микрофона",
    "deaf0": "Мут наушников",
    "deaf1": "Размут наушников",
    "timeout": "Таймаут",
}

CHANNEL_FIELDS_RU = {
    "name": "Название канала",
    "type": "Тип канала",
    "position": "Позиция канала",

    "overwrites": "Права доступа",

    "topic": "Тема канала",

    "bitrate": "Битрейт",
    "rtc_region": "RTC регион",
    "video_quality_mode": "Качество видео",

    "user_limit": "Лимит пользователей",

    "slowmode_delay": "Медленный режим",
    "default_thread_slowmode_delay": "Медленный режим тредов",

    "default_auto_archive_duration": "Автоархивация тредов",

    "nsfw": "NSFW",

    "available_tags": "Доступные теги",
    "default_reaction": "Реакция по умолчанию",
}
