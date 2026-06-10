# Railway Reservation Seat Analyzer 
"""
Problem Statement 
A railway coach has seats represented as follows: seats = [     
"Booked", "Available", "Booked", "Booked",     
"Available", "Available", "Booked", "Available",     
"Booked", "Booked", "Available", "Booked" ] 
Requirements Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers.
"""
seats = [     
    "Booked", "Available", "Booked", "Booked",     
    "Available", "Available", "Booked", "Available",     
    "Booked", "Booked", "Available", "Booked" 
]

#----------------------------------------------
# Function to count booked and available seats
#----------------------------------------------
def count_seats(seats):
    booked_count = seats.count("Booked")
    available_count = seats.count("Available")
    return booked_count, available_count

#----------------------------------------------
# Function to find the first available seat
#----------------------------------------------
def first_available(seats):
    return seats.index("Available") + 1  # Adding 1 to convert to seat number


#----------------------------------------------
# Function to calculate occupancy percentage
#----------------------------------------------
def occupancy_percentage(seats):
    total_seats = len(seats)
    booked_count = seats.count("Booked")
    percentage = (booked_count / total_seats) * 100
    return percentage

#----------------------------------------------
# Function to display all available seat numbers
#----------------------------------------------
def display_available_seats(seats):
    print("Available Seats:")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i+1, end=' ')  # Adding 1 to convert to seat number


#----------------------------------------------
# Main function to execute the requirements
#----------------------------------------------
if __name__ == "__main__":
    booked, available = count_seats(seats)
    print(f"Booked Seats: {booked}, Available Seats: {available}")
    
    first_available_seat = first_available(seats)
    print(f"First Available Seat Number: {first_available_seat}")
    
    occupancy = occupancy_percentage(seats)
    print(f"Occupancy Percentage: {occupancy:.2f}%")
    
    display_available_seats(seats)
 