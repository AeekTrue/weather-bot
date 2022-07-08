from os import environ

TOKEN = environ["TELEBOT_TOKEN"]
CREATOR_ID = environ.get("TELEBOT_OWNER_ID")

WEBHOOK_URL = f"https://howisweatherbot.herokuapp.com"
WEBHOOK_PATH = f"/{TOKEN}/".replace(':', '').replace('-', '')
