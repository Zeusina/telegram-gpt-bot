import logging
import os
from src.telegram_gpt_bot.utils.logging_tools import get_logger
from aiogram import Bot, Dispatcher
from src.telegram_gpt_bot.telegram.handlers.commands import register_user_commands, commands
from aiogram.types import BotCommand


async def setup_bot() -> tuple[Bot, Dispatcher]:
    logger = get_logger("telegram/bot")
    bot = Bot(os.getenv("TELEGRAM_TOKEN"))
    dp = Dispatcher()
    register_user_commands(dp)
    await register_bot_commands(bot)
    return bot, dp


async def start_polling(telegram_stuff: tuple[Bot, Dispatcher]):
    logger = get_logger("telegram/bot")
    bot = telegram_stuff[0]
    dp = telegram_stuff[1]
    await dp.start_polling(bot)


async def register_bot_commands(bot: Bot) -> None:
    logger = get_logger("telegram/bot")
    logger.info("Start register bot commands...")
    commands_for_register = []
    for command in commands.commands:
        commands_for_register.append(BotCommand(command=command[0], description=command[1]))
        logger.debug("Added for register /" + command[0])
    try:
        await bot.set_my_commands(commands=commands_for_register)
        logging.info("Bot commands successfully registered in telegram")
    except Exception as e:
        logger.error("There was an error when registering bot commands in telegram", exc_info=True)