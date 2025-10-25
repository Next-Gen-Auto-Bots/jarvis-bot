"""Handler for sending SMS messages via Textbelt API."""
import logging
import requests
from telegram import Update
from telegram.ext import ContextTypes
from bot.config import TEXTBELT_URL, TEXTBELT_KEY

logger = logging.getLogger(__name__)


async def sms(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an SMS message using the Textbelt API.
    
    Args:
        update: Telegram update object
        context: Telegram context object with command arguments
        
    Usage:
        /sms <phone_number> <message>
    """
    try:
        if len(context.args) < 2:
            await update.message.reply_text(
                "Usage: /sms <phone_number> <message>\n"
                "Example: /sms +1234567890 Hello World"
            )
            return

        phone_number = context.args[0]
        message_text = ' '.join(context.args[1:])
        
        logger.info(f"Attempting to send SMS to {phone_number[:4]}****")
        
        try:
            response = requests.post(
                TEXTBELT_URL,
                data={
                    'phone': phone_number,
                    'message': message_text,
                    'key': TEXTBELT_KEY,
                },
                timeout=10  # 10 second timeout
            )
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.Timeout:
            logger.error("Textbelt API request timed out")
            await update.message.reply_text(
                "Error: Request timed out. Please try again later."
            )
            return
        except requests.exceptions.RequestException as e:
            logger.error(f"Textbelt API request failed: {e}")
            await update.message.reply_text(
                "Error: Failed to connect to SMS service. Please try again later."
            )
            return

        logger.info(f"Textbelt response: {result}")

        if result.get('success'):
            await update.message.reply_text("✅ SMS sent successfully!")
        else:
            error_message = result.get('error', 'Unknown error')
            logger.warning(f"Failed to send SMS: {error_message}")
            await update.message.reply_text(
                f"❌ Failed to send SMS: {error_message}"
            )
            
    except Exception as e:
        logger.exception(f"Unexpected error in sms handler: {e}")
        await update.message.reply_text(
            f"❌ Unexpected error: {str(e)}"
        )
