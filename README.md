# Jarvis Bot 🤖

A modular Telegram bot for sending SMS and placeholder voice calls.

## Features
- `/start` — Welcome message
- `/sms <number> <message>` — Sends SMS via Textbelt
- `/call <number>` — Placeholder for future voice call integration

## Setup

1. Clone the repo
2. Create a `.env` file with your credentials:
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-token-here
   TEXTBELT_KEY=textbelt
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```bash
   python bot/main.py
   ```

## Usage

Once the bot is running, you can interact with it on Telegram using the following commands:

- **`/start`** — Get a welcome message and overview of available commands
- **`/sms <phone_number> <message>`** — Send an SMS to the specified phone number with your message
- **`/call <phone_number>`** — Placeholder command for future voice call functionality

### Examples

```
/sms +1234567890 Hello from Jarvis Bot!
/call +1234567890
```

## Requirements

- Python 3.7+
- python-telegram-bot
- python-dotenv
- requests

## Configuration

Make sure to obtain:
1. A Telegram Bot Token from [@BotFather](https://t.me/botfather)
2. A Textbelt API key (or use "textbelt" for limited free tier)

## License

MIT License
