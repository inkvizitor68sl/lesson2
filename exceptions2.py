#!/usr/bin/python3.6

def get_summ(num_one, num_two):
    try:
        summ = int(num_one) + int(num_two)
        return summ
    except ValueError:
        return("Cant get int from num_one or num_two")
    except TypeError:
        return("You doing it wrong, probably dict or list")

print(get_summ(1,2))
print(get_summ(15,16))
print(get_summ(1,"asf"))
print(get_summ(1,[1,2,3]))
