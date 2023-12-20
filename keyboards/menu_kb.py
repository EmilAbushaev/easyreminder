from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton


profile_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Профиль'),
        KeyboardButton(text='Новая запись'),
        KeyboardButton(text='Удалить запись'),
        KeyboardButton(text='Все записи'),

    ],
], resize_keyboard=True, one_time_keyboard=False)
