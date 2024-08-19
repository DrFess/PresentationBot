import asyncio
import logging

from aiogram import Bot, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from handlers import menu_handlers, presentation_handlers
from settings import TOKEN

bot = Bot(token=TOKEN)
router = Router()


@router.message(Command(commands=['start']))
async def command_start_handler(message: Message):
    await message.answer('Привет, я - бот для создания презентаций с картинками. Для начала нажми /menu')


async def main():
    dp = Dispatcher()
    dp.include_routers(
        router,
        menu_handlers.router,
        presentation_handlers.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
