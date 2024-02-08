from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN = os.environ.get('bot_token')

PROJECT_NAME = 'store-bot-example'

WEBHOOK_PATH = '/webhook/' + BOT_TOKEN

ADMINS = [000000000, 1234567890]
