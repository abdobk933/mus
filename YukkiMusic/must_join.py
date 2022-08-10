from functools import wraps
from config.config import MUST_JOIN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


def must_join_channel(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(MUST_JOIN, message.from_user.id)
            if MUST_JOIN.isalpha():          
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await message._client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
        except UserNotParticipant:
            return await message.reply(
                    f"يجب عليك الاشتراك في قناه البوت لكي تسطيع استخدامه",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضغط للاشتراك", url=f"https://t.me/{MUST_JOIN}"),
                            ],
                            [
                                InlineKeyboardButton("@𝑳 𝑬 𝑮 𝑬 𝑵 𝑫.❤_", url=f"https://t.me/UR_ML"),
                            ] 
                         ] 
                      ) 
                   ) 
        return await func(_, message)    
    return sz_message
