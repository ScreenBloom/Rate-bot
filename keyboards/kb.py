from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🌟Оценивать")).add(
    KeyboardButton("👤Профиль"),
    KeyboardButton("⚡Vip"),
    KeyboardButton("✨Лучшие Анкеты")).add(
    KeyboardButton("🔎История Оценок"))


floor = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("Парень"),
    KeyboardButton("️Девушка"))


who = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("️Парней"),
    KeyboardButton("️‍Девушек"),
    KeyboardButton("Любой"))
