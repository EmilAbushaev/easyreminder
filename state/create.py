from aiogram.fsm.state import StatesGroup, State


class CreateState(StatesGroup):
    person_name = State()
    person_date = State()
