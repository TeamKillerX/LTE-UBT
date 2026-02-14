# LTE-UBT Plugins

## Plugin Structure

Place your custom plugins in the `plugins` directory. Each plugin should be a Python file with Pyrogram handlers.

## Example Plugin

**plugins/ping.py**

```python
from pyrogram import Client, filters
from pyrogram.types import Message
import time

@Client.on_message(
    ~filters.scheduled
    & filters.command("ping", prefixes=".")
    & filters.me
    & ~filters.forwarded
)
async def ping_command(client: Client, message: Message):
    """Check bot response time"""
    start = time.time()
    msg = await message.edit("`Pong!`")
    end = time.time()
    await msg.edit(f"`Pong! {round((end - start) * 1000)}ms`")
```

## Available Filters

| Filter | Description |
|--------|-------------|
| `filters.me` | Only messages from yourself |
| `filters.command(["cmd"])` | Command triggers |
| `~filters.scheduled` | Exclude scheduled messages |
| `~filters.forwarded` | Exclude forwarded messages |

## Plugin Examples

**plugins/echo.py**

```python
@Client.on_message(
    filters.command("echo", prefixes=".")
    & filters.me
)
async def echo_command(client: Client, message: Message):
    """Echo the message"""
    if len(message.command) > 1:
        text = message.text.split(None, 1)[1]
        await message.edit(text)
```

**plugins/help.py**

```python
@Client.on_message(
    filters.command("help", prefixes=".")
    & filters.me
)
async def help_command(client: Client, message: Message):
    """Show available commands"""
    commands = """
**Available Commands:**
.ping - Check response time
.echo <text> - Repeat your message
.help - Show this message
    """
    await message.edit(commands)
```

## Best Practices

- Use descriptive function names
- Add docstrings to explain commands
- Handle errors gracefully
- Keep plugins small and focused
- Use `filters.me` to prevent accidental triggers

## Loading Plugins

Plugins are automatically loaded from the `plugins` directory. No additional configuration needed.
