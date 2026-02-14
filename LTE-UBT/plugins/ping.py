import asyncio
from datetime import datetime as dt

from pyrogram import Client, filters


@Client.on_message(
    ~filters.scheduled
    & filters.command(["ping"], ["."])
    & filters.me
    & ~filters.forwarded
)
async def ping(uptime, message):
    start = dt.now()
    _ = await message.reply_text("**Pong!!**")
    await asyncio.sleep(1.5)
    end = dt.now()
    duration = (end - start).microseconds / 1000
    await _.edit_text(
        f" **Pong !!** " f"`%sms` \n" f" **Uptime** - " f"`{uptime}` " % (duration)
    )
