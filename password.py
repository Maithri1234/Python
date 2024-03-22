import string
import random

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user to specify the desired length of the password
try:
    password_length = int(input("Enter the desired length of the password: "))
    # Ensure the length is a positive number
    if password_length <= 0:
        raise ValueError("The length must be a positive number.")
except ValueError as e:
    print("Invalid input:", e)
else:
    # Generate and display the password
    print("Generated password:", generate_password(password_length))
