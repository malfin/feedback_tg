# 1036910512:AAFWawYZ20rB1ZZN8y3rlbdy1_xIbDJOuzc

import telebot

user_id = 642873481

token = "1036910512:AAFWawYZ20rB1ZZN8y3rlbdy1_xIbDJOuzc"

bot = telebot.TeleBot(token)


def send_message_to_tg(first_name, phone_number, email, text):
    message = f'Имя: {first_name}.\nНомер телефона: {phone_number}.\nEmail: {email}.\nСообщение:\n{text}.\n'
    bot.send_message(user_id, message)
