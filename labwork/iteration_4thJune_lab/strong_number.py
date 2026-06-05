# Program to check whether a number is a Strong Number or not
# Take input from the user
num = int(input("Enter a number: "))
# Store the original number for comparison later
original_num = num
# Variable to store the sum of factorials of digits
sum_fact = 0
# Process each digit of the number
while num > 0:
    # Extract the last digit
    digit = num % 10
    # Calculate factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    # Add factorial to the sum
    sum_fact += fact
    # Remove the last digit from the number
    num //= 10
# check 
if sum_fact == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")