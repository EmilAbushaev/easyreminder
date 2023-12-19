from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='запускаем бота'
        ),
        # BotCommand(
        #     command='help',
        #     description='помощь в работе бота'
        # )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
