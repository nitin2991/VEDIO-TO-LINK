import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON, USER_REPLY_TEXT
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats','auth_secret','deauth_secret', 'auth', 'sbatch', 'exit', 'add_admin', 'del_admin', 'admins', 'add_prem', 'ping', 'restart', 'ch2l', 'cancel']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚊𝚒𝚝 𝙼𝚛/𝙼𝚒𝚜𝚜 ...! 🫷", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("𝚂𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 𝚆𝚎𝚗𝚝 𝚆𝚛𝚘𝚗𝚐..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 𝚂𝚑𝚊𝚛𝚎 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])

    await reply_text.edit(f"<b<blockquote>Remove Ads In Just 50 Rupees @Legal_file_share_bot</blockquote>\n📤𝙷𝚎𝚛𝚎 𝙸𝚜 𝚈𝚘𝚞𝚛 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙻𝚒𝚗𝚔📥</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        try:
            await post_message.edit_reply_markup(reply_markup)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await post_message.edit_reply_markup(reply_markup)
        except Exception:
            pass

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 𝚂𝚑𝚊𝚛𝚎 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await message.edit_reply_markup(reply_markup)
    except Exception:
        pass
