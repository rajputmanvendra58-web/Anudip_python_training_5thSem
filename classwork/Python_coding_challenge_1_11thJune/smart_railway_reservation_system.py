# Problem 1: Smart Railway Reservation System
"""
Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample 
Data seats = {     
1: "Booked",     
2: "Available",    
3: "Booked",     
4: "Available",     
5: "Booked",     
6: "Booked",     
7: "Available",     
8: "Booked",    
9: "Available",     
10: "Booked" } 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage. 
"""

# Smart Railway Reservation System

# Dictionary to store seat number and booking status
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# -------------------------------
# Task 1 : Display Available Seats
# -------------------------------
print("Available Seats:")

for seat_no, status in seats.items():
    if status == "Available":
        print(seat_no, end=" ")

print("\n")

# -----------------------------------------
# Task 2 : Count Booked and Available Seats
# -----------------------------------------
booked_count = 0
available_count = 0

for status in seats.values():
    if status == "Booked":
        booked_count += 1
    else:
        available_count += 1

print("Booked Seats :", booked_count)
print("Available Seats :", available_count)

# ------------------------------------
# Task 3 : Reserve First Available Seat
# ------------------------------------
for seat_no, status in seats.items():
    if status == "Available":
        seats[seat_no] = "Booked"
        print(f"\nSeat {seat_no} Reserved Successfully.")
        break

# --------------------------------------
# Task 4 : Cancel Booking with Validation
# --------------------------------------
try:
    seat_number = int(input("\nEnter Seat Number to Cancel Booking: "))

    # Check whether seat exists or not
    if seat_number not in seats:
        print("Invalid Seat Number!")

    # Check if seat is already available
    elif seats[seat_number] == "Available":
        print("Seat is already available.")

    else:
        seats[seat_number] = "Available"
        print(f"Booking of Seat {seat_number} Cancelled Successfully.")

except ValueError:
    print("Please enter a valid numeric seat number.")

# -----------------------------------------
# Task 5 : Save Updated Data into Text File
# -----------------------------------------
file = open("reservations.txt", "w")

for seat_no, status in seats.items():
    file.write(f"Seat {seat_no} : {status}\n")

file.close()

print("\nReservation Details Saved Successfully.")

# ---------------------------------
# Task 6 : Occupancy Percentage
# ---------------------------------
booked_count = 0

for status in seats.values():
    if status == "Booked":
        booked_count += 1

occupancy_percentage = (booked_count / len(seats)) * 100

print(f"Occupancy Percentage : {occupancy_percentage:.1f}%")