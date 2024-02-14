from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, Command

from dotenv import load_dotenv, find_dotenv
import os
import asyncio

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hello my dear {message.from_user.full_name}. I'm your personal telegram-bot: ")


@dp.message_handler(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")


@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer("This is a help message. What do you need help with?")


@dp.message_handler(commands=['echo'])
async def echo_cmd(message: types.Message):
    await message.answer("Enter the text you want me to echo!")


@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if text in ['hi', 'hello', 'привіт', "здоровенькі були"]:
        await message.answer(f"Hello {message.from_user.full_name}")
    elif text in ['goodbuy', 'buy', 'бувай', "пака"]:
        await message.answer(f"Goodbye {message.from_user.full_name}")
    else:
        await message.reply("I don't understand you")


async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())






