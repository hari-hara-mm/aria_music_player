import os
from pyrogram import Client, filters
from pyrogram.types import Message
from VCPlayBot.helpers.filters import command
from VCPlayBot.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "rmdownloads", "cleardownloads"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚊𝚕𝚕 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍 𝚏𝚒𝚕𝚎𝚜**")
    else:
        await message.reply_text("❌ **𝙽𝚘 𝚏𝚒𝚕𝚎𝚜 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍**")
        
@Client.on_message(command(["clean", "wipe", "rmr"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚊𝚕𝚕 𝚛𝚊𝚠 𝚏𝚒𝚕𝚎𝚜**")
    else:
        await message.reply_text("❌ **𝙽𝚘 are 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍**")
        
