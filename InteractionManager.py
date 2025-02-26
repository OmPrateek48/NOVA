import telebot
import os
from AdminControl import is_admin  # Corrected import

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Ensure you set this in your environment
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hello! I am NOVA. How can I assist you?")

@bot.message_handler(commands=['admin'])
def admin_check(message):
    if is_admin(str(message.from_user.id)):  # Ensure comparison is done properly
        bot.reply_to(message, "You have admin privileges.")
    else:
        bot.reply_to(message, "You are not authorized.")

def send_message(chat_id, text):
    bot.send_message(chat_id, text)

if __name__ == "__main__":
    print("InteractionManager is running...")
    bot.polling()
