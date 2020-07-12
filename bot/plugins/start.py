from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"Hi {m.from_user.first_name}.\n\nI'm Screenshot Generator RoBot. I Can Provide Screenshots From Your Video Files Without Downloading The Entire File (almost instantly). For More Details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌  Support Group', url='https://t.me/HB4All'),
                    InlineKeyboardButton('🔖  More', url='https://t.me/HB4All_Bot')
                ],
                [
                    InlineKeyboardButton('🤖 HB4All Bots', url='https://t.me/BotlistHB4All'),
                    InlineKeyboardButton('👨  Master', url='https://t.me/happyboy59')
                ]
            ]
        )
    )
