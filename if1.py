#!/usr/bin/python3.6

def get_occupation_from_age(age):
    age_int = int(age)
    if age_int < 0:
        return "Отрицательный возраст - это как?"
    elif age_int <= 2:
        return "До трех в сады не берут"
    if age_int <= 5:
        return "Ему в детский сад"
    elif age_int <= 17:
        return "Этому место в школе"
    elif age_int <= 23:
        return "Пора в ВУЗ"
    elif age_int <= 65:
        return "Работать, солнце ещё высоко."
    elif age_int <= 145:
        return "Пора бы на пенсию, но можно и поработать"
    else:
        return "Люди столько не живут, воспользуйтесь версией для эльфов"


age = input("Введите возраст: ")
occupation = get_occupation_from_age(age)
print(occupation)
