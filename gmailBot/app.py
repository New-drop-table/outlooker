import asyncio
import logging
import sys
from os import getenv
from uuid import uuid4

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db_init import is_exist, insert_user, add_email, get_users, add_auth_code, get_auth_code, set_is_auth
from loader import con, gmail_client

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

    auth_code = str(uuid4())
    add_auth_code(message.from_user.id, auth_code)
    gmail_client.send_email(email, "Auth Code", auth_code)

    await message.answer("We sent the auth code to you email! Send me back this, adding /code in the beginning!")


@dp.message(Command("users"))
async def command_start_handler(message: Message) -> None:

    get_users()

    await message.answer("fetched")


@dp.message(Command("code"))
async def command_start_handler(message: Message) -> None:

    code_user :str = message.text.split()[-1]
    code_db : str = get_auth_code(message.from_user.id)

    if(code_db == code_user):
        set_is_auth(message.from_user.id, True)
        await message.answer("You are authenticated!")
    else:
        await message.answer("The code is wrong, try again :)")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    con.close()
