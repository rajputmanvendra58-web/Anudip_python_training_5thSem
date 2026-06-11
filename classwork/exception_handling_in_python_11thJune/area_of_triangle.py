# Problem Statement: Area of a Triangle Using Three Sides with Exception Handling
"""
Design a Python program to calculate the area of a triangle using Heron's Formula. 
The program should accept the lengths of the three sides of the triangle from the user and display the calculated area. 
However, the program must handle the following exceptional situations gracefully: 
1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error message.  
2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be greater than zero.  
3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality Theorem, notify the user that the triangle is invalid.  
4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful feedback using exception handling.  
5. Display a message indicating that the triangle area calculation process has been completed, 
regardless of whether the calculation was successful or an exception occurred.  
Note: Use Heron's Formula to calculate 
the area of the triangle: 
𝑠=(𝑎+𝑏+𝑐)/2 
Area=√(𝑠(𝑠−𝑎)(𝑠−𝑏)(𝑠−𝑐) ) 
Sample Scenario: 
A construction engineer is using an application to estimate the amount of material required for a triangular plot of land. 
Incorrect measurements or invalid data entry should not cause the application to crash; instead, 
it should guide the user by displaying appropriate error messages and allowing them to understand the issue with the provided inputs. 
"""

#--------------Program for Area of a Triangle Using Three Sides with Exception Handling-------------------
try:
    a= float(input("Enter the first side of the triangle: "))
    b= float(input("Enter the second side of the triangle: "))
    c= float(input("Enter the third side of the triangle: "))
    if a<=0:
        raise Exception("Triangle side must be greater than zero.")
        
    if b<=0:
        raise Exception("Triangle side must be greater than zero.")
        
    if c<=0:
        raise Exception("Triangle side must be greater than zero.")

    if a+b<c:
        raise Exception("Invalid triangle: The given side length do not satisfy the Triangle Inequality Theorem.")

    if b+c<a:
        raise Exception("Invalid triangle: The given side length do not satisfy the Triangle Inequality Theorem.")
        
    if a+c<b:
        raise Exception("Invalid triangle: The given side length do not satisfy the Triangle Inequality Theorem.")
        
    import math 

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Area of triangle =", area) 
    
except ValueError:
    print("Error: Please enter a valid numeric value for each side.") # error if there is non numeric value
    
except Exception as e:
    print("Error:", str(e)) # storing the exception in e and then printing
    
finally:
    print("Triangle area calculation process completed.") # triangle area calculation

  