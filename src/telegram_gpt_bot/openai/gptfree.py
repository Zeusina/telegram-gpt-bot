import gpt4free
from gpt4free import Provider
import logging


async def request_to_gpt(promt: str) -> str:
    logging.basicConfig(level=logging.DEBUG)

    # usage You
    response = bytes(
        gpt4free.Completion.create(Provider.You, prompt=promt), "utf-8").decode('unicode-escape')
    return response
