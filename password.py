import random
import string

def password_generater(length=12):
    c = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(c) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = password_generater(password_length)
    print(f"Generated password: {password}")

print(main())