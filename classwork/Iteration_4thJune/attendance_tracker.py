 # Program to count present and absent students
present = 0
absent = 0
student = 1

while student <= 30:
    print("Student", student)
    attendance = input("Attendance (Present/Absent): ")

    if attendance.lower() == "present":
        present += 1
    elif attendance.lower() == "absent":
        absent += 1
    else:
        print("Invalid Input")
        continue

    student += 1

print("No. of Students Present :", present)
print("No. of Students Absent :", absent)