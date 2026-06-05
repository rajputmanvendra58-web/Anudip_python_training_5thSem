# Program for Bus Seat Reservation Analysis 
# Problem Statement 
# A bus has seats represented as: 
# seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
# Where: 
# • 1 → Seat Booked  
# • 0 → Seat Available 
# Write a program to: 
# 1. Count booked and available seats.  
# 2. Find the first available seat and stop searching immediately. 
# 3. Create a list of all available seat numbers.  
# 4. Determine whether the bus is more than 70% occupied.  

# List representing bus seats
# 1 = Booked, 0 = Available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Variables to count booked and available seats
booked = 0
available = 0

# Counting booked and available seats
for seat in seats:
    if seat == 1:
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)

# Finding the first available seat
first_available = -1

for i in range(len(seats)):
    if seats[i] == 0:
        first_available = i + 1   # Seat numbers start from 1
        break                     # Stop searching immediately

print("First Available Seat:", first_available)

# Creating a list of all available seat numbers
available_seats = []

for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

print("Available Seat Numbers:", available_seats)

# Calculating occupancy percentage
occupancy = (booked / len(seats)) * 100

print("Bus Occupancy:", occupancy, "%")

# Checking if occupancy is more than 70%
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")