import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TEXTBELT_URL = "https://textbelt.com/text"
TEXTBELT_KEY = os.getenv("TEXTBELT_KEY", "textbelt")  # Default to demo key
