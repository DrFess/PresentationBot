from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command(commands=['menu']))
async def command_start_handler(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Создать презентацию', callback_data='create_presentation'))
    await message.answer(
        'Чтобы создать презентацию, нажмите на кнопку "Создать презентацию"',
        reply_markup=builder.as_markup())
