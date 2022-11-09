import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZp7eIAACYn9jQ4fSHUbGxAMFJz_-kaRcOuoRWAACDgcAAruXGFbarx8_grqJYh4E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , 🥀\n\n
๏ This is [{bn}](t.me/{bu}) ,  !
➻ The most Powerful telegram music  bot with some awesome and useful features.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🖤 by : [𝗬𝗔𝗦𝗛𝗨🥀](https://t.me/{me}) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "📨 Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "📨 Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/Friend_yashu"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat="GIRL_FRIEND_MUSIC_BOT"
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://github.com/Akashjshhd/yashu-X-kittu"
                    )]
            ]
       ),
    )

