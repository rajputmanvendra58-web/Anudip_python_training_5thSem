# Text Compression Analyzer 
"""
Problem Statement 
A compressed message is given: AAABBBCCCDDDAAA 
Tasks 
Write a program to: 
1. Count occurrences of each character.  
2. Create a dictionary of character frequencies.  
3. Display unique characters.  
4. Find the most frequent character.  
5. Create a compressed output:  A3B3C3D3A3 
6. Calculate compression ratio. 
"""
# Take compressed text as input
text = input("Enter Text: ").upper()

# Create dictionary to store character frequencies
frequency = {}

# Count occurrences of each character
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Display character frequencies
print("\nCharacter Frequencies:")
for key in frequency:
    print(key, "->", frequency[key])

# Display unique characters
unique_characters = list(frequency.keys())
print("Unique Characters:", unique_characters)

# Find most frequent character
most_frequent = ""
max_count = 0

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        most_frequent = key

print("Most Frequent Character:", most_frequent)

# Create compressed output
compressed = ""
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

# Add last character group
compressed += text[-1] + str(count)

print("Compressed Output:", compressed)

# Calculate lengths
original_length = len(text)
compressed_length = len(compressed)

# Calculate compression ratio
compression_ratio = (compressed_length / original_length) * 100

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(compression_ratio, 2), "%")