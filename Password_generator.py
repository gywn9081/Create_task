import random
import time
import string
import secrets
from typing import Counter
# * code was tested with 3.8.3 may not work with other versions 


def number_generator():
    selected_numbers = [] #! The next line should be in its own function
    password_length = 11 #TODO: should be an input later on 
    length_for_string = int(password_length / 2)
    numbers = string.digits
    if password_length % 2 == 1:
        length_for_string = password_length - 1
        length_for_string = int(length_for_string / 2)
    space_left = password_length - length_for_string
    for i in range(length_for_string):
        selected_numbers.append(secrets.choice(numbers))
    return (selected_numbers, space_left)


# * This function should get the x param from number_generator for space left
def character_generator(x):
    #! I could not find a better way of defineing my vars before reference
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
    g = 11
    counters = 0
    while counters < g:
        random = secrets.randbelow(3)
        if random == 0:
            temp_storage.append(secrets.choice(i))
        if random == 1:
            temp_storage.append(secrets.choice(x))
        if random == 2:
            temp_storage.append(secrets.choice(w))
        counters += 1
    return "".join(temp_storage)





#? should really be in a function so I can use with other programs 
number = (number_generator())
character = character_generator(number[1])
special = special_character_generator(character[1]) 
print(making_the_pass(number[0], character[0], special, 11))