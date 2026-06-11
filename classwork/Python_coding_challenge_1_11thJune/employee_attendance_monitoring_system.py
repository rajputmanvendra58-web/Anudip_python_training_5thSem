# Problem 6: Employee Attendance Monitoring System 
"""
Problem Statement 
Employee attendance records are stored in attendance.txt. 
Sample Input/Data (attendance.txt) 
EMP101,P 
EMP102,A 
EMP103,P 
EMP104,P 
EMP105,A 
EMP106,P 
EMP107,P 
EMP108,A 
EMP109,P 
EMP110,P 
Tasks 
1. Count present and absent employees.  
2. Display absent employee IDs.  
3. Calculate attendance percentage.  
4. Generate an absentee report in absent_report.txt.  
5. Display employees eligible for attendance awards (100% attendance).  
"""

# Employee Attendance Monitoring System

# List to store employee records
employees = []

# ----------------------------------
# Read data from attendance.txt
# ----------------------------------
try:
    file = open("attendance.txt", "r")

    for line in file:
        line = line.strip()

        emp_id, status = line.split(",")

        employees.append([emp_id, status])

    file.close()

except FileNotFoundError:
    print("attendance.txt file not found!")
    exit()

# ----------------------------------
# Task 1 : Count Present and Absent Employees
# ----------------------------------
present_count = 0
absent_count = 0

for employee in employees:

    if employee[1] == "P":
        present_count += 1
    else:
        absent_count += 1

print("Present Employees :", present_count)
print("Absent Employees :", absent_count)

# ----------------------------------
# Task 2 : Display Absent Employee IDs
# ----------------------------------
print("\nAbsent Employee IDs")
print("-" * 25)

for employee in employees:

    if employee[1] == "A":
        print(employee[0])

# ----------------------------------
# Task 3 : Calculate Attendance Percentage
# ----------------------------------
attendance_percentage = (present_count / len(employees)) * 100

print(f"\nAttendance Percentage : {attendance_percentage:.1f}%")

# ----------------------------------
# Task 4 : Generate Absentee Report
# ----------------------------------
try:
    file = open("absent_report.txt", "w")

    for employee in employees:

        if employee[1] == "A":
            file.write(employee[0] + "\n")

    file.close()

    print("Absentee Report Generated Successfully.")

except:
    print("Error while creating report!")

# ----------------------------------
# Task 5 : Attendance Award Eligibility
# ----------------------------------
print("\nAttendance Award Eligibility")
print("-" * 30)

award_found = False

for employee in employees:

    # Employee is eligible only if not absent
    if employee[1] == "P":
        continue
    else:
        award_found = False
        break

if absent_count == 0:
    print("All Employees Eligible for Attendance Award")
else:
    print("Not Applicable")