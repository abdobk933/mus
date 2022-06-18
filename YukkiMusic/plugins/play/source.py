import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس فمبير","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b6d7f12c06eb782447c7e.png",
        caption=f"""[ ?????????????? ???? ???????????? ???????????? ??](https://t.me/XxvprxX)\n\n[ ?????? ???????? ???????????? ???? ???????????????? ??](https://t.me/XxvprxX)\n\n[ ???????????? ?????? ?????????????? ?????????? ??](https://t.me/XxvprxX)\n\n||[  ?????????????????? ](https://t.me/XxlllllllllllllllllllllllllllxX)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ˹ 𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸فمـبــيرـ͢）⛧", url=f"https://t.me/XxlllllllllllllllllllllllllllxX"), 
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄«𝐕𝘼𝙈𝘽𝙄𝙍🖥", url=f"https://t.me/XxvprxX"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/VPllllllbot?startgroup=true"),
                ],

            ]

        ),

    )
