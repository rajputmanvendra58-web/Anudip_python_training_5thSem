# Problem 3: Smart Parking Management System 
"""
Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data parking_slots = [     
"Occupied", 
"Vacant", 
"Occupied", 
"Vacant",     
"Occupied", 
"Occupied", 
"Vacant", 
"Occupied",     
"Vacant", 
"Occupied" ] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt. 
"""

# Smart Parking Management System

# List storing parking slot status
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# -----------------------------------
# Task 1 : Display Vacant Slot Numbers
# -----------------------------------
print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")

print("\n")

# -----------------------------------
# Task 2 : Count Occupied and Vacant Slots
# -----------------------------------
occupied_count = 0
vacant_count = 0

for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1
    else:
        vacant_count += 1

print("Occupied Slots :", occupied_count)
print("Vacant Slots :", vacant_count)

# -----------------------------------
# Task 3 : Allocate First Vacant Slot
# -----------------------------------
allocated = False

for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print(f"\nVehicle Allocated to Slot {i + 1}")
        allocated = True
        break

if not allocated:
    print("No Vacant Slot Available!")

# -----------------------------------
# Task 4 : Calculate Occupancy Percentage
# -----------------------------------
occupied_count = 0

for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1

occupancy_percentage = (occupied_count / len(parking_slots)) * 100

print(f"\nOccupancy Percentage : {occupancy_percentage:.1f}%")

# -----------------------------------
# Task 5 : Save Updated Data to File
# -----------------------------------
try:
    file = open("parking.txt", "w")

    for i in range(len(parking_slots)):
        file.write(f"Slot {i + 1} : {parking_slots[i]}\n")

    file.close()

    print("Parking Details Saved Successfully.")

except:
    print("Error while saving file!")