from data import config as cfg
from loader import bot

async def admin_notify(text):
    for admin in cfg.ADMINS:
        admin = int(admin)
        await bot.send_message(chat_id=admin,text=text)