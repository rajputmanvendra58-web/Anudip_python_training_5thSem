# Assignment 3: Chat Message Analytics Dashboard 
"""
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies. 
"""

# Chat Message Analytics Dashboard

messages = []

# ----------------------------------
# Input Number of Messages
# ----------------------------------
while True:

    try:
        n = int(input("Enter number of messages (Minimum 20): "))

        if n >= 20:
            break

        print("Please enter at least 20 messages.")

    except ValueError:
        print("Enter a valid integer.")

# ----------------------------------
# Input Messages
# ----------------------------------
for i in range(n):

    while True:

        message = input(f"\nEnter Message {i + 1}: ")

        # Validation
        if message.strip() == "":
            print("Message cannot be empty.")
            continue

        messages.append(message)
        break

# Dictionary to store overall word frequency
word_frequency = {}

# Variables for challenge report
most_frequent_word = ""
highest_frequency = 0

longest_message = ""
shortest_message = messages[0]

total_words_all_messages = 0

print("\n========== MESSAGE ANALYSIS ==========")

# ----------------------------------
# Analyze Each Message
# ----------------------------------
for message in messages:

    words = message.split()

    total_words = len(words)
    total_characters = len(message)

    total_words_all_messages += total_words

    vowels = 0
    consonants = 0

    # Count vowels and consonants
    for ch in message:

        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowels += 1

            else:
                consonants += 1

    # Find longest word
    longest_word = words[0]

    for word in words:

        if len(word) > len(longest_word):
            longest_word = word

    # Find shortest word
    shortest_word = words[0]

    for word in words:

        if len(word) < len(shortest_word):
            shortest_word = word

    # Create frequency dictionary
    message_frequency = {}

    for word in words:

        word = word.lower()

        if word in message_frequency:
            message_frequency[word] += 1

        else:
            message_frequency[word] = 1

        # Overall frequency dictionary
        if word in word_frequency:
            word_frequency[word] += 1

        else:
            word_frequency[word] = 1

    # Repeated words
    repeated_words = []

    for word in message_frequency:

        if message_frequency[word] > 1:
            repeated_words.append(word)

    # Words starting with vowels
    vowel_words = []

    for word in words:

        if word[0].lower() in "aeiou":
            vowel_words.append(word)

    # Words longer than 5 characters
    long_words = []

    for word in words:

        if len(word) > 5:
            long_words.append(word)

    # Display analysis
    print("\nMessage :", message)
    print("Total Words :", total_words)
    print("Total Characters :", total_characters)
    print("Vowels :", vowels)
    print("Consonants :", consonants)
    print("Longest Word :", longest_word)
    print("Shortest Word :", shortest_word)
    print("Repeated Words :", repeated_words)
    print("Words Starting With Vowels :", vowel_words)
    print("Words Longer Than 5 Characters :", long_words)
    print("Word Frequency Dictionary :", message_frequency)

    # Longest Message
    if len(message) > len(longest_message):
        longest_message = message

    # Shortest Message
    if len(message) < len(shortest_message):
        shortest_message = message

# ----------------------------------
# Most Frequently Used Word
# ----------------------------------
for word in word_frequency:

    if word_frequency[word] > highest_frequency:

        highest_frequency = word_frequency[word]
        most_frequent_word = word

# ----------------------------------
# Average Words Per Message
# ----------------------------------
average_words = total_words_all_messages / n

# ----------------------------------
# Final Dashboard Report
# ----------------------------------
print("\n========== DASHBOARD REPORT ==========")

print("Most Frequently Used Word :", most_frequent_word)
print("Longest Message :", longest_message)
print("Shortest Message :", shortest_message)
print("Average Words Per Message :", round(average_words, 2))