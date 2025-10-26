# Jarvis Bot 🤖

A comprehensive, production-ready Telegram bot featuring advanced voice calling, multi-provider SMS, AI-powered Q&A, and multilingual support with robust architecture and enterprise-grade security.

## ✨ Latest Features & Upgrades

### 🎯 Core Capabilities
- **Voice Calling** 📞: Initiate voice calls with advanced telephony features
- **Multi-Provider SMS** 📱: Support for Textbelt, Twilio, and multiple SMS gateways
- **AI Intent Recognition** 🧠: Intelligent query processing and contextual responses
- **Multilingual Support** 🌍: Localized `/start` command with 15+ language support
- **Advanced Q&A System** ❓: AI-powered question answering with context awareness

### 🏗️ Architecture Enhancements
- **Modular Handler System**: Clean separation of concerns with dedicated handlers
- **Enterprise Security**: Environment-based configuration with zero hardcoded secrets
- **Robust Error Handling**: Comprehensive error recovery and user feedback
- **Professional Logging**: Detailed logging system for monitoring and debugging
- **Scalable Design**: Production-ready architecture for high-load scenarios

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Telegram Bot Token
- API credentials for desired services (SMS, voice calling)

### Installation

```bash
# Clone the repository
git clone https://github.com/Next-Gen-Auto-Bots/jarvis-bot.git
cd jarvis-bot

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API credentials

# Run the bot
python bot/main.py
```

### Environment Configuration

Create a `.env` file with the following variables:

```env
# Required
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# SMS Providers (choose one or multiple)
TEXTBELT_API_KEY=your_textbelt_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number

# Voice Calling
VOICE_API_KEY=your_voice_provider_key
VOICE_API_SECRET=your_voice_provider_secret

# AI Features
OPENAI_API_KEY=your_openai_key
CLAUDE_API_KEY=your_claude_key

# Optional Configurations
LOG_LEVEL=INFO
DEBUG_MODE=false
MAX_MESSAGE_LENGTH=4096
```

## 📋 Commands Reference

### Basic Commands
- **`/start`** — Multilingual welcome with language selection
- **`/help`** — Comprehensive command guide with examples
- **`/status`** — Bot health check and service status
- **`/settings`** — User preferences and configuration

### Communication Features
- **`/sms <phone> <message> [--provider textbelt|twilio]`** — Send SMS with provider selection
- **`/call <phone> [--message "text"] [--duration 30]`** — Initiate voice calls
- **`/voicemail <phone> <message>`** — Leave voice messages

### AI Features
- **`/ask <question>`** — AI-powered question answering
- **`/chat <message>`** — Contextual AI conversation
- **`/intent <text>`** — Analyze user intent and provide responses
- **`/translate <text> [--to language]`** — Multi-language translation

### Administrative
- **`/logs [--lines 50]`** — View recent bot logs (admin only)
- **`/stats`** — Usage statistics and analytics
- **`/config`** — View current configuration (sanitized)

## 🔧 Advanced Usage

### SMS Configuration

#### Using Textbelt (Free Tier Available)
```bash
# Send SMS via Textbelt
/sms +1234567890 "Hello from Jarvis!" --provider textbelt

# Check Textbelt quota
/sms --quota textbelt
```

#### Using Twilio (Production Grade)
```bash
# Send SMS via Twilio
/sms +1234567890 "Production message" --provider twilio

# Send with delivery confirmation
/sms +1234567890 "Important message" --provider twilio --confirm
```

### Voice Calling Features

#### Basic Voice Calls
```bash
# Simple voice call
/call +1234567890

# Call with custom message
/call +1234567890 --message "This is Jarvis calling you"

# Scheduled call
/call +1234567890 --schedule "2023-12-25 10:00" --timezone "UTC"
```

#### Advanced Voice Features
```bash
# Conference call setup
/conference --participants "+1234567890,+0987654321" --duration 60

# Voice broadcast
/broadcast --file voice_message.mp3 --recipients "+1234567890,+0987654321"
```

### AI Integration

#### Intent Recognition
```bash
# Basic intent analysis
/intent "I want to order pizza"
# Response: Intent: ORDER_FOOD, Confidence: 0.95, Entities: ["pizza"]

# Complex query processing
/ask "What's the weather like and should I call my mom?"
# Processes multiple intents and provides contextual responses
```

#### Multilingual Support
The bot automatically detects user language and responds appropriately:
- English, Spanish, French, German, Italian, Portuguese
- Russian, Chinese (Simplified/Traditional), Japanese, Korean
- Arabic, Hindi, Turkish, Dutch, Swedish

### Custom Handlers

Extend the bot with custom handlers:

```python
# bot/handlers/custom_handler.py
from telegram.ext import CommandHandler
from bot.core import get_logger

logger = get_logger(__name__)

async def custom_command(update, context):
    """Custom command implementation"""
    try:
        # Your custom logic here
        await update.message.reply_text("Custom response")
        logger.info(f"Custom command executed by {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Custom command error: {e}")
        await update.message.reply_text("Command failed. Please try again.")

# Register in main.py
application.add_handler(CommandHandler("custom", custom_command))
```

## 🛠️ Troubleshooting

### Common Issues

#### SMS Not Sending
```bash
# Check provider configuration
/config --section sms

# Test provider connectivity
/sms --test textbelt
/sms --test twilio

# View detailed logs
/logs --filter sms --lines 20
```

**Solutions:**
1. Verify API credentials in `.env`
2. Check account balance/quota
3. Ensure phone numbers are in E.164 format (+1234567890)
4. Review rate limiting settings

#### Voice Calls Failing
```bash
# Check voice service status
/status --service voice

# Test voice configuration
/call --test +1234567890
```

**Solutions:**
1. Verify voice API credentials
2. Check supported regions for target number
3. Ensure sufficient account balance
4. Review firewall settings for voice traffic

#### AI Features Not Responding
```bash
# Check AI service status
/status --service ai

# Test API connectivity
/ask --test "Hello"
```

**Solutions:**
1. Verify OpenAI/Claude API keys
2. Check API quota and billing status
3. Review rate limiting configurations
4. Test with simpler queries first

#### Bot Not Starting
```bash
# Check configuration
python -c "from bot.config import validate_config; validate_config()"

# View startup logs
python bot/main.py --debug
```

**Solutions:**
1. Verify all required environment variables
2. Check Python version compatibility (3.8+)
3. Ensure all dependencies are installed
4. Review file permissions

### Performance Optimization

#### High Load Scenarios
- Enable connection pooling for database operations
- Implement message queuing for SMS/voice operations
- Use Redis for caching frequent queries
- Configure load balancing for multiple bot instances

#### Memory Management
```python
# Monitor memory usage
/stats --memory

# Clear cache
/cache --clear

# Restart bot gracefully
/restart --graceful
```

### Error Codes Reference

| Code | Service | Description | Solution |
|------|---------|-------------|-----------|
| E001 | SMS | Invalid phone number | Use E.164 format |
| E002 | SMS | Provider API error | Check credentials |
| E003 | Voice | Call setup failed | Verify voice config |
| E004 | AI | Rate limit exceeded | Wait or upgrade plan |
| E005 | Bot | Configuration error | Check .env file |

## 🏆 Best Practices

### Security
1. **Never commit `.env` files** to version control
2. **Rotate API keys regularly** (monthly recommended)
3. **Use webhook URLs with HTTPS** in production
4. **Implement rate limiting** for user commands
5. **Sanitize all user inputs** before processing
6. **Enable audit logging** for compliance

### Development
1. **Use virtual environments** for dependency isolation
2. **Follow PEP 8** coding standards
3. **Write comprehensive unit tests** for handlers
4. **Document all custom functions** with docstrings
5. **Use type hints** for better code quality
6. **Implement graceful shutdown** handling

### Production Deployment
1. **Use process managers** (systemd, PM2, supervisord)
2. **Configure monitoring** and alerting
3. **Set up log rotation** to prevent disk space issues
4. **Implement health checks** for service monitoring
5. **Use load balancers** for high availability
6. **Regular backups** of configuration and data

### Performance
1. **Monitor response times** for all commands
2. **Implement caching** for frequently accessed data
3. **Use connection pooling** for external APIs
4. **Optimize database queries** with proper indexing
5. **Profile memory usage** regularly
6. **Scale horizontally** when needed

## 📊 Monitoring & Analytics

### Built-in Metrics
```bash
# View usage statistics
/stats --detailed

# Check service health
/health --all-services

# Monitor performance
/performance --last-24h
```

### External Monitoring
Integrate with monitoring platforms:
- **Prometheus + Grafana** for metrics visualization
- **ELK Stack** for log analysis
- **New Relic/DataDog** for APM
- **PagerDuty** for alerting

## 🤝 Contributing

### Development Setup
```bash
# Fork the repository
git clone https://github.com/your-username/jarvis-bot.git
cd jarvis-bot

# Create development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/ -v

# Check code quality
flake8 bot/
black bot/
mypy bot/
```

### Submission Guidelines
1. **Create feature branches** from `main`
2. **Write tests** for new functionality
3. **Update documentation** for changes
4. **Follow commit message conventions**
5. **Ensure CI passes** before submitting PR

## 🆘 Support

### Getting Help
- 📖 **Documentation**: Comprehensive guides and examples
- 🐛 **Issues**: Report bugs or request features on GitHub
- 💬 **Discussions**: Community support and questions
- 📧 **Contact**: Direct support for critical issues

### Community Resources
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Python Telegram Bot Library](https://python-telegram-bot.readthedocs.io/)
- [SMS Provider Documentation](https://textbelt.com/docs) / [Twilio Docs](https://www.twilio.com/docs)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Excellent Telegram Bot API wrapper
- [Textbelt](https://textbelt.com/) - Reliable SMS API service
- [Twilio](https://www.twilio.com/) - Enterprise communication platform
- [OpenAI](https://openai.com/) - AI capabilities integration
- Community contributors and testers

---

**Made with ❤️ by Next-Gen Auto Bots**

*For enterprise support and custom implementations, contact us at: enterprise@nextgenautobots.com*
