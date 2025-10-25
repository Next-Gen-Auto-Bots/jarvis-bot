# Jarvis Bot 🤖

A modular, production-ready Telegram bot for sending SMS and voice calls with improved architecture, robust error handling, and secure configuration management.

## ✨ Recent Upgrades & Improvements

### Code Architecture Enhancements
- **Refactored Code Structure**: Completely reorganized codebase with modular handler-based architecture for better maintainability
- **Enhanced Error Handling**: Comprehensive try-catch blocks and graceful error recovery throughout the application
- **Improved Logging**: Detailed logging system for debugging and monitoring bot operations
- **Handler Separation**: Commands organized into dedicated handler modules for cleaner code organization

### Security & Configuration
- **Environment-Based Configuration**: Migrated all sensitive credentials to `.env` file for enhanced security
- **python-dotenv Integration**: Secure loading of environment variables with validation
- **No Hardcoded Secrets**: All API keys and tokens now safely stored in environment variables

### Dependencies & Tools
- **Updated Requirements**: Added `python-dotenv` for environment management
- **Clean Dependencies**: Streamlined `requirements.txt` with essential packages only
- **Python Telegram Bot**: Using latest stable version for reliable bot operations

## 🚀 Features

- **`/start`** — Welcome message with bot introduction
- **`/sms <phone> <message>`** — Send SMS via Textbelt (self-hosted or API)
- **`/call <number>`** — Placeholder for future voice call integration
- **Modular Design** — Easy to extend with new commands and handlers
- **Error Recovery** — Graceful handling of API failures and network issues
- **Secure Configuration** — Environment-based secrets management

## 📋 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Next-Gen-Auto-Bots/jarvis-bot.git
cd jarvis-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- `python-telegram-bot` - Telegram Bot API wrapper
- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Telegram Bot Configuration
BOT_TOKEN=your_telegram_bot_token_here

# Textbelt Configuration
TEXTBELT_API_KEY=textbelt  # Use 'textbelt' for demo (1 SMS/day) or your paid key
TEXTBELT_URL=https://textbelt.com/text  # Or your self-hosted URL
```

**How to get your Bot Token:**
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow the prompts
3. Copy the API token provided
4. Paste it into your `.env` file

### 4. Set up Self-Hosted Textbelt Server (Recommended for Unlimited SMS)

For unlimited SMS without API key restrictions, self-host the open-source Textbelt server:

**Why Self-Host?**
- ✅ **Unlimited SMS** - No rate limits or quotas
- ✅ **No API key required** - Direct access to your own server
- ✅ **Free and open-source** - Complete control over your messaging infrastructure
- ✅ **Production-ready** - Reliable infrastructure for scaling

**Quick Setup:**

```bash
# Clone Textbelt repository
git clone https://github.com/typpo/textbelt.git
cd textbelt

# Install dependencies
npm install

# Configure your SMS provider (Twilio, Nexmo, etc.)
# Edit lib/config.js with your provider credentials

# Start the server
node server.js
```

Then update your `.env` file:
```env
TEXTBELT_URL=http://localhost:9090/text  # Or your server URL
TEXTBELT_API_KEY=textbelt
```

### 5. Run the Bot

```bash
python bot/main.py
```

You should see:
```
Bot started successfully!
```

## 📱 Usage

Once your bot is running:

1. **Start a chat** with your bot on Telegram
2. Send **`/start`** to see the welcome message
3. Send **`/sms <phone> <message>`** to send an SMS

**Example:**
```
/sms +1234567890 Hello from Jarvis Bot!
```

## 📊 SMS Options Comparison

| Option | Cost | Limit | API Key Required |
|--------|------|-------|------------------|
| **Self-Hosted Textbelt** | Free (+ SMS provider costs) | Unlimited | ❌ No |
| Textbelt Demo (textbelt.com) | Free | 1 SMS/day | ✅ Yes (`textbelt`) |
| Textbelt Paid (textbelt.com) | $0.09/SMS | Pay-as-you-go | ✅ Yes (paid key) |

## 💡 Recommendations

- **For Development/Testing:** Use the self-hosted Textbelt server with a free-tier SMS provider
- **For Production:** Deploy self-hosted Textbelt on a VPS with your preferred SMS gateway (Twilio, etc.)
- **For Quick Testing:** Use the public demo key (limited to 1 SMS per day per number)

## 🐛 Troubleshooting

### SMS not sending?
- Verify your `TEXTBELT_URL` is correct and the server is running
- Check that your `.env` file is properly configured
- Review bot logs for error messages

### Self-hosted server not working?
- Ensure your SMS gateway credentials are properly configured in Textbelt
- Check that port 9090 (or your custom port) is accessible
- Verify your SMS provider account has sufficient credits

### Rate limit errors?
- Switch from public API to self-hosted solution
- If using self-hosted, check your SMS provider's rate limits

### Bot not responding?
- Verify your `BOT_TOKEN` is correct in `.env`
- Check your internet connection
- Ensure the bot is running without errors

## 🔮 Future Enhancements

- 📞 Voice call integration via Fonoster API
- 📧 Email notification support
- 🌐 Multi-language support
- 📊 Usage analytics and reporting
- 🔔 Scheduled messaging capabilities
- 🔐 User authentication and authorization
- 📝 Message templates and bulk sending

## 📚 Resources

- [Textbelt Self-Hosted Server](https://github.com/typpo/textbelt) - Open-source SMS server
- [Textbelt Documentation](https://textbelt.com) - Public API documentation
- [Telegram Bot API](https://core.telegram.org/bots/api) - Bot development guide
- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/) - Library documentation
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management

## 🏗️ Project Structure

```
jarvis-bot/
├── bot/
│   ├── handlers/          # Command handlers (modular organization)
│   ├── __init__.py        # Package initialization
│   ├── config.py          # Configuration management
│   └── main.py            # Main bot application (refactored)
├── .env                   # Environment variables (create this)
├── .github/
│   └── workflows/         # CI/CD workflows
├── LICENSE                # MIT License
├── README.md              # This file
├── SECURITY.md            # Security policy
└── requirements.txt       # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 👤 Author

**Next-Gen-Auto-Bots**
- GitHub: [@Next-Gen-Auto-Bots](https://github.com/Next-Gen-Auto-Bots)

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Note:** This bot is for educational and legitimate communication purposes only. Always comply with local telecommunications laws and regulations when sending SMS messages.
