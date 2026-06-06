#Program for Smart Parking System 
"""
Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
• 1 = Occupied  
• 0 = Available  Write a program to: 
• Count occupied and available slots. 
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.
"""

# Smart Parking System

# List representing parking slots
# 1 = Occupied, 0 = Available
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Variables to count occupied and available slots
occupied = 0
available = 0

# Counting occupied and available slots
for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots =", occupied)
print("Available Slots =", available)

# Finding the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot Number =", i + 1)
        break

# Displaying all available slot numbers
print("Available Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1, end=" ")

print()

# Checking whether parking occupancy exceeds 75%
occupancy_percentage = (occupied / len(slots)) * 100

print("Occupancy Percentage =", occupancy_percentage, "%")

if occupancy_percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")