#!/usr/bin/python3.6

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
import datetime
import ephem
from cities_db import city_game_db as city_game_db
from random import shuffle

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

city_game_dict = {"tst" : ["Москва", "Тамбов", "Ангола"],
"tst2": ["Москва", "Москва"] }

city_game_letter_dict = {"tst": "А", "tst2": "Б"}

#city_game_db = {"а" : ['Абаза', 'Абакан', ], 
#"б" : ['Беломорск', 'Белозерск']}

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

def cities_game(bot, update):
    cities_player_username = update.message.chat.username
    user_city_name = update.message.text.split()[1].capitalize()
    user_city_first_letter = user_city_name[0]
    user_city_last_letter = user_city_name[-1]
    forbidden_last_letters = ["ь", "ы", "ъ", "ё", "й"]
    if user_city_last_letter in forbidden_last_letters:
        user_city_last_letter = user_city_name[-2]
    if user_city_name == "Сдаюсь":
        try:
            del city_game_dict[cities_player_username]
            del city_game_letter_dict[cities_player_username]
        except KeyError:
            pass
        update.message.reply_text("Ура, я победил! Начни новую игру с /cities Город")
        return 0
    elif user_city_name not in city_game_db[user_city_first_letter.lower()]:
        update.message.reply_text("Давай существующие в России города, а не вымышленные")
        return 0
    if cities_player_username not in city_game_dict:
        city_game_dict.update({cities_player_username: []})
        update.message.reply_text("Новая игра началась, чтобы сдаться используй команду /cities сдаюсь")
    if cities_player_username not in city_game_letter_dict:
        # user_city_first_letter used as just placeholder here
        city_game_letter_dict.update({cities_player_username: user_city_first_letter})
    elif city_game_letter_dict[cities_player_username].lower() != user_city_first_letter.lower():
        update.message.reply_text("Не принимается, тебе на " + city_game_letter_dict[cities_player_username])
        return 0
    if user_city_name in city_game_dict.get(cities_player_username):
        update.message.reply_text("Этот город уже был")
        return 0
    else:
        city_game_dict.get(cities_player_username).append(user_city_name)
    cites_for_letter_ended = True
    shuffle(city_game_db[user_city_last_letter])
    for city in city_game_db[user_city_last_letter]:
        if city not in city_game_dict.get(cities_player_username):
            cites_for_letter_ended = False
            bot_city_last_letter = city[-1]
            if bot_city_last_letter in forbidden_last_letters:
                bot_city_last_letter = city[-2]
            update.message.reply_text(city + ", тебе на " + bot_city_last_letter)
            city_game_dict.get(cities_player_username).append(city)
            city_game_letter_dict.update({cities_player_username: bot_city_last_letter})
            return 0
    if cites_for_letter_ended == True:
        update.message.reply_text("Ты победил, у меня нет городов на букву " + user_city_last_letter)
        del city_game_dict[cities_player_username]
        del city_game_letter_dict[cities_player_username]
        return 0
    update.message.reply_text(city_game_dict[cities_player_username])
 

def main():
    mybot = Updater("673810459:AAGJK6PsyyFrQMPWhyJLuq3Dc_NRqPBjdV0")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("abqr", greet_user))
    dp.add_handler(CommandHandler("planet", planet_position))
    dp.add_handler(CommandHandler("cities", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()
