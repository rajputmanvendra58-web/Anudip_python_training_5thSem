# Assignment 2: Email Validation & Domain Analytics System 
"""
Problem Statement 
An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
"""


# Email Validation & Domain Analytics System

emails = []

# Dictionary to store domain counts
domain_count = {}

# List to store invalid emails
invalid_emails = []

# ----------------------------------
# Input Number of Emails
# ----------------------------------
while True:

    try:
        n = int(input("Enter number of emails (Minimum 20): "))

        if n >= 20:
            break

        print("Please enter at least 20 emails.")

    except ValueError:
        print("Please enter a valid integer.")

# ----------------------------------
# Input Emails
# ----------------------------------
for i in range(n):

    email = input(f"\nEnter Email {i + 1}: ")
    emails.append(email)

print("\n========== EMAIL ANALYSIS ==========")

# ----------------------------------
# Analyze Each Email
# ----------------------------------
for email in emails:

    print("\nEmail:", email)

    # Validation Checks
    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    # Invalid Email
    if not valid:

        print("Status : Invalid Email")
        invalid_emails.append(email)

    else:

        print("Status : Valid Email")

        # Extract Username
        username = email[:email.index("@")]

        # Extract Domain and Extension
        domain_part = email[email.index("@") + 1:]

        domain = domain_part

        extension = domain_part.split(".")[-1]

        # Count digits in username
        digit_count = 0

        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # Count special characters in username
        special_count = 0

        for ch in username:
            if not ch.isalnum():
                special_count += 1

        # Store domain frequency
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

        # Display Details
        print("Username :", username)
        print("Domain :", domain)
        print("Extension :", extension)
        print("Digits in Username :", digit_count)
        print("Special Characters :", special_count)

# ----------------------------------
# Display Invalid Emails
# ----------------------------------
print("\n========== INVALID EMAILS ==========")

if len(invalid_emails) == 0:
    print("No Invalid Emails Found")

else:
    for email in invalid_emails:
        print(email)

# ----------------------------------
# Domain Report
# ----------------------------------
print("\n========== DOMAIN REPORT ==========")

for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")