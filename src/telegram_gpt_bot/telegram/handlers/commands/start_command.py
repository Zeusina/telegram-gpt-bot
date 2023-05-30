from aiogram.types import Message
from src.telegram_gpt_bot.utils.logging_tools import get_logger
import logging


async def start_command(message: Message):
    logger = logging.getLogger("telegram/handlers/commands/start_command")
    await message.answer(f"Привет, {message.from_user.full_name}!")
    logger.info("Bot started by: " + message.chat.full_name)

