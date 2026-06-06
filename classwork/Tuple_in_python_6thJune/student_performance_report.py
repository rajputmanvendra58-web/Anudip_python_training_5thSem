#Student Record Management Using Tuples
'''--------------------------------------
Each student's record should contain:
  •	Student ID 
  •	Student Name 
  •	Course Name 
  •	Fees Paid 
Store the details of 5 students using tuples and perform the following operations:
  1. Display all student records. 
  2. Display the first student's details. 
  3. Display the last student's details using negative indexing. 
  4. Display only Student ID and Name for all students. 
  5. Count the total number of students. 
  6. Check whether a student named "Rahul" exists in the records. 
-----------------------------------------------------------------------'''
#creating student data
students = (
    (101, "Rahul", "Python", 25000),
    (102, "Priya", "Java", 30000),
    (103, "Amit", "Data Science", 45000),
    (104, "Sneha", "Python", 25000),
    (105, "Rohan", "MERN", 40000)
)
#-----------------------------------------
#Task 1: To display all student record
print("----- Student's Records -----")
for record in students:
	print("Student id : ",record[0])
	print("Name : ",record[1])
	print("Course : ",record[2])
	print("Fee Paid : Rs",record[3])
	print("---------------------------")
#-----------------------------------------
#task 2 : To display first student details
print("Record of First Student : ")
print("Id : ",students[0][0])
print("Name : ",students[0][1])
print("Course : ",students[0][2])
print("Fee Paid : Rs ",students[0][3])
print("---------------------------------")
#-----------------------------------------
#task 3 : To display the last student's details using negative indexing
print("Record of Last Student : ")
print("Id : ",students[-1][0])
print("Name : ",students[-1][1])
print("Course : ",students[-1][2])
print("Fee Paid : Rs ",students[-1][3])
print("---------------------------------")
#-----------------------------------------
#Task 4: To display only Student ID and Name for all students. 
print("----- Student's Records -----")
for record in students:
  print("Student id : ",record[0])
  print("Name : ",record[1])
  print("---------------------------")
#-----------------------------------------
#task 5 : To display count of all students
print("Total Count : ",len(students))
print("------------------------------")
#--------------------------------------------
#Task 6: To check whether a student named "Rahul" exists in the records. 
count = 0
for record in students:
  if(record[1] == 'Rahul'):
    count+=1
    break
if(count == 0):
  print("No Student with Name 'Rahul' exists")
else:
  print("Rahul exists in Record")