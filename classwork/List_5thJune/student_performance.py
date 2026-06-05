# Student Performance Analyzer
#  Problem Statement 
# A teacher has marks of students stored in a list. 
# marks = [78, 45, 92, 35, 88, 40, 99, 56]
# Write a program to:
#  1. Display all passed students (marks ≥ 40). 
#  2. Count the number of failed students. 
# 3. Find the highest and lowest marks without using max() or min(). 
#  4. Create a new list containing marks above 75.   
#List of Students marks
marks=[78,45,92,35,88,40,99,56]

#List to store the passed students
passed_students=[]

#counter for failed students
failed_count=0

#initialise the highest and lowest mark
highest=marks[0]
lowest=marks[0]

#New list containing marks above 75
merit_list=[]

#traverse the list
for mark in marks:
    #check for pass/fail
    if mark>=40:
        passed_students.append(mark)
    else:
        failed_count+=1
    #for finding Highest marks
    if mark>highest:
        highest=mark
    #for finding Lowest marks
    if mark<lowest:
        lowest=mark
    #for adding the marks above from 75  to the merit list
    if mark>75:
        merit_list.append(mark)

#Display Results
print("Passed Students : ",passed_students)
print("Failed count : ",failed_count)
print ("Highest marks: ",highest)
print("Lowest Marks : ",lowest)
print("Merit List : ",merit_list)
        

    


