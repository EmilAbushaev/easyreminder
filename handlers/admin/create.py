from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.create import CreateState
from utils.database import Database
import os
import re


async def create_person(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Назовите имя именинника')
    await state.set_state(CreateState.person_name)


async def create_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f'Когда у {message.text} день рождения? \n'
        f'Введите дату в формате дд.мм.гггг')
    await state.update_data(pername=message.text)
    await state.set_state(CreateState.person_date)


async def create_date(message: Message, state: FSMContext, bot: Bot):
    if re.findall('(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d', message.text):
        await state.update_data(perdate=message.text)
        person_data = await state.get_data()
        per_name = person_data.get('pername')
        per_date = person_data.get('perdate')
        msg = f'Запись создана. У {per_name} день рождения {per_date}\n\nЯ вам напомню!'
        await bot.send_message(message.from_user.id, msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_person(per_name, per_date)
        await state.clear()

    else:
        await bot.send_message(message.from_user.id, f'Дата указана в неверном формате')