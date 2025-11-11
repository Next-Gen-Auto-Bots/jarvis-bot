<div align="center">

# 🤖 Jarvis Bot

### Your Enterprise-Grade Telegram Automation Assistant

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)](https://telegram.org/)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

**Production-tuned • Security-first • AI-powered • Privacy-focused**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing) • [Security](#-security)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Commands Reference](#-commands-reference)
- [Development](#-development)
- [Testing](#-testing)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Jarvis Bot** is a production-tuned, security-first automation assistant for Telegram that delivers:
- 🚀 Ultra-fast CI/CD guardrails with pre-merge policy checks
- 🔒 Least-privilege orchestration and automated secret rotation
- 📱 Multi-provider communications (SMS, Voice) with intelligent failover
- 🤖 AI-powered natural language understanding and intent detection
- 🛡️ Enterprise-grade security with zero-trust architecture
- 🌍 Privacy-first design with decentralized network support

Built for regulated teams, audited environments, and high-velocity DevOps workflows, Jarvis Bot combines enterprise reliability with developer-friendly simplicity.

---

## ✨ Features

### 🎯 Core Capabilities

#### 📞 Multi-Channel Communications
- **SMS Messaging**: Send SMS via Textbelt or Twilio with automatic failover
- **Voice Calls**: Initiate phone calls with custom messages (Twilio)
- **Provider Flexibility**: Switch between providers on-the-fly with `--provider` flag
- **Smart Routing**: Automatic retry and fallback mechanisms

#### 🤖 AI-Powered Intelligence
- **Natural Language Processing**: Understand user intent from plain text
- **Multi-Provider AI**: Support for OpenAI GPT and DeepSeek models
- **Intent Detection**: Automatically route requests to appropriate handlers
- **Contextual Q&A**: Answer questions with AI-powered responses
- **Learning System**: Log suggestions for continuous improvement

#### 🌍 Multilingual Support
- **20+ Languages**: Full translation support for global teams
- **User Preferences**: Save language settings per user
- **Auto-Translation**: All bot messages translated to user's language
- **Language Detection**: Smart language identification

#### 📊 Analytics & Monitoring
- **Usage Statistics**: Track requests, intents, and patterns
- **Health Checks**: Monitor component status and API connectivity
- **Structured Logging**: JSON logs with correlation IDs for SIEMs
- **Request History**: Complete audit trail of all interactions

### 🔒 Decentralized & Private Network Power

**Privacy-first communications that can't be censored, intercepted, or shut down.**

Jarvis Bot harnesses the full power of decentralized networks to deliver ultra-private, censorship-resistant communications:

- **🧅 Tor Network Integration**: Route communications through Tor with military-grade onion routing
- **🔗 Matrix Protocol Support**: Federated, end-to-end encrypted messaging via Matrix/Element
- **🛡️ Multi-Layer Encryption**: 
  - End-to-end encrypted messaging with perfect forward secrecy
  - Tor-routed traffic with triple-layer onion encryption
  - Ephemeral sessions with automatic key rotation
  - Zero-knowledge architecture
- **🌍 Censorship Resistance**:
  - Tor hidden services for private bot access
  - Matrix federation for global reach without single points of failure
  - Works in heavily censored networks

**This isn't just privacy—this is digital sovereignty.**

### 🔐 Enterprise Security

Security isn't a feature—it's the architecture:

- ✅ **Zero-Trust Posture**: Default-deny policies and explicit allowlists
- ✅ **Least Privilege**: Granular RBAC for commands, handlers, and integrations
- ✅ **Secret Management**: No hardcoded secrets, .env templating, vault integration
- ✅ **Audit Trail**: Immutable structured logs with correlation IDs
- ✅ **Compliance Ready**: SOC 2, ISO 27001, HIPAA-ready patterns
- ✅ **Threat Modeling**: Protection against SSRF, injection, and abuse
- ✅ **Dependency Security**: Regular security audits with pip-audit and Bandit

### 🛠️ CI/CD & DevOps

- ⚡ Protected branches with required security checks
- ⚡ Automated code scanning and dependency audits
- ⚡ Environment promotions via signed releases
- ⚡ Drift detection and automated canaries
- ⚡ Health endpoints for orchestrators

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Telegram API                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Bot Application Layer                      │
│  ┌────────────┐  ┌────────────┐  ┌─────────────┐       │
│  │   Router   │─▶│  Handlers  │─▶│  Providers  │       │
│  └────────────┘  └────────────┘  └─────────────┘       │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┬──────────────┐
        ▼            ▼            ▼              ▼
   ┌────────┐  ┌─────────┐  ┌─────────┐   ┌──────────┐
   │ OpenAI │  │DeepSeek │  │ Twilio  │   │Textbelt  │
   └────────┘  └─────────┘  └─────────┘   └──────────┘
```

**Key Components:**

- **Router**: Intent detection and command routing
- **Handlers**: Command processors (SMS, Call, Start, AI, etc.)
- **Providers**: External API integrations (SMS, AI, Voice)
- **Logger**: Structured logging with audit trails
- **Translator**: Multi-language support engine

**Design Principles:**

- 🔹 Modular handlers with clean boundaries
- 🔹 Dependency inversion for testability
- 🔹 Resilience layer (retries, backoff, circuit breakers)
- 🔹 Horizontal scalability (stateless workers)
- 🔹 Cloud-native (containers, serverless-ready)

---

## 💰 Cost & Billing Transparency

**Jarvis Bot is 100% FREE and open-source (MIT License).** There are NO charges from the bot itself.

However, some **optional features** use third-party services that may charge fees:
- **Telegram:** FREE (required for core functionality)
- **SMS (Textbelt):** Free tier available, paid plans ~$10 for 200 messages (optional)
- **SMS/Calls (Twilio):** Pay-as-you-go pricing, ~$0.0075 per SMS (optional)
- **AI (OpenAI/DeepSeek):** Pay-per-use, only if you configure them (optional)

**You control all costs.** The bot only uses services YOU configure with YOUR API keys. See [BILLING.md](BILLING.md) for complete cost transparency and how to avoid unexpected charges.

**Important:** If you see GitHub billing notifications, those are from GitHub services (Actions, storage, etc.), not Jarvis Bot. See [FAQ.md](FAQ.md#q-why-am-i-seeing-a-github-billing-message) for details.

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** (Python 3.12 recommended)
- **Telegram Bot Token** (from [@BotFather](https://t.me/botfather))
- **Optional**: Twilio/Textbelt credentials for SMS/Voice
- **Optional**: OpenAI/DeepSeek API keys for AI features

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Next-Gen-Auto-Bots/Jarvis-bot.git
cd Jarvis-bot
```

#### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your credentials
nano .env  # or use your preferred editor
```

**Minimum required configuration:**
```env
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
```

#### 5. Run the Bot

```bash
python bot/main.py
```

You should see:
```
INFO - Bot started successfully with AI-powered Q&A and intent detection
INFO - DeepSeek API: Not configured
INFO - OpenAI API: Not configured
```

🎉 **Your bot is now running!** Open Telegram and send `/start` to your bot.

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with your credentials:

#### 🔑 Required Configuration

```env
# Telegram Bot Token (REQUIRED)
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

#### 📱 SMS Provider Configuration (Optional)

**Textbelt** (Easy setup, limited free tier):
```env
TEXTBELT_KEY=textbelt  # Use 'textbelt' for testing (limited messages)
```

**Twilio** (Enterprise-grade, requires account):
```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

#### 🤖 AI Provider Configuration (Optional)

**OpenAI**:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**DeepSeek** (Cost-effective alternative):
```env
DEEPSEEK_API_KEY=your_deepseek_api_key
```

### 🔒 Security Best Practices

⚠️ **NEVER commit your `.env` file to version control!**

- ✅ Use `.env.example` as a template
- ✅ Keep API keys in secure vaults (AWS Secrets Manager, HashiCorp Vault)
- ✅ Rotate secrets regularly
- ✅ Use different credentials for dev/staging/production
- ✅ Enable 2FA on all provider accounts

---

## 💡 Usage Examples

### Basic Commands

#### Start the Bot
```
/start
```
Displays welcome message and available commands in your preferred language.

#### Get Help
```
/help
```
Shows comprehensive command guide with examples.

#### Check Health Status
```
/health
```
Displays bot status and configured components.

### 📱 Sending SMS

#### Simple SMS (Textbelt - Default)
```
/sms +1234567890 Hello from Jarvis Bot!
```

#### SMS via Specific Provider
```
/sms +1234567890 Important message --provider twilio
```

#### SMS Best Practices
- Always use E.164 format: `+[country code][number]`
- Example: `+14155552671` (US number)
- Textbelt: Free tier limited to ~10 messages
- Twilio: Requires paid account but more reliable

### 📞 Making Calls

#### Simple Call
```
/call +1234567890
```
Plays default greeting message.

#### Call with Custom Message
```
/call +1234567890 This is an automated reminder about your appointment
```

**Note**: Voice calls require Twilio configuration.

### 🤖 AI Interactions

#### Ask AI Directly
```
/ai What's the weather like in San Francisco?
/ai Explain quantum computing in simple terms
/ai How do I configure environment variables?
```

#### Natural Language (Auto-Intent Detection)
Simply type a message without a command:
```
How do I send an SMS?
What can you help me with?
Tell me about your features
```

The bot will detect your intent and respond appropriately!

### 🌍 Language Settings

#### View Available Languages
```
/setlang
```

#### Set Your Language
```
/setlang es    # Spanish
/setlang fr    # French
/setlang ja    # Japanese
/setlang zh-cn # Chinese (Simplified)
```

**Supported Languages**: English, Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese (Simplified & Traditional), Arabic, Hindi, Bengali, Turkish, Dutch, Polish, Ukrainian, Vietnamese, Thai

### 📊 View Statistics
```
/stats
```
Shows:
- Total requests processed
- Intent distribution
- Suggestions logged

---

## 📚 Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Start bot and show welcome | `/start` |
| `/help` | Show comprehensive help | `/help` |
| `/health` | Check system health | `/health` |
| `/sms <phone> <message>` | Send SMS | `/sms +1234567890 Hello` |
| `/sms <phone> <message> --provider <name>` | Send SMS via provider | `/sms +123 Test --provider twilio` |
| `/call <phone> [message]` | Make voice call | `/call +1234567890` |
| `/ai <question>` | Ask AI anything | `/ai What is Python?` |
| `/stats` | View usage statistics | `/stats` |
| `/setlang [code]` | Set/view language | `/setlang es` |

---

## 🛠️ Development

### Project Structure

```
Jarvis-bot/
├── bot/
│   ├── __init__.py
│   ├── main.py              # Main bot application
│   ├── config.py            # Configuration loader
│   └── handlers/
│       ├── __init__.py
│       ├── start.py         # Start & language handlers
│       ├── sms.py           # SMS functionality
│       └── call.py          # Voice call functionality
├── .github/
│   └── workflows/           # CI/CD pipelines
├── logs/                    # Runtime logs (gitignored)
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

### Setting Up Development Environment

```bash
# Clone and navigate
git clone https://github.com/Next-Gen-Auto-Bots/Jarvis-bot.git
cd Jarvis-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies including dev tools
pip install -r requirements.txt
pip install pylint flake8 black pytest autopep8

# Set up pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

### Code Quality Tools

#### Linting
```bash
# Check with flake8
flake8 bot/ --max-line-length=127 --statistics

# Check with pylint
pylint bot/**/*.py
```

#### Auto-formatting
```bash
# Format with black
black bot/

# Or use autopep8
autopep8 --in-place --aggressive --aggressive bot/**/*.py
```

#### Security Scanning
```bash
# Check dependencies for vulnerabilities
pip install pip-audit
pip-audit

# Scan code for security issues
pip install bandit
bandit -r bot/
```

### Adding New Features

1. **Create a new handler** in `bot/handlers/`
2. **Register the handler** in `bot/main.py`
3. **Add tests** (when test infrastructure is ready)
4. **Update documentation** (README, .env.example)
5. **Run linters** and fix any issues
6. **Submit a PR** with clear description

---

## 🧪 Testing

### Current Status

⚠️ **Test infrastructure is being developed.** Currently, the repository uses manual testing and CI linting.

### Running Basic Checks

```bash
# Syntax check
python -m py_compile bot/main.py bot/handlers/*.py

# Lint check
flake8 bot/ --select=E9,F63,F7,F82 --show-source

# Import check
python -c "from bot.main import run; print('✓ Imports OK')"
```

### Manual Testing Checklist

- [ ] Bot starts without errors
- [ ] `/start` command works
- [ ] `/help` command displays correctly
- [ ] `/health` shows component status
- [ ] SMS sending works (if configured)
- [ ] Voice calls work (if configured)
- [ ] AI commands respond (if configured)
- [ ] Language switching works
- [ ] Statistics tracking works

---

## 🔒 Security

### Security Features

- ✅ **No Hardcoded Secrets**: All credentials via environment variables
- ✅ **Input Validation**: Phone numbers, commands, and messages validated
- ✅ **Structured Logging**: Security events logged for SIEM integration
- ✅ **Error Handling**: Safe error messages without information disclosure
- ✅ **Dependencies**: Regular security audits with pip-audit
- ✅ **Code Scanning**: Automated CodeQL and Bandit scans

### Security Best Practices

#### 🔐 Credential Management
- Store credentials in `.env` (never commit)
- Use environment-specific secrets (dev/staging/prod)
- Rotate API keys regularly
- Use read-only tokens where possible

#### 🛡️ Access Control
- Limit bot permissions to required scopes
- Monitor unusual activity patterns
- Implement rate limiting in production
- Log all security-relevant events

#### 📊 Monitoring & Auditing
- Review `logs/requests.json` regularly
- Monitor for suspicious patterns
- Set up alerts for failures
- Audit access to credentials

### Reporting Security Issues

🔒 **Please do NOT open public issues for security vulnerabilities.**

Email security concerns to: **enterprise@nextgenautobots.com**

We take security seriously and will respond promptly.

---

## ❓ Troubleshooting

### Common Issues

#### Bot doesn't start

**Problem**: `telegram.error.InvalidToken`
```
Solution: Check TELEGRAM_BOT_TOKEN in .env file
- Verify token from @BotFather
- Ensure no extra spaces or quotes
- Token format: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

**Problem**: `ModuleNotFoundError: No module named 'telegram'`
```bash
Solution: Install dependencies
pip install -r requirements.txt
```

#### SMS not sending

**Problem**: SMS fails with Textbelt quota error
```
Solution: 
- Free 'textbelt' key limited to ~10 messages
- Get paid key from https://textbelt.com
- Or switch to Twilio: /sms +123 message --provider twilio
```

**Problem**: Twilio authentication error
```
Solution: Verify in .env:
- TWILIO_ACCOUNT_SID (starts with AC)
- TWILIO_AUTH_TOKEN
- TWILIO_PHONE_NUMBER (E.164 format: +1234567890)
```

#### AI not responding

**Problem**: AI returns fallback message
```
Solution: Configure AI provider in .env:
- OPENAI_API_KEY or DEEPSEEK_API_KEY
- Verify API key is valid
- Check account has credits/quota
```

#### Voice calls not working

**Problem**: Call fails immediately
```
Solution:
- Voice calls require Twilio only
- Verify Twilio credentials in .env
- Ensure phone number is E.164 format (+1234567890)
- Check Twilio account balance
```

#### Language translation issues

**Problem**: Translation doesn't work
```
Solution:
- googletrans uses Google Translate (free, rate-limited)
- If rate-limited, wait a few minutes
- Restart bot to reset connection
```

### Debug Mode

Enable detailed logging:

```python
# In bot/main.py, change logging level:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Change from INFO to DEBUG
)
```

### Getting Help

1. **Check this README** - Most answers are here
2. **Review logs** - Check `logs/` directory
3. **GitHub Issues** - Search existing issues
4. **Discussions** - Community Q&A
5. **Email Support** - enterprise@nextgenautobots.com

---

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug fixes, new features, or documentation improvements, your help makes Jarvis Bot better.

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Jarvis-bot.git
   cd Jarvis-bot
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   # Run linters
   flake8 bot/
   pylint bot/**/*.py
   
   # Test the bot
   python bot/main.py
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Amazing new feature"
   ```
   
   Use conventional commits:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for changes to existing features
   - `Docs:` for documentation only
   - `Refactor:` for code refactoring

6. **Push and Create PR**
   ```bash
   git push origin feature/amazing-feature
   ```
   Then open a Pull Request on GitHub.

### Contribution Guidelines

- ✅ Follow PEP 8 style guide
- ✅ Add docstrings to functions and classes
- ✅ Keep functions focused and small
- ✅ Update README for new features
- ✅ Ensure all CI checks pass
- ✅ Be respectful and constructive

### Development Focus Areas

We're particularly interested in:
- 🧪 **Test Infrastructure**: Help build comprehensive test suite
- 📚 **Documentation**: Tutorials, guides, and examples
- 🌍 **Internationalization**: Additional language support
- 🔌 **Integrations**: New provider support (Discord, Slack, etc.)
- 🛡️ **Security**: Enhanced security features
- 🎨 **UI/UX**: Better user interactions

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Next-Gen Auto Bots

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **python-telegram-bot** - Excellent Telegram Bot API wrapper
- **Twilio** - Reliable communications platform
- **OpenAI & DeepSeek** - AI language models
- **Google Translate** - Translation services
- **Contributors** - Everyone who helps improve this project

---

## 📞 Support & Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues)
- **GitHub Discussions**: [Community Q&A and design proposals](https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/discussions)
- **Email**: enterprise@nextgenautobots.com
- **Website**: [nextgenautobots.com](https://nextgenautobots.com)

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=Next-Gen-Auto-Bots/Jarvis-bot&type=Date)](https://star-history.com/#Next-Gen-Auto-Bots/Jarvis-bot&Date)

---

## 📚 Documentation

- **[README.md](README.md)** - You are here! Project overview and quick start
- **[BILLING.md](BILLING.md)** - Complete cost transparency and billing information
- **[FAQ.md](FAQ.md)** - Frequently asked questions about setup, usage, billing, and security
- **[SECURITY.md](SECURITY.md)** - Security policy, best practices, and vulnerability reporting
- **[LICENSE](LICENSE)** - MIT License full text

## 🆘 Support
<div align="center">

**Built with ❤️ by Next-Gen Auto Bots**

*Secure speed, without compromise.*

[⬆ Back to Top](#-jarvis-bot)

</div>
