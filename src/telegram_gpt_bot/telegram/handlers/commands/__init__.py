import logging
from aiogram import Router
from aiogram.filters.command import CommandStart, Command
from src.telegram_gpt_bot.telegram.handlers.commands import start_command, ai_command

logger = logging.getLogger('telegram/handlers/commands/__init__.py')


def register_user_commands(router: Router) -> None:
    router.message.register(start_command.start_command, CommandStart())
    router.message.register(ai_command.ai_command, Command("ai", ignore_case=True))
    logger.info("User commands registered")
