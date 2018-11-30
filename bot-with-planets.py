#!/usr/bin/python3.6

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
import datetime
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    print("Вызван /start")
    greet_username = update.message.chat.username
    print(update)
    update.message.reply_text("I am dummy, you are " + greet_username)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet_position(bot, update):
    today_date = datetime.datetime.now().strftime('%d/%m/%Y')
    planet_name = update.message.text.split()[1].capitalize()
    try:
        planet_obj = getattr(ephem, planet_name)
        planet_obj = planet_obj(today_date)
        planet_constellation = ephem.constellation(planet_obj)[1]
        update.message.reply_text("Planet " + planet_name + " is in " + planet_constellation + "today")
    except AttributeError:
        update.message.reply_text("Probably planet " + planet_name + " is unknown")

def main():
    mybot = Updater("673810459:AAGJK6PsyyFrQMPWhyJLuq3Dc_NRqPBjdV0")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("abqr", greet_user))
    dp.add_handler(CommandHandler("planet", planet_position))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()
