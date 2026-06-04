# Program for Number Guessing Game
import random
# Generate a random secret number between 1 and 50
secret_number = random.randint(1, 50)
# Variable to count the number of attempts
attempts = 0
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50")
# Repeat until the correct number is guessed
while True:
    guess = int(input("Enter your guess: "))
    # Increase attempt count
    attempts += 1
    # Check the guess
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct Guess")
        print("Total Attempts =", attempts)
        break