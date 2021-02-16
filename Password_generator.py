import random
import time
import string
import secrets



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
def character_generator(i, x):
    counter = 0
    characters = []
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    num_letters = int(x / 2)
    if x % 2 == 1:
        num_letters = x - 1
        num_letters = int(num_letters / 2)
    characters_remaining = int(x - num_letters)
    while counter < 2:
        characters.append(secrets.randbelow(2))
        counter += 1
    print(characters)



print(number_generator())
print(character_generator(0, 6))