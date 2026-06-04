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
    #validate equilateral triangle
    if(a==b==c):
        print("Above sides form an equilateral triangle")
        #validate isosceles triangle
elif(a==b or b==c or c==a):
            print("Above sides form an isosceles triangle")
        #validate scalene triangle
else:
    print("Above sides form a scalen triangle")