from utils import get_env_from_file, configurate_logging
import asyncio
from telegram import bot


async def main():
    configurate_logging.configurate_logging()
    get_env_from_file.get_env_from_file()


if __name__ == "__main__":
    asyncio.run(main())
    telegram_stuff = asyncio.run(bot.setup_bot())
    asyncio.run(bot.start_polling(telegram_stuff))

