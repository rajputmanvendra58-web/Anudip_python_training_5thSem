# Program for Attendance Tracker
"""
Create Attendance tracker of 30 students. 
Ask the user to input roll number of student and also input whether student is Present or Absent. 
Store the data in dictionary where roll number will be used as a key and Attendance as Value. 
Display the roll number of students who are Present.
"""

# ---------------------------------------------------------------
#create dictionary to store roll number and attendance status
attendance = {} 
# Input attendance of 30 students
for i in range(30):
    roll_no = input(f"Enter Roll Number of Student {i + 1}: ")
    status = input("Enter Attendance (Present/Absent): ").capitalize()
    # Data validation for attendance
    while status not in ["Present", "Absent"]:
        print("Invalid input! Please enter Present or Absent.")
        status = input("Enter Attendance (Present/Absent): ").capitalize()
    attendance[roll_no] = status
# Display students who are Present
print("-----------------------------------------------")
print("\nRoll Numbers of Present Students:")
for roll_no, status in attendance.items():
    if status == "Present":
        print(roll_no)