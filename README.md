# Jarvis Bot 🤖
A modular Telegram bot for sending SMS and placeholder voice calls.

## Features
- `/start` — Welcome message
- `/sms <number> <message>` — Sends SMS via Textbelt
- `/call <number>` — Placeholder for future voice call integration

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Next-Gen-Auto-Bots/jarvis-bot.git
cd jarvis-bot
```

### 2. Set up Self-Hosted Textbelt Server (Recommended for Unlimited SMS)

For unlimited SMS without API key restrictions, you can self-host the open-source Textbelt server:

**Why Self-Host?**
- ✅ **Unlimited SMS** - No rate limits or quotas
- ✅ **No API key required** - Direct access to your own server
- ✅ **Free and open-source** - Complete control over your messaging infrastructure
- ✅ **Privacy** - Your messages stay on your infrastructure

**Self-Hosted Textbelt Setup Steps:**

1. Clone and set up the Textbelt server:
   ```bash
   git clone https://github.com/typpo/textbelt.git
   cd textbelt
   npm install
   ```

2. Start the Textbelt server:
   ```bash
   npm start
   ```
   The server will run on `http://localhost:9090` by default.

3. (Optional) For production, deploy it on a VPS or cloud server and use a reverse proxy (nginx/Apache) with SSL.

4. Test your self-hosted server:
   ```bash
   curl -X POST http://localhost:9090/text \
     -d number=1234567890 \
     -d message="Hello from Textbelt!"
   ```

**Important:** The self-hosted version requires proper SMS gateway configuration (Twilio, Nexmo, or other providers) as documented in the [Textbelt repository](https://github.com/typpo/textbelt).

### 3. Configure Environment Variables

Create a `.env` file in the project root with your credentials:

**For Self-Hosted Textbelt (Recommended):**
```env
TELEGRAM_BOT_TOKEN=your-telegram-token-here
TEXTBELT_URL=http://localhost:9090/text
# No TEXTBELT_KEY needed when self-hosted!
```

**For Textbelt Public API (Limited Usage):**
```env
TELEGRAM_BOT_TOKEN=your-telegram-token-here
TEXTBELT_URL=https://textbelt.com/text
TEXTBELT_KEY=textbelt  # Demo key - limited to 1 SMS/day
# For production with public API, get a paid key from textbelt.com
```

**Configuration Notes:**
- `TEXTBELT_URL`: Set this to your self-hosted server URL (e.g., `http://localhost:9090/text` or `https://yourdomain.com/text`)
- `TEXTBELT_KEY`: Only required when using the public Textbelt API. **Not needed for self-hosted instances.**
- When self-hosting, the bot will send requests directly to your server without API key validation

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Bot
```bash
python bot/main.py
```

## Notes

### SMS Options Comparison

| Option | Cost | Limit | API Key Required |
|--------|------|-------|------------------|
| **Self-Hosted Textbelt** | Free (+ SMS provider costs) | Unlimited | ❌ No |
| Textbelt Demo (textbelt.com) | Free | 1 SMS/day | ✅ Yes (`textbelt`) |
| Textbelt Paid (textbelt.com) | $0.09/SMS | Pay-as-you-go | ✅ Yes (paid key) |

### Recommendations
- **For Development/Testing:** Use the self-hosted Textbelt server with a free-tier SMS provider
- **For Production:** Deploy self-hosted Textbelt on a VPS with your preferred SMS gateway (Twilio, etc.)
- **For Quick Testing:** Use the public demo key (limited to 1 SMS per day per number)

### Future Enhancements
- Voice call integration planned via Fonoster API
- Additional messaging providers support

## Resources
- [Textbelt Self-Hosted Server](https://github.com/typpo/textbelt) - Open-source SMS server
- [Textbelt Documentation](https://textbelt.com) - Public API documentation
- [Telegram Bot API](https://core.telegram.org/bots/api) - Bot development guide

## Usage

Once your bot is running:

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send `/sms <phone_number> <message>` to send an SMS
4. Example: `/sms +1234567890 Hello from Jarvis Bot!`

## Troubleshooting

- **SMS not sending?** Verify your `TEXTBELT_URL` is correct and the server is running
- **Self-hosted server not working?** Check that your SMS gateway credentials are properly configured in Textbelt
- **Rate limit errors?** Switch from public API to self-hosted solution

## License

MIT License - See LICENSE file for details
