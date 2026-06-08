'''----------------------------------------------------
Problem Statement: Student Result Management System 
Scenario 
A school wants to store and manage student marks. 
student_marks = { 
"Anuj": 85, 
"Rahul": 72, 
"Priya": 91, 
"Neha": 68, 
"Amit": 78 
} 
The principal asks for the following information: 
Tasks 
• Display the marks of Priya.  
• Display the marks of Amit.  
• Update Rahul's marks from 72 to 80.  
• Check whether a student named Rohan exists.  
• Display all student names.  
• Display all marks.  
• Find the highest scorer.  
• Add a new student: 
Rohan : 88 
• Remove a student: 
Neha 
• Display all student records. 
---------------------------------------------'''
#creating a dictionary to store student marks
student_marks = { 
"Anuj": 85, 
"Rahul": 72, 
"Priya": 91, 
"Neha": 68, 
"Amit": 78 
}
#----------------------------------------------------
#to display the marks of Priya
print("Marks of Priya : ",student_marks['Priya'])
#--------------------------------------------------
#to display the marks of Amit
print("Marks of Amit : ",student_marks['Amit'])
#--------------------------------------------------
#to update Rahul's marks from 72 to 80
student_marks['Rahul'] = 80
#--------------------------------------------------
#to check whether a student named Rohan exists  
if 'Rohan' in student_marks:
    print("Rohan exists in the records.")
else:
    print("Rohan does not exist in the records.")
#--------------------------------------------------
#to display all student names
print("All student names : ",student_marks.keys())
#--------------------------------------------------
#to display all marks
print("All marks : ",student_marks.values())
#--------------------------------------------------
#to find the highest scorer
dict_items = list(student_marks.items())
highest_scorer = dict_items[0][0]
high_score = dict_items[0][1]
for item in dict_items:
    if item[1] > high_score:
        highest_scorer = item[0]
        high_score = item[1]
print("Highest scorer is : ",highest_scorer," with marks : ",high_score)
#--------------------------------------------------
#Display all student records
print("All student records : ")
print(student_marks)


'''
Output:
Marks of Priya :  91
Marks of Amit :  78
Rohan does not exist in the records.
All student names :  dict_keys(['Anuj', 'Rahul', 'Priya', 'Neha', 'Amit'])
All marks :  dict_values([85, 80, 91, 68, 78])
dict_items([('Anuj', 85), ('Rahul', 80), ('Priya', 91), ('Neha', 68), ('Amit', 78)])
Highest scorer is :  Priya  with marks :  91
All student records : 
{'Anuj': 85, 'Rahul': 80, 'Priya': 91, 'Neha': 68, 'Amit': 78}
'''