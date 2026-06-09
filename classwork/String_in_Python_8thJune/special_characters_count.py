# Write a Program to Input a sentence from user and count the number of special characters in it.
print("Enter a sentence:")
sentence = input()
special_characters_count = 0
for char in sentence:
    if not char.isalnum() and not char.isspace():
        special_characters_count += 1
print("Number of special characters:", special_characters_count)