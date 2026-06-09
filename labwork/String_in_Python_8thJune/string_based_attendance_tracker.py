# String-Based Attendance Tracker 
"""
Problem Statement 
Attendance of a student for 15 days is represented as: PPAPPPAAPPPPAPP 
Where:
    • P = Present  
    • A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.
"""
# Take attendance record as input
attendance = input("Enter Attendance Record: ").upper()

# Count present and absent days
present_days = attendance.count("P")
absent_days = attendance.count("A")

# Calculate attendance percentage
attendance_percentage = (present_days / len(attendance)) * 100

# Find longest present streak
max_present_streak = 0
current_present_streak = 0

for ch in attendance:
    if ch == "P":
        current_present_streak += 1
        if current_present_streak > max_present_streak:
            max_present_streak = current_present_streak
    else:
        current_present_streak = 0

# Find longest absent streak
max_absent_streak = 0
current_absent_streak = 0

for ch in attendance:
    if ch == "A":
        current_absent_streak += 1
        if current_absent_streak > max_absent_streak:
            max_absent_streak = current_absent_streak
    else:
        current_absent_streak = 0

# Display results
print("\nAttendance Record:", attendance)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
print("Longest Present Streak:", max_present_streak)
print("Longest Absent Streak:", max_absent_streak)

# Check attendance status
if attendance_percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Above 75%")  