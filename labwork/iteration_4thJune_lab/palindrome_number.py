# Program to check Reverse Number and Palindrome Number
num = int(input("Enter a number: "))
original = num
reverse = 0
# Reverse the number
while num > 0:
    #to check the last digit
    digit = num % 10
    #adding the last digit
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse Number:", reverse)
# Check palindrome
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
