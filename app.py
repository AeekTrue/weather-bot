from fastapi import FastAPI
from telebot.types import Update

import settings
from bot import bot

app = FastAPI()


@app.get("/")
def index():
	return {
		"message": "Hello, world!",
	}


@app.post(settings.WEBHOOK_PATH)
def process_webhook(update: dict):
	if update:
		update = Update.de_json(update)
		bot.process_new_updates([update])
	else:
		return
