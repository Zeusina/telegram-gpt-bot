import logging

from utils import env_tools, logging_tools, config_tools
import asyncio
from telegram import bot


async def main():
    config = config_tools.Config().get_instance()
    logging_tools.configurate_logging(level=config.get_log_level())
    env_tools.get_env_from_file()
    telegram_stuff = await bot.setup_bot()
    await bot.start_polling(telegram_stuff)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error("Bot was stopped by user")

