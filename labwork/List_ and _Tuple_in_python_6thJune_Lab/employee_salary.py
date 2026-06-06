#Program for Employee Salary Processing 
"""
Problem Statement 
Employee data is stored as tuples: 
employees = [     
("Rahul", 35000),     
("Priya", 55000),     
("Amit", 42000),     
("Neha", 65000) ] 
Write a program to: 
• Display employees earning above ₹50,000.  
• Find the highest-paid employee.  
• Calculate total salary expenditure.  
• Count employees earning below ₹40,000.
"""
#Employee Salary Processing 

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Task 1: Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")
for emp in employees:
    if emp[1] > 50000:
        print(emp[0], "-", emp[1])

# Task 2: Find the highest-paid employee
highest_paid = employees[0]

for emp in employees:
    if emp[1] > highest_paid[1]:
        highest_paid = emp

print("\nHighest Paid Employee:")
print(highest_paid[0], "-", highest_paid[1])

# Task 3: Calculate total salary expenditure
total_salary = 0

for emp in employees:
    total_salary += emp[1]

print("\nTotal Salary Expenditure =", total_salary)

# Task 4: Count employees earning below ₹40,000
count_below_40000 = 0

for emp in employees:
    if emp[1] < 40000:
        count_below_40000 += 1

print("\nEmployees earning below ₹40,000 =", count_below_40000)