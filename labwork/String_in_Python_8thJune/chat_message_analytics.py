# Chat Message Analytics
"""
Problem Statement 
A chat application stores a message: Python is awesome and Python is easy to learn Tasks 
Write a program to:
1. Count total characters.  
2. Count total words.  
3. Find the longest word.  
4. Find the shortest word.  
5. Count how many times the word "Python" appears.  
6. Create a list of words having more than 4 characters.  
7. Display all words starting with a vowel.  
8. Count the number of vowels and consonants.
"""
# Chat Message Analytics
message = "Python is awesome and Python is easy to learn"
# Task 1: Count total characters
total_characters = len(message)
#----------------------------------------------
# Task 2: Count total words
words = message.split()
total_words = len(words)
#----------------------------------------------
# Task 3: Find the longest word
longest_word = max(words, key=len)
#----------------------------------------------
# Task 4: Find the shortest word
shortest_word = min(words, key=len)
#----------------------------------------------
# Task 5: Count how many times the word "Python" appears
python_count = words.count("Python")
#----------------------------------------------
# Task 6: Create a list of words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)
#----------------------------------------------
# Task 7: Display all words starting with a vowel
vowel_words = []
vowels = "AEIOUaeiou"

for word in words:
    if word[0] in vowels:
        vowel_words.append(word)
#----------------------------------------------
# Task 8: Count the number of vowels and consonants
vowel_count = 0
consonant_count = 0
vowels = "AEIOUaeiou"

for char in message:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
#----------------------------------------------
# Displaying results
print(f"Total characters: {total_characters}")
print(f"Total words: {total_words}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")
print(f"Occurrences of 'Python': {python_count}")
print(f"Words with more than 4 characters: {long_words}")
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

"""
output:
Total characters: 49
Total words: 9  
Longest word: awesome
Shortest word: is
Occurrences of 'Python': 2
Words with more than 4 characters: ['Python', 'awesome', 'Python', 'learn']
Vowels: 16, Consonants: 24
"""
