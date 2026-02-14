# LTEUBT

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://python.org)
[![Pyrogram](https://img.shields.io/badge/pyrogram-latest-red)](https://pyrogram.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Plugin Example

Create `plugins/echo.py`:

```python
from pyrogram import Client, filters

@Client.on_message(filters.me & filters.command("echo"))
async def echo(client, message):
    if len(message.command) > 1:
        text = message.text.split(None, 1)[1]
        await message.edit(text)
```

## License

MIT License • Free for everyone, forever.

**Note:** RyzenthUBT Max (paid version) coming in 2027. LTEUBT remains completely free.
