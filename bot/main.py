import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from bot.config import TOKEN
from bot.handlers.call import call
from bot.handlers.sms import sms
from bot.handlers.start import start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def run():
    """Initialize and run the Telegram bot."""
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # Register command handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("sms", sms))
        app.add_handler(CommandHandler("call", call))
        
        logger.info("Bot started successfully")
        app.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise


if __name__ == "__main__":
    run()
