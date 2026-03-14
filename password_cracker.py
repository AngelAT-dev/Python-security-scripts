import itertools
import string

password = input("Enter the password to crack (for simulation): ")

characters = string.ascii_lowercase + string.digits

print("Starting brute force attack simulation...\n")

attempts = 0

for length in range(1, 6):
    for guess in itertools.product(characters, repeat=length):
        guess = ''.join(guess)
        attempts += 1

        if guess == password:
            print(f"Password found: {guess}")
            print(f"Attempts: {attempts}")
            exit()

print("Password not found.")
