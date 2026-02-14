import asyncio
import time
from datetime import datetime as dt

from pyrogram import Client, filters
from LTEUBT import StartTime

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += f"{time_list.pop()}, "
    time_list.reverse()
    readable_time += ":".join(time_list)
    return readable_time

@Client.on_message(
    ~filters.scheduled
    & filters.command(["ping"], ["."])
    & filters.me
    & ~filters.forwarded
)
async def ping(client, message):
    uptime = readable_time((time() - StartTime))
    start = dt.now()
    _ = await message.reply_text("**Pong!!**")
    await asyncio.sleep(1.5)
    end = dt.now()
    duration = (end - start).microseconds / 1000
    await _.edit_text(
        f" **Pong !!** " f"`%sms` \n" f" **Uptime** - " f"`{uptime}` " % (duration)
    )
