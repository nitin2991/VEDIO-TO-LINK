from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚃𝚑𝚎 𝙵𝚒𝚛𝚜𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝙵𝚛𝚘𝚖 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⏩ (𝚠𝚒𝚝𝚑 𝚀𝚞𝚘𝚝𝚎𝚜)..\n\n𝙾𝚛 𝚂𝚎𝚗𝚍 𝚃𝚑𝚎 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙿𝚘𝚜𝚝 𝙻𝚒𝚗𝚔\n𝚄𝚜𝚎 /sbatch 𝙵𝚘𝚛 𝚂𝚝𝚘𝚙𝚙𝚒𝚗𝚐.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except Exception as e:
            print(e)
            return
        if first_message.text == "/sbatch":
            return
        f_msg_id = await get_message_id(client, first_message)
        
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ 𝙴𝚛𝚛𝚘𝚛\n\n𝚃𝚑𝚒𝚜 𝙵𝚘𝚛𝚠𝚊𝚛𝚍𝚎𝚍 𝙿𝚘𝚜𝚝 𝙸𝚜 𝙽𝚘𝚝 𝙵𝚛𝚘𝚖 𝙼𝚢 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙾𝚛 𝚃𝚑𝚒𝚜 𝙻𝚒𝚗𝚔 𝙸𝚜 𝚃𝚊𝚔𝚎𝚗 𝙵𝚛𝚘𝚖 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕.", quote = True)
            continue
    while True:
        try:
            second_message = await client.ask(text = "𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚃𝚑𝚎 𝙻𝚊𝚜𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝙵𝚛𝚘𝚖 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⏩ (𝚠𝚒𝚝𝚑 𝚀𝚞𝚘𝚝𝚎𝚜)..\n𝙾𝚛 𝚂𝚎𝚗𝚍 𝚃𝚑𝚎 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙿𝚘𝚜𝚝 𝙻𝚒𝚗𝚔\n𝚄𝚜𝚎 /sbatch 𝙵𝚘𝚛 𝚂𝚝𝚘𝚙𝚙𝚒𝚗𝚐.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        if second_message.text == "/sbatch":
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ 𝙴𝚛𝚛𝚘𝚛\n\n𝚃𝚑𝚒𝚜 𝙵𝚘𝚛𝚠𝚊𝚛𝚍𝚎𝚍 𝙿𝚘𝚜𝚝 𝙸𝚜 𝙽𝚘𝚝 𝙵𝚛𝚘𝚖 𝙼𝚢 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙾𝚛 𝚃𝚑𝚒𝚜 𝙻𝚒𝚗𝚔 𝙸𝚜 𝚃𝚊𝚔𝚎𝚗 𝙵𝚛𝚘𝚖 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕", quote = True)
            continue
        
    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 𝚂𝚑𝚊𝚛𝚎 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b><blockquote><bold>🧑‍💻 𝙷𝚎𝚛𝚎 𝙸𝚜 𝚈𝚘𝚞𝚛 𝙲𝚘𝚍𝚎.<blockquote><bold>\n\n<blockquote><bold>𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 @Nitin_510\n\n<code><blockquote><bold>{base64_string}</blockquote></bold></code></blockquote></bold></b>\n\n<b><blockquote><bold>📤𝙷𝚎𝚛𝚎 𝙸𝚜 𝚈𝚘𝚞𝚛 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙻𝚒𝚗𝚔📥</blockquote></bold>\n\n<blockquote><bold>𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 @dd_free_dishh</blockquote></bold></b>\n\n</blockquote><bold>{link}</blockquote></bold>", quote=True, reply_markup=reply_markup)



@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝙵𝚘𝚛𝚖 𝚃𝚑𝚎 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 ⏩ (𝚠𝚒𝚝𝚑 𝚀𝚞𝚘𝚝𝚎𝚜)..\n𝙾𝚛 𝚂𝚎𝚗𝚍 𝚃𝚑𝚎 𝙳𝙱 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝙿𝚘𝚜𝚝 𝙻𝚒𝚗𝚔\n𝚃𝚢𝚙𝚎 /sgen 𝙵𝚘𝚛 𝚂𝚝𝚘𝚙𝚙𝚒𝚗𝚐.", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except Exception:
            return
        if channel_message.text == "/sgen":
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ 𝙴𝚛𝚛𝚘𝚛\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"🔁 𝚂𝚑𝚊𝚛𝚎 𝚄𝚁𝙻", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b><blockquote><bold>🧑‍💻 𝙷𝚎𝚛𝚎 𝙸𝚜 𝚈𝚘𝚞𝚛 𝙲𝚘𝚍𝚎.</blockquote></bold>\n\n<blockquote><bold>𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 @Nitin_510</blockquote></bold>\n\n<code><blockquote><bold>{base64_string}</blockquote></bold></code></b>\n\n<b><blockquote><bold>📤𝙷𝚎𝚛𝚎 𝙸𝚜 𝚈𝚘𝚞𝚛 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙻𝚒𝚗𝚔📥</blockquote></bold>\n\n<blockquote><bold>𝚁𝙴𝙼𝙾𝚅𝙴 𝙰𝙳𝚂 𝙱𝚄𝚈 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 𝙸𝚗 𝚓𝚞𝚜𝚝 70 𝚛𝚞𝚙𝚎𝚎𝚜 𝚖𝚘𝚗𝚝𝚑>>@DD_FREE_DISHH</blockquote></bold></b>\n\n<blockquote><bold>{link}</blockquote></bold>", quote=True, reply_markup=reply_markup)
