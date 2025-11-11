# Frequently Asked Questions (FAQ)

## 💰 Billing & Costs

### Q: Does Jarvis Bot cost money?
**A:** No! Jarvis Bot is completely free and open-source (MIT License). However, some optional features require third-party services that may charge fees (Twilio, OpenAI, etc.). You control whether to use these services.

### Q: I saw a billing notification - is Jarvis Bot charging me?
**A:** No. Jarvis Bot cannot charge you. If you see billing notifications, they are from:
1. **GitHub** - for GitHub services (Actions, storage, etc.)
2. **Twilio** - if you configured SMS/call services
3. **OpenAI/DeepSeek** - if you configured AI features

See [BILLING.md](BILLING.md) for detailed information.

### Q: Why am I seeing a GitHub billing message?
**A:** GitHub billing is separate from Jarvis Bot. GitHub may charge you for:
- GitHub Actions usage (CI/CD)
- Private repository storage
- GitHub LFS bandwidth
- GitHub Packages storage

Check your GitHub billing at: https://github.com/settings/billing

### Q: How can I avoid unexpected charges?
**A:** 
1. Only configure services you understand and need
2. Set spending limits in service provider accounts (Twilio, OpenAI, etc.)
3. Start with free tiers (e.g., "textbelt" key for testing)
4. Monitor usage logs (`logs/requests.json`)
5. Read [BILLING.md](BILLING.md) for complete cost control strategies

### Q: Can the bot charge my credit card?
**A:** Absolutely not. The bot:
- Has no access to your payment information
- Cannot make purchases on your behalf
- Only uses services YOU configure with YOUR API keys
- Cannot execute commands without your explicit input

## 🔧 Setup & Configuration

### Q: What do I need to run Jarvis Bot?
**A:** Minimum requirements:
1. Python 3.10+
2. Telegram Bot Token (free from @BotFather)
3. That's it for basic functionality!

Optional (for additional features):
- Twilio credentials for SMS/calls
- OpenAI or DeepSeek API key for AI features

### Q: Where do I get a Telegram Bot Token?
**A:**
1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow the prompts to name your bot
4. Copy the token provided
5. Add it to your `.env` file as `TELEGRAM_BOT_TOKEN`

### Q: How do I set up SMS functionality?
**A:** You have two options:

**Option 1: Textbelt (Easier, for testing)**
1. Use `TEXTBELT_KEY=textbelt` in `.env` (gives ~10 free test messages)
2. For production, get a key from https://textbelt.com

**Option 2: Twilio (More reliable, for production)**
1. Sign up at https://www.twilio.com
2. Get your Account SID, Auth Token, and Phone Number
3. Add them to your `.env` file

See [README.md](README.md#environment) for detailed setup.

### Q: Do I need AI features?
**A:** No! AI features (OpenAI, DeepSeek) are completely optional. The bot works perfectly without them for:
- SMS sending (`/sms`)
- Phone calls (`/call`)
- Multi-language support (`/setlang`)
- Basic command handling

AI features add natural language Q&A capabilities.

## 🛡️ Security & Privacy

### Q: Is my data secure?
**A:** Yes. Jarvis Bot follows security best practices:
- No hardcoded secrets
- `.env` file for sensitive credentials (never committed)
- Structured logging with PII redaction
- Zero-trust architecture
- See [SECURITY.md](SECURITY.md) for full details

### Q: What data does the bot collect?
**A:** 
- **Locally logged:** User requests, detected intents, bot responses (in `logs/requests.json`)
- **Not sent anywhere:** All logs stay on your server
- **You control:** You can disable logging or delete log files anytime

### Q: Can others see my messages?
**A:** 
- Messages sent via Telegram: End-to-end encrypted by Telegram
- SMS via Twilio/Textbelt: Subject to provider policies
- Local logs: Only accessible on your server
- **Best practice:** Don't send sensitive information via SMS

### Q: How do I secure my API keys?
**A:**
1. Never commit `.env` file to Git (it's in `.gitignore`)
2. Use environment variables in production
3. Rotate keys periodically
4. Enable two-factor authentication on service accounts
5. Use IP restrictions where available (Twilio, OpenAI)

## 🚀 Usage & Features

### Q: What commands does the bot support?
**A:**
- `/start` - Show welcome message and available commands
- `/sms <phone> <message>` - Send SMS
- `/call <phone>` - Make voice call (demo)
- `/setlang [code]` - Set language preference
- `/ai <question>` - Ask AI a question (if configured)
- `/stats` - View bot usage statistics

### Q: How do I send an SMS?
**A:**
```
/sms +1234567890 Hello, this is a test message
```

You can specify a provider:
```
/sms +1234567890 Hello --provider twilio
/sms +1234567890 Hello --provider textbelt
```

### Q: Can I use the bot in other languages?
**A:** Yes! The bot supports 20+ languages including:
- English, Spanish, French, German, Italian, Portuguese
- Russian, Japanese, Korean, Chinese (Simplified/Traditional)
- Arabic, Hindi, Bengali, Turkish, Dutch, Polish
- Ukrainian, Vietnamese, Thai

Use `/setlang` to see all options and set your preference.

### Q: Why isn't my SMS sending?
**A:** Check these common issues:
1. Is your API key configured in `.env`?
2. Is the phone number in correct format (+1234567890)?
3. Do you have credits/quota with the provider (Textbelt/Twilio)?
4. Check logs for error messages
5. Try the alternative provider with `--provider` flag

### Q: How do I make a phone call?
**A:**
```
/call +1234567890
```

**Note:** This requires Twilio configuration and is a demo feature. Configure your Twilio credentials in `.env` for it to work.

## 🐛 Troubleshooting

### Q: Bot doesn't respond to my commands
**A:**
1. Check if the bot is running (`python bot/main.py`)
2. Verify your `TELEGRAM_BOT_TOKEN` is correct in `.env`
3. Check logs for error messages
4. Ensure you're using `/` prefix for commands (e.g., `/start`)

### Q: "Module not found" errors
**A:**
```bash
pip install -r requirements.txt
```

Make sure all dependencies are installed.

### Q: "Twilio client not initialized" error
**A:** This means Twilio credentials are not configured. Either:
1. Add Twilio credentials to `.env` (for real functionality)
2. Ignore if you don't need call/Twilio SMS features

### Q: AI features not working
**A:**
1. Check if `OPENAI_API_KEY` or `DEEPSEEK_API_KEY` is set in `.env`
2. Verify API keys are valid and have credits
3. Check logs for API error messages
4. The bot will still work without AI - just won't answer general questions

### Q: Getting rate limit errors
**A:**
- **Twilio:** You may have exceeded account limits - check Twilio console
- **OpenAI:** You've hit rate limits - wait or upgrade plan
- **Textbelt:** Free key has strict limits - get a paid key or use Twilio

## 📊 Logs & Monitoring

### Q: Where are the logs?
**A:** 
- `logs/requests.json` - All user requests and responses
- `logs/suggestions.json` - AI-generated improvement suggestions
- Console output - Real-time logging during bot execution

### Q: How do I view statistics?
**A:** Use the `/stats` command in Telegram to see:
- Total requests processed
- Intent distribution
- Suggestions logged

Or directly read `logs/requests.json`.

### Q: Can I disable logging?
**A:** Yes, but it's not recommended for production. To disable:
1. Comment out `log_request()` calls in `bot/main.py`
2. Or implement a config flag to toggle logging

## 🔄 Updates & Maintenance

### Q: How do I update the bot?
**A:**
```bash
git pull origin main
pip install -r requirements.txt
# Restart the bot
python bot/main.py
```

### Q: Is the bot actively maintained?
**A:** Yes! Check the GitHub repository for:
- Latest releases: https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/releases
- Open issues: https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues
- Contribution guidelines in README.md

### Q: Can I contribute?
**A:** Absolutely! We welcome contributions:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request
5. See [README.md](README.md#-contributing) for guidelines

## 🆘 Getting Help

### Q: Where can I get help?
**A:**
- **Bot Issues:** GitHub Issues - https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues
- **Billing Questions:** See [BILLING.md](BILLING.md) for provider-specific support links
- **Security Concerns:** See [SECURITY.md](SECURITY.md) for reporting vulnerabilities
- **General Questions:** GitHub Discussions

### Q: How do I report a bug?
**A:**
1. Check if the issue already exists in GitHub Issues
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Logs (with sensitive data removed)
   - Your environment (OS, Python version)

### Q: How do I request a feature?
**A:**
1. Check GitHub Issues for existing feature requests
2. Create a new issue with "Feature Request" label
3. Describe the feature, use case, and benefits
4. Be open to discussion and alternative implementations

## 📜 Licensing

### Q: Can I use this bot commercially?
**A:** Yes! Jarvis Bot is released under the MIT License, which allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

Just include the original license and copyright notice.

### Q: Can I sell this bot?
**A:** Yes, the MIT License permits commercial use. However:
- You must include the original MIT license
- You cannot claim sole authorship
- Consider contributing improvements back to the community

### Q: Do I need to credit the authors?
**A:** The MIT License requires you to include the license and copyright notice, but you don't need to actively credit the authors in your product (though it's appreciated!).

---

## 📚 Additional Resources

- [README.md](README.md) - Project overview and quick start
- [BILLING.md](BILLING.md) - Comprehensive billing and cost information
- [SECURITY.md](SECURITY.md) - Security policy and best practices
- [LICENSE](LICENSE) - MIT License full text

**Still have questions?** Open a GitHub Discussion or Issue!
