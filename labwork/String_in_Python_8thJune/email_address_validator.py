# Email Address Validator 
"""
Problem Statement 
A user enters an email address: rahul.sharma2026@gmail.com 
Tasks 
Write a program to: 
1. Extract username.  
2. Extract domain name.  
3. Extract extension.  
4. Count digits present in username.  
5. Count special characters.  
6. Check whether:  
    o Exactly one '@' exists.  
    o At least one '.' exists after '@'.  
7. Display Valid Email or Invalid Email.  
"""
# Email Address Validator

email = "rahul.sharma2026@gmail.com"

# Task 1: Extract username
username = email.split("@")[0]

# Task 2: Extract domain name
domain = email.split("@")[1].split(".")[0]

# Task 3: Extract extension
extension = email.split(".")[-1]

# Task 4: Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

# Task 5: Count special characters
special_count = 0
special_chars = []

for ch in email:
    if not ch.isalnum():
        special_count += 1
        special_chars.append(ch)

# Task 6: Validation

# Condition 1: Exactly one '@'
at_check = email.count("@") == 1

# Condition 2: At least one '.' after '@'
dot_check = "." in email.split("@")[1] if at_check else False

# Condition 3: Username should not be empty
username_check = len(username) > 0

# Condition 4: Domain should not be empty
domain_check = len(domain) > 0

# Final Validation
valid = (
    at_check and
    dot_check and
    username_check and
    domain_check
)

# Display Results
print("Email:", email)
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)
print("Special Character List:", special_chars)

if valid:
    print("Email Status: Valid")
else:
    print("Email Status: Invalid")

"""
output:
Email: rahul.sharma2026@gmail.com
Username: rahul.sharma2026
Domain: gmail
Extension: com
Digits Found: 4
Special Characters Found: 3
Special Character List: ['.', '@', '.']
Email Status: Valid
"""