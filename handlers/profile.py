from aiogram import Bot
from aiogram.types import Message
from utils.database import Database
import os


async def view_profile(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    contact = db.select_user_id(message.from_user.id)
    await bot.send_message(message.from_user.id, f'Вас зовут {contact[1]}, ваш номер телефона {contact[2]}')
