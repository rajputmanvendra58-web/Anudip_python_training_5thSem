#wap to check the three sides form a triangle or not
a = float(input("Enter first side: "))
#validate input
if a < 0:
    exit("Sides must be positive numbers.")
b = float(input("Enter second side: "))
#validate input
if b < 0:
    exit("Sides must be positive numbers.")
c = float(input("Enter third side: "))
#validate input
if c < 0:
    exit("Sides must be positive numbers.")
#------------------------------------------------
#check triangle formation or not
if a + b > c and a + c > b and b + c > a:
    print("The three sides form a triangle.")
else:
    print("The three sides do not form a triangle.")