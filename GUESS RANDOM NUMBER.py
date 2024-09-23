import random

def guess_number(limit):
    random_number = random.randint(1, limit)
    attempts = 0

    while True:
        guess = int(input(f"Guess a number between 1 and {limit}: "))
        attempts += 1

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Example
num= int(input("Enter the range from 0 to :"))
guess_number(num)
