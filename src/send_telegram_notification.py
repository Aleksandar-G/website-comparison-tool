from telebot import TeleBot
import os
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()


from helper_funcs import Website


def send_telegram_message(website: Website):

    API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
    CHATID = os.getenv("TELEGRAM_CHATID")

    bot = TeleBot(API_TOKEN)
    chat_id = CHATID

    # Message to send
    message = f"{website.name} has new listings URL:{website.url}"

    # Send the message
    bot.send_message(chat_id=chat_id, text=message)

    print("Telegram message send")