# Problem 9: University Course Enrollment Management System
"""
Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data enrollment = {     
"Python": 45,     
"Java": 38,     
"Data Science": 52,     
"Web Development": 34,     
"Machine Learning": 41,     
"Cloud Computing": 29,     
"Cyber Security": 33,     
"DBMS": 48,     
"Networking": 26, 
"Operating Systems": 37} 
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
    o High Demand (>40)  
    o Medium Demand (30–40)  
    o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments). 
"""

# University Course Enrollment Management System

# Dictionary storing course names and enrollments
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# ----------------------------------
# Task 1 : Display Courses Having More Than 40 Enrollments
# ----------------------------------
print("Courses with More Than 40 Enrollments:")
print("-" * 40)

for course, students in enrollment.items():
    if students > 40:
        print(course)

# ----------------------------------
# Task 2 : Find Most and Least Popular Courses
# ----------------------------------
most_popular = list(enrollment.keys())[0]
least_popular = list(enrollment.keys())[0]

for course, students in enrollment.items():

    if students > enrollment[most_popular]:
        most_popular = course

    if students < enrollment[least_popular]:
        least_popular = course

print("\nMost Popular Course:")
print(f"{most_popular} ({enrollment[most_popular]} students)")

print("\nLeast Popular Course:")
print(f"{least_popular} ({enrollment[least_popular]} students)")

# ----------------------------------
# Task 3 : Calculate Total Enrollments
# ----------------------------------
total_enrollments = 0

for students in enrollment.values():
    total_enrollments += students

print("\nTotal Enrollments:", total_enrollments)

# ----------------------------------
# Task 4 : Create Demand Categories
# ----------------------------------
high_demand = []
medium_demand = []
low_demand = []

for course, students in enrollment.items():

    if students > 40:
        high_demand.append(course)

    elif students >= 30:
        medium_demand.append(course)

    else:
        low_demand.append(course)

print("\nHigh Demand:")
print(high_demand)

print("\nMedium Demand:")
print(medium_demand)

print("\nLow Demand:")
print(low_demand)

# ----------------------------------
# Task 5 : Count Courses Requiring Promotion
# (<35 enrollments)
# ----------------------------------
promotion_count = 0

for students in enrollment.values():

    if students < 35:
        promotion_count += 1

print("\nCourses Requiring Promotion:", promotion_count)

