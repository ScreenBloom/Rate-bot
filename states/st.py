from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards import kb, ik
from loader import dp
from utils.db_api import database as db


class UserState(StatesGroup):
    name = State()
    photo = State()
    change_name = State()
    change_photo = State()
    change_about_me = State()

@dp.message_handler(state=UserState.name)
async def main(message: types.Message,state: FSMContext):
    try:
        name = message.text
        await state.update_data(name=name)
        await message.answer("📷Отправьте фото которое будет отображено у вас в профиле!")
        await UserState.photo.set()
    except Exception as e:
        pass

@dp.message_handler(state=UserState.photo,content_types=types.ContentTypes.PHOTO)
async def main(message: types.Message,state: FSMContext):
    try:
        photo_id = message.photo[0].file_id
        data = await state.get_data()
        db.create_ankets(message.from_user.id,data['name'],photo_id)
        await message.answer("👥<b>Выберите ваш пол:</b>",reply_markup=kb.floor)
        await state.finish()
    except Exception as e:
        pass


@dp.message_handler(state=UserState.change_name)
async def main(message: types.Message,state: FSMContext):
    try:
        name = message.text
        db.update_ankets(message.from_user.id,'name',name)
        await message.answer("🎗Ваше имя изменено!",reply_markup=kb.menu)
        await state.finish()
    except Exception as e:
        pass

@dp.message_handler(state=UserState.change_photo,content_types=types.ContentTypes.PHOTO)
async def main(message: types.Message,state: FSMContext):
    try:
        photo_id = message.photo[0].file_id
        db.update_ankets(message.from_user.id,'photo',photo_id)
        await message.answer("🎗Ваше фото успешно изменено!",reply_markup=kb.menu)
        await state.finish()
    except Exception as e:
        pass


@dp.message_handler(state=UserState.change_about_me)
async def main(message: types.Message,state: FSMContext):
    try:
        text = message.text
        db.update_ankets(message.from_user.id,'about_me',text)
        await message.answer("🎗Ваши изменения успешно приняты!",reply_markup=kb.menu)
        await state.finish()
    except Exception as e:
        pass