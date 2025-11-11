from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from deep_translator import GoogleTranslator
import json
import os

# User language preferences storage (in production, use a database)
USER_LANGUAGES = {}
LANG_FILE = "user_languages.json"

# Load saved user language preferences
if os.path.exists(LANG_FILE):
    try:
        with open(LANG_FILE, 'r') as f:
            USER_LANGUAGES = json.load(f)
    except BaseException:
        pass


def save_user_languages():
    """Save user language preferences to file"""
    try:
        with open(LANG_FILE, 'w') as f:
            json.dump(USER_LANGUAGES, f)
    except BaseException:
        pass


def get_user_language(user_id: int) -> str:
    """Get user's preferred language, default to English"""
    return USER_LANGUAGES.get(str(user_id), 'en')


def translate_text(text: str, target_lang: str) -> str:
    """Translate text to target language"""
    if target_lang == 'en':
        return text
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except BaseException:
        return text  # Return original text if translation fails


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command with multilingual support"""
    user_id = update.effective_user.id
    user_lang = get_user_language(user_id)

    # Base welcome message in English
    welcome_msg = """Welcome to Jarvis Bot!

Commands:
/start - Start the bot
/sms <message> - Send SMS
/call <number> - Make a call (demo only)
/setlang - Set your preferred language

I can communicate in multiple languages! Use /setlang to change your language preference."""

    # Translate the message
    translated_msg = translate_text(welcome_msg, user_lang)

    await update.message.reply_text(translated_msg)


async def setlang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /setlang command for language selection"""
    user_id = update.effective_user.id
    current_lang = get_user_language(user_id)

    # If no language code provided, show available languages
    if not context.args:
        lang_list = """Available Languages:

/setlang en - English
/setlang es - Spanish (Español)
/setlang fr - French (Français)
/setlang de - German (Deutsch)
/setlang it - Italian (Italiano)
/setlang pt - Portuguese (Português)
/setlang ru - Russian (Русский)
/setlang ja - Japanese (日本語)
/setlang ko - Korean (한국어)
/setlang zh-cn - Chinese Simplified (简体中文)
/setlang zh-tw - Chinese Traditional (繁體中文)
/setlang ar - Arabic (العربية)
/setlang hi - Hindi (हिन्दी)
/setlang bn - Bengali (বাংলা)
/setlang tr - Turkish (Türkçe)
/setlang nl - Dutch (Nederlands)
/setlang pl - Polish (Polski)
/setlang uk - Ukrainian (Українська)
/setlang vi - Vietnamese (Tiếng Việt)
/setlang th - Thai (ไทย)

Usage: /setlang <language_code>
Example: /setlang es

Current language: {}""".format(current_lang)

        translated_list = translate_text(lang_list, current_lang)
        await update.message.reply_text(translated_list)
        return

    # Get the language code from arguments
    new_lang = context.args[0].lower()

    # Validate language code (basic validation)
    valid_langs = [
        'en',
        'es',
        'fr',
        'de',
        'it',
        'pt',
        'ru',
        'ja',
        'ko',
        'zh-cn',
        'zh-tw',
        'ar',
        'hi',
        'bn',
        'tr',
        'nl',
        'pl',
        'uk',
        'vi',
        'th']

    if new_lang not in valid_langs:
        error_msg = f"Invalid language code: {new_lang}\nUse /setlang to see available languages."
        translated_error = translate_text(error_msg, current_lang)
        await update.message.reply_text(translated_error)
        return

    # Save the new language preference
    USER_LANGUAGES[str(user_id)] = new_lang
    save_user_languages()

    success_msg = f"Language successfully changed to: {new_lang}\nAll bot messages will now be in your selected language!"
    translated_success = translate_text(success_msg, new_lang)
    await update.message.reply_text(translated_success)

# Export handlers for registration


def register_handlers(application):
    """Register start and setlang handlers"""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setlang", setlang))
