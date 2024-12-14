import random
import string
import secrets
import hashlib

def gen_pwd(length=15, all_characters = True):
    if all_characters:
        all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def check_password_strength(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    if len(password) < 8:
        return "Weak"
    elif (has_uppercase and has_lowercase and has_digit) or (has_uppercase and has_lowercase and has_symbol):
        return "Medium"
    elif (has_uppercase and has_lowercase and has_digit and has_symbol):
        return "Strong"
    else:
        return "Weak"
def main():
    while True:
        length = int(input("Enter the desired password length (or 0 to exit): "))
        if length == 0:
            break
        password = gen_pwd(length)
        print("Generated password:", password)
        strength = check_password_strength(password)
        print("Password strength:", strength)
if __name__ == "__main__":
    main()