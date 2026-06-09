# Employee ID Validation and Analysis System 
"""
Problem Statement 
A company generates employee IDs in the following format: EMP2026ANUJ458 
Tasks 
Write a program to: 
1. Count the number of uppercase letters.  
2. Count the number of digits.  
3. Extract the joining year.  
4. Extract the employee name.  
5. Check whether the ID follows these rules:  
    o Starts with "EMP"  
    o Contains exactly 4 digits for the year  
    o Ends with exactly 3 digits  
6. Create a list containing all digits present in the ID.  
7. Find the sum of all digits present in the ID.  
8. Display whether the ID is valid or invalid.  
"""

# Employee ID Validation and Analysis System

employee_id = "EMP2026ANUJ458"

# Task 1: Count uppercase letters
uppercase_count = 0
for ch in employee_id:
    if ch.isupper():
        uppercase_count += 1

# Task 2: Count digits
digit_count = 0
for ch in employee_id:
    if ch.isdigit():
        digit_count += 1

# Task 3: Extract joining year
joining_year = employee_id[3:7]

# Task 4: Extract employee name
employee_name = employee_id[7:-3]

# Task 5: Verify ID rules
valid = (
    employee_id.startswith("EMP") and
    employee_id[3:7].isdigit() and
    len(employee_id[3:7]) == 4 and
    employee_id[-3:].isdigit() and
    len(employee_id[-3:]) == 3
)

# Task 6: Create a list containing all digits
digit_list = []
for ch in employee_id:
    if ch.isdigit():
        digit_list.append(int(ch))

# Task 7: Find sum of all digits
sum_of_digits = sum(digit_list)

# Task 8: Display results
print("Employee ID:", employee_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digit_list)
print("Sum of Digits:", sum_of_digits)

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")

"""
output:
Employee ID: EMP2026ANUJ458
Uppercase Letters: 7
Digits: 7
Joining Year: 2026
Employee Name: ANUJ
Digit List: [2, 0, 2, 6, 4, 5, 8]
Sum of Digits: 27
ID Status: Valid
"""

