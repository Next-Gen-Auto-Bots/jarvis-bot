"""Handler for sending SMS messages via multiple providers (Textbelt & Twilio)."""
import logging
import requests
from telegram import Update
from telegram.ext import ContextTypes
from bot.config import TEXTBELT_URL, TEXTBELT_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

logger = logging.getLogger(__name__)

# SMS Provider constants
PROVIDER_TEXTBELT = 'textbelt'
PROVIDER_TWILIO = 'twilio'
DEFAULT_PROVIDER = PROVIDER_TEXTBELT


class SMSProvider:
    """Base class for SMS providers."""
    
    def send(self, phone_number: str, message: str) -> dict:
        """Send SMS via provider. Returns dict with success status and message."""
        raise NotImplementedError


class TextbeltProvider(SMSProvider):
    """Textbelt SMS provider implementation."""
    
    def __init__(self, api_key: str = None, api_url: str = None):
        self.api_key = api_key or TEXTBELT_KEY
        self.api_url = api_url or TEXTBELT_URL
    
    def send(self, phone_number: str, message: str) -> dict:
        """Send SMS via Textbelt API."""
        try:
            response = requests.post(
                self.api_url,
                data={
                    'phone': phone_number,
                    'message': message,
                    'key': self.api_key
                },
                timeout=10
            )
            response.raise_for_status()
            result = response.json()
            
            if result.get('success'):
                return {
                    'success': True,
                    'message': f"SMS sent successfully via Textbelt to {phone_number[:4]}****",
                    'quota_remaining': result.get('quotaRemaining'),
                    'text_id': result.get('textId')
                }
            else:
                error_msg = result.get('error', 'Unknown error')
                return {
                    'success': False,
                    'message': f"Textbelt error: {error_msg}"
                }
        except requests.exceptions.Timeout:
            return {'success': False, 'message': 'Textbelt request timed out'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'message': f'Textbelt request failed: {str(e)}'}
        except Exception as e:
            return {'success': False, 'message': f'Textbelt unexpected error: {str(e)}'}


class TwilioProvider(SMSProvider):
    """Twilio SMS provider implementation."""
    
    def __init__(self, account_sid: str = None, auth_token: str = None, from_phone: str = None):
        self.account_sid = account_sid or TWILIO_ACCOUNT_SID
        self.auth_token = auth_token or TWILIO_AUTH_TOKEN
        self.from_phone = from_phone or TWILIO_PHONE_NUMBER
    
    def send(self, phone_number: str, message: str) -> dict:
        """Send SMS via Twilio API."""
        try:
            if not all([self.account_sid, self.auth_token, self.from_phone]):
                return {
                    'success': False,
                    'message': 'Twilio credentials not configured properly'
                }
            
            # Twilio REST API endpoint
            url = f'https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json'
            
            response = requests.post(
                url,
                auth=(self.account_sid, self.auth_token),
                data={
                    'From': self.from_phone,
                    'To': phone_number,
                    'Body': message
                },
                timeout=10
            )
            
            if response.status_code == 201:
                result = response.json()
                return {
                    'success': True,
                    'message': f"SMS sent successfully via Twilio to {phone_number[:4]}****",
                    'sid': result.get('sid'),
                    'status': result.get('status')
                }
            else:
                try:
                    error_data = response.json()
                    error_msg = error_data.get('message', 'Unknown error')
                except:
                    error_msg = f'HTTP {response.status_code}'
                return {
                    'success': False,
                    'message': f"Twilio error: {error_msg}"
                }
        except requests.exceptions.Timeout:
            return {'success': False, 'message': 'Twilio request timed out'}
        except requests.exceptions.RequestException as e:
            return {'success': False, 'message': f'Twilio request failed: {str(e)}'}
        except Exception as e:
            return {'success': False, 'message': f'Twilio unexpected error: {str(e)}'}


def get_provider(provider_name: str) -> SMSProvider:
    """Factory function to get SMS provider instance."""
    providers = {
        PROVIDER_TEXTBELT: TextbeltProvider,
        PROVIDER_TWILIO: TwilioProvider
    }
    
    provider_class = providers.get(provider_name.lower())
    if not provider_class:
        raise ValueError(f"Unknown provider: {provider_name}. Available: {', '.join(providers.keys())}")
    
    return provider_class()


async def sms(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an SMS message using multiple provider options.
    
    Args:
        update: Telegram update object
        context: Telegram context object with command arguments
        
    Usage:
        /sms <phone_number> <message> [--provider textbelt|twilio]
        
    Examples:
        /sms +1234567890 Hello World
        /sms +1234567890 Hello World --provider twilio
        /sms +1234567890 Hello World --provider textbelt
    """
    
    try:
        # Check minimum arguments
        if len(context.args) < 2:
            await update.message.reply_text(
                "❌ Invalid usage\n\n"
                "📱 Usage: /sms <phone_number> <message> [--provider textbelt|twilio]\n\n"
                "📝 Examples:\n"
                "  • /sms +1234567890 Hello World\n"
                "  • /sms +1234567890 Hello World --provider twilio\n"
                "  • /sms +1234567890 Hello World --provider textbelt\n\n"
                "🔧 Available providers: textbelt (default), twilio"
            )
            return
        
        # Parse arguments
        phone_number = context.args[0]
        
        # Check for provider flag
        provider_name = DEFAULT_PROVIDER
        message_args = context.args[1:]
        
        # Look for --provider flag
        if '--provider' in message_args:
            try:
                provider_index = message_args.index('--provider')
                if provider_index + 1 < len(message_args):
                    provider_name = message_args[provider_index + 1]
                    # Remove provider arguments from message
                    message_args = message_args[:provider_index] + message_args[provider_index + 2:]
                else:
                    await update.message.reply_text("❌ --provider flag requires a value (textbelt or twilio)")
                    return
            except ValueError:
                pass  # --provider not found, use default
        
        # Join remaining args as message
        message_text = ' '.join(message_args)
        
        if not message_text.strip():
            await update.message.reply_text("❌ Message cannot be empty")
            return
        
        # Validate phone number format
        if not phone_number.startswith('+'):
            await update.message.reply_text(
                f"⚠️ Warning: Phone number should start with '+' (country code)\n"
                f"Proceeding with: {phone_number}"
            )
        
        logger.info(f"Attempting to send SMS via {provider_name} to {phone_number[:4]}****")
        
        # Send initial processing message
        status_msg = await update.message.reply_text(
            f"📤 Sending SMS via {provider_name.upper()}...\n"
            f"📞 To: {phone_number[:4]}****\n"
            f"📝 Message: {message_text[:50]}{'...' if len(message_text) > 50 else ''}"
        )
        
        # Get provider and send SMS
        try:
            provider = get_provider(provider_name)
        except ValueError as e:
            await status_msg.edit_text(
                f"❌ Error: {str(e)}\n\n"
                f"Please use one of: textbelt, twilio"
            )
            return
        
        # Send the SMS
        result = provider.send(phone_number, message_text)
        
        # Format response based on result
        if result['success']:
            response_text = f"✅ {result['message']}\n\n"
            response_text += f"📱 Provider: {provider_name.upper()}\n"
            response_text += f"📞 To: {phone_number}\n"
            response_text += f"📝 Message: {message_text}\n"
            
            # Add provider-specific info
            if 'quota_remaining' in result and result['quota_remaining'] is not None:
                response_text += f"\n📊 Quota remaining: {result['quota_remaining']}"
            if 'text_id' in result:
                response_text += f"\n🆔 Text ID: {result['text_id']}"
            if 'sid' in result:
                response_text += f"\n🆔 Message SID: {result['sid']}"
            if 'status' in result:
                response_text += f"\n📈 Status: {result['status']}"
            
            await status_msg.edit_text(response_text)
            logger.info(f"SMS sent successfully via {provider_name} to {phone_number[:4]}****")
        else:
            response_text = f"❌ Failed to send SMS\n\n"
            response_text += f"📱 Provider: {provider_name.upper()}\n"
            response_text += f"❗ Error: {result['message']}\n\n"
            response_text += f"💡 Tip: Try using a different provider with --provider flag"
            
            await status_msg.edit_text(response_text)
            logger.error(f"SMS send failed via {provider_name}: {result['message']}")
    
    except Exception as e:
        error_msg = (
            f"❌ Unexpected error occurred\n\n"
            f"Error: {str(e)}\n\n"
            f"Please check your inputs and try again."
        )
        await update.message.reply_text(error_msg)
        logger.error(f"SMS handler error: {str(e)}", exc_info=True)
