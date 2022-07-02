import telebot
from telebot import types

import settings


bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
	bot.send_message(msg.chat.id, f"""Hello, {msg.from_user.first_name}!
	I'm WeatherBot, you weather informer!
	Send me /howisweather to get weather""")


@bot.message_handler(commands=['howisweather'])
def weather(msg: types.Message):
	bot.send_message(msg.chat.id, "This feature coming soon.")
	