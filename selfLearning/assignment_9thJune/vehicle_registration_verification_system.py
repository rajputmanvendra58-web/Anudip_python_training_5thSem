#  Assignment 4: Vehicle Registration Verification System  
"""
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example MH12AB4589 DL05XY9988 KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
    o First 2 characters = Alphabets  
    o Next 2 characters = Digits  
    o Next 2 characters = Alphabets  
    o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
"""

# Vehicle Registration Verification System

vehicles = []

# Dictionary to store state-wise vehicle count
state_count = {}

# List to store invalid vehicle numbers
invalid_vehicles = []

# ----------------------------------
# Input Number of Vehicles
# ----------------------------------
while True:

    try:
        n = int(input("Enter number of vehicle registrations (Minimum 20): "))

        if n >= 20:
            break

        print("Please enter at least 20 vehicle registrations.")

    except ValueError:
        print("Please enter a valid integer.")

# ----------------------------------
# Input Vehicle Numbers
# ----------------------------------
for i in range(n):

    while True:

        vehicle = input(f"\nEnter Vehicle Registration {i + 1}: ").upper()

        # Validation: Registration number should contain exactly 10 characters
        if len(vehicle) != 10:
            print("Vehicle number must contain exactly 10 characters.")
            continue

        vehicles.append(vehicle)
        break

print("\n========== VEHICLE ANALYSIS ==========")

# ----------------------------------
# Analyze Each Vehicle Number
# ----------------------------------
for vehicle in vehicles:

    # Extract different parts
    state_code = vehicle[:2]
    district_code = vehicle[2:4]
    series = vehicle[4:6]
    vehicle_number = vehicle[6:]

    letters = 0
    digits = 0

    # Count letters and digits
    for ch in vehicle:

        if ch.isalpha():
            letters += 1

        elif ch.isdigit():
            digits += 1

    # ----------------------------------
    # Validate Format
    # Format:
    # AA00AA0000
    # ----------------------------------
    valid = True

    if not vehicle[:2].isalpha():
        valid = False

    if not vehicle[2:4].isdigit():
        valid = False

    if not vehicle[4:6].isalpha():
        valid = False

    if not vehicle[6:].isdigit():
        valid = False

    # ----------------------------------
    # Display Details
    # ----------------------------------
    print("\nVehicle Number :", vehicle)
    print("State Code :", state_code)
    print("District Code :", district_code)
    print("Series :", series)
    print("Vehicle Number :", vehicle_number)
    print("Total Letters :", letters)
    print("Total Digits :", digits)

    if valid:

        print("Status : Valid Registration")

        # Count vehicles state-wise
        if state_code in state_count:
            state_count[state_code] += 1

        else:
            state_count[state_code] = 1

    else:

        print("Status : Invalid Registration")
        invalid_vehicles.append(vehicle)

# ----------------------------------
# Display Invalid Registrations
# ----------------------------------
print("\n========== INVALID REGISTRATIONS ==========")

if len(invalid_vehicles) == 0:

    print("No Invalid Registrations Found")

else:

    for vehicle in invalid_vehicles:
        print(vehicle)

# ----------------------------------
# State-wise Report
# ----------------------------------
print("\n========== STATE-WISE REPORT ==========")

for state in state_count:

    print(state, "->", state_count[state], "Vehicles")