from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users import lt
from handlers.users import misc as ms
from keyboards import ik, kb
from loader import dp
from states import st
from utils.db_api import database as db


@dp.callback_query_handler(state="*")
async def main(call: types.CallbackQuery, state: FSMContext):
    params = call.data.split("-")
    match params[0]:
        case "back_to_menu":
            await call.message.delete()
            await call.message.answer("📓Меню:",reply_markup=kb.menu)

        case "back_to_change_to_profile":
            await state.finish()
            await call.message.delete()
            await call.message.answer_photo(photo=db.get_user_ankets(call.from_user.id)['photo'],
                                            caption=lt.profile_user(call.from_user.id),reply_markup=ik.keyboard_user)

        #Change_profile_user
        case "change_name":
            await call.message.delete()
            await call.message.answer("💠Введите имя которое будет отображено у вас в профиле:")
            await st.UserState.change_name.set()

        case "change_photo":
            await call.message.delete()
            await call.message.answer("📸Отправьте фото которое будет отображено у вас в профиле:")
            await st.UserState.change_photo.set()

        case "change_about_me":
            await call.message.delete()
            await call.message.answer("💡Напишите о себе:")
            await st.UserState.change_about_me.set()

        case "change_floor":
            await call.message.delete()
            await call.message.answer("📍Выберите ваш пол:",reply_markup=ik.change_floor)

        case "change_man":
            await call.message.delete()
            db.update_ankets(call.from_user.id,'floor',"Парень")
            await call.message.answer("🎗Ваш пол успешно изменен!",reply_markup=kb.menu)

        case "chanhe_woman":
            await call.message.delete()
            db.update_ankets(call.from_user.id,'floor',"Девушка")
            await call.message.answer("🎗Ваш пол успешно изменен!", reply_markup=kb.menu)

        case "change_who":
            await call.message.delete()
            await call.message.answer("📍Выберите кого хотите оценивать:",reply_markup=ik.change_who)

        case "change_who_man":
            await call.message.delete()
            db.update_ankets(call.from_user.id,'who',"Парней")
            await call.message.answer("🎗Ваши изменения успешно приняты!",reply_markup=kb.menu)

        case "change_who_woman":
            await call.message.delete()
            db.update_ankets(call.from_user.id, 'who', "Девушек")
            await call.message.answer("🎗Ваши изменения успешно приняты!",reply_markup=kb.menu)

        case "change_who_any":
            await call.message.delete()
            db.update_ankets(call.from_user.id,'who',"Любой")
            await call.message.answer("🎗Ваши изменения успешно приняты!", reply_markup=kb.menu)



