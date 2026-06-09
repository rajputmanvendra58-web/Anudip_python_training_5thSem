# Vehicle Number Plate Verification
"""
Problem Statement 
A vehicle number plate is entered: MH12AB4589 
Tasks 
Write a program to: 
1. Extract state code.  
2. Extract district code.  
3. Extract vehicle series.  
4. Extract vehicle number.  
5. Count letters and digits separately.  
6. Verify:  
    o First 2 characters must be alphabets.  
    o Next 2 must be digits.  
    o Next 2 must be alphabets.  
    o Last 4 must be digits.  
7. Display whether the number plate is valid.
"""
# Vehicle Number Plate Verification

vehicle_no = "MH12AB4589"

# Task 1: Extract state code
state_code = vehicle_no[:2]

# Task 2: Extract district code
district_code = vehicle_no[2:4]

# Task 3: Extract vehicle series
series = vehicle_no[4:6]

# Task 4: Extract vehicle number
vehicle_number = vehicle_no[6:]

# Task 5: Count letters and digits separately
letter_count = 0
digit_count = 0

for ch in vehicle_no:
    if ch.isalpha():
        letter_count += 1
    elif ch.isdigit():
        digit_count += 1

# Task 6: Verify format
valid = (
    vehicle_no[:2].isalpha() and
    vehicle_no[2:4].isdigit() and
    vehicle_no[4:6].isalpha() and
    vehicle_no[6:].isdigit() and
    len(vehicle_no[6:]) == 4
)

# Task 7: Display results
print("Vehicle Number:", vehicle_no)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letter_count)
print("Total Digits:", digit_count)

if valid:
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")

"""
output:
Vehicle Number: MH12AB4589
State Code: MH
District Code: 12
Series: AB
Vehicle Number: 4589
Total Letters: 4
Total Digits: 6
Vehicle Number Status: Valid
"""

