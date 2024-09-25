from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.create_presentation import create_slide

router = Router()


class PresentationSteps(StatesGroup):
    images_step = State()


@router.callback_query(F.data == 'create_presentation')
async def create_presentation(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправь мне все фото для одного слайда и описание для этого слайда')
    await state.set_state(PresentationSteps.images_step)


@router.message(F.photo, PresentationSteps.images_step)
async def get_images(message: Message):
    if message.caption is not None:
        text = message.caption
    else:
        text = ''
    await message.bot.download(
        file=message.photo[-1].file_id,
        destination=f'images/temp/{message.photo[-1].file_unique_id}.jpg'
    )
    create_slide(text=text)
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Закончить и получить презентацию', callback_data='given_presentation'))
    await message.answer(
        'Слайд создан, для нового слайда также отправь все фото для него и подпись',
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == 'given_presentation', PresentationSteps.images_step)
async def give_presentation(callback: CallbackQuery, state: FSMContext):
    presentation_file = FSInputFile('/Users/aleksejdegtarev/PycharmProjects/PresentationBot/utils/given.pptx')
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Создать презентацию', callback_data='create_presentation'))
    await callback.message.answer_document(document=presentation_file, reply_markup=builder.as_markup())
    await state.clear()
