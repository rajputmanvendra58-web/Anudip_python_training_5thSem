#Program for Student Result Management System
# Initialize total marks and failed subjects count
total = 0
failed_subjects = 0
# Accept marks of 5 subjects
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks
    # Check if student is failed (less than 40 marks)
    if marks < 40:
        failed_subjects += 1
# Calculate percentage
percentage = total / 5
# Determine grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"
# Display results
print("\n----- RESULT -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)