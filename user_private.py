from aiogram.filters import CommandStart, Command
from aiogram import types, Router

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hello my dear friend {message.from_user.full_name}. I`m your personal telegram-bot!")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")


@user_private_router.message()
async def echo(message: types.Message):
    text = message.text
    if text in ['hi', 'hello', 'привіт', "здоровенькі були"]:
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text in ['goodbuy', 'buy', 'бувай', "пака"]:
        await message.answer(f"Goodbye {message.from_user.full_name}")
    else:
        await message.reply("I don't understand you")