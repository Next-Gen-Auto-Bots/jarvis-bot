import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# SMS Provider Configuration
# Textbelt
TEXTBELT_URL = "https://textbelt.com/text"
TEXTBELT_KEY = os.getenv("TEXTBELT_KEY", "textbelt")  # Default to demo key

# Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
