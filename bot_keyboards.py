from telebot.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup()
send_location_button = KeyboardButton('Send location📍', request_location=True)
main_keyboard.add(send_location_button)
