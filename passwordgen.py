import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_special = input("Include special characters? (y/n): ").lower() == "y"

characters = string.ascii_lowercase

if use_uppercase:
    characters += string.ascii_uppercase

if use_numbers:
    characters += string.digits

if use_special:
    characters += string.punctuation

if length < 1:
    print("Password length must be at least 1.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)