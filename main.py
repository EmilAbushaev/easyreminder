import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from utils.commands import set_commands
from aiogram.filters import Command
from handlers.start import get_start
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


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
