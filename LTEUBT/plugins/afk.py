from time import time

from pyrogram import Client, filters

from LTEUBT.sqlite._db import delete_afk_in_db, get_afk, is_afk, set_afk_in_db


@Client.on_message(
    ~filters.scheduled
    & filters.command("afk", prefixes=".")
    & filters.me
    & ~filters.forwarded
)
async def afk(client, message):
    start_time = str(int(time()))
    reason = " ".join(message.command[1:]).strip()

    if not reason:
        return await message.reply_text("AFK reason is missing.")

    get_afk = await is_afk(client.me.id)
    if get_afk:
        return await message.reply_text("AFK mode is already enabled.")

    await set_afk_in_db(
        user_id=client.me.id,
        afk_time=start_time,
        afk_reason=reason,
        is_afk=True
    )

    return await message.reply_text(
        f"{message.from_user.first_name} <b>is now AFK</b>\n"
        f"<b>Reason:</b> <code>{reason}</code>"
    )

@Client.on_message(
    ~filters.scheduled
    & filters.command("unafk", prefixes=".")
    & filters.me
    & ~filters.forwarded
)
async def unafk(client, message):
    get_afk = await is_afk(client.me.id)
    if not get_afk:
        await message.reply_text("AFK mode is already disabled.")
        return
    await delete_afk_in_db(client.me.id)
    return await message.reply_text(f"{message.from_user.first_name} <b>is no longer AFK!</b>")

@Client.on_message(
    filters.group
    & filters.mentioned
    & filters.incoming
    & ~filters.bot
)
async def check_afk(client, message):
    get_afk = await get_afk(client.me.id)
    if not get_afk:
        return
    if get_afk and get_afk["is_afk"]:
        return await message.reply_text(get_afk["reason"])
