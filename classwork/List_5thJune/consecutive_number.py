# Program for Consecutive Number Detector 
# Problem Statement 
# Given a list: 
# numbers = [4, 5, 6, 10, 11, 15, 16, 17] 
# Write a program to find all pairs of consecutive numbers.

#List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17] 

#Empty list to store consecutive pairs
consecutive_pairs = []
# range(0, len(numbers) - 1) use kiya taaki aakhiri element ke baad loop bahar na jaye
for i in range(0, len(numbers) - 1):
    # Agar agla number (numbers[i+1]) pichle number se 1 bada hai
    if numbers[i+1] == numbers[i] + 1:
        #print pairs
        print(numbers[i], "and", numbers[i+1], "are consecutive")
        pair = (numbers[i], numbers[i+1]) 
        consecutive_pairs.append(pair)
# print additional list 
print("Consecutive Pairs List:", consecutive_pairs)