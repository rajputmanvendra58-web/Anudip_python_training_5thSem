#Program for Guessing the secret number
# Secret number selected by the game
secret_number = 7
# Take the first guess from the user
guess = int(input("Guess the Number: "))
# Keep asking until the correct number is guessed
while guess != secret_number:
    print("Wrong Guess. Try Again.")
    guess = int(input("Guess the Number: "))
# Executed when the correct number is entered
print("Congratulations! You guessed the correct number.")