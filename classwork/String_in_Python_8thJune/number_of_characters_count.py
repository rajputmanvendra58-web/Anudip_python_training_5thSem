# Write a program to input a string and input a sentence from user and count the number of characters present in it without using len function.
print("Enter a sentence:")
sentence = input()  
character_count = 0
for char in sentence:
    character_count += 1
print("Number of characters:", character_count)
