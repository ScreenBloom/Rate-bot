import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext

from data import config as cfg
from data import text as txt
from handlers.users import lt
from handlers.users import misc as ms
from keyboards import kb, ik
from loader import dp
from payments import aio
from utils.db_api import database as db


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    match message.text:
        case "Парень":
            db.update_ankets(message.from_user.id,"floor","️Парень")
            await message.answer("<b>Выберите кого хотите оценивать:</b>",reply_markup=kb.who)

        case "️Девушка":
            db.update_ankets(message.from_user.id,"floor","Девушка")
            await message.answer("<b>Выберите кого хотите оценивать:</b>", reply_markup=kb.who)

        case "️Парней":
            db.update_ankets(message.from_user.id,"who","Парней")
            await message.answer("📖 Регистрация пройдена успешна✔️\n\n"
                                 "Выберите действие⤵️", reply_markup=kb.menu)

        case "Девушек":
            db.update_ankets(message.from_user.id, "who", "‍Девушек")
            await message.answer("📖 Регистрация пройдена успешна✔️\n\n"
                                 "Выберите действие⤵️", reply_markup=kb.menu)

        case "Любой":
            db.update_ankets(message.from_user.id, "who", "Любой")
            await message.answer("📖 Регистрация пройдена успешна✔️\n\n"
                                 "Выберите действие⤵️", reply_markup=kb.menu)

        #MENU
        case "👤Профиль":
            await message.answer_photo(photo=db.get_user_ankets(message.from_user.id)['photo']
                                       ,caption=lt.profile_user(message.from_user.id),reply_markup=ik.keyboard_user)

        case "⚡Vip":
            if db.get_user(message.from_user.id)['vip'] == 0:
                data = aio.create_invoice(100)
                await message.answer(txt.buy_vip,reply_markup=ik.pay_mrkp(data))
                await asyncio.sleep(80)
                for i in range(30):
                    if aio.is_payed(data['id']):
                        db.update_userfield(message.from_user.id, "vip", 1)
                        await message.answer(f"<b>Спасибо за приобретения VIP!</b>",
                                                  reply_markup=kb.menu)
                        await ms.admin_notify(
                            text=f"✅<b>Пользователь @{message.from_user.username} опалтил VIP.</b>")
                        break
                    await asyncio.sleep(20)
            else:
                await message.answer("Вы уже преобрели VIP, можете воспользоваться новыми функциями!",reply_markup=kb.menu)

        case "✨Лучшие Анкеты":
            await message.answer(lt.best_profiles(),reply_markup=kb.menu)

        case "🌟Оценивать":
            histori = db.get_all_history_ankets(message.from_user.id)['id_ankets']
            data = db.get_user_ankets(message.from_user.id)['who']
            if data == "Парней":
                man_ankets = db.all_man_ankets()
                print(man_ankets)
            if data == "Девушек":
                girls_ankets = db.all_girl_ankets()
                print(girls_ankets)
            if data == "Любой":
                all_ankets = db.all_ankets()
                if all_ankets in histori:
                    print("0")
                else:
                    print(1)