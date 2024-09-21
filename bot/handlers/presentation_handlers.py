from pprint import pprint

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


class PresentationSteps(StatesGroup):
    first_step = State()
    images_step = State()


@router.callback_query(F.data == 'create_presentation')
async def create_presentation(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PresentationSteps.first_step)
    await callback.message.answer('Отправь мне фото и описание для первого слайда')


@router.message(PresentationSteps.first_step)
async def get_images(message: Message, state: FSMContext):
    await state.set_state(PresentationSteps.images_step)
    await message.bot.download(file=message.photo[-1].file_id, destination=f'images/{message.photo[-1].file_unique_id}.jpg')
    await message.answer(f'Фото с номером {message.photo[-1].file_unique_id} сохранил')


@router.message(PresentationSteps.images_step)
async def give_presentation(message: Message, state: FSMContext):
    pass
