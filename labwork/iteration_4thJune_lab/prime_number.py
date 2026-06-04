#Program to analyse Prime numbers
#Accepting the number from the user
num = int(input("Enter a number: "))
# number less than or equal to 1 are not prime
if num <= 1:
    print(f"{num} is not a prime number")
else:
    #assume the number is prime initially
    is_prime = True
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            #if divisible the number is not prime
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")