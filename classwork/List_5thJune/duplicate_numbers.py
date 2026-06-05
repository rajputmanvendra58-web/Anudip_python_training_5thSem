# Create a list of 20 numbers entered by the user
numbers = []

for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    #append into list 
    numbers.append(num)

# Number whose duplicates are to be removed but keeping the original number
temp = int(input("Enter the number to remove its duplicate: "))
#finding the frequency of given number
frequency=numbers.count(temp)
if frequency == 0:
    print("Number not Found")
elif frequency == 1:
    print("No duplicates are Found")
else:
    #reversing the list
    numbers.reverse()
    for i in range (1,frequency):
        numbers.remove(temp)
    #Reversing the list again
    numbers.reverse()
    print("After Removing duplicates")
    print(numbers)