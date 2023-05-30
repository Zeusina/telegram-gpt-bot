from aiogram.types import Message
from src.telegram_gpt_bot.utils.logging_tools import get_logger
from src.telegram_gpt_bot.openai import gptfree
from aiogram.filters import CommandObject


async def ai_command(message: Message, command: CommandObject):
    logger = get_logger("telegram/handlers/commands/ai_command")
    if command.args:
        logger.debug("Get ai request from user: " + message.chat.full_name or message.chat.username)
        sent_message = await message.answer("Запрос отправлен нейросети. Подождите")
        message_text = message.text
        ai_response = str(await gptfree.request_to_gpt(message_text + " Ответ дай на русском языке"))
        await sent_message.edit_text(ai_response)
    else:
        logger.debug("Get ai request without argument from user: " + message.chat.full_name or message.chat.username)
        await message.answer("Этот текст еще не написан")