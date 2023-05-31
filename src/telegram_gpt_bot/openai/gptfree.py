
from src.telegram_gpt_bot.openai.gpt4free import Provider

from src.telegram_gpt_bot.openai import gpt4free
from src.telegram_gpt_bot.utils.logging_tools import get_logger


async def request_to_gpt(promt: str) -> str:
    logger = get_logger("openai/gptfree")

    # usage You
    response = bytes(
        gpt4free.Completion.create(Provider.You, prompt=promt), "utf-8").decode('unicode-escape')
    return response
