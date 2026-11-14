import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}! Я твой первый бот 🤖")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Команды:\n"
        "/start — начать\n"
        "/help — помощь\n"
        "/about — о боте\n\n"
        "Пришли число — я возведу его в квадрат."
    )


@dp.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        "Я учебный бот 🤖\n"
        "Написан на Python + aiogram 3.\n"
        "Умею: повторять текст и считать квадраты чисел."
    )


@dp.message(F.text.isdigit())          # только цифры: "5", "123"
async def square(message: Message):
    number = int(message.text)
    await message.answer(f"{number}² = {number ** 2}")


@dp.message(F.sticker | F.photo)       # стикер ИЛИ фото
async def not_text(message: Message):
    await message.answer("Я пока понимаю только текст 🙂")


@dp.message(F.text)                    # всё остальное — эхо (всегда последним!)
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())