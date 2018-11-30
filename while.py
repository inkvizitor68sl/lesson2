#!/usr/bin/python3.6

qa_dict = {"Как дела?": "Хорошо!", 
    "Что делаешь?": "Программирую",
    "Абырвалг?": "ГлавРыба",
    "?": "Ты из лиги лени."}

def ask_user():
    while True:
        user_say = input('Как дела?: ')
        if user_say.lower() == 'хорошо':
            print('У меня тоже =)')
            break
        else:
            print('Не люблю негатив, давай попробуем снова.')

def ask_computer():
    while True:
        user_ask = input('Теперь твой вопрос: ')
        if qa_dict.get(user_ask) != None:
            print(qa_dict.get(user_ask))
            break
        else:
            print('Я не очень умный, задай другой вопрос.')       

ask_user()
ask_computer()
