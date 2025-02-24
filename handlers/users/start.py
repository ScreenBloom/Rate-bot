from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards import kb, ik
from loader import dp
from states import st
from utils.db_api import database as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db.create_user(message.from_user.id,message.from_user.username)
    db.create_user_assessed(message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name}!🌸\n"
                        "Добро пожаловать в мир бесплатной оценки внешности! \n\n"
                        "Здесь ты сможешь оценить облик других людей, а также начать общение с тем, кто тебе понравится!🔥👀")

    if not db.get_user_ankets(message.from_user.id):
        await message.answer("📖 Регистрация!\n\n"
                             "<b>Введите имя которое будет отображено у вас в профиле.</b>")
        await st.UserState.name.set()
    else:
        await message.answer("Выберите действие⤵️", reply_markup=kb.menu)