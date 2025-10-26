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

### SMS Functionality Upgrade 📱
- **Multi-Provider Support**: Integrated both Textbelt and Twilio SMS providers
- **Provider Selection**: Choose your preferred SMS provider via command-line flag
- **Enhanced Error Handling**: Comprehensive error messages and fallback suggestions
- **Detailed Status Messages**: Real-time feedback with provider-specific information
- **Flexible Configuration**: Easy provider switching with `--provider` flag

## 🚀 Features

- **`/start`** — Welcome message with bot introduction
- **`/sms <phone_number> <message> [--provider textbelt|twilio]`** — Send SMS via multiple providers (Textbelt or Twilio)
  - Example: `/sms +1234567890 Hello World`
  - Example: `/sms +1234567890 Hello World --provider twilio`
  - Example: `/sms +1234567890 Hello World --provider textbelt`
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

### 3. Configure Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Telegram Bot Token (Required)
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# SMS Provider Configuration

# Textbelt (Optional - defaults to demo key)
TEXTBELT_KEY=your_textbelt_api_key  # Use 'textbelt' for testing (limited quota)

# Twilio (Optional - required for Twilio SMS)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number  # E.g., +1234567890
```

**Note**: You can use either Textbelt or Twilio, or configure both for flexibility.

### 4. Run the Bot
```bash
python main.py
```

## 🔧 Configuration Details

### SMS Providers

#### Textbelt (Default)
- **Free tier available** with limited quota
- No signup required for testing
- Set `TEXTBELT_KEY=textbelt` for demo mode
- Obtain API key from [textbelt.com](https://textbelt.com) for production use

#### Twilio
- **Enterprise-grade** SMS delivery
- Requires Twilio account signup
- Configure `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`
- Get credentials from [Twilio Console](https://console.twilio.com)

### Provider Selection

By default, the bot uses **Textbelt** as the SMS provider. You can specify a different provider using the `--provider` flag:

```bash
# Use Textbelt (default)
/sms +1234567890 Hello World

# Explicitly use Textbelt
/sms +1234567890 Hello World --provider textbelt

# Use Twilio
/sms +1234567890 Hello World --provider twilio
```

## 📚 Project Structure

```
jarvis-bot/
├── main.py                 # Bot entry point
├── bot/
│   ├── __init__.py
│   ├── config.py           # Configuration management
│   └── handlers/
│       ├── __init__.py
│       ├── start.py        # /start command handler
│       ├── sms.py          # /sms command handler (multi-provider)
│       └── call.py         # /call command handler
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment configuration
└── README.md              # This file
```

## 🛠️ Usage Examples

### Basic SMS (Default Provider)
```bash
/sms +1234567890 Hello from Jarvis!
```

### SMS with Twilio Provider
```bash
/sms +1234567890 This message is sent via Twilio --provider twilio
```

### SMS with Textbelt Provider
```bash
/sms +1234567890 This message is sent via Textbelt --provider textbelt
```

## 🔐 Security Best Practices

1. **Never commit `.env` file** to version control
2. Use **strong API keys** and rotate them regularly
3. **Restrict bot access** to authorized users only
4. **Monitor API usage** to detect unusual activity
5. **Use environment variables** for all sensitive data

## 🐛 Troubleshooting

### SMS Not Sending

1. **Check API credentials** in `.env` file
2. **Verify phone number format** (must include country code with `+`)
3. **Check API quota/limits** for your provider
4. **Review bot logs** for detailed error messages
5. **Try alternative provider** using `--provider` flag

### Textbelt Issues
- Ensure `TEXTBELT_KEY` is set correctly
- Free tier has limited quota (10 messages)
- Consider upgrading to paid plan for production use

### Twilio Issues
- Verify all three Twilio credentials are set
- Ensure `TWILIO_PHONE_NUMBER` is a valid Twilio number
- Check Twilio account balance and status
- Review Twilio Console for delivery logs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) — Telegram Bot API wrapper
- [Textbelt](https://textbelt.com) — Free SMS API service
- [Twilio](https://www.twilio.com) — Enterprise SMS API service

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.
