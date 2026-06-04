# Program to enter the correct ATM PIN
pin = input("Enter your 4-Digit ATM PIN: ")  # User enters PIN

while len(pin) != 4:  # Check whether PIN is 4 digits
    pin = input("Kindly enter a 4-Digit PIN: ")

while pin != "7487":  # Verify correct PIN
    pin = input("Incorrect PIN, Try Again: ")

print("ACCESS GRANTED")  # Access granted after correct PIN