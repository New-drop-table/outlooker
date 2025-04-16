import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db_init import is_exist, insert_user, add_email, get_users
from loader import con

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6931652129:AAEjipnLIJI3t_bA3pezCnkxUCE52RbbqL0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    insert_user(message.from_user.id)

    await message.answer("Hello, send your email")


@dp.message(Command("email"))
async def command_start_handler(message: Message) -> None:

    insert_user(message.from_user.id)
    email :str = message.text.split()[-1]

    add_email(message.from_user.id, email)

    await message.answer("Successfully inserted the email")


@dp.message(Command("users"))
async def command_start_handler(message: Message) -> None:

    get_users()

    await message.answer("fetched")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    con.close()
