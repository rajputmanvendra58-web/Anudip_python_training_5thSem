#  License Key Verification System
"""
Problem Statement 
A software license key is entered: ABCD-EFGH-IJKL-MNOP 
Tasks 
Write a program to: 
1. Verify there are exactly 4 groups.  
2. Verify each group contains exactly 4 characters.  
3. Count total letters.  
4. Count vowels.  
5. Remove hyphens and display the merged key.  
6. Create a list containing all groups.  
7. Display whether the key format is valid.  
"""
# Take license key as input
license_key = input("Enter License Key: ").upper()

# Split the key into groups using '-'
groups = license_key.split("-")

# Count number of groups
num_groups = len(groups)

# Assume key is valid initially
is_valid = True

# Check if there are exactly 4 groups
if num_groups != 4:
    is_valid = False

# Check if each group contains exactly 4 characters
for group in groups:
    if len(group) != 4:
        is_valid = False

# Count total letters and vowels
total_letters = 0
total_vowels = 0

for ch in license_key:
    if ch.isalpha():
        total_letters += 1

        if ch in "AEIOU":
            total_vowels += 1

# Remove hyphens from the key
merged_key = license_key.replace("-", "")

# Display results
print("\nGroups:", groups)
print("Number of Groups:", num_groups)
print("Total Letters:", total_letters)
print("Total Vowels:", total_vowels)
print("Merged Key:", merged_key)

# Display validation status
if is_valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")