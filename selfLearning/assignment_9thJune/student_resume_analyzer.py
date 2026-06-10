# Assignment 6: Student Resume Analyzer 
"""
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords. 
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard. 
"""


# Student Resume Analyzer

# ----------------------------------
# Input Resume
# ----------------------------------

while True:

    resume = input("Enter Resume Details:\n")

    # Validation
    if resume.strip() == "":
        print("Resume cannot be empty.")
        continue

    break

# ----------------------------------
# Count Total Characters and Words
# ----------------------------------

total_characters = len(resume)

words = resume.split()

total_words = len(words)

# ----------------------------------
# Extract Email IDs
# ----------------------------------

emails = []

for word in words:

    if "@" in word and "." in word:
        emails.append(word)

# ----------------------------------
# Extract Phone Numbers
# ----------------------------------

phone_numbers = []

for word in words:

    clean_word = word.strip(".,()[]{}")

    if clean_word.isdigit() and len(clean_word) == 10:
        phone_numbers.append(clean_word)

# ----------------------------------
# Skill List
# ----------------------------------

skills_list = [
    "python", "java", "c", "c++", "sql",
    "html", "css", "javascript",
    "react", "nodejs", "mongodb",
    "communication", "leadership"
]

# ----------------------------------
# Count Skills and Skill Frequency
# ----------------------------------

skill_frequency = {}

for word in words:

    word = word.lower().strip(".,!?")

    if word in skills_list:

        if word in skill_frequency:
            skill_frequency[word] += 1

        else:
            skill_frequency[word] = 1

# ----------------------------------
# Count Total Skills Mentioned
# ----------------------------------

total_skills = 0

for skill in skill_frequency:
    total_skills += skill_frequency[skill]

# ----------------------------------
# Find Repeated Keywords
# ----------------------------------

word_frequency = {}

for word in words:

    word = word.lower().strip(".,!?")

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

print("\nRepeated Keywords:")

for word in word_frequency:

    if word_frequency[word] > 1:
        print(word)

# ----------------------------------
# Most Frequently Used Word
# ----------------------------------

most_frequent_word = ""
highest_frequency = 0

for word in word_frequency:

    if word_frequency[word] > highest_frequency:

        highest_frequency = word_frequency[word]
        most_frequent_word = word

# ----------------------------------
# Detect Duplicate Skills
# ----------------------------------

duplicate_skills = []

for skill in skill_frequency:

    if skill_frequency[skill] > 1:
        duplicate_skills.append(skill)

# ----------------------------------
# Most Frequent Skill
# ----------------------------------

most_frequent_skill = ""

max_skill_frequency = 0

for skill in skill_frequency:

    if skill_frequency[skill] > max_skill_frequency:

        max_skill_frequency = skill_frequency[skill]
        most_frequent_skill = skill

# ----------------------------------
# Top 5 Keywords
# ----------------------------------

sorted_keywords = sorted(
    word_frequency,
    key=word_frequency.get,
    reverse=True
)

# ----------------------------------
# Summary Dashboard
# ----------------------------------

print("\n========== RESUME ANALYSIS REPORT ==========")

print("Total Words :", total_words)
print("Total Characters :", total_characters)

print("Email IDs Found :", len(emails))
print("Phone Numbers Found :", len(phone_numbers))

print("Emails :", emails)
print("Phone Numbers :", phone_numbers)

print("Total Skills Mentioned :", total_skills)

print("Most Frequent Word :", most_frequent_word)

print("Most Frequent Skill :", most_frequent_skill)

print("Duplicate Skills :", duplicate_skills)

print("\nSkill Frequency Report:")

for skill in skill_frequency:
    print(skill, ":", skill_frequency[skill])

print("\nTop 5 Keywords:")

for keyword in sorted_keywords[:5]:
    print(keyword)