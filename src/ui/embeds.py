from disnake import ui, MediaGalleryItem, ButtonStyle, File

from core.utils import get_asset


class VerificationUI(ui.Container):
    def __init__(self) -> None:
        media = ui.MediaGallery(
            MediaGalleryItem(
                "attachment://verification-banner.png"
            )
        )

        text_block = ui.TextDisplay(
            "## 👋 Добро пожаловать на Requiem!\n"
            "Мы рады видеть тебя в нашем сообществе.\n"
            "Перед тем как продолжить - убедись, что ты ознакомился с основными принципами, которые делают Requiem безопасным и комфортным пространством для всех."
        )

        separator = ui.Separator(divider=True)

        rules_block = ui.TextDisplay(
            "- Ознакомься с [правилами сервера](https://v4nixd.xyz/requiem)\n"
            "- Соблюдай [условия использования Discord](https://discord.com/terms)\n"
            "- Не нарушай [Правила сообщества Discord](https://discord.com/guidelines)"
        )

        footer_block = ui.TextDisplay(
            "-# ⚠️ Нажимая кнопку ниже, ты подтверждаешь, что согласен(а) с правилами **Requiem**, а также условиями и политикой Discord."
        )

        buttons_row = ui.ActionRow(
            ui.Button(
                label="Продолжить",
                style=ButtonStyle.gray,
                custom_id="verify_user",
                emoji="✅"
            ),
            ui.Button(
                label="Admin",
                style=ButtonStyle.gray,
                custom_id="verify_admin",
                emoji="🔒"
            )
        )

        super().__init__(
            media,
            text_block,
            separator,
            rules_block,
            footer_block,
            buttons_row
        )

    def get_file(self) -> File:
        return get_asset("verification-banner.png")
