
import g4f
from src.telegram_gpt_bot.utils.logging_tools import get_logger


async def request_to_gpt(promt: str) -> str:
    logger = get_logger("openai/gptfree")

    response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
            {"role": "user", "content": promt}], stream=False, provider=g4f.Provider.ChatgptAi)
    return response
