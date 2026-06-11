# Problem 7: Movie Ticket Booking System 
"""
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data tickets = {     
"A1": "Booked",     
"A2": "Available",     
"A3": "Booked",     
"A4": "Available",     
"B1": "Booked",     
"B2": "Available",     
"B3": "Booked",     
"B4": "Available",     
"C1": "Booked",     
"C2": "Available" } 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  
"""

# Movie Ticket Booking System

# Dictionary storing seat booking status
tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# ----------------------------------
# Task 1 : Display Available Seats
# ----------------------------------
print("Available Seats:")
print("-" * 20)

for seat, status in tickets.items():
    if status == "Available":
        print(seat)

# ----------------------------------
# Task 2 : Count Booked and Available Seats
# ----------------------------------
booked_count = 0
available_count = 0

for status in tickets.values():

    if status == "Booked":
        booked_count += 1
    else:
        available_count += 1

print("\nBooked Seats :", booked_count)
print("Available Seats :", available_count)

# ----------------------------------
# Task 3 : Reserve First Available Seat
# ----------------------------------
reserved = False

for seat, status in tickets.items():

    if status == "Available":
        tickets[seat] = "Booked"
        print(f"\nSeat {seat} Reserved Successfully.")
        reserved = True
        break

if not reserved:
    print("No Seats Available!")

# ----------------------------------
# Task 4 : Save Updated Booking Details
# ----------------------------------
try:
    file = open("tickets.txt", "w")

    for seat, status in tickets.items():
        file.write(f"{seat} : {status}\n")

    file.close()

    print("Booking Details Saved Successfully.")

except:
    print("Error while saving file!")

# ----------------------------------
# Task 5 : Calculate Hall Occupancy Percentage
# ----------------------------------
booked_count = 0

for status in tickets.values():

    if status == "Booked":
        booked_count += 1

occupancy_percentage = (booked_count / len(tickets)) * 100

print(f"Hall Occupancy Percentage : {occupancy_percentage:.1f}%")