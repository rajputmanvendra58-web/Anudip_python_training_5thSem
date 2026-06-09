#  Program to obtain the area and perimeter of rectangle
# import the mensuration module
import mensuration 
# get the length and width of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# calculate the area and perimeter of the rectangle
area = mensuration.rectangle_area(length, width)
perimeter = mensuration.rectangle_perimeter(length, width)
# display the area and perimeter of the rectangle
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)

#-----------------------------------------------------------------
# Program to obtain the area and perimeter of square
# get the side of the square from the user
side = float(input("Enter the side of the square: "))
# calculate the area and perimeter of the square
area = mensuration.square_area(side)
perimeter = mensuration.square_perimeter(side)
# display the area and perimeter of the square
print("The area of the square is: ", area)
print("The perimeter of the square is: ", perimeter)


#-----------------------------------------------------------------
# Program to obtain the area and perimeter of circle
# get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))
# calculate the area and perimeter of the circle
area = mensuration.circle_area(radius)
perimeter = mensuration.circle_perimeter(radius)
# display the area and perimeter of the circle
print("The area of the circle is: ", area)
print("The perimeter of the circle is: ", perimeter)


