import os
import logging
from telegram import Update
from telegram.ext import ContextTypes
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Configure logging
logger = logging.getLogger(__name__)

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')


class TwilioCallHandler:
    """Handler for Twilio voice call operations."""
    
    def __init__(self):
        """Initialize Twilio client with credentials."""
        self.client = None
        if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
            try:
                self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                logger.info("Twilio client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Twilio client: {e}")
        else:
            logger.warning("Twilio credentials not configured")
    
    def make_call(self, to_number: str, message: str = None) -> dict:
        """Make an outgoing voice call using Twilio.
        
        Args:
            to_number: The phone number to call (E.164 format: +1234567890)
            message: Optional custom message to play during call
            
        Returns:
            dict: Call status information including call_sid, status, and error if any
        """
        if not self.client:
            return {
                'success': False,
                'error': 'Twilio client not initialized. Please configure TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN.',
                'call_sid': None,
                'status': 'failed'
            }
        
        if not TWILIO_PHONE_NUMBER:
            return {
                'success': False,
                'error': 'TWILIO_PHONE_NUMBER not configured',
                'call_sid': None,
                'status': 'failed'
            }
        
        # Default TwiML message
        default_message = "Hello! This is a test call from Jarvis Bot. Thank you for using our service."
        twiml_message = message or default_message
        
        # Create TwiML response
        twiml = f'<Response><Say voice="alice">{twiml_message}</Say></Response>'
        
        try:
            call = self.client.calls.create(
                to=to_number,
                from_=TWILIO_PHONE_NUMBER,
                twiml=twiml
            )
            
            logger.info(f"Call initiated successfully. SID: {call.sid}")
            return {
                'success': True,
                'call_sid': call.sid,
                'status': call.status,
                'to': to_number,
                'from': TWILIO_PHONE_NUMBER,
                'error': None
            }
            
        except TwilioRestException as e:
            logger.error(f"Twilio API error: {e.msg} (Code: {e.code})")
            return {
                'success': False,
                'error': f"Twilio error: {e.msg}",
                'error_code': e.code,
                'call_sid': None,
                'status': 'failed'
            }
        except Exception as e:
            logger.error(f"Unexpected error during call: {e}")
            return {
                'success': False,
                'error': f"Unexpected error: {str(e)}",
                'call_sid': None,
                'status': 'failed'
            }


# Initialize the handler
twilio_handler = TwilioCallHandler()


async def call(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /call command with Twilio voice call integration.
    
    Usage:
        /call +1234567890
        /call +1234567890 Custom message to play during the call
    
    Args:
        update: Incoming update from Telegram.
        context: Context object for the callback.
    """
    # Parse arguments
    if not context.args:
        await update.message.reply_text(
            "❌ *Usage Error*\n\n"
            "Please provide a phone number to call.\n\n"
            "*Format:*\n"
            "`/call +1234567890`\n"
            "`/call +1234567890 Your custom message`\n\n"
            "*Note:* Phone number must be in E.164 format (e.g., +1234567890)",
            parse_mode='Markdown'
        )
        return
    
    # Extract phone number and optional message
    to_number = context.args[0]
    custom_message = ' '.join(context.args[1:]) if len(context.args) > 1 else None
    
    # Validate phone number format (basic validation)
    if not to_number.startswith('+'):
        await update.message.reply_text(
            "❌ *Invalid Phone Number*\n\n"
            f"The number `{to_number}` is not in valid E.164 format.\n\n"
            "Phone numbers must start with '+' followed by country code and number.\n"
            "Example: +1234567890",
            parse_mode='Markdown'
        )
        return
    
    # Inform user that call is being initiated
    status_message = await update.message.reply_text(
        "📞 *Initiating Call...*\n\n"
        f"*To:* `{to_number}`\n"
        f"*Message:* {custom_message or 'Default greeting'}",
        parse_mode='Markdown'
    )
    
    # Make the call
    result = twilio_handler.make_call(to_number, custom_message)
    
    # Send response based on result
    if result['success']:
        await status_message.edit_text(
            "✅ *Call Initiated Successfully*\n\n"
            f"*To:* `{to_number}`\n"
            f"*From:* `{result['from']}`\n"
            f"*Call SID:* `{result['call_sid']}`\n"
            f"*Status:* `{result['status']}`\n\n"
            "The recipient should receive the call shortly.",
            parse_mode='Markdown'
        )
        logger.info(f"User {update.effective_user.id} initiated call to {to_number}")
    else:
        error_details = f"*Error:* {result['error']}\n"
        if 'error_code' in result:
            error_details += f"*Error Code:* {result['error_code']}\n"
        
        await status_message.edit_text(
            "❌ *Call Failed*\n\n"
            f"{error_details}\n"
            "*Troubleshooting:*\n"
            "• Ensure Twilio credentials are configured\n"
            "• Verify phone number is in E.164 format\n"
            "• Check Twilio account balance and permissions\n"
            "• Verify destination number is valid",
            parse_mode='Markdown'
        )
        logger.error(f"Call failed for user {update.effective_user.id}: {result['error']}")
