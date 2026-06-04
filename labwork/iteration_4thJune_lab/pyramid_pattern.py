# Program to print a Number Pyramid and Reverse Number Pyramid
# Accept number of rows from the user
rows = int(input("Enter the number of rows: "))
print("\nNumber Pyramid:")
# Loop to print the pyramid pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print("\nReverse Number Pyramid:")
# Loop to print the reverse pyramid pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()