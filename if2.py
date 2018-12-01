#!/usr/bin/python3.6

def two_strings_comparser(string1, string2):
    if type(string1) != str or type(string2) != str:
        return 0
    elif string1 == string2:
        return 1 
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 and string2 == "learn":
        return 3

print(two_strings_comparser("string", 1))
print(two_strings_comparser("string", "string"))
print(two_strings_comparser("string_longer", "string"))
print(two_strings_comparser("short", "learn"))
