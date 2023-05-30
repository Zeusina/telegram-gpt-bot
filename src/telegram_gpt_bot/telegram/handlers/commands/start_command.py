from aiogram.types import Message
from ....utils.logging_tools import get_logger


async def start_command(message: Message):
    logger = get_logger("telegram/handlers/commands/start_command")
    await message.answer(f"Привет, {message.from_user.full_name}!")
    logger.info("Bot started by: " + message.chat.full_name)

