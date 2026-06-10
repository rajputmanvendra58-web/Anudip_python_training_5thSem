# Assignment 1: Password Security Analyzer 
"""
Problem Statement 
A cybersecurity company wants to analyze user passwords before allowing account creation. 
The system should accept at least 15 passwords and generate a security report. 
Requirements 
For each password: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Check minimum length (8 characters).  
6. Check if spaces exist.  
7. Determine password strength:  
    o Strong  
    o Medium  
    o Weak  
8. Display repeated characters.  
9. Count vowels and consonants.  
10. Identify the most frequently occurring character. 
"""

# Password Security Analyzer

# List to store all valid passwords
passwords = []

# -----------------------------
# Input Number of Passwords
# -----------------------------
while True:

    try:
        n = int(input("Enter number of passwords (Minimum 15): "))

        if n >= 15:
            break

        print("Please enter at least 15 passwords.")

    except ValueError:
        print("Please enter a valid integer.")

# -----------------------------
# Input Passwords with Validation
# -----------------------------
for i in range(n):

    while True:

        password = input(f"\nEnter Password {i + 1}: ")

        # Validation 1: Password should not be empty
        if password == "":
            print("Password cannot be empty.")
            continue

        # Validation 2: Password should not contain spaces
        if " " in password:
            print("Password should not contain spaces.")
            continue

        # Validation 3: Minimum length should be 8
        if len(password) < 8:
            print("Password must contain at least 8 characters.")
            continue

        # If all validations pass, store password
        passwords.append(password)
        break

# Counters for final report
strong_count = 0
medium_count = 0
weak_count = 0

print("\n========== PASSWORD ANALYSIS ==========")

# -----------------------------
# Analyze Each Password
# -----------------------------
for password in passwords:

    # Counters
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    # Dictionary to store frequency of characters
    frequency = {}

    # Traverse each character
    for ch in password:

        # Count uppercase letters
        if ch.isupper():
            uppercase += 1

        # Count lowercase letters
        elif ch.islower():
            lowercase += 1

        # Count digits
        elif ch.isdigit():
            digits += 1

        # Count special characters
        else:
            special += 1

        # Count vowels and consonants
        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowels += 1

            else:
                consonants += 1

        # Store frequency of each character
        if ch in frequency:
            frequency[ch] += 1

        else:
            frequency[ch] = 1

    # -----------------------------
    # Find Repeated Characters
    # -----------------------------
    repeated_characters = []

    for key in frequency:

        if frequency[key] > 1:
            repeated_characters.append(key)

    # -----------------------------
    # Find Most Frequent Character
    # -----------------------------
    max_frequency = 0
    most_frequent_character = ""

    for key in frequency:

        if frequency[key] > max_frequency:

            max_frequency = frequency[key]
            most_frequent_character = key

    # -----------------------------
    # Check Length and Spaces
    # -----------------------------
    length_check = len(password) >= 8
    space_check = " " in password

    # -----------------------------
    # Determine Password Strength
    # -----------------------------
    if (uppercase > 0 and lowercase > 0 and
            digits > 0 and special > 0 and
            length_check):

        strength = "Strong"
        strong_count += 1

    elif length_check and (
            (uppercase > 0 and lowercase > 0) or
            (lowercase > 0 and digits > 0) or
            (uppercase > 0 and digits > 0)):

        strength = "Medium"
        medium_count += 1

    else:

        strength = "Weak"
        weak_count += 1

    # -----------------------------
    # Display Analysis
    # -----------------------------
    print("\nPassword :", password)
    print("Uppercase Letters :", uppercase)
    print("Lowercase Letters :", lowercase)
    print("Digits :", digits)
    print("Special Characters :", special)
    print("Minimum Length (8) :", length_check)
    print("Contains Spaces :", space_check)
    print("Password Strength :", strength)
    print("Repeated Characters :", repeated_characters)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Most Frequent Character :", most_frequent_character)

# -----------------------------
# Final Security Report
# -----------------------------
print("\n========== SECURITY REPORT ==========")

print("Total Passwords Analyzed :", n)
print("Strong Passwords :", strong_count)
print("Medium Passwords :", medium_count)
print("Weak Passwords :", weak_count)