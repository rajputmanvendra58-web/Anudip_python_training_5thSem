# Password Strength Analyzer
""" 
Problem Statement 
A user enters a password. Python@2026! 
Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. Rules: 
• Minimum length 8  
• Contains at least:  
o 1 uppercase letter  
o 1 lowercase letter  
o 1 digit  
o 1 special character  
Additionally: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Display all digits separately.  
6. Display all special characters separately. 
"""
# Password Strength Analyzer

password = "Python@2026!"

# Task 1: Count uppercase letters
uppercase_count = 0

# Task 2: Count lowercase letters
lowercase_count = 0

# Task 3: Count digits
digit_count = 0

# Task 4: Count special characters
special_count = 0

# Task 5: Store all digits separately
digits_found = []

# Task 6: Store all special characters separately
special_chars = []

# Checking each character
for ch in password:
    
    if ch.isupper():
        uppercase_count += 1

    elif ch.islower():
        lowercase_count += 1

    elif ch.isdigit():
        digit_count += 1
        digits_found.append(ch)

    else:
        special_count += 1
        special_chars.append(ch)

# Password Strength Check
if (len(password) >= 8 and
    uppercase_count >= 1 and
    lowercase_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):
    
    strength = "Strong"

elif len(password) >= 8:
    strength = "Medium"

else:
    strength = "Weak"

# Display Output
print("Password:", password)
print("Uppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
print("Digits Found:", digits_found)
print("Special Characters Found:", special_chars)
print("Password Strength:", strength)