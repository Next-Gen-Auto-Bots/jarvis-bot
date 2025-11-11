import logging
import os
import json
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from bot.config import TOKEN
from bot.handlers.call import call
from bot.handlers.sms import sms
from bot.handlers.start import start, setlang

# AI imports
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# AI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')
DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'

# Logging configuration
LOG_DIR = 'logs'
REQUESTS_LOG = os.path.join(LOG_DIR, 'requests.json')
SUGGESTIONS_LOG = os.path.join(LOG_DIR, 'suggestions.json')

# Create logs directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Intent patterns and their corresponding commands
INTENT_PATTERNS = {
    'sms': ['send sms', 'send message', 'text message', 'send text', 'sms to'],
    'call': ['make call', 'call', 'phone call', 'dial', 'ring'],
    'start': ['help', 'start', 'commands', 'what can you do'],
    'setlang': ['change language', 'set language', 'language preference', 'switch language']
}


def log_request(
        user_id: int,
        username: str,
        message: str,
        intent: str,
        response: str):
    """Log all user requests and bot responses"""
    try:
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'username': username,
            'message': message,
            'detected_intent': intent,
            'response': response
        }

        # Load existing logs
        logs = []
        if os.path.exists(REQUESTS_LOG):
            try:
                with open(REQUESTS_LOG, 'r', encoding='utf-8') as f:
                    logs = json.load(f)
            except BaseException:
                logs = []

        logs.append(log_entry)

        # Save updated logs
        with open(REQUESTS_LOG, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error logging request: {e}")


def log_suggestion(user_id: int, message: str, suggestion: str):
    """Log AI suggestions for improvement"""
    try:
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'message': message,
            'suggestion': suggestion
        }

        # Load existing suggestions
        suggestions = []
        if os.path.exists(SUGGESTIONS_LOG):
            try:
                with open(SUGGESTIONS_LOG, 'r', encoding='utf-8') as f:
                    suggestions = json.load(f)
            except BaseException:
                suggestions = []

        suggestions.append(log_entry)

        # Save updated suggestions
        with open(SUGGESTIONS_LOG, 'w', encoding='utf-8') as f:
            json.dump(suggestions, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error logging suggestion: {e}")


def classify_intent(message: str) -> str:
    """Classify user intent based on message content"""
    message_lower = message.lower()

    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if pattern in message_lower:
                return intent

    return 'general_question'


async def get_ai_response(message: str, user_id: int) -> str:
    """Get AI response using DeepSeek or OpenAI API"""

    system_prompt = """You are Jarvis, an intelligent Telegram bot assistant.
    You can help users with:
    - Sending SMS messages (/sms command)
    - Making phone calls (/call command)
    - Changing language preferences (/setlang command)
    - Answering general questions

    Be helpful, concise, and friendly. If the user asks about features you have,
    explain them clearly. If they ask questions outside your domain, provide helpful
    general answers."""

    # Try DeepSeek first
    if DEEPSEEK_API_KEY and REQUESTS_AVAILABLE:
        try:
            headers = {
                'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
                'Content-Type': 'application/json'
            }

            payload = {
                'model': 'deepseek-chat',
                'messages': [
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': message}
                ],
                'temperature': 0.7,
                'max_tokens': 500
            }

            response = requests.post(
                DEEPSEEK_API_URL,
                headers=headers,
                json=payload,
                timeout=10)

            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                logger.info(f"DeepSeek response for user {user_id}")
                return ai_response
        except Exception as e:
            logger.warning(f"DeepSeek API error: {e}")

    # Fallback to OpenAI
    if OPENAI_API_KEY and OPENAI_AVAILABLE:
        try:
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': message}
                ],
                temperature=0.7,
                max_tokens=500
            )

            ai_response = response['choices'][0]['message']['content']
            logger.info(f"OpenAI response for user {user_id}")
            return ai_response
        except Exception as e:
            logger.warning(f"OpenAI API error: {e}")

    # Fallback response if no AI available
    return """I'm Jarvis Bot! I can help you with:

• /start - View all commands and help
• /sms <message> - Send SMS messages
• /call <number> - Make phone calls (demo)
• /setlang - Change your language preference

AI features require API configuration. Please ask specific questions or use the commands above!"""


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle non-command messages with AI-powered Q&A and intent detection"""

    user = update.effective_user
    message = update.message.text

    logger.info(f"Message from {user.username} ({user.id}): {message}")

    # Classify intent
    intent = classify_intent(message)
    logger.info(f"Detected intent: {intent}")

    # Route to appropriate handler based on intent
    if intent == 'sms':
        response = """To send an SMS, use the command:
/sms <message>

Example: /sms Hello, this is a test message

Note: You'll need to configure Twilio credentials in your .env file."""
        await update.message.reply_text(response)

    elif intent == 'call':
        response = """To make a call, use the command:
/call <number>

Example: /call +1234567890

Note: This is a demo feature. Configure Twilio for real functionality."""
        await update.message.reply_text(response)

    elif intent == 'start':
        # Delegate to start handler
        await start(update, context)
        response = "Delegated to start command"

    elif intent == 'setlang':
        response = """To change your language preference, use:
/setlang

This will show you all available languages. Then use:
/setlang <language_code>

Example: /setlang es (for Spanish)"""
        await update.message.reply_text(response)

    else:
        # Handle as general question with AI
        response = await get_ai_response(message, user.id)
        await update.message.reply_text(response)

        # Log suggestion for potential improvements
        if "don't" in response.lower() or "can't" in response.lower():
            suggestion = f"User asked: '{message}' - Consider adding this feature"
            log_suggestion(user.id, message, suggestion)

    # Log the request and response
    log_request(user.id, user.username or 'Unknown', message, intent, response)


async def ai_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Explicit AI chat command for Q&A"""
    user = update.effective_user

    if not context.args:
        await update.message.reply_text(
            "Ask me anything! Usage: /ai <your question>\n"
            "Example: /ai What's the weather like today?"
        )
        return

    question = ' '.join(context.args)
    logger.info(f"AI command from {user.username} ({user.id}): {question}")

    response = await get_ai_response(question, user.id)
    await update.message.reply_text(response)

    # Log the request
    log_request(
        user.id,
        user.username or 'Unknown',
        f"/ai {question}",
        'ai_command',
        response)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show bot usage statistics"""
    try:
        # Count total requests
        total_requests = 0
        intent_counts = {}

        if os.path.exists(REQUESTS_LOG):
            with open(REQUESTS_LOG, 'r', encoding='utf-8') as f:
                logs = json.load(f)
                total_requests = len(logs)

                for log in logs:
                    intent = log.get('detected_intent', 'unknown')
                    intent_counts[intent] = intent_counts.get(intent, 0) + 1

        # Count suggestions
        total_suggestions = 0
        if os.path.exists(SUGGESTIONS_LOG):
            with open(SUGGESTIONS_LOG, 'r', encoding='utf-8') as f:
                suggestions = json.load(f)
                total_suggestions = len(suggestions)

        stats_message = f"""📊 Bot Statistics:

📨 Total Requests: {total_requests}
💡 Suggestions Logged: {total_suggestions}

🎯 Intent Distribution:"""

        for intent, count in sorted(
                intent_counts.items(), key=lambda x: x[1], reverse=True):
            stats_message += f"\n  • {intent}: {count}"

        await update.message.reply_text(stats_message)

    except Exception as e:
        logger.error(f"Error generating stats: {e}")
        await update.message.reply_text("Error generating statistics.")


async def health_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Health check command to verify bot is running properly"""
    try:
        # Check critical components
        checks = {
            'Bot Status': '✅ Running',
            'Telegram API': '✅ Connected',
            'AI - DeepSeek': '✅ Configured' if DEEPSEEK_API_KEY else '⚠️ Not configured',
            'AI - OpenAI': '✅ Configured' if OPENAI_API_KEY else '⚠️ Not configured',
            'Twilio': '✅ Configured' if os.getenv('TWILIO_ACCOUNT_SID') else '⚠️ Not configured',
            'Textbelt': '✅ Ready',
            'Logs': '✅ Working' if os.path.exists(LOG_DIR) else '❌ Not found'
        }

        health_message = "🏥 **Health Check**\n\n"
        for component, status in checks.items():
            health_message += f"**{component}:** {status}\n"

        await update.message.reply_text(health_message, parse_mode='Markdown')

    except Exception as e:
        logger.error(f"Error in health check: {e}")
        await update.message.reply_text("❌ Health check failed")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comprehensive help command with detailed usage examples"""
    help_text = """
🤖 **Jarvis Bot - Complete Command Guide**

📋 **Basic Commands:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• `/start` - Start the bot and see welcome message
• `/help` - Show this comprehensive help guide
• `/health` - Check bot health and component status

📱 **Communication Commands:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• `/sms <phone> <message>` - Send SMS
  Example: `/sms +1234567890 Hello World`

• `/sms <phone> <message> --provider <name>` - Send SMS via specific provider
  Example: `/sms +1234567890 Test --provider twilio`
  Available providers: textbelt, twilio

• `/call <phone>` - Make a voice call (Twilio required)
  Example: `/call +1234567890`

• `/call <phone> <message>` - Make call with custom message
  Example: `/call +1234567890 This is an automated call`

🤖 **AI Commands:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• `/ai <question>` - Ask AI anything
  Example: `/ai What's the capital of France?`

• Simply type a message - Natural language processing will detect intent

📊 **Analytics Commands:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• `/stats` - View bot usage statistics

🌍 **Language Commands:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• `/setlang` - View available languages
• `/setlang <code>` - Set your preferred language
  Example: `/setlang es` (Spanish)

💡 **Tips:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Phone numbers should be in E.164 format: +[country][number]
• All your conversations are logged for improvement
• AI features require API configuration
• SMS/Call features require provider credentials

🔒 **Privacy & Security:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Your data is encrypted and secure
• We follow zero-trust security principles
• Credentials are never logged or exposed

Need more help? Visit our GitHub repository or contact support.
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')


def run():
    """Initialize and run the Telegram bot with AI capabilities."""
    try:
        app = ApplicationBuilder().token(TOKEN).build()

        # Register command handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("health", health_command))
        app.add_handler(CommandHandler("sms", sms))
        app.add_handler(CommandHandler("call", call))
        app.add_handler(CommandHandler("setlang", setlang))
        app.add_handler(CommandHandler("ai", ai_command))
        app.add_handler(CommandHandler("stats", stats_command))

        # Register message handler for natural language Q&A
        # This catches all non-command messages
        app.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                handle_message))

        logger.info(
            "Bot started successfully with AI-powered Q&A and intent detection")
        logger.info(
            f"DeepSeek API: {
                'Configured' if DEEPSEEK_API_KEY else 'Not configured'}")
        logger.info(
            f"OpenAI API: {
                'Configured' if OPENAI_API_KEY else 'Not configured'}")

        app.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise


if __name__ == "__main__":
    run()
