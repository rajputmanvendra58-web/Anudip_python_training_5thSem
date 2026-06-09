# Username Generator System
"""
Problem Statement 
A student enters: Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics. 
"""
# Take student's name as input
name = input("Enter Your Name: ")

# Remove spaces from the name
username = name.replace(" ", "")

# Convert username to lowercase
username = username.lower()

# Append current year
username = username + "2026"

# Check username length
if len(username) > 12:
    username = username[:12]

# Initialize counters
vowels = 0
consonants = 0

# Count vowels and consonants
for ch in username:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display results
print("\nOriginal Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")