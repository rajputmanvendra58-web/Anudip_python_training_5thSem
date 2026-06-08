# Employee Performance Dashboard
"""
Problem Statement 
Employee performance scores are stored as: 
performance = {     
"EMP101": 92,     
"EMP102": 78,     
"EMP103": 45,     
"EMP104": 88,     
"EMP105": 97,     
"EMP106": 56,     
"EMP107": 81,     
"EMP108": 64,     
"EMP109": 39,     
"EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80. 
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Create separate lists:  
    o Excellent (≥ 90) 
    o Good (75–89)  
    o Average (60–74)  o Poor (< 60)
"""
# Creating a Dictionary for Employee Performance
performance = {     
"EMP101": 92,     
"EMP102": 78,     
"EMP103": 45,     
"EMP104": 88,     
"EMP105": 97,     
"EMP106": 56,     
"EMP107": 81,     
"EMP108": 64,     
"EMP109": 39,     
"EMP110": 73 
}

# Task 1: to Display employees scoring above 80. 
print("Employees Scoring above 80: ")
for emp_id,score in performance.items():
    if score>80:
        print(emp_id)

# Task 2: to Count employees needing improvement (score < 60). 
improvement_count=0
for score in performance.values():
    if score<60:
        improvement_count += 1
print ("Employees Needing Improvemnt: ",improvement_count)

# Task 3: to Find the top performer.
dict_items=list(performance.items())
top_emp=dict_items[0][0]
top_perform=dict_items[0][1]
for item in dict_items:
    if item[1]>top_perform:
        top_emp=item[0]
        top_perform=item[1]
print("Top Performer: ",top_emp,"(",top_perform,")")

# Task 4: to Calculate average performance score.
average_score= sum(performance.values())/len(performance)
print("Average Score: ",average_score)

# Task 5: to Create separate lists: 
excellent = []
good = []
average = []
poor = []

for emp_id, score in performance.items():

    if score >= 90:
        excellent.append(emp_id)

    elif score >= 75:
        good.append(emp_id)

    elif score >= 60:
        average.append(emp_id)

    else:
        poor.append(emp_id)

print("\nExcellent:")
print(excellent)
print("\nGood:")
print(good)
print("\nAverage:")
print(average)
print("\nPoor:")
print(poor)


"""
Output:-
Employees Scoring above 80: 
EMP101
EMP104
EMP105
EMP107
Employees Needing Improvemnt:  3
Top Performer:  EMP105 ( 97 )
Average Score:  71.3

Excellent:
['EMP101', 'EMP105']

Good:
['EMP102', 'EMP104', 'EMP107']

Average:
['EMP108', 'EMP110']

Poor:
['EMP103', 'EMP106', 'EMP109']
"""