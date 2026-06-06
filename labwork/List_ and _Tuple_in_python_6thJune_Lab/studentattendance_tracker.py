# Program for Student Attendance Tracker
""" 
Problem Statement Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
• Count present and absent days.  
• Calculate attendance percentage.  
• Determine eligibility (minimum 75% attendance).  
• Display positions where the student was absent.
"""  

# Task 1: Store attendance data

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Task 2: Count present and absent days

present_count = 0
absent_count = 0

for status in attendance:
    if status == 'P':
        present_count += 1
    else:
        absent_count += 1

print("Present Days =", present_count)
print("Absent Days =", absent_count)

# Task 3: Calculate attendance percentage

total_days = len(attendance)
attendance_percentage = (present_count / total_days) * 100

print("Attendance Percentage =", attendance_percentage, "%")

# Task 4: Determine eligibility (minimum 75%)

if attendance_percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Task 5: Display positions where student was absent

print("Absent on Days:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)   # +1 because days start from 1, not 0