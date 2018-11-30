#!/usr/bin/python3.6

age = input("Введите возраст: ")

def get_occupation_from_age(age):
    age_int = int(age)
    if 0 <= age_int <= 2:
        return("До трех в сады не берут")
    if 3 <= age_int <= 5:
        return("Ему в детский сад")
    elif 6 <= age_int <= 17:
        return("Этому место в школе")
    elif 18 <= age_int <= 23:
        return("Пора в ВУЗ")
    elif age_int < 0:
        return("Отрицательный возраст - это как?")
    elif age_int > 120:
        return("Вампир или Маклауд?")
    else:
        return("Работать, солнце ещё высоко.")
    # TODO: ввести пенсию =) 

occupation = get_occupation_from_age(age)
print(occupation)
