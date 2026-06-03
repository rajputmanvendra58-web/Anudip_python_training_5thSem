#wap to calculate area and perimeter of rectangle
length=float(input("enter length:"))   #length of the rectangle
if length < 0 :
     exit("the length must be positive")
breadth=float(input("enter breadth:"))   #breadth of the rectangle     
if breadth < 0:
    exit("the breadth must be positive")
else:
#to display perimeter
     print("The perimeter of rectangle= ",2*(length+breadth))
#to display area
     print("The area of rectangle= ",length*breadth)
