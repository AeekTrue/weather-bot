import telebot
from telebot import types

import settings
from bot_keyboards import main_keyboard
from log import logger

bot = telebot.TeleBot(settings.TOKEN)
logger.success("Telegram bot is running!")


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
	bot.send_message(chat_id=msg.chat.id,
	                 text=f"""Hello, {msg.from_user.first_name}!
	I'm WeatherBot, weather informer!
	Send me /howisweather to get weather""",
	                 reply_markup=main_keyboard)


@bot.message_handler(commands=['howisweather'])
def weather(msg: types.Message):
	bot.send_message(msg.chat.id, "This feature coming soon.")


@bot.message_handler()
def default(msg: types.Message):
	logger.info(msg.json())
