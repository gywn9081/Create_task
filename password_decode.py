

def printing_saved_passwords():
    stored_passwords = open("password.py", "r")
    passwords = stored_passwords.read()
    ind_passwords = passwords.split(",")
    length = ind_passwords.len()
    for i in range(length):
        print(i)


    stored_passwords.close()


if __name__ == "__main__":
    printing_saved_passwords()