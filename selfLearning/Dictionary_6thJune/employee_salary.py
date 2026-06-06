# Employee Salary Processing 
"""
Sample Data salary = {     
"EMP101": 45000,     
"EMP102": 62000,     
"EMP103": 38000,     
"EMP104": 75000,     
"EMP105": 54000,     
"EMP106": 29000,     
"EMP107": 82000,     
"EMP108": 48000,     
"EMP109": 36000,     
"EMP110": 68000 
}
Tasks 
• Display employees earning above ₹60,000.  
• Count employees earning below ₹40,000.  
• Find the highest-paid employee.  
• Create a list of employees eligible for a bonus (salary > ₹50,000).  
• Calculate the average salary.   
"""

# Employee Salary Processing

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Task 1: Display employees earning above ₹60,000
print("Task 1: Employees earning above ₹60,000")

for emp_id, sal in salary.items():
    if sal > 60000:
        print(emp_id, ":", sal)

# Task 2: Count employees earning below ₹40,000
count_below_40000 = 0

for sal in salary.values():
    if sal < 40000:
        count_below_40000 += 1

print("\nTask 2: Employees earning below ₹40,000 =", count_below_40000)

# Task 3: Find the highest-paid employee
highest_paid = max(salary, key=salary.get)

print("\nTask 3: Highest-paid employee")
print(highest_paid, ":", salary[highest_paid])

# Task 4: Create a list of employees eligible for bonus
bonus_list = []

for emp_id, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp_id)

print("\nTask 4: Employees eligible for bonus")
print(bonus_list)

# Task 5: Calculate the average salary
total_salary = sum(salary.values())
average_salary = total_salary / len(salary)

print("\nTask 5: Average Salary =", average_salary)