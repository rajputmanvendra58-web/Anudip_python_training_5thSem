# Problem 4: School Report Card Generator
"""
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
Passed Students: 9 
Failed Students: 1 
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90). 
"""

# School Report Card Generator

# List to store student records
students = []

# ----------------------------------
# Reading data from marks.txt file
# ----------------------------------
try:
    file = open("marks.txt", "r")

    for line in file:
        line = line.strip()

        student_id, name, marks = line.split(",")

        # Convert marks into integer
        marks = int(marks)

        students.append([student_id, name, marks])

    file.close()

except FileNotFoundError:
    print("marks.txt file not found!")
    exit()

# ----------------------------------
# Function to calculate grade
# ----------------------------------
def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"

# ----------------------------------
# Task 1 & 2
# Generate Report Card File
# ----------------------------------
report_file = open("report_card.txt", "w")

for student in students:

    grade = calculate_grade(student[2])

    report_file.write(
        f"{student[0]}, {student[1]}, Marks={student[2]}, Grade={grade}\n"
    )

report_file.close()

# ----------------------------------
# Task 3 : Display Topper Details
# ----------------------------------
topper = students[0]

for student in students:

    if student[2] > topper[2]:
        topper = student

print("\nTOPPER DETAILS")
print("-" * 30)
print(f"Name : {topper[1]}")
print(f"Marks : {topper[2]}")

# ----------------------------------
# Task 4 : Count Pass and Fail Students
# ----------------------------------
pass_count = 0
fail_count = 0

for student in students:

    if student[2] >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("\nPASS / FAIL REPORT")
print("-" * 30)
print("Passed Students :", pass_count)
print("Failed Students :", fail_count)

# ----------------------------------
# Task 5 : Merit Certificate Holders
# ----------------------------------
print("\nMERIT CERTIFICATE HOLDERS")
print("-" * 30)

merit_found = False

for student in students:

    if student[2] >= 90:
        print(student[1])
        merit_found = True

if merit_found == False:
    print("No Merit Certificate Holders")

print("\nReport Cards Generated Successfully.")