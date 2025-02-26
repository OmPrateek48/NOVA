import telebot
import os
from AdminControl import is_admin

TOKEN = os.getenv("7877540006:AAG5FtR5VakjadL14Bbi1ym2V746Lk_Yxbo")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hello! I am NOVA. How can I assist you?")

@bot.message_handler(commands=['admin'])
def admin_check(message):
    if is_admin(message.from_user.id):
        bot.reply_to(message, "You have admin privileges.")
    else:
        bot.reply_to(message, "You are not authorized.")

def send_message(chat_id, text):
    bot.send_message(chat_id, text)

if __name__ == "__main__":
    print("InteractionManager is running...")
    bot.polling()
