from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


keyboard_user = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="🗣Изменить Имя",callback_data="change_name"),
    InlineKeyboardButton(text="🌁Изменить Фото",callback_data="change_photo"),
    InlineKeyboardButton(text="✍Изменить О себе",callback_data="change_about_me")).add(
    InlineKeyboardButton(text="🫂Изменить Пол",callback_data="change_floor"),
    InlineKeyboardButton(text="❔Изменить кого Оценивать",callback_data="change_who")).add(
    InlineKeyboardButton(text="◀Назад",callback_data="back_to_menu"))


change_floor = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Парень",callback_data="change_man"),
    InlineKeyboardButton(text="Девушка",callback_data="chanhe_woman"),
    InlineKeyboardButton(text="◀Назад",callback_data="back_to_change_to_profile"))

change_who = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text="Парней",callback_data="change_who_man"),
    InlineKeyboardButton(text="Девушек",callback_data="change_who_woman"),
    InlineKeyboardButton(text="Любой",callback_data="change_who_any")).add(
    InlineKeyboardButton(text="◀Назад",callback_data="back_to_change_to_profile"))


def pay_mrkp(url):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text="💳 Оплатить",url=url),
        InlineKeyboardButton(text="❌ Отмена",callback_data='off_state')
    )