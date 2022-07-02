from bot import bot
from settings import WEBHOOK_URL, WEBHOOK_PATH

bot.remove_webhook()
bot.set_webhook(WEBHOOK_URL + WEBHOOK_PATH)