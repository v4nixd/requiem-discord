import asyncio

from importlib import import_module

from disnake import AppCmdInter
from disnake.ext import commands
from openai import AsyncOpenAI

from main import Main

AI_ROLE_ID = 1435787436130046075


class AskCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        self.client: AsyncOpenAI | None = None
        print("AskCommand cog Loaded")

    def _resolve_main_get_ai(self) -> AsyncOpenAI | None:
        try:
            main_mod = import_module("__main__")
            Main = getattr(main_mod, "Main", None)
            if Main:
                return Main.get_ai()
        except Exception:
            pass

    @commands.slash_command(name="ask")
    @commands.has_role(AI_ROLE_ID)
    @commands.guild_only()
    async def ask(self, inter: AppCmdInter, prompt: str) -> None:
        await inter.response.defer(ephemeral=True)

        if not self.client:
            self.client = self._resolve_main_get_ai()

        try:
            if not self.client:
                await inter.edit_original_response(content="AI client unavailable.")
                return

            async with self.client.responses.stream(
                model="gpt-5-nano",
                input=[
                    {"role": "system", "content": (
                        "Ты — интеллектуальный ассистент, отвечающий в стиле ChatGPT, "
                        "но с учётом ограничений Discord Markdown.\n\n"

                        "### Форматирование:\n"
                        "- Используй только Discord Markdown: **жирный**, *курсив*, `код`, ```блоки``` и цитаты `>`.\n"
                        "- Не используй HTML, LaTeX, таблицы, эмодзи или нестандартные символы.\n"
                        "- Заголовки оформляй как `## Раздел` или `### Подраздел` (через `#`, а не жирный текст).\n"
                        "- Разделяй смысловые блоки пустой строкой.\n"
                        "- Никогда не используй длинные сплошные параграфы без форматирования.\n\n"

                        "### Стиль ответа:\n"
                        "- Пиши структурно и красиво, с визуальной иерархией, как ChatGPT.\n"
                        "- Избегай вводных фраз типа 'конечно' или 'вот ответ'. Сразу переходи к сути.\n"
                        "- Для списков используй `-` или нумерацию.\n"
                        "- Код и примеры всегда помещай в блок ```python``` или просто ```.\n"
                        "- Если ответ технический — выделяй ключевые термины жирным.\n"
                        "- Не вставляй ссылки, если их нельзя кликнуть.\n"
                        "- Никогда не выходи за рамки Markdown Discord — никаких HTML, JSON, XML, LaTeX, или таблиц.\n"
                        "- Никогда не ставь точки в конце блоков и кода.\n\n"

                        "### Контекст:\n"
                        "- Ты работаешь как ассистент в Discord-боте проекта Requiem.\n"
                        "- Пользователь может быть программистом, геймером или создателем систем — адаптируйся под стиль.\n"
                        "- Твоя цель — выдавать ответы, которые приятно читать в чате: чисто, красиво и с форматированием."
                    )},
                    {"role": "user", "content": prompt}
                ]
            ) as stream:
                response_text = ""
                stop = False

                async def _periodic_updater():
                    while True:
                        await asyncio.sleep(1.0)
                        try:
                            await inter.edit_original_response(content=response_text or "...")
                        except Exception:
                            pass
                        if stop:
                            break
                updater_task = asyncio.create_task(_periodic_updater())

                try:
                    async for event in stream:
                        if event.type == "response.output_text.delta":
                            delta = event.delta
                            if isinstance(delta, str):
                                response_text += delta
                            elif hasattr(delta, "content"):
                                response_text += getattr(
                                    delta,
                                    "content"
                                ) or ""
                            elif isinstance(delta, dict) and "content" in delta:
                                response_text += delta.get("content") or ""
                finally:
                    stop = True
                    try:
                        await updater_task
                    except Exception:
                        pass

            answer = response_text

            if not answer:
                answer = "No answer received."
            if len(answer) > 2000:
                answer = answer[:1997] + "..."

            await inter.edit_original_response(content=answer)

        except Exception as e:
            await inter.edit_original_response(content=f"Ошибка при обращении к API: {type(e).__name__}")
            print(e)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(AskCommand(bot))
