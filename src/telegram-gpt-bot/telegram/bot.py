import logging
import os
from typing import Tuple

import aiogram.client.bot
from aiogram import Bot, Dispatcher, types


async def setup_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(os.getenv("TELEGRAM_TOKEN"))
    dp = Dispatcher()
    return bot, dp


async def start_polling(telegram_stuff: tuple[Bot, Dispatcher]):
    bot = telegram_stuff[0]
    dp = telegram_stuff[1]
    await dp.start_polling(bot)