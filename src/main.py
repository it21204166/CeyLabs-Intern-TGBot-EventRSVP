# src/main.py
from typing import Final
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json
import os
import logging
from utils.event_info import get_event_info
from utils.registration import register_user, get_user_by_email
from utils.group_invitation import invite_user_to_group

# Load config
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
with open(CONFIG_PATH, 'r') as file:
    config = json.load(file)

TOKEN: Final = config['BOT_TOKEN']
BOT_USERNAME: Final = '@ceylabs_tg_bot'
GROUP_ID: Final = config['GROUP_ID']
GROUP_INVITE_LINK: Final = config['GROUP_INVITE_LINK']

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(get_event_info())
    except Exception as e:
        logger.error(f"Error in start_command: {e}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Commands:\n/start - Get event details\n/register - Register for tickets\n/help - Get help")
    except Exception as e:
        logger.error(f"Error in help_command: {e}")

async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text('Please provide your name, email, and number of tickets (e.g., John Doe, john@example.com, 2)')
    except Exception as e:
        logger.error(f"Error in register_command: {e}")

async def process_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text: str = update.message.text
        chat_id = update.message.chat.id

        if ',' in text:
            parts = [part.strip() for part in text.split(',')]
            if len(parts) == 3:
                name, email, tickets = parts
                user = get_user_by_email(email)
                if user:
                    await update.message.reply_text('You have already registered.')
                else:
                    user = register_user(name, email, tickets)
                    await update.message.reply_text(f'Thank you, {name}. Your registration is confirmed. Your ticket ID is: {user["id"]}')
                    await invite_user_to_group(chat_id, GROUP_INVITE_LINK, context)
            else:
                await update.message.reply_text('Invalid registration format.')
    except Exception as e:
        logger.error(f"Error in process_registration: {e}")

# Error Handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    bot = Bot(TOKEN)

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('register', register_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_registration))

    # Error
    app.add_error_handler(error)

    # Poll the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
