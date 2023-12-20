from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import datetime
from utils.database import Database


def person_list_kb():
    db = Database(os.getenv('DATABASE_NAME'))
    persons = db.db_select_all('persons')
    kb = InlineKeyboardBuilder()
    for person in persons:
        kb.button(text=f'{person[1]}', callback_data=f'{person[0]}')
    kb.adjust(1)
    return kb.as_markup()
