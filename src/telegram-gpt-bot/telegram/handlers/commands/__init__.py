import logging
from aiogram import Router
from aiogram.filters.command import CommandStart, Command
from .start_command import start_command

logger = logging.getLogger('telegram/handlers/commands/__init__.py')


def register_user_commands(router: Router) -> None:
    router.message.register(start_command, CommandStart())

    logger.info("User commands registered")
