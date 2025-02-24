from utils.db_api import database as db


def profile_user(user_id):
    data = db.get_user_ankets(user_id)
    text = f"""
    👤Имя: {data['name']}
👫Ваш пол: {data['floor']}

❓Вы будете оценивать: {data['who']}
✍️О себе: {data['about_me']}

🏆Ваш Рейтинг: {data['rating']}"""
    return text


def best_profiles():
    data = db.best_profiles()
    result_text = "<u>Toп 3 Лучших Анкет:</u>💎\n\n"
    for i, row in enumerate(data):
        if i == 0:
            place = "Первое место:"
        elif i == 1:
            place = "Второе место:"
        elif i == 2:
            place = "Третье место:"
        result_text += f"<b>{place}</b>\n\n👤Имя: {row[1]}\n ⛓Пол: {row[3]}\n 💡Rating: {row[6]}\n\n"
    return result_text