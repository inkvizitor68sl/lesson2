#!/usr/bin/python3.6

def ask_user():
    while True:
        try:
            user_say = input('Как дела?: ')
            if user_say.lower() == 'хорошо':
                print('У меня тоже =)')
                break
            else:
                print('Не люблю негатив, давай попробуем снова.')
        except KeyboardInterrupt:
            print("\nПока!")
            break

ask_user()
