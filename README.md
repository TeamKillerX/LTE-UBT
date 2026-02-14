# LTE-UBT (Lite Userbot)
LTE-UBT is a lightweight userbot built with Pyrogram. It features a minimal plugin system and integrates with Userbot-Auth for authentication.

# Features
- Built with Pyrogram
- Small, modular plugins
- Userbot-Auth integration

## Deploy LTE-UBT with Docker

## Quick Start

```bash
git clone https://github.com/TeamKillerX/LTE-UBT
cd LTE-UBT

docker build -t lte-ubt .

docker run -d \
  --name lte-ubt \
  -e API_ID=your_api_id \
  -e API_HASH=your_api_hash \
  -e SESSION_STRING=your_session_string \
  -e UBT_SECRET=your_secret \
  lte-ubt
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| API_ID | Your Telegram API ID |
| API_HASH | Your Telegram API Hash |
| UBT_SECRET | Userbot-Auth secret key |

## Docker Compose

```yaml
version: '3'
services:
  lte-ubt:
    build: .
    container_name: lte-ubt
    environment:
      - API_ID=your_api_id
      - API_HASH=your_api_hash
      - UBT_SECRET=your_secret
      - SESSION_STRING=your_session_string
    restart: unless-stopped
```

Run with compose:

```bash
docker-compose up -d
```

## Logs

```bash
docker logs -f lte-ubt
```

## Stop Container

```bash
docker stop lte-ubt
docker rm lte-ubt
```
# License
- [MIT License](https://github.com/TeamKillerX/LTE-UBT)
