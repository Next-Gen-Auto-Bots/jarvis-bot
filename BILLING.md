# Billing & Cost Transparency

## 🆓 Jarvis Bot is Free & Open Source

**Jarvis Bot itself is completely free.** This project is released under the MIT License, which means you can use, modify, and distribute it at no cost.

**There are NO charges from Jarvis Bot.** If you see billing notifications, they are from third-party services you've chosen to use, not from the bot itself.

## 💰 Understanding Potential Costs

While the bot software is free, some **optional features** require third-party services that may charge fees:

### 1. Telegram Bot (Required - FREE)
- **Cost:** FREE
- **Provider:** Telegram
- **Notes:** Telegram bots are completely free with no usage limits
- **Required for:** Core bot functionality

### 2. SMS Services (Optional)

#### Textbelt
- **Cost:** Free tier available (limited messages), paid plans start at ~$10 for 200 messages
- **Provider:** Textbelt
- **Website:** https://textbelt.com
- **Notes:** Default SMS provider, "textbelt" key gives ~10 free test messages
- **You control:** How many messages you send

#### Twilio
- **Cost:** Pay-as-you-go pricing (~$0.0075 per SMS in the US)
- **Provider:** Twilio
- **Website:** https://www.twilio.com/pricing
- **Notes:** Requires account setup, more reliable for production
- **You control:** How many messages/calls you make

### 3. Voice Calls (Optional)
- **Provider:** Twilio
- **Cost:** Pay-as-you-go (~$0.013 per minute in the US)
- **Website:** https://www.twilio.com/pricing/voice
- **You control:** How many calls you make and their duration

### 4. AI Features (Optional)

#### OpenAI
- **Cost:** Pay-per-use (e.g., GPT-3.5-turbo: ~$0.002 per 1K tokens)
- **Provider:** OpenAI
- **Website:** https://openai.com/pricing
- **Notes:** Only charged if you configure and use the API
- **You control:** Whether to enable and how much you use

#### DeepSeek
- **Cost:** Pay-per-use (competitive pricing, often cheaper than OpenAI)
- **Provider:** DeepSeek
- **Website:** https://platform.deepseek.com
- **Notes:** Only charged if you configure and use the API
- **You control:** Whether to enable and how much you use

### 5. GitHub Services (If you fork/host on GitHub)
- **GitHub Actions:** Free tier: 2,000 minutes/month (public repos unlimited)
- **GitHub Storage:** Free tier: 500MB (private repos)
- **GitHub LFS:** Free tier: 1GB storage, 1GB bandwidth/month
- **Website:** https://github.com/pricing

**Note:** The billing message you saw is likely from **GitHub for GitHub services**, not Jarvis Bot.

## 🔒 No Hidden Charges - You Are In Control

### How Charging Works
1. **YOU must create accounts** with third-party services (Twilio, OpenAI, etc.)
2. **YOU must add API keys** to your `.env` file
3. **YOU must execute commands** that use paid services (e.g., `/sms`, `/call`)
4. **Charges come directly from the service provider** you signed up with

### The Bot CANNOT:
- ❌ Charge your credit card
- ❌ Access your payment information
- ❌ Use services you haven't configured
- ❌ Send messages/make calls without your explicit command
- ❌ Make any purchases on your behalf

## 🛡️ How to Avoid Unexpected Charges

### 1. Understand What You're Enabling
- Read the pricing page of any service before adding its API key
- Set up billing alerts in your service provider accounts
- Start with free tiers and demo keys when available

### 2. Use Cost Controls
- **Twilio:** Set account spending limits in your Twilio console
- **OpenAI:** Set monthly usage limits in your OpenAI account
- **GitHub:** Monitor usage in Settings > Billing

### 3. Monitor Your Usage
- Check logs regularly (`logs/requests.json`)
- Use the `/stats` command to see bot usage
- Review service provider dashboards monthly

### 4. Use Free Alternatives
- Use "textbelt" key for testing SMS (limited free messages)
- Skip AI features if cost is a concern (bot works without them)
- Run the bot locally instead of on paid hosting

### 5. Secure Your Keys
- Never commit your `.env` file to Git
- Use environment secrets in CI/CD
- Rotate keys if compromised
- Implement IP restrictions where available

## 📊 GitHub Billing Specifically

### What GitHub Charges For
If you're hosting this bot repository on GitHub, you may be charged for:

1. **Private Repository Features** (if repo is private)
   - Free for public repos
   - GitHub Pro: $4/month for private repos with advanced features

2. **GitHub Actions Minutes** (if using CI/CD)
   - Public repos: Unlimited
   - Private repos: 2,000 free minutes/month, then ~$0.008/minute

3. **GitHub Packages/Storage**
   - Free tier: 500MB
   - Additional storage: ~$0.25/GB/month

4. **GitHub LFS Bandwidth**
   - Free tier: 1GB/month
   - Additional: ~$0.0875/GB

### The Yellow Banner Message

If you saw this message:
> "Your current bill for usage on GitHub is overdue for payment. Please make a payment by November 18, 2025..."

**This is a GitHub billing notice, NOT related to Jarvis Bot.** This means:
- You have GitHub charges for GitHub services (Actions, storage, etc.)
- You need to pay GitHub directly at https://github.com/settings/billing
- This has nothing to do with the Jarvis Bot software

### How to Check Your GitHub Charges
1. Go to: https://github.com/settings/billing
2. Review "Current usage" and "Payment history"
3. Identify what GitHub services are causing charges
4. Adjust your usage or upgrade your plan as needed

## 🆘 If You See Unexpected Charges

### Step 1: Identify the Source
Check these billing dashboards:
- GitHub: https://github.com/settings/billing
- Twilio: https://console.twilio.com/us1/billing
- OpenAI: https://platform.openai.com/account/billing
- DeepSeek: https://platform.deepseek.com/billing
- Textbelt: Check email receipts

### Step 2: Review Usage Logs
- Check `logs/requests.json` for bot activity
- Review service provider usage dashboards
- Look for unexpected command executions

### Step 3: Secure Your Account
- Immediately change all API keys if unauthorized usage is suspected
- Enable two-factor authentication on all services
- Review who has access to your `.env` file or deployment environment

### Step 4: Contact Provider Support
- Each service has support channels for billing disputes
- GitHub Support: https://support.github.com
- Twilio Support: https://support.twilio.com
- OpenAI Support: https://help.openai.com

### Step 5: Disable Services (If Needed)
- Remove API keys from `.env` to immediately stop usage
- Delete or suspend provider accounts
- Stop the bot with `Ctrl+C` or stop your hosting service

## 📞 Getting Help

### For Jarvis Bot Issues
- GitHub Issues: https://github.com/Next-Gen-Auto-Bots/Jarvis-bot/issues
- Include: What service, what command, what you expected vs. what happened

### For Billing/Charge Questions
- **GitHub charges:** https://support.github.com
- **Twilio charges:** https://support.twilio.com
- **OpenAI charges:** https://help.openai.com
- **DeepSeek charges:** https://platform.deepseek.com/support

## 🔑 Summary

✅ **Jarvis Bot is FREE** - MIT License, no cost to use  
✅ **You control all costs** - You must configure and use paid services  
✅ **No hidden charges** - All costs are from services YOU signed up for  
✅ **GitHub billing is separate** - GitHub may charge for their services (Actions, storage, etc.)  
✅ **Stay informed** - Read pricing pages, set limits, monitor usage  

**Remember:** The bot cannot charge you for anything. It only uses services you've explicitly configured with your own API keys.
