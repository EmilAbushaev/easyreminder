from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state.create import CreateState
from keyboards.person_kb import person_list_kb
from utils.database import Database
import os
import re


async def delete_person(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите, кого хотите удалить?', reply_markup=person_list_kb())
    await state.set_state(CreateState.person_name)


async def remove_selected_person(call: CallbackQuery, state: FSMContext):
    await state.update_data(pername=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    del_data = await state.get_data()
    db = Database(os.getenv('DATABASE_NAME'))
    db.delete_person(del_data['pername'])
    await state.clear()