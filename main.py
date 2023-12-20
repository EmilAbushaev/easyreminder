import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F

from state.create import CreateState
from utils.commands import set_commands
from aiogram.filters import Command
from handlers.start import get_start
from handlers.profile import view_profile
from handlers.admin.create import create_person, create_name, create_date
from handlers.admin.delete import delete_person
from handlers.register import start_register, register_phone, register_name
from state.register import RegisterState


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot) -> None:
    await bot.send_message(247276897, text='Бот запущен')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))

dp.message.register(start_register, F.text == 'Зарегистрироваться')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)

dp.message.register(view_profile, F.text == 'Профиль')
dp.message.register(create_person, F.text == 'Новая запись')
dp.message.register(create_name, CreateState.person_name)
dp.message.register(create_date, CreateState.person_date)

dp.message.register(delete_person,  F.text == 'Удалить запись')
# dp.callback_query.register(select_place, CreateState.place)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
