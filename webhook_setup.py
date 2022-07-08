from bot import bot
from settings import WEBHOOK_URL, WEBHOOK_PATH
from log import logger

bot.remove_webhook()
bot.set_webhook(WEBHOOK_URL + WEBHOOK_PATH)
logger.info(f'Set webhook: {WEBHOOK_URL + WEBHOOK_PATH}')
