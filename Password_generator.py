import random
import time
import string
import secrets    
from typing import Counter


def user_input():
    user = int(input("please enter how long you would like your password to be "))
    return (user)


def number_generator(i):
    selected_numbers = [] #! The next line should be in its own function
    password_length = i
    length_for_string = int(password_length / 2)
    numbers = string.digits
    if password_length % 2 == 1:
        length_for_string = password_length - 1
        length_for_string = int(length_for_string / 2)
    space_left = password_length - length_for_string
    for i in range(length_for_string):
        selected_numbers.append(secrets.choice(numbers))
    return (selected_numbers, space_left)


def character_generator(x):
    has1, has0, acceptable = False, False, False 
    choice = []
    counter = 0
    characters = []
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num_letters = int(x / 2)
    if x % 2 == 1:
        num_letters = x - 1
        num_letters = int(num_letters / 2)
    characters_remaining = int(x - num_letters)
    while counter < num_letters:
        choice.append(secrets.randbelow(2))
        counter += 1
    for y in choice:
        if y == 1:
            has1 = True
        elif y == 0:
            has0 = True
        if has1 == True and has0 == True:
            acceptable = True
    if acceptable == False:
        if has1 == False:
            choice.pop()
            choice.append(1)
        elif has0 == False:
            choice.pop()
            choice.append(0)
    for z in choice:
        if z == 1:
            characters.append(secrets.choice(uppercase))
        if z == 0:
            characters.append(secrets.choice(lowercase))
    return (characters, characters_remaining)


def special_character_generator(i):
    chosen_characters = []
    special_chara = "@?{[}]-+!#$%^&*()_~"
    for x in range(i):
        chosen_characters.append(secrets.choice(special_chara))
    return (chosen_characters)


# * i number, x character, w special 
def making_the_pass(i, x, w, g):
    temp_storage = []
    counter = g
    lists = i + x + w
    counters = 0
    while counters < g:
        random = secrets.randbelow(g)
        temp_characters = lists.pop(random)
        temp_storage.append(temp_characters)
        g -= 1
    return "".join(temp_storage)


def initialize():
    input_user = user_input()
    number = (number_generator(input_user))
    character = character_generator(number[1])
    special = special_character_generator(character[1]) 
    print(making_the_pass(number[0], character[0], special, input_user))
    reruns()


def reruns():
    again = input("Would you like to generate another password \n").upper()
    if again == "YES":
        initialize()
    elif again == "NO":
        print("hi")
        quit
    else:
        print("Sorry we could not get that please try again")
        time.sleep(.2)
        reruns()


if __name__ == "__main__":
    initialize()