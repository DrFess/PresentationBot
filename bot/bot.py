import asyncio
import logging

from aiogram import Bot, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from bot.settings import TOKEN

bot = Bot(token=TOKEN, parse_mode='HTML')
router = Router()


@router.message(Command(commands=['start']))
async def command_start_handler(message: Message):
    await message.answer('Привет, я - бот для детского травмпункта.')


async def main():
    dp = Dispatcher()
    dp.include_routers(
        router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
