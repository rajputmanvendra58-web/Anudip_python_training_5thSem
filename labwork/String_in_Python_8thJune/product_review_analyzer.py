# Product Review Analyzer 
"""
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
4. Find all words appearing only once.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words. 
"""
# Take review as input from the user
review = input("Enter Product Review: ")

# Convert review into a list of words
words = review.split()

# 1. Count total words
total_words = len(words)

# 2. Create a dictionary for word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# 3. Find the most frequently used word
most_frequent_word = ""
max_count = 0

for word in frequency:
    if frequency[word] > max_count:
        max_count = frequency[word]
        most_frequent_word = word

# 4. Find words appearing only once
single_occurrence_words = []

for word in frequency:
    if frequency[word] == 1:
        single_occurrence_words.append(word)

# 5. Count words having more than 5 characters
long_words_count = 0

for word in words:
    if len(word) > 5:
        long_words_count += 1

# 6. Display words in reverse order
reverse_words = words[::-1]

# 7. Create a list of unique words
unique_words = list(frequency.keys())

# Display Output
print("\nTotal Words:", total_words)

print("\nWord Frequencies:")
for word in frequency:
    print(word, "->", frequency[word])

print("\nMost Frequent Word:", most_frequent_word)

print("\nWords Appearing Once:")
print(single_occurrence_words)

print("\nWords Having More Than 5 Characters:")
print(long_words_count)

print("\nWords in Reverse Order:")
print(reverse_words)

print("\nUnique Words:")
print(unique_words)