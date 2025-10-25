# Jarvis Bot 🤖
A modular Telegram bot for sending SMS and placeholder voice calls.
## Features
- `/start` — Welcome message
- `/sms <phone> <message>` — Sends SMS via Textbelt
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

## Notes
- Textbelt demo key allows limited usage. Replace with your own for production.
- Voice call integration planned via Fonoster API.

## Usage
Once the bot is running, you can interact with it on Telegram using the following commands:
