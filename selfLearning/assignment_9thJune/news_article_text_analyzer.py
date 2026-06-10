# Assignment 5: News Article Text Analyzer 
"""
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word frequencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
"""

# News Article Text Analyzer

# ----------------------------------
# Input Article
# ----------------------------------

while True:

    article = input("Enter News Article:\n")

    # Validation
    if article.strip() == "":
        print("Article cannot be empty.")
        continue

    break

# ----------------------------------
# Basic Counts
# ----------------------------------

total_characters = len(article)

words = article.split()

total_words = len(words)

# Count sentences
sentences = 0

for ch in article:

    if ch in ".!?":
        sentences += 1

# ----------------------------------
# Count Vowels and Consonants
# ----------------------------------

vowels = 0
consonants = 0

for ch in article:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowels += 1

        else:
            consonants += 1

# ----------------------------------
# Find Longest and Shortest Word
# ----------------------------------

longest_word = words[0]
shortest_word = words[0]

for word in words:

    # Remove punctuation
    clean_word = word.strip(".,!?")

    if len(clean_word) > len(longest_word):
        longest_word = clean_word

    if len(clean_word) < len(shortest_word):
        shortest_word = clean_word

# ----------------------------------
# Create Word Frequency Dictionary
# ----------------------------------

frequency = {}

for word in words:

    word = word.lower().strip(".,!?")

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

# ----------------------------------
# Most Frequent Word
# ----------------------------------

most_frequent_word = ""
highest_frequency = 0

for word in frequency:

    if frequency[word] > highest_frequency:

        highest_frequency = frequency[word]
        most_frequent_word = word

# ----------------------------------
# Words Appearing Only Once
# ----------------------------------

print("\nWords Appearing Only Once:")

for word in frequency:

    if frequency[word] == 1:
        print(word)

# ----------------------------------
# Words Appearing More Than 5 Times
# ----------------------------------

print("\nWords Appearing More Than 5 Times:")

for word in frequency:

    if frequency[word] > 5:
        print(word)

# ----------------------------------
# Count Words Starting With Each Alphabet
# ----------------------------------

alphabet_count = {}

for word in frequency:

    first_letter = word[0].upper()

    if first_letter in alphabet_count:
        alphabet_count[first_letter] += 1

    else:
        alphabet_count[first_letter] = 1

# ----------------------------------
# Display Alphabet Report
# ----------------------------------

print("\nWords Starting With Each Alphabet:")

for letter in alphabet_count:

    print(letter, ":", alphabet_count[letter])

# ----------------------------------
# Display Unique Words
# ----------------------------------

print("\nUnique Words:")

for word in frequency:
    print(word)

# ----------------------------------
# Calculate Average Word Length
# ----------------------------------

total_length = 0

for word in words:

    total_length += len(word.strip(".,!?"))

average_word_length = total_length / total_words

# ----------------------------------
# Final Summary Report
# ----------------------------------

print("\n========== TEXT SUMMARY ==========")

print("Total Characters :", total_characters)
print("Total Words :", total_words)
print("Total Sentences :", sentences)
print("Vowels :", vowels)
print("Consonants :", consonants)

print("Longest Word :", longest_word)
print("Shortest Word :", shortest_word)

print("Most Frequent Word :", most_frequent_word)

print("Vocabulary Size :", len(frequency))

print("Average Word Length :", round(average_word_length, 2))