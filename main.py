import telebot

bot = telebot.TeleBot('1813066837:AAFyTtHPeZnKXq7tznxzUpdIN1fOPjJsEJs')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Halo bro, ada apa?')