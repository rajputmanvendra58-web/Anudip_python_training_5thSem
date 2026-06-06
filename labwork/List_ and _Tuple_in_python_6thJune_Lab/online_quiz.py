# Problem Statement 
"""
Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] 
Write a program to: 
• Calculate score.  
• Display incorrectly answered question numbers.  
• Count correct and wrong answers.  
• Determine pass/fail (minimum 60%).  
"""

# Problem Statement 7: Online Quiz Evaluation

# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

# Variables for counting
score = 0
correct_count = 0
wrong_count = 0

print("Incorrectly Answered Question Numbers:")

# Task 1, 2 and 3
for i in range(len(correct)):
    
    if correct[i] == student[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1
        print("Question", i + 1)

# Display score
print("\nScore:", score)

# Display correct and wrong answers count
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

# Task 4: Determine Pass/Fail (minimum 60%)
percentage = (score / len(correct)) * 100

print("Percentage:", percentage, "%")

if percentage >= 60:
    print("Result: Pass")
else:
    print("Result: Fail")