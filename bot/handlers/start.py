from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Welcome to Jarvis Bot!

Commands:
/sms <number> <message>
/call <number> (demo only)"""
    )
