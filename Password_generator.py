import random
import time
import string
import secrets



def password_generator():
    passwordlength = 11 #TODO: should be an input later on
    numbers = string.digits
    if passwordlength % 2 == 1:
        length_for_string = passwordlength + 1
        length_for_string = int(length_for_string / 2)

    for i in range(length_for_string):
        print(secrets.choice(numbers))

    print("hi") 






password_generator()