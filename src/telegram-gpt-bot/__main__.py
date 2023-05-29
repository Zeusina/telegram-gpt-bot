import logging

from utils import env_tools, logging_tools
import asyncio
from telegram import bot


async def main():
    logging_tools.configurate_logging()
    env_tools.get_env_from_file()
    telegram_stuff = await bot.setup_bot()
    await bot.start_polling(telegram_stuff)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error("Bot was stopped by user")

